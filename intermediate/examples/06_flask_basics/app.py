#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Flask Web框架基础示例
展示如何创建一个简单的Web应用，包括路由、模板和表单处理。
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

# 创建Flask应用实例 (Create Flask application instance)
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于flash消息 (Used for flash messages)

# 模拟数据库 - 任务列表（实际应用中会使用真正的数据库）
# (Mock database - task list (in a real application, a real database would be used))
tasks = [
    {
        'id': 1,
        'title': '学习Flask基础',
        'description': '了解Flask的路由、模板和请求处理',
        'created_at': '2023-01-15 08:30:00',
        'completed': False
    },
    {
        'id': 2,
        'title': '构建简单的Web应用',
        'description': '创建一个简单的任务管理应用',
        'created_at': '2023-01-16 10:45:00',
        'completed': True
    },
    {
        'id': 3,
        'title': '学习数据库集成',
        'description': '了解如何将Flask与SQLite或其他数据库集成',
        'created_at': '2023-01-18 14:20:00',
        'completed': False
    }
]

# 路由：主页 (Route: Home page)
@app.route('/')
def index():
    """渲染主页 (Render the home page)"""
    return render_template('index.html', tasks=tasks)

# 路由：关于页面 (Route: About page)
@app.route('/about')
def about():
    """渲染关于页面 (Render the about page)"""
    return render_template('about.html')

# 路由：查看任务详情 (Route: View task details)
@app.route('/task/<int:task_id>')
def view_task(task_id):
    """
    渲染任务详情页
    (Render the task details page)
    
    参数:
        task_id (int): 任务ID
    """
    # 查找任务 (Find the task)
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task:
        return render_template('task_details.html', task=task)
    else:
        flash('任务不存在 (Task does not exist)', 'error')
        return redirect(url_for('index'))

# 路由：添加新任务（显示表单） (Route: Add new task (show form))
@app.route('/task/new', methods=['GET'])
def new_task():
    """渲染添加任务表单 (Render the add task form)"""
    return render_template('task_form.html')

# 路由：添加新任务（处理表单提交） (Route: Add new task (handle form submission))
@app.route('/task/new', methods=['POST'])
def add_task():
    """处理添加任务表单的提交 (Handle the submission of the add task form)"""
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title:
        flash('标题不能为空 (Title cannot be empty)', 'error')
        return redirect(url_for('new_task'))
    
    # 生成新任务ID (Generate new task ID)
    new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
    
    # 创建新任务 (Create new task)
    task = {
        'id': new_id,
        'title': title,
        'description': description,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'completed': False
    }
    
    # 添加到任务列表 (Add to task list)
    tasks.append(task)
    
    flash('任务已成功添加 (Task added successfully)', 'success')
    return redirect(url_for('index'))

# 路由：标记任务为已完成 (Route: Mark task as completed)
@app.route('/task/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    """
    标记任务为已完成
    (Mark task as completed)
    
    参数:
        task_id (int): 任务ID
    """
    # 查找任务 (Find the task)
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task:
        task['completed'] = True
        flash('任务已标记为已完成 (Task marked as completed)', 'success')
    else:
        flash('任务不存在 (Task does not exist)', 'error')
    
    return redirect(url_for('index'))

# 路由：删除任务 (Route: Delete task)
@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    """
    删除任务
    (Delete task)
    
    参数:
        task_id (int): 任务ID
    """
    global tasks
    
    # 删除任务 (Delete the task)
    tasks = [t for t in tasks if t['id'] != task_id]
    
    flash('任务已删除 (Task deleted)', 'success')
    return redirect(url_for('index'))

# 自定义错误处理 (Custom error handling)
@app.errorhandler(404)
def page_not_found(e):
    """处理404错误 (Handle 404 error)"""
    return render_template('404.html'), 404

# 运行应用 (Run the application)
if __name__ == '__main__':
    # 创建模板目录 (Create templates directory)
    import os
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # 为了方便演示，如果模板文件不存在，创建它们 (For demonstration, create template files if they don't exist)
    template_files = {
        'templates/index.html': '''
<!DOCTYPE html>
<html>
<head>
    <title>任务管理器 | 主页</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .task { border: 1px solid #ccc; margin: 10px 0; padding: 10px; border-radius: 5px; }
        .task.completed { background-color: #f8f8f8; }
        .task-title { font-weight: bold; }
        .flash { padding: 10px; margin: 10px 0; border-radius: 5px; }
        .flash.success { background-color: #dff0d8; border: 1px solid #d6e9c6; color: #3c763d; }
        .flash.error { background-color: #f2dede; border: 1px solid #ebccd1; color: #a94442; }
        .nav { margin-bottom: 20px; }
        .nav a { margin-right: 15px; }
        .button { display: inline-block; padding: 5px 10px; background-color: #4CAF50; color: white; 
                 text-decoration: none; border-radius: 3px; border: none; cursor: pointer; }
        .button.danger { background-color: #f44336; }
        form { display: inline; }
    </style>
</head>
<body>
    <h1>任务管理器 (Task Manager)</h1>
    
    <div class="nav">
        <a href="{{ url_for('index') }}">主页 (Home)</a>
        <a href="{{ url_for('new_task') }}">添加任务 (Add Task)</a>
        <a href="{{ url_for('about') }}">关于 (About)</a>
    </div>
    
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <h2>任务列表 (Task List)</h2>
    
    {% if tasks %}
        {% for task in tasks %}
            <div class="task {% if task.completed %}completed{% endif %}">
                <div class="task-title">{{ task.title }}</div>
                <div>{{ task.description }}</div>
                <div>创建于 (Created): {{ task.created_at }}</div>
                <div>
                    状态 (Status): 
                    {% if task.completed %}
                        已完成 (Completed)
                    {% else %}
                        待办 (Pending)
                    {% endif %}
                </div>
                <div style="margin-top: 10px;">
                    <a href="{{ url_for('view_task', task_id=task.id) }}" class="button">
                        查看详情 (View Details)
                    </a>
                    
                    {% if not task.completed %}
                        <form action="{{ url_for('complete_task', task_id=task.id) }}" method="post">
                            <button type="submit" class="button">
                                标记为已完成 (Mark as Completed)
                            </button>
                        </form>
                    {% endif %}
                    
                    <form action="{{ url_for('delete_task', task_id=task.id) }}" method="post" 
                          onsubmit="return confirm('确定要删除此任务吗? (Are you sure you want to delete this task?)');">
                        <button type="submit" class="button danger">
                            删除 (Delete)
                        </button>
                    </form>
                </div>
            </div>
        {% endfor %}
    {% else %}
        <p>当前没有任务。(No tasks available.)</p>
    {% endif %}
</body>
</html>
        ''',
        
        'templates/about.html': '''
<!DOCTYPE html>
<html>
<head>
    <title>任务管理器 | 关于</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .nav { margin-bottom: 20px; }
        .nav a { margin-right: 15px; }
    </style>
</head>
<body>
    <h1>关于任务管理器 (About Task Manager)</h1>
    
    <div class="nav">
        <a href="{{ url_for('index') }}">主页 (Home)</a>
        <a href="{{ url_for('new_task') }}">添加任务 (Add Task)</a>
        <a href="{{ url_for('about') }}">关于 (About)</a>
    </div>
    
    <h2>项目信息 (Project Information)</h2>
    <p>这是一个使用Flask框架构建的简单任务管理器Web应用。</p>
    <p>(This is a simple task manager web application built with the Flask framework.)</p>
    
    <h2>功能 (Features)</h2>
    <ul>
        <li>查看任务列表 (View task list)</li>
        <li>添加新任务 (Add new tasks)</li>
        <li>标记任务为已完成 (Mark tasks as completed)</li>
        <li>删除任务 (Delete tasks)</li>
    </ul>
    
    <h2>技术栈 (Technology Stack)</h2>
    <ul>
        <li>Python</li>
        <li>Flask Web框架</li>
        <li>HTML/CSS</li>
    </ul>
    
    <p><a href="{{ url_for('index') }}">返回主页 (Return to Home)</a></p>
</body>
</html>
        ''',
        
        'templates/task_details.html': '''
<!DOCTYPE html>
<html>
<head>
    <title>任务管理器 | 任务详情</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .task { border: 1px solid #ccc; margin: 10px 0; padding: 10px; border-radius: 5px; }
        .task.completed { background-color: #f8f8f8; }
        .task-title { font-size: 24px; margin-bottom: 10px; }
        .nav { margin-bottom: 20px; }
        .nav a { margin-right: 15px; }
        .button { display: inline-block; padding: 5px 10px; background-color: #4CAF50; color: white; 
                 text-decoration: none; border-radius: 3px; border: none; cursor: pointer; }
        .button.danger { background-color: #f44336; }
        form { display: inline; }
    </style>
</head>
<body>
    <h1>任务详情 (Task Details)</h1>
    
    <div class="nav">
        <a href="{{ url_for('index') }}">主页 (Home)</a>
        <a href="{{ url_for('new_task') }}">添加任务 (Add Task)</a>
        <a href="{{ url_for('about') }}">关于 (About)</a>
    </div>
    
    <div class="task {% if task.completed %}completed{% endif %}">
        <div class="task-title">{{ task.title }}</div>
        <p><strong>描述 (Description):</strong> {{ task.description }}</p>
        <p><strong>创建于 (Created):</strong> {{ task.created_at }}</p>
        <p>
            <strong>状态 (Status):</strong> 
            {% if task.completed %}
                已完成 (Completed)
            {% else %}
                待办 (Pending)
            {% endif %}
        </p>
        
        <div style="margin-top: 20px;">
            {% if not task.completed %}
                <form action="{{ url_for('complete_task', task_id=task.id) }}" method="post">
                    <button type="submit" class="button">
                        标记为已完成 (Mark as Completed)
                    </button>
                </form>
            {% endif %}
            
            <form action="{{ url_for('delete_task', task_id=task.id) }}" method="post"
                  onsubmit="return confirm('确定要删除此任务吗? (Are you sure you want to delete this task?)');">
                <button type="submit" class="button danger">
                    删除 (Delete)
                </button>
            </form>
        </div>
    </div>
    
    <p><a href="{{ url_for('index') }}">返回任务列表 (Return to Task List)</a></p>
</body>
</html>
        ''',
        
        'templates/task_form.html': '''
<!DOCTYPE html>
<html>
<head>
    <title>任务管理器 | 添加任务</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], textarea { width: 100%; padding: 8px; box-sizing: border-box; }
        textarea { height: 100px; }
        .button { display: inline-block; padding: 8px 15px; background-color: #4CAF50; color: white; 
                 text-decoration: none; border-radius: 3px; border: none; cursor: pointer; }
        .nav { margin-bottom: 20px; }
        .nav a { margin-right: 15px; }
        .flash { padding: 10px; margin: 10px 0; border-radius: 5px; }
        .flash.error { background-color: #f2dede; border: 1px solid #ebccd1; color: #a94442; }
    </style>
</head>
<body>
    <h1>添加新任务 (Add New Task)</h1>
    
    <div class="nav">
        <a href="{{ url_for('index') }}">主页 (Home)</a>
        <a href="{{ url_for('new_task') }}">添加任务 (Add Task)</a>
        <a href="{{ url_for('about') }}">关于 (About)</a>
    </div>
    
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <form action="{{ url_for('add_task') }}" method="post">
        <div class="form-group">
            <label for="title">标题 (Title) *</label>
            <input type="text" id="title" name="title" required>
        </div>
        
        <div class="form-group">
            <label for="description">描述 (Description)</label>
            <textarea id="description" name="description"></textarea>
        </div>
        
        <div class="form-group">
            <button type="submit" class="button">添加任务 (Add Task)</button>
            <a href="{{ url_for('index') }}" style="margin-left: 10px;">取消 (Cancel)</a>
        </div>
    </form>
</body>
</html>
        ''',
        
        'templates/404.html': '''
<!DOCTYPE html>
<html>
<head>
    <title>任务管理器 | 页面未找到</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; text-align: center; }
        .error-code { font-size: 72px; margin: 20px 0; color: #f44336; }
        .nav { margin-bottom: 20px; }
        .nav a { margin-right: 15px; }
    </style>
</head>
<body>
    <div class="nav">
        <a href="{{ url_for('index') }}">主页 (Home)</a>
        <a href="{{ url_for('new_task') }}">添加任务 (Add Task)</a>
        <a href="{{ url_for('about') }}">关于 (About)</a>
    </div>
    
    <div class="error-code">404</div>
    <h1>页面未找到 (Page Not Found)</h1>
    <p>您请求的页面不存在。 (The page you requested does not exist.)</p>
    <p><a href="{{ url_for('index') }}">返回主页 (Return to Home)</a></p>
</body>
</html>
        '''
    }
    
    # 创建模板文件 (Create template files)
    for file_path, content in template_files.items():
        # 确保目录存在 (Ensure directory exists)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # 如果文件不存在，创建它 (Create file if it doesn't exist)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    # 打印指南 (Print guide)
    print("=" * 80)
    print("Flask应用已设置！ (Flask application is set up!)")
    print("要运行应用，请执行以下命令: (To run the application, execute the following command:)")
    print("  python app.py")
    print("然后在浏览器中访问: (Then visit in your browser:)")
    print("  http://127.0.0.1:5000/")
    print("=" * 80)
    
    # 运行应用 (Run the application)
    app.run(debug=True) 