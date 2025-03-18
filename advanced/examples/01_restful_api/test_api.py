#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
RESTful API 测试模块

本模块包含对任务管理API的单元测试，使用pytest测试框架。
测试内容包括用户注册、登录、任务的CRUD操作等功能。
"""

import pytest
import json
import os
from api import app, db, User, Task
from datetime import datetime, timedelta

# 测试客户端
@pytest.fixture
def client():
    """创建测试客户端"""
    # 使用临时数据库文件
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_tasks_api.db'
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        # 设置应用上下文
        with app.app_context():
            # 创建数据库表
            db.create_all()
            yield client
            # 清理：删除数据库表
            db.drop_all()
    
    # 测试完成后删除测试数据库文件
    if os.path.exists('test_tasks_api.db'):
        os.remove('test_tasks_api.db')

# 测试用户注册
def test_user_registration(client):
    """测试用户注册功能"""
    # 注册请求数据
    user_data = {
        'username': 'testuser',
        'password': 'password123',
        'email': 'test@example.com'
    }
    
    # 发送POST请求到注册API
    response = client.post(
        '/api/auth/register',
        data=json.dumps(user_data),
        content_type='application/json'
    )
    
    # 检查响应状态码
    assert response.status_code == 201
    
    # 检查响应消息
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == '用户创建成功'
    
    # 确认用户已添加到数据库
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None
        assert user.email == 'test@example.com'

# 测试重复用户名注册
def test_duplicate_username_registration(client):
    """测试使用重复用户名注册时的处理"""
    # 先创建一个用户
    user_data = {
        'username': 'testuser',
        'password': 'password123',
        'email': 'test@example.com'
    }
    
    client.post(
        '/api/auth/register',
        data=json.dumps(user_data),
        content_type='application/json'
    )
    
    # 尝试使用相同用户名注册
    response = client.post(
        '/api/auth/register',
        data=json.dumps(user_data),
        content_type='application/json'
    )
    
    # 检查是否返回409冲突错误
    assert response.status_code == 409
    
    # 检查错误消息
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == '用户名已存在'

# 测试用户登录
def test_user_login(client):
    """测试用户登录功能"""
    # 先注册一个用户
    user_data = {
        'username': 'testuser',
        'password': 'password123',
        'email': 'test@example.com'
    }
    
    client.post(
        '/api/auth/register',
        data=json.dumps(user_data),
        content_type='application/json'
    )
    
    # 尝试登录
    login_data = {
        'username': 'testuser',
        'password': 'password123'
    }
    
    response = client.post(
        '/api/auth/login',
        data=json.dumps(login_data),
        content_type='application/json'
    )
    
    # 检查响应状态码
    assert response.status_code == 200
    
    # 检查是否返回了访问令牌
    data = json.loads(response.data)
    assert 'access_token' in data
    assert data['access_token'] is not None

# 获取测试用户的token
@pytest.fixture
def auth_token(client):
    """获取已认证用户的访问令牌"""
    # 注册一个用户
    user_data = {
        'username': 'testuser',
        'password': 'password123',
        'email': 'test@example.com'
    }
    
    client.post(
        '/api/auth/register',
        data=json.dumps(user_data),
        content_type='application/json'
    )
    
    # 获取登录令牌
    login_data = {
        'username': 'testuser',
        'password': 'password123'
    }
    
    response = client.post(
        '/api/auth/login',
        data=json.dumps(login_data),
        content_type='application/json'
    )
    
    data = json.loads(response.data)
    return data['access_token']

# 测试创建任务
def test_create_task(client, auth_token):
    """测试创建任务功能"""
    # 任务数据
    task_data = {
        'title': '测试任务',
        'description': '这是一个测试任务',
        'priority': 1,
        'due_date': (datetime.utcnow() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')
    }
    
    # 发送请求创建任务
    response = client.post(
        '/api/tasks',
        data=json.dumps(task_data),
        content_type='application/json',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 检查响应状态码
    assert response.status_code == 201
    
    # 检查返回的任务数据
    data = json.loads(response.data)
    assert data['title'] == '测试任务'
    assert data['description'] == '这是一个测试任务'
    assert data['priority'] == 1
    assert data['completed'] is False

# 测试获取任务列表
def test_get_task_list(client, auth_token):
    """测试获取任务列表功能"""
    # 创建几个测试任务
    task_data = [
        {'title': '任务1', 'description': '描述1', 'priority': 0},
        {'title': '任务2', 'description': '描述2', 'priority': 1},
        {'title': '任务3', 'description': '描述3', 'priority': 2}
    ]
    
    for task in task_data:
        client.post(
            '/api/tasks',
            data=json.dumps(task),
            content_type='application/json',
            headers={'Authorization': f'Bearer {auth_token}'}
        )
    
    # 获取任务列表
    response = client.get(
        '/api/tasks',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 检查响应状态码
    assert response.status_code == 200
    
    # 检查任务列表数据
    data = json.loads(response.data)
    assert 'items' in data
    assert len(data['items']) == 3
    
    # 检查分页信息
    assert data['page'] == 1
    assert data['per_page'] == 10
    assert data['total'] == 3

# 测试获取单个任务
def test_get_task_detail(client, auth_token):
    """测试获取任务详情功能"""
    # 创建一个测试任务
    task_data = {
        'title': '详情测试任务',
        'description': '这是用于测试获取任务详情的任务',
        'priority': 2
    }
    
    response = client.post(
        '/api/tasks',
        data=json.dumps(task_data),
        content_type='application/json',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 获取任务ID
    created_task = json.loads(response.data)
    task_id = created_task['id']
    
    # 获取任务详情
    response = client.get(
        f'/api/tasks/{task_id}',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 检查响应状态码
    assert response.status_code == 200
    
    # 检查任务详情
    task = json.loads(response.data)
    assert task['id'] == task_id
    assert task['title'] == '详情测试任务'
    assert task['description'] == '这是用于测试获取任务详情的任务'
    assert task['priority'] == 2

# 测试更新任务
def test_update_task(client, auth_token):
    """测试更新任务功能"""
    # 创建一个测试任务
    task_data = {
        'title': '原始任务',
        'description': '这是原始描述',
        'priority': 0
    }
    
    response = client.post(
        '/api/tasks',
        data=json.dumps(task_data),
        content_type='application/json',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 获取任务ID
    created_task = json.loads(response.data)
    task_id = created_task['id']
    
    # 更新任务数据
    update_data = {
        'title': '更新后的任务',
        'description': '这是更新后的描述',
        'priority': 1,
        'completed': True
    }
    
    response = client.put(
        f'/api/tasks/{task_id}',
        data=json.dumps(update_data),
        content_type='application/json',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 检查响应状态码
    assert response.status_code == 200
    
    # 检查更新后的任务
    updated_task = json.loads(response.data)
    assert updated_task['id'] == task_id
    assert updated_task['title'] == '更新后的任务'
    assert updated_task['description'] == '这是更新后的描述'
    assert updated_task['priority'] == 1
    assert updated_task['completed'] is True

# 测试删除任务
def test_delete_task(client, auth_token):
    """测试删除任务功能"""
    # 创建一个测试任务
    task_data = {
        'title': '要删除的任务',
        'description': '这个任务将被删除'
    }
    
    response = client.post(
        '/api/tasks',
        data=json.dumps(task_data),
        content_type='application/json',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 获取任务ID
    created_task = json.loads(response.data)
    task_id = created_task['id']
    
    # 删除任务
    response = client.delete(
        f'/api/tasks/{task_id}',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 检查响应状态码
    assert response.status_code == 200
    
    # 检查删除消息
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == '任务已删除'
    
    # 尝试获取已删除的任务，应返回404
    response = client.get(
        f'/api/tasks/{task_id}',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    assert response.status_code == 404

# 测试过滤任务
def test_filter_tasks(client, auth_token):
    """测试按状态和优先级过滤任务"""
    # 创建测试任务
    tasks = [
        {'title': '低优先级任务', 'priority': 0, 'completed': False},
        {'title': '中优先级任务', 'priority': 1, 'completed': False},
        {'title': '高优先级任务', 'priority': 2, 'completed': False},
        {'title': '已完成任务', 'priority': 1, 'completed': True}
    ]
    
    for task in tasks:
        client.post(
            '/api/tasks',
            data=json.dumps(task),
            content_type='application/json',
            headers={'Authorization': f'Bearer {auth_token}'}
        )
    
    # 按优先级过滤
    response = client.get(
        '/api/tasks?priority=2',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    data = json.loads(response.data)
    assert len(data['items']) == 1
    assert data['items'][0]['title'] == '高优先级任务'
    
    # 按完成状态过滤
    response = client.get(
        '/api/tasks?completed=true',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    data = json.loads(response.data)
    assert len(data['items']) == 1
    assert data['items'][0]['title'] == '已完成任务'
    
    # 综合过滤
    response = client.get(
        '/api/tasks?priority=1&completed=false',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    data = json.loads(response.data)
    assert len(data['items']) == 1
    assert data['items'][0]['title'] == '中优先级任务'

# 测试获取用户资料
def test_get_user_profile(client, auth_token):
    """测试获取用户资料功能"""
    response = client.get(
        '/api/user/profile',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    # 检查响应状态码
    assert response.status_code == 200
    
    # 检查用户信息
    user_data = json.loads(response.data)
    assert 'id' in user_data
    assert user_data['username'] == 'testuser'
    assert user_data['email'] == 'test@example.com'
    
    # 确保不返回密码
    assert 'password' not in user_data

# 测试使用无效token
def test_invalid_token(client):
    """测试使用无效令牌访问受保护资源"""
    response = client.get(
        '/api/tasks',
        headers={'Authorization': 'Bearer invalid_token'}
    )
    
    # 应该返回401未授权
    assert response.status_code == 401 