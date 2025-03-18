#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Web任务管理器项目
一个完整的任务管理Web应用，使用Flask和SQLite实现。
包含用户登录、任务CRUD操作、任务分类等功能。
"""

import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# 创建Flask应用实例
app = Flask(__name__)
app.config.update(
    SECRET_KEY='dev_key_for_session',
    DATABASE=os.path.join(app.root_path, 'tasks.db')
)

# 数据库连接函数
def get_db():
    """
    获取数据库连接
    如果不存在，则创建一个新的连接
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    """如果存在，关闭数据库连接"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """初始化数据库表结构"""
    db = get_db()
    
    # 创建用户表
    db.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 创建任务分类表
    db.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    # 创建任务表
    db.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        due_date TIMESTAMP,
        priority INTEGER DEFAULT 0,
        completed INTEGER DEFAULT 0,
        user_id INTEGER NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
    ''')
    
    # 提交事务
    db.commit()
    
    # 检查是否有默认用户，如果没有则创建
    cursor = db.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        db.execute(
            'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
            ('admin', generate_password_hash('password'), 'admin@example.com')
        )
        db.execute(
            'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
            ('user', generate_password_hash('password'), 'user@example.com')
        )
        db.commit()
    
    # 检查是否有默认分类，如果没有则创建
    cursor = db.execute('SELECT COUNT(*) FROM categories')
    if cursor.fetchone()[0] == 0:
        categories = [
            ('工作', 1), ('学习', 1), ('个人', 1),
            ('工作', 2), ('学习', 2), ('个人', 2)
        ]
        db.executemany(
            'INSERT INTO categories (name, user_id) VALUES (?, ?)',
            categories
        )
        db.commit()

# 用户登录所需的装饰器
def login_required(view):
    """确保用户已登录的装饰器"""
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            flash('请先登录！ (Please login first!)', 'error')
            return redirect(url_for('login'))
        return view(**kwargs)
    wrapped_view.__name__ = view.__name__
    return wrapped_view

# 路由：首页
@app.route('/')
def index():
    """首页路由处理函数"""
    return render_template('index.html')

# 路由：注册
@app.route('/register', methods=('GET', 'POST'))
def register():
    """用户注册处理"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        db = get_db()
        error = None

        if not username:
            error = '用户名不能为空 (Username is required)'
        elif not password:
            error = '密码不能为空 (Password is required)'
        elif not email:
            error = '邮箱不能为空 (Email is required)'
        elif db.execute(
            'SELECT id FROM users WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f'用户 {username} 已注册 (User {username} is already registered)'
        elif db.execute(
            'SELECT id FROM users WHERE email = ?', (email,)
        ).fetchone() is not None:
            error = f'邮箱 {email} 已被使用 (Email {email} is already in use)'

        if error is None:
            # 创建新用户
            db.execute(
                'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                (username, generate_password_hash(password), email)
            )
            db.commit()
            
            # 获取新用户ID
            user_id = db.execute(
                'SELECT id FROM users WHERE username = ?', (username,)
            ).fetchone()[0]
            
            # 为新用户创建默认分类
            default_categories = [('工作', user_id), ('学习', user_id), ('个人', user_id)]
            db.executemany(
                'INSERT INTO categories (name, user_id) VALUES (?, ?)',
                default_categories
            )
            db.commit()
            
            flash('注册成功，请登录！ (Registration successful, please login!)', 'success')
            return redirect(url_for('login'))
        
        flash(error, 'error')

    return render_template('auth/register.html')

# 路由：登录
@app.route('/login', methods=('GET', 'POST'))
def login():
    """用户登录处理"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        
        # 查询用户
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = '用户名不存在 (Username not found)'
        elif not check_password_hash(user['password'], password):
            error = '密码错误 (Incorrect password)'

        if error is None:
            # 登录成功，保存用户ID到session
            session.clear()
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash(f'欢迎回来，{username}！ (Welcome back, {username}!)', 'success')
            return redirect(url_for('dashboard'))

        flash(error, 'error')

    return render_template('auth/login.html')

# 路由：注销
@app.route('/logout')
def logout():
    """用户注销处理"""
    session.clear()
    flash('您已成功注销 (You have been logged out)', 'success')
    return redirect(url_for('index'))

# 路由：用户仪表板
@app.route('/dashboard')
@login_required
def dashboard():
    """用户仪表板，显示任务概况"""
    db = get_db()
    user_id = session['user_id']
    
    # 获取用户的任务统计
    total_tasks = db.execute(
        'SELECT COUNT(*) FROM tasks WHERE user_id = ?', (user_id,)
    ).fetchone()[0]
    
    completed_tasks = db.execute(
        'SELECT COUNT(*) FROM tasks WHERE user_id = ? AND completed = 1', (user_id,)
    ).fetchone()[0]
    
    pending_tasks = total_tasks - completed_tasks
    
    # 获取今天到期的任务
    today = datetime.now().strftime('%Y-%m-%d')
    due_today = db.execute(
        'SELECT COUNT(*) FROM tasks WHERE user_id = ? AND date(due_date) = ? AND completed = 0',
        (user_id, today)
    ).fetchone()[0]
    
    # 获取高优先级任务
    high_priority = db.execute(
        'SELECT COUNT(*) FROM tasks WHERE user_id = ? AND priority = 2 AND completed = 0',
        (user_id,)
    ).fetchone()[0]
    
    # 获取按分类统计的任务数量
    categories = db.execute(
        '''
        SELECT c.id, c.name, COUNT(t.id) as task_count
        FROM categories c
        LEFT JOIN tasks t ON c.id = t.category_id AND t.completed = 0
        WHERE c.user_id = ?
        GROUP BY c.id
        ''',
        (user_id,)
    ).fetchall()
    
    # 获取最近添加的5个任务
    recent_tasks = db.execute(
        '''
        SELECT t.id, t.title, t.due_date, t.priority, c.name as category_name
        FROM tasks t
        LEFT JOIN categories c ON t.category_id = c.id
        WHERE t.user_id = ? AND t.completed = 0
        ORDER BY t.created_at DESC
        LIMIT 5
        ''',
        (user_id,)
    ).fetchall()
    
    return render_template('dashboard.html', 
                           total_tasks=total_tasks, 
                           completed_tasks=completed_tasks,
                           pending_tasks=pending_tasks,
                           due_today=due_today,
                           high_priority=high_priority,
                           categories=categories,
                           recent_tasks=recent_tasks)

# 路由：任务列表
@app.route('/tasks')
@login_required
def task_list():
    """显示用户的任务列表"""
    db = get_db()
    user_id = session['user_id']
    
    # 获取过滤参数
    status = request.args.get('status', 'pending')
    category_id = request.args.get('category', 'all')
    priority = request.args.get('priority', 'all')
    
    # 构建查询
    query = '''
    SELECT t.*, c.name as category_name 
    FROM tasks t
    LEFT JOIN categories c ON t.category_id = c.id
    WHERE t.user_id = ?
    '''
    params = [user_id]
    
    # 应用过滤
    if status == 'pending':
        query += ' AND t.completed = 0'
    elif status == 'completed':
        query += ' AND t.completed = 1'
    
    if category_id != 'all' and category_id.isdigit():
        query += ' AND t.category_id = ?'
        params.append(int(category_id))
    
    if priority != 'all' and priority.isdigit():
        query += ' AND t.priority = ?'
        params.append(int(priority))
    
    # 排序
    query += ' ORDER BY t.due_date ASC, t.priority DESC'
    
    # 执行查询
    tasks = db.execute(query, params).fetchall()
    
    # 获取分类列表，用于过滤
    categories = db.execute(
        'SELECT id, name FROM categories WHERE user_id = ?',
        (user_id,)
    ).fetchall()
    
    return render_template('tasks/list.html', 
                           tasks=tasks,
                           categories=categories,
                           current_status=status,
                           current_category=category_id,
                           current_priority=priority)

# 路由：添加任务
@app.route('/tasks/add', methods=('GET', 'POST'))
@login_required
def add_task():
    """添加新任务"""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date'] or None
        priority = request.form['priority']
        category_id = request.form['category_id'] or None
        user_id = session['user_id']
        
        error = None
        
        if not title:
            error = '标题不能为空 (Title is required)'
        
        if error is None:
            db = get_db()
            db.execute(
                '''
                INSERT INTO tasks 
                (title, description, due_date, priority, category_id, user_id)
                VALUES (?, ?, ?, ?, ?, ?)
                ''',
                (title, description, due_date, priority, category_id, user_id)
            )
            db.commit()
            flash('任务已添加 (Task has been added)', 'success')
            return redirect(url_for('task_list'))
        
        flash(error, 'error')
    
    # 获取分类列表
    db = get_db()
    categories = db.execute(
        'SELECT id, name FROM categories WHERE user_id = ?',
        (session['user_id'],)
    ).fetchall()
    
    return render_template('tasks/form.html', categories=categories, task=None)

# 路由：编辑任务
@app.route('/tasks/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit_task(id):
    """编辑现有任务"""
    db = get_db()
    user_id = session['user_id']
    
    # 获取任务信息
    task = db.execute(
        'SELECT * FROM tasks WHERE id = ? AND user_id = ?',
        (id, user_id)
    ).fetchone()
    
    if task is None:
        flash('任务不存在或您无权编辑 (Task does not exist or you do not have permission to edit it)', 'error')
        return redirect(url_for('task_list'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date'] or None
        priority = request.form['priority']
        category_id = request.form['category_id'] or None
        completed = 1 if 'completed' in request.form else 0
        
        error = None
        
        if not title:
            error = '标题不能为空 (Title is required)'
        
        if error is None:
            db.execute(
                '''
                UPDATE tasks
                SET title = ?, description = ?, due_date = ?, 
                priority = ?, category_id = ?, completed = ?
                WHERE id = ?
                ''',
                (title, description, due_date, priority, category_id, completed, id)
            )
            db.commit()
            flash('任务已更新 (Task has been updated)', 'success')
            return redirect(url_for('task_list'))
        
        flash(error, 'error')
    
    # 获取分类列表
    categories = db.execute(
        'SELECT id, name FROM categories WHERE user_id = ?',
        (user_id,)
    ).fetchall()
    
    return render_template('tasks/form.html', categories=categories, task=task)

# 路由：删除任务
@app.route('/tasks/<int:id>/delete', methods=['POST'])
@login_required
def delete_task(id):
    """删除任务"""
    db = get_db()
    user_id = session['user_id']
    
    # 检查任务是否存在且属于当前用户
    task = db.execute(
        'SELECT id FROM tasks WHERE id = ? AND user_id = ?',
        (id, user_id)
    ).fetchone()
    
    if task is None:
        flash('任务不存在或您无权删除 (Task does not exist or you do not have permission to delete it)', 'error')
    else:
        db.execute('DELETE FROM tasks WHERE id = ?', (id,))
        db.commit()
        flash('任务已删除 (Task has been deleted)', 'success')
    
    return redirect(url_for('task_list'))

# 路由：标记任务为已完成/未完成
@app.route('/tasks/<int:id>/toggle', methods=['POST'])
@login_required
def toggle_task(id):
    """标记任务为已完成或未完成"""
    db = get_db()
    user_id = session['user_id']
    
    # 检查任务是否存在且属于当前用户
    task = db.execute(
        'SELECT id, completed FROM tasks WHERE id = ? AND user_id = ?',
        (id, user_id)
    ).fetchone()
    
    if task is None:
        flash('任务不存在或您无权修改 (Task does not exist or you do not have permission to modify it)', 'error')
    else:
        new_status = 0 if task['completed'] else 1
        status_text = '已完成 (completed)' if new_status else '未完成 (pending)'
        
        db.execute(
            'UPDATE tasks SET completed = ? WHERE id = ?',
            (new_status, id)
        )
        db.commit()
        flash(f'任务已标记为{status_text} (Task marked as {status_text})', 'success')
    
    return redirect(url_for('task_list'))

# 路由：分类管理
@app.route('/categories', methods=['GET'])
@login_required
def category_list():
    """显示用户的任务分类列表"""
    db = get_db()
    user_id = session['user_id']
    
    # 获取分类列表以及每个分类下的任务数量
    categories = db.execute(
        '''
        SELECT c.id, c.name, 
               COUNT(t.id) as task_count,
               SUM(CASE WHEN t.completed = 0 THEN 1 ELSE 0 END) as pending_count
        FROM categories c
        LEFT JOIN tasks t ON c.id = t.category_id
        WHERE c.user_id = ?
        GROUP BY c.id
        ORDER BY c.name
        ''',
        (user_id,)
    ).fetchall()
    
    return render_template('categories/list.html', categories=categories)

# 路由：添加分类
@app.route('/categories/add', methods=['GET', 'POST'])
@login_required
def add_category():
    """添加新分类"""
    if request.method == 'POST':
        name = request.form['name']
        user_id = session['user_id']
        
        error = None
        
        if not name:
            error = '分类名称不能为空 (Category name is required)'
        
        if error is None:
            db = get_db()
            db.execute(
                'INSERT INTO categories (name, user_id) VALUES (?, ?)',
                (name, user_id)
            )
            db.commit()
            flash('分类已添加 (Category has been added)', 'success')
            return redirect(url_for('category_list'))
        
        flash(error, 'error')
    
    return render_template('categories/form.html', category=None)

# 路由：编辑分类
@app.route('/categories/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_category(id):
    """编辑现有分类"""
    db = get_db()
    user_id = session['user_id']
    
    # 获取分类信息
    category = db.execute(
        'SELECT * FROM categories WHERE id = ? AND user_id = ?',
        (id, user_id)
    ).fetchone()
    
    if category is None:
        flash('分类不存在或您无权编辑 (Category does not exist or you do not have permission to edit it)', 'error')
        return redirect(url_for('category_list'))
    
    if request.method == 'POST':
        name = request.form['name']
        
        error = None
        
        if not name:
            error = '分类名称不能为空 (Category name is required)'
        
        if error is None:
            db.execute(
                'UPDATE categories SET name = ? WHERE id = ?',
                (name, id)
            )
            db.commit()
            flash('分类已更新 (Category has been updated)', 'success')
            return redirect(url_for('category_list'))
        
        flash(error, 'error')
    
    return render_template('categories/form.html', category=category)

# 路由：删除分类
@app.route('/categories/<int:id>/delete', methods=['POST'])
@login_required
def delete_category(id):
    """删除分类"""
    db = get_db()
    user_id = session['user_id']
    
    # 检查分类是否存在且属于当前用户
    category = db.execute(
        'SELECT id FROM categories WHERE id = ? AND user_id = ?',
        (id, user_id)
    ).fetchone()
    
    if category is None:
        flash('分类不存在或您无权删除 (Category does not exist or you do not have permission to delete it)', 'error')
    else:
        # 将该分类下的任务重置为无分类
        db.execute(
            'UPDATE tasks SET category_id = NULL WHERE category_id = ?',
            (id,)
        )
        # 删除分类
        db.execute('DELETE FROM categories WHERE id = ?', (id,))
        db.commit()
        flash('分类已删除 (Category has been deleted)', 'success')
    
    return redirect(url_for('category_list'))

# 应用启动入口
if __name__ == '__main__':
    # 初始化数据库
    with app.app_context():
        init_db()
    
    # 如果 templates 目录不存在，则创建
    templates_dir = os.path.join(app.root_path, 'templates')
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
        
        # 在此处可以添加基本模板文件的创建逻辑
        # ...
    
    # 设置调试模式运行
    app.run(debug=True) 