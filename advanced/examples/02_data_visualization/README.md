# 高级数据可视化示例 (Advanced Data Visualization Example)

这个项目展示了如何创建一个前后端分离的数据可视化 Web 应用，结合了 Flask RESTful API 和 Vue.js 前端，
使用 ECharts 库实现多种类型的交互式数据可视化效果。

## 功能特性 (Features)

- 前后端分离架构 (Front-end and Back-end Separation)
- RESTful API 设计 (RESTful API Design)
- 交互式数据可视化 (Interactive Data Visualization)
- 响应式用户界面 (Responsive UI)
- 多种图表类型 (Multiple Chart Types)
- 暗色模式支持 (Dark Mode Support)

## 图表类型 (Chart Types)

- 时间序列图 (Time Series Charts)
- 趋势分析 (Trend Analysis)
- 分类对比 (Category Comparison)
- 地理数据可视化 (Geographic Data Visualization)
- 散点图和聚类 (Scatter Plots and Clustering)
- 网络关系图 (Network Relationship Graphs)
- 桑基图 (Sankey Diagrams)
- 仪表盘 (Gauge Charts)
- 雷达图 (Radar Charts)

## 技术栈 (Tech Stack)

### 后端 (Backend)

- Python 3.x
- Flask (Web 框架)
- Flask-CORS (跨域资源共享)
- Pandas (数据处理)
- NumPy (数学计算)
- scikit-learn (数据生成)

### 前端 (Frontend)

- HTML5/CSS3
- JavaScript
- Vue.js (渐进式框架)
- Axios (HTTP 客户端)
- ECharts (可视化库)

## 项目结构 (Project Structure)

```
02_data_visualization/
├── api.py                  # 数据API，提供各种类型的数据
├── server.py               # 服务器启动脚本
├── requirements.txt        # 项目依赖
├── static/                 # 静态资源目录
│   ├── index.html          # 主HTML页面
│   ├── css/                # 样式表
│   │   └── styles.css      # 主样式表
│   └── js/                 # JavaScript脚本
│       ├── app.js          # Vue应用入口
│       └── charts.js       # ECharts配置和渲染
└── README.md               # 项目文档
```

## 数据结构 (Data Structure)

API 提供以下类型的数据：

1. **时间序列数据 (Time Series)**

   - 日期 (Date)
   - 销售额 (Sales)
   - 流量 (Traffic)
   - 用户数 (Users)

2. **分类数据 (Category Data)**

   - 类别 (Category)
   - 销售额 (Sales)
   - 利润 (Profit)
   - 客户数 (Customers)

3. **地理数据 (Geographic Data)**

   - 省份名称 (Province Name)
   - 数值 (Value)
   - 额外数据 (GDP, Population)

4. **散点图数据 (Scatter Data)**

   - X 坐标 (X Coordinate)
   - Y 坐标 (Y Coordinate)
   - 类别 (Category)

5. **网络图数据 (Network Data)**

   - 节点 (Nodes)
   - 连接 (Links)

6. **仪表盘数据 (Gauge Data)**
   - 指标名称 (Metric Name)
   - 当前值 (Current Value)
   - 目标值 (Target Value)

## API 端点 (API Endpoints)

| 端点                    | 方法 | 描述                   |
| ----------------------- | ---- | ---------------------- |
| `/api`                  | GET  | API 信息和可用端点列表 |
| `/api/data/time-series` | GET  | 获取时间序列数据       |
| `/api/data/categories`  | GET  | 获取分类数据           |
| `/api/data/geo`         | GET  | 获取地理数据           |
| `/api/data/scatter`     | GET  | 获取散点图数据         |
| `/api/data/network`     | GET  | 获取网络关系图数据     |
| `/api/data/gauge`       | GET  | 获取仪表盘数据         |
| `/api/data/all`         | GET  | 获取所有类型的数据     |

## 安装与运行 (Installation and Usage)

1. 安装依赖 (Install dependencies):

```
pip install -r requirements.txt
```

2. 运行应用 (Run the application):

```
python server.py
```

3. 在浏览器中访问 (Visit in browser):

```
http://127.0.0.1:5001
```

## 学习要点 (Learning Points)

通过本示例，您将学习：

1. **前后端分离架构**

   - RESTful API 设计
   - 前后端通信
   - 跨域资源共享

2. **数据处理与生成**

   - 使用 Pandas 处理数据
   - 生成模拟数据
   - 数据格式转换

3. **数据可视化技术**

   - 多种图表类型的实现
   - 交互式可视化
   - 数据驱动的 UI 更新

4. **Vue.js 应用开发**

   - 组件化开发
   - 响应式数据绑定
   - 生命周期管理

5. **服务器多线程**
   - 同时运行多个服务
   - 线程安全
   - 进程通信

## 扩展思路 (Extension Ideas)

- 添加实时数据更新功能 (Add real-time data updates)
- 实现数据导出功能 (Implement data export functionality)
- 添加用户认证 (Add user authentication)
- 连接真实数据源 (Connect to real data sources)
- 添加更多高级分析功能 (Add more advanced analytics features)
- 优化移动设备体验 (Optimize mobile experience)
- 添加图表注释和协作功能 (Add chart annotations and collaboration features)
