# Flask 基础示例 (Flask Basics Example)

这个示例展示了如何使用 Flask 框架创建一个简单的 Web 应用。
(This example demonstrates how to create a simple web application using the Flask framework.)

## 功能概述 (Feature Overview)

- 任务列表显示 (Task list display)
- 添加新任务 (Add new tasks)
- 查看任务详情 (View task details)
- 标记任务完成 (Mark tasks as completed)
- 删除任务 (Delete tasks)
- 错误处理 (Error handling)

## 文件结构 (File Structure)

- `app.py` - 主应用文件，包含所有路由和应用逻辑
- `templates/` - 包含所有 HTML 模板
  - `index.html` - 主页，显示任务列表
  - `about.html` - 关于页面
  - `task_details.html` - 任务详情页面
  - `task_form.html` - 添加任务表单
  - `404.html` - 404 错误页面
- `requirements.txt` - 项目依赖

## 学习要点 (Learning Points)

1. **Flask 应用创建与配置** (Flask Application Creation and Configuration)

   - 创建 Flask 应用实例
   - 设置密钥

2. **路由系统** (Routing System)

   - 基本 URL 路由
   - 带参数的路由
   - HTTP 方法限制

3. **模板渲染** (Template Rendering)

   - 使用 Jinja2 模板
   - 模板继承
   - 条件与循环

4. **表单处理** (Form Handling)

   - 获取表单数据
   - 表单验证

5. **用户反馈** (User Feedback)

   - Flash 消息系统

6. **重定向与 URL 生成** (Redirection and URL Generation)
   - 使用 redirect 和 url_for

## 如何运行 (How to Run)

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

## 进一步学习 (Further Learning)

- 尝试添加新的功能，如任务编辑或任务分类
  (Try adding new features, such as task editing or task categorization)
- 将内存中的任务列表替换为数据库存储
  (Replace the in-memory task list with database storage)
- 添加用户认证系统
  (Add a user authentication system)
- 改进 UI/UX 设计
  (Improve the UI/UX design)
