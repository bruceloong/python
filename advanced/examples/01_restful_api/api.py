#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
RESTful API示例 - 任务管理API

这个示例展示了如何使用Flask创建一个RESTful API，
实现了任务资源的CRUD操作，包括JWT认证、请求验证、
错误处理、数据分页等功能。
"""

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os

# 创建Flask应用
app = Flask(__name__)

# 配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks_api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key-for-jwt'  # 在生产环境中应使用环境变量
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# 初始化扩展
db = SQLAlchemy(app)
jwt = JWTManager(app)
api = Api(app)

# 数据模型
class User(db.Model):
    """用户模型"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Task(db.Model):
    """任务模型"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime)
    priority = db.Column(db.Integer, default=0)  # 0=低, 1=中, 2=高
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'<Task {self.title}>'

# 用于输出的字段定义
task_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'completed': fields.Boolean,
    'due_date': fields.DateTime(dt_format='iso8601'),
    'priority': fields.Integer,
    'created_at': fields.DateTime(dt_format='iso8601'),
    'user_id': fields.Integer
}

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
}

# 请求解析器
task_parser = reqparse.RequestParser()
task_parser.add_argument('title', type=str, required=True, help='标题不能为空')
task_parser.add_argument('description', type=str)
task_parser.add_argument('completed', type=bool)
task_parser.add_argument('due_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S') if x else None)
task_parser.add_argument('priority', type=int, choices=[0, 1, 2])

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='用户名不能为空')
user_parser.add_argument('password', type=str, required=True, help='密码不能为空')
user_parser.add_argument('email', type=str, required=True, help='邮箱不能为空')

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True, help='用户名不能为空')
login_parser.add_argument('password', type=str, required=True, help='密码不能为空')

# 资源类
class UserRegistration(Resource):
    """用户注册API"""
    def post(self):
        args = user_parser.parse_args()
        
        # 检查用户名是否已存在
        if User.query.filter_by(username=args['username']).first():
            return {'message': '用户名已存在'}, 409
        
        # 检查邮箱是否已存在
        if User.query.filter_by(email=args['email']).first():
            return {'message': '邮箱已被使用'}, 409
        
        # 创建新用户
        hashed_password = generate_password_hash(args['password'])
        new_user = User(
            username=args['username'],
            password=hashed_password,
            email=args['email']
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return {'message': '用户创建成功'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': f'创建用户时出错: {str(e)}'}, 500

class UserLogin(Resource):
    """用户登录API"""
    def post(self):
        args = login_parser.parse_args()
        
        # 查找用户
        user = User.query.filter_by(username=args['username']).first()
        
        # 检查用户是否存在及密码是否正确
        if not user or not check_password_hash(user.password, args['password']):
            return {'message': '用户名或密码错误'}, 401
        
        # 创建访问令牌
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200

class TaskList(Resource):
    """任务列表API"""
    @jwt_required()
    @marshal_with(task_fields)
    def get(self):
        # 获取当前用户ID
        current_user_id = get_jwt_identity()
        
        # 分页参数
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # 过滤参数
        completed = request.args.get('completed')
        priority = request.args.get('priority', type=int)
        
        # 构建查询
        query = Task.query.filter_by(user_id=current_user_id)
        
        if completed is not None:
            completed = completed.lower() == 'true'
            query = query.filter_by(completed=completed)
        
        if priority is not None:
            query = query.filter_by(priority=priority)
        
        # 执行分页查询
        tasks = query.order_by(Task.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
        
        # 为响应添加分页元数据
        response = {
            'items': tasks.items,
            'page': tasks.page,
            'per_page': tasks.per_page,
            'total': tasks.total,
            'pages': tasks.pages
        }
        
        return response
    
    @jwt_required()
    @marshal_with(task_fields)
    def post(self):
        # 获取当前用户ID
        current_user_id = get_jwt_identity()
        
        # 解析请求数据
        args = task_parser.parse_args()
        
        # 创建新任务
        new_task = Task(
            title=args['title'],
            description=args['description'],
            completed=args['completed'] if args['completed'] is not None else False,
            due_date=args['due_date'],
            priority=args['priority'] if args['priority'] is not None else 0,
            user_id=current_user_id
        )
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return new_task, 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=f"创建任务时出错: {str(e)}")

class TaskDetail(Resource):
    """单个任务API"""
    @jwt_required()
    @marshal_with(task_fields)
    def get(self, task_id):
        # 获取当前用户ID
        current_user_id = get_jwt_identity()
        
        # 查找任务
        task = Task.query.filter_by(id=task_id, user_id=current_user_id).first()
        
        if not task:
            abort(404, message="任务不存在")
        
        return task
    
    @jwt_required()
    @marshal_with(task_fields)
    def put(self, task_id):
        # 获取当前用户ID
        current_user_id = get_jwt_identity()
        
        # 查找任务
        task = Task.query.filter_by(id=task_id, user_id=current_user_id).first()
        
        if not task:
            abort(404, message="任务不存在")
        
        # 解析请求数据
        args = task_parser.parse_args()
        
        # 更新任务
        task.title = args['title']
        task.description = args['description'] if args['description'] is not None else task.description
        task.completed = args['completed'] if args['completed'] is not None else task.completed
        task.due_date = args['due_date'] if args['due_date'] is not None else task.due_date
        task.priority = args['priority'] if args['priority'] is not None else task.priority
        
        try:
            db.session.commit()
            return task, 200
        except Exception as e:
            db.session.rollback()
            abort(500, message=f"更新任务时出错: {str(e)}")
    
    @jwt_required()
    def delete(self, task_id):
        # 获取当前用户ID
        current_user_id = get_jwt_identity()
        
        # 查找任务
        task = Task.query.filter_by(id=task_id, user_id=current_user_id).first()
        
        if not task:
            abort(404, message="任务不存在")
        
        try:
            db.session.delete(task)
            db.session.commit()
            return {'message': '任务已删除'}, 200
        except Exception as e:
            db.session.rollback()
            abort(500, message=f"删除任务时出错: {str(e)}")

class UserProfile(Resource):
    """用户配置文件API"""
    @jwt_required()
    @marshal_with(user_fields)
    def get(self):
        # 获取当前用户ID
        current_user_id = get_jwt_identity()
        
        # 查找用户
        user = User.query.get(current_user_id)
        
        if not user:
            abort(404, message="用户不存在")
        
        return user

# 注册API路由
api.add_resource(UserRegistration, '/api/auth/register')
api.add_resource(UserLogin, '/api/auth/login')
api.add_resource(TaskList, '/api/tasks')
api.add_resource(TaskDetail, '/api/tasks/<int:task_id>')
api.add_resource(UserProfile, '/api/user/profile')

# 错误处理
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': '未找到资源'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': '服务器内部错误'}), 500

# 创建数据库表
@app.before_first_request
def create_tables():
    db.create_all()

# API根路径
@app.route('/api', methods=['GET'])
def api_root():
    return jsonify({
        'message': '欢迎访问任务管理API',
        'version': '1.0',
        'endpoints': {
            'auth': {
                'register': '/api/auth/register',
                'login': '/api/auth/login'
            },
            'tasks': {
                'list': '/api/tasks',
                'detail': '/api/tasks/<task_id>'
            },
            'user': {
                'profile': '/api/user/profile'
            }
        }
    })

# 主程序
if __name__ == '__main__':
    # 如果数据库文件不存在，创建它
    if not os.path.exists('tasks_api.db'):
        with app.app_context():
            db.create_all()
    
    # 启动应用
    app.run(debug=True, port=5000) 