# Web 任务管理器项目 (Web Task Manager Project)

这是一个完整的 Web 任务管理应用，结合了 Flask 框架和 SQLite 数据库，实现了一个功能齐全的任务管理系统。
(This is a complete web task management application that combines the Flask framework with SQLite database to implement a fully-featured task management system.)

## 项目概述 (Project Overview)

本项目是 Python 学习过程中的综合实践项目，整合了之前学习的多个技术点，包括：
(This project is a comprehensive practical project in the Python learning process, integrating multiple technical points learned previously, including:)

- Flask Web 框架 (Flask Web Framework)
- SQLite 数据库 (SQLite Database)
- 用户认证与授权 (User Authentication and Authorization)
- 表单处理与验证 (Form Processing and Validation)
- 响应式 Web 设计 (Responsive Web Design)

## 功能特性 (Features)

### 用户管理 (User Management)

- 用户注册 (User Registration)
- 用户登录 (User Login)
- 用户注销 (User Logout)

### 任务管理 (Task Management)

- 创建新任务 (Create New Tasks)
- 查看任务列表 (View Task List)
- 按状态、分类和优先级过滤任务 (Filter Tasks by Status, Category, and Priority)
- 编辑现有任务 (Edit Existing Tasks)
- 标记任务为已完成/未完成 (Mark Tasks as Completed/Pending)
- 删除任务 (Delete Tasks)

### 分类管理 (Category Management)

- 创建任务分类 (Create Task Categories)
- 编辑分类 (Edit Categories)
- 删除分类 (Delete Categories)

### 数据可视化 (Data Visualization)

- 仪表板概览 (Dashboard Overview)
- 任务统计 (Task Statistics)
- 按分类统计任务数量 (Task Count by Category)

## 技术栈 (Technology Stack)

- **后端** (Backend):

  - Python 3.x
  - Flask Web 框架 (Flask Web Framework)
  - SQLite 数据库 (SQLite Database)
  - Flask-Login (用户会话管理)
  - Flask-WTF (表单处理与验证)

- **前端** (Frontend):
  - HTML5
  - CSS3 (响应式设计)
  - JavaScript
  - 自定义 CSS 框架 (Custom CSS Framework)

## 项目结构 (Project Structure)

```
07_web_task_manager/
├── app.py                  # 主应用文件
├── tasks.db                # SQLite数据库文件
├── static/                 # 静态资源目录
│   ├── styles.css          # 主样式表
│   ├── script.js           # JavaScript脚本
│   └── images/             # 图片资源
├── templates/              # HTML模板目录
│   ├── base.html           # 基础模板
│   ├── index.html          # 首页
│   ├── dashboard.html      # 用户仪表板
│   ├── auth/               # 认证相关模板
│   │   ├── login.html      # 登录页面
│   │   └── register.html   # 注册页面
│   ├── tasks/              # 任务相关模板
│   │   ├── list.html       # 任务列表
│   │   └── form.html       # 任务表单(添加/编辑)
│   └── categories/         # 分类相关模板
│       ├── list.html       # 分类列表
│       └── form.html       # 分类表单(添加/编辑)
└── requirements.txt        # 项目依赖
```

## 数据库设计 (Database Design)

### 用户表 (Users Table)

- id: 用户 ID (User ID)
- username: 用户名 (Username)
- password: 密码哈希 (Password Hash)
- email: 电子邮件 (Email)
- created_at: 创建时间 (Creation Time)

### 分类表 (Categories Table)

- id: 分类 ID (Category ID)
- name: 分类名称 (Category Name)
- user_id: 用户 ID (User ID) - 外键 (Foreign Key)

### 任务表 (Tasks Table)

- id: 任务 ID (Task ID)
- title: 任务标题 (Task Title)
- description: 任务描述 (Task Description)
- created_at: 创建时间 (Creation Time)
- due_date: 截止日期 (Due Date)
- priority: 优先级 (Priority) - 0(低)，1(中)，2(高)
- completed: 完成状态 (Completion Status) - 0(未完成)，1(已完成)
- user_id: 用户 ID (User ID) - 外键 (Foreign Key)
- category_id: 分类 ID (Category ID) - 外键 (Foreign Key)

## 安装与运行 (Installation and Running)

1. 安装依赖 (Install dependencies):

   ```
   pip install -r requirements.txt
   ```

2. 运行应用 (Run the application):

   ```
   python app.py
   ```

3. 在浏览器中访问 (Visit in your browser):
   ```
   http://127.0.0.1:5000/
   ```

## 默认用户 (Default Users)

应用会自动创建两个默认用户用于测试：
(The application automatically creates two default users for testing:)

1. 管理员用户 (Admin User):

   - 用户名 (Username): admin
   - 密码 (Password): password

2. 普通用户 (Regular User):
   - 用户名 (Username): user
   - 密码 (Password): password

## 学习要点 (Learning Points)

通过本项目，你将学习：
(Through this project, you will learn:)

1. **Flask 应用结构化** (Flask Application Structuring)

   - 路由设计 (Route Design)
   - 应用配置 (Application Configuration)
   - 错误处理 (Error Handling)

2. **用户认证与授权** (User Authentication and Authorization)

   - 密码哈希 (Password Hashing)
   - 会话管理 (Session Management)
   - 装饰器用于保护路由 (Decorators for Route Protection)

3. **数据库集成** (Database Integration)

   - SQLite 数据库连接 (SQLite Database Connection)
   - 数据库模式设计 (Database Schema Design)
   - SQL 查询与事务 (SQL Queries and Transactions)

4. **Web 前端** (Web Frontend)

   - 响应式 CSS 设计 (Responsive CSS Design)
   - 表单处理 (Form Handling)
   - 客户端交互 (Client-side Interactions)

5. **应用功能实现** (Application Feature Implementation)
   - CRUD 操作 (CRUD Operations)
   - 数据过滤与搜索 (Data Filtering and Searching)
   - 用户体验优化 (User Experience Optimization)

## 进一步改进 (Further Improvements)

可以考虑以下方向进行项目扩展：
(Consider the following directions for project expansion:)

- 添加搜索功能 (Add search functionality)
- 实现任务重复周期 (Implement task recurrence cycles)
- 添加标签系统 (Add a tagging system)
- 集成电子邮件提醒 (Integrate email reminders)
- 实现团队协作功能 (Implement team collaboration features)
- 添加 API 接口 (Add API interfaces)
- 添加数据导入/导出功能 (Add data import/export functions)
