# RESTful API 示例

这个示例展示了如何使用 Flask 框架创建一个专业级别的 RESTful API，
实现了任务管理功能，包括用户认证、资源操作、参数验证等。

## 功能特性

- RESTful API 设计规范实现
- JWT (JSON Web Token) 认证
- 数据验证与错误处理
- SQLAlchemy ORM 数据库集成
- 资源表示与序列化
- 请求参数解析与验证
- 分页支持
- 筛选与排序
- 全面的测试套件

## 技术栈

- Flask - Web 框架
- Flask-RESTful - RESTful API 扩展
- Flask-SQLAlchemy - ORM 数据库集成
- Flask-JWT-Extended - JWT 认证
- SQLite - 数据库
- Pytest - 测试框架

## API 端点

| 端点                   | 方法   | 描述                      | 权限   |
| ---------------------- | ------ | ------------------------- | ------ |
| `/api`                 | GET    | API 根端点，获取 API 信息 | 公开   |
| `/api/auth/register`   | POST   | 用户注册                  | 公开   |
| `/api/auth/login`      | POST   | 用户登录，获取 JWT 令牌   | 公开   |
| `/api/tasks`           | GET    | 获取当前用户的任务列表    | 需认证 |
| `/api/tasks`           | POST   | 创建新任务                | 需认证 |
| `/api/tasks/<task_id>` | GET    | 获取特定任务详情          | 需认证 |
| `/api/tasks/<task_id>` | PUT    | 更新特定任务              | 需认证 |
| `/api/tasks/<task_id>` | DELETE | 删除特定任务              | 需认证 |
| `/api/user/profile`    | GET    | 获取当前用户资料          | 需认证 |

## 请求与响应示例

### 用户注册

**请求:**

```
POST /api/auth/register
Content-Type: application/json

{
  "username": "newuser",
  "password": "password123",
  "email": "user@example.com"
}
```

**成功响应:**

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "message": "用户创建成功"
}
```

### 用户登录

**请求:**

```
POST /api/auth/login
Content-Type: application/json

{
  "username": "newuser",
  "password": "password123"
}
```

**成功响应:**

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 创建任务

**请求:**

```
POST /api/tasks
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "title": "学习RESTful API",
  "description": "学习如何设计和实现RESTful API",
  "priority": 1,
  "due_date": "2023-12-31T23:59:59"
}
```

**成功响应:**

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "title": "学习RESTful API",
  "description": "学习如何设计和实现RESTful API",
  "completed": false,
  "due_date": "2023-12-31T23:59:59",
  "priority": 1,
  "created_at": "2023-06-15T10:30:00",
  "user_id": 1
}
```

## 安装与运行

1. 安装依赖:

   ```
   pip install -r requirements.txt
   ```

2. 运行应用:

   ```
   python api.py
   ```

3. 运行测试:
   ```
   pytest test_api.py -v
   ```

## 使用工具测试 API

可以使用如下工具测试 API:

- [curl](https://curl.se/) - 命令行工具
- [Postman](https://www.postman.com/) - API 测试工具
- [Insomnia](https://insomnia.rest/) - API 测试工具
- [HTTPie](https://httpie.io/) - 命令行 HTTP 客户端

## 学习要点

通过本示例，你将学习以下内容:

1. **RESTful API 设计原则**

   - 资源命名与 URL 设计
   - HTTP 方法使用
   - 状态码应用
   - 版本控制

2. **认证与授权**

   - JWT 工作原理
   - 令牌验证
   - 资源权限控制

3. **请求处理**

   - 参数解析与验证
   - 错误处理
   - 数据格式化

4. **数据库集成**

   - 模型设计
   - 关系定义
   - 查询构建

5. **测试策略**
   - 单元测试设计
   - 测试 fixture
   - 测试覆盖率

## 扩展学习方向

- 添加更复杂的查询和过滤功能
- 实现 API 速率限制
- 添加 API 文档(使用 Swagger/OpenAPI)
- 添加刷新令牌功能
- 实现 API 版本控制
- 添加缓存支持
- 实现基于角色的访问控制
