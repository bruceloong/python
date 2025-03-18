/**
 * 数据可视化图表渲染文件
 * 包含各种图表的配置和渲染函数
 */

// 通用图表初始化函数
function initChart(containerId) {
  const container = document.getElementById(containerId);
  if (!container) {
    console.error(`图表容器未找到: ${containerId}`);
    return null;
  }

  // 初始化ECharts实例
  return echarts.init(container);
}

// 时间序列图表渲染
function renderTimeSeriesChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 准备数据
  const dates = data.map((item) => item.date);
  const sales = data.map((item) => item.sales);
  const traffic = data.map((item) => item.traffic);
  const users = data.map((item) => item.users);

  // 设置图表选项
  const option = {
    title: {
      text: "时间序列数据分析",
      left: "center",
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
        label: {
          backgroundColor: "#6a7985",
        },
      },
    },
    legend: {
      data: ["销售额", "流量", "用户数"],
      top: 30,
    },
    toolbox: {
      feature: {
        saveAsImage: { title: "保存为图片" },
      },
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: [
      {
        type: "category",
        boundaryGap: false,
        data: dates,
      },
    ],
    yAxis: [
      {
        type: "value",
        name: "销售额",
        position: "left",
      },
      {
        type: "value",
        name: "流量/用户数",
        position: "right",
      },
    ],
    series: [
      {
        name: "销售额",
        type: "line",
        smooth: true,
        lineStyle: {
          width: 3,
          shadowColor: "rgba(0,0,0,0.3)",
          shadowBlur: 10,
          shadowOffsetY: 8,
        },
        yAxisIndex: 0,
        data: sales,
      },
      {
        name: "流量",
        type: "line",
        smooth: true,
        yAxisIndex: 1,
        data: traffic,
      },
      {
        name: "用户数",
        type: "line",
        smooth: true,
        yAxisIndex: 1,
        data: users,
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 趋势分析图表
function renderTrendChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 准备数据
  const dates = data.map((item) => item.date);
  const sales = data.map((item) => item.sales);

  // 计算移动平均线 (7天)
  const movingAvg = [];
  for (let i = 0; i < sales.length; i++) {
    if (i < 6) {
      movingAvg.push("-");
      continue;
    }

    let sum = 0;
    for (let j = i - 6; j <= i; j++) {
      sum += sales[j];
    }
    movingAvg.push((sum / 7).toFixed(2));
  }

  // 设置图表选项
  const option = {
    title: {
      text: "销售趋势分析",
      left: "center",
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow",
      },
    },
    legend: {
      data: ["日销售额", "7日移动平均"],
      top: 30,
    },
    toolbox: {
      feature: {
        saveAsImage: { title: "保存为图片" },
      },
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: {
      type: "category",
      data: dates,
    },
    yAxis: {
      type: "value",
      name: "销售额",
    },
    series: [
      {
        name: "日销售额",
        type: "bar",
        data: sales,
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "#83bff6" },
            { offset: 0.5, color: "#188df0" },
            { offset: 1, color: "#188df0" },
          ]),
        },
      },
      {
        name: "7日移动平均",
        type: "line",
        smooth: true,
        data: movingAvg,
        symbolSize: 6,
        lineStyle: {
          width: 3,
        },
        itemStyle: {
          color: "#ff9f7f",
        },
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 销售概览图表
function renderSalesOverviewChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 准备数据
  const dates = data.map((item) => item.date);
  const sales = data.map((item) => item.sales);

  // 计算变化百分比
  const changes = [];
  for (let i = 1; i < sales.length; i++) {
    const change = (((sales[i] - sales[i - 1]) / sales[i - 1]) * 100).toFixed(
      2
    );
    changes.push(change);
  }
  changes.unshift("-"); // 第一天没有变化率

  // 设置图表选项
  const option = {
    title: {
      text: "最近七天销售概览",
      left: "center",
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
      },
      formatter: function (params) {
        const dateIndex = params[0].dataIndex;
        const changeText =
          changes[dateIndex] === "-"
            ? ""
            : `<br/>较前一天: <span style="color:${
                changes[dateIndex] >= 0 ? "#3dc371" : "#ec5050"
              }">${changes[dateIndex]}%</span>`;

        return `${dates[dateIndex]}<br/>${params[0].seriesName}: ${params[0].value}${changeText}`;
      },
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: {
      type: "category",
      data: dates,
    },
    yAxis: {
      type: "value",
      name: "销售额",
    },
    series: [
      {
        name: "销售额",
        type: "bar",
        data: sales,
        markLine: {
          data: [{ type: "average", name: "平均值" }],
          label: {
            formatter: "平均: {c}",
          },
        },
        itemStyle: {
          color: function (params) {
            // 设置颜色基于变化百分比
            if (params.dataIndex === 0) return "#3498db";

            const change = changes[params.dataIndex];
            if (change >= 0) {
              return "#3dc371";
            } else {
              return "#ec5050";
            }
          },
        },
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 分类饼图
function renderCategoryPieChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 准备数据
  const pieData = data.map((item) => ({
    name: item.category,
    value: item["销售额"],
  }));

  // 设置图表选项
  const option = {
    title: {
      text: "销售额分类分布",
      left: "center",
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b}: {c} ({d}%)",
    },
    legend: {
      orient: "vertical",
      left: 10,
      top: "middle",
      data: data.map((item) => item.category),
    },
    series: [
      {
        name: "销售额",
        type: "pie",
        radius: ["40%", "70%"],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 10,
          borderColor: "#fff",
          borderWidth: 2,
        },
        label: {
          show: false,
          position: "center",
        },
        emphasis: {
          label: {
            show: true,
            fontSize: "18",
            fontWeight: "bold",
          },
        },
        labelLine: {
          show: false,
        },
        data: pieData,
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 分类柱状图
function renderCategoryBarChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 准备数据
  const categories = data.map((item) => item.category);
  const sales = data.map((item) => item["销售额"]);
  const profits = data.map((item) => item["利润"]);
  const customers = data.map((item) => item["客户数"]);

  // 设置图表选项
  const option = {
    title: {
      text: "分类指标对比",
      left: "center",
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow",
      },
    },
    legend: {
      data: ["销售额", "利润", "客户数"],
      top: 30,
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: {
      type: "category",
      data: categories,
    },
    yAxis: [
      {
        type: "value",
        name: "金额",
        position: "left",
      },
      {
        type: "value",
        name: "客户数",
        position: "right",
      },
    ],
    series: [
      {
        name: "销售额",
        type: "bar",
        data: sales,
        yAxisIndex: 0,
      },
      {
        name: "利润",
        type: "bar",
        data: profits,
        yAxisIndex: 0,
      },
      {
        name: "客户数",
        type: "bar",
        data: customers,
        yAxisIndex: 1,
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 雷达图
function renderRadarChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 准备数据 - 归一化处理
  const indicators = [
    { name: "销售额", max: Math.max(...data.map((item) => item["销售额"])) },
    { name: "利润", max: Math.max(...data.map((item) => item["利润"])) },
    { name: "客户数", max: Math.max(...data.map((item) => item["客户数"])) },
  ];

  const seriesData = data.map((item) => ({
    value: [item["销售额"], item["利润"], item["客户数"]],
    name: item.category,
  }));

  // 设置图表选项
  const option = {
    title: {
      text: "分类指标雷达图",
      left: "center",
    },
    tooltip: {
      trigger: "item",
    },
    legend: {
      data: data.map((item) => item.category),
      top: 30,
    },
    radar: {
      indicator: indicators,
      radius: "65%",
    },
    series: [
      {
        type: "radar",
        data: seriesData,
        areaStyle: {},
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 地理数据图表
function renderGeoChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 设置图表选项
  const option = {
    title: {
      text: "中国区域数据分布",
      left: "center",
    },
    tooltip: {
      trigger: "item",
      formatter: function (params) {
        const data = params.data;
        if (!data) return params.name;

        return `${params.name}<br/>
                        数值: ${data.value}<br/>
                        GDP: ${data.extraData.gdp}<br/>
                        人口: ${(data.extraData.population / 10000).toFixed(
                          2
                        )}万`;
      },
    },
    visualMap: {
      min: 0,
      max: 1000,
      text: ["高", "低"],
      realtime: false,
      calculable: true,
      inRange: {
        color: ["#e0f3f8", "#045a8d"],
      },
    },
    series: [
      {
        name: "数据分布",
        type: "map",
        map: "china",
        emphasis: {
          label: {
            show: true,
          },
        },
        data: data,
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 散点图
function renderScatterChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 将数据按类别分组
  const categories = {};
  data.forEach((item) => {
    if (!categories[item.category]) {
      categories[item.category] = [];
    }
    categories[item.category].push([item.x, item.y]);
  });

  // 准备系列数据
  const seriesData = Object.keys(categories).map((category) => ({
    name: `聚类 ${category}`,
    type: "scatter",
    data: categories[category],
    symbolSize: 10,
  }));

  // 设置图表选项
  const option = {
    title: {
      text: "聚类散点图分析",
      left: "center",
    },
    tooltip: {
      trigger: "item",
      formatter: function (params) {
        return `${params.seriesName}<br/>
                        X: ${params.value[0].toFixed(2)}<br/>
                        Y: ${params.value[1].toFixed(2)}`;
      },
    },
    legend: {
      data: Object.keys(categories).map((category) => `聚类 ${category}`),
      top: 30,
    },
    grid: {
      left: "3%",
      right: "3%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: {
      type: "value",
      name: "X轴",
      scale: true,
    },
    yAxis: {
      type: "value",
      name: "Y轴",
      scale: true,
    },
    series: seriesData,
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 网络关系图
function renderNetworkChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 设置图表选项
  const option = {
    title: {
      text: "网络关系图",
      left: "center",
    },
    tooltip: {
      trigger: "item",
      formatter: function (params) {
        if (params.dataType === "node") {
          return `${params.data.name}<br/>类别: ${params.data.category}<br/>值: ${params.data.value}`;
        } else {
          return `${params.data.source} → ${params.data.target}<br/>强度: ${params.data.value}`;
        }
      },
    },
    legend: {
      data: ["类别0", "类别1", "类别2", "类别3"],
      top: 30,
    },
    series: [
      {
        name: "网络关系",
        type: "graph",
        layout: "force",
        data: data.nodes,
        links: data.links,
        categories: [
          { name: "类别0" },
          { name: "类别1" },
          { name: "类别2" },
          { name: "类别3" },
        ],
        roam: true,
        label: {
          show: true,
          position: "right",
        },
        force: {
          repulsion: 100,
          edgeLength: 50,
        },
        emphasis: {
          focus: "adjacency",
          lineStyle: {
            width: 5,
          },
        },
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 桑基图
function renderSankeyChart(containerId, networkData) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 从网络数据生成桑基图数据
  const nodes = networkData.nodes.map((node) => ({
    name: node.name,
  }));

  // 仅使用一部分连接避免桑基图过于复杂
  const links = networkData.links.slice(0, 15).map((link) => {
    const sourceNode = networkData.nodes.find((n) => n.id === link.source);
    const targetNode = networkData.nodes.find((n) => n.id === link.target);
    return {
      source: sourceNode.name,
      target: targetNode.name,
      value: link.value * 10, // 放大值以使其更明显
    };
  });

  // 设置图表选项
  const option = {
    title: {
      text: "数据流向图",
      left: "center",
    },
    tooltip: {
      trigger: "item",
      formatter: "{b} -> {c}",
    },
    series: [
      {
        name: "数据流",
        type: "sankey",
        layout: "none",
        data: nodes,
        links: links,
        emphasis: {
          focus: "adjacency",
        },
        lineStyle: {
          color: "gradient",
          curveness: 0.5,
        },
      },
    ],
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}

// 仪表盘图表
function renderGaugeChart(containerId, data) {
  const chart = initChart(containerId);
  if (!chart) return null;

  // 准备系列数据
  const seriesData = data
    .map((item, index) => {
      const colorStops =
        item.value > item.target
          ? [
              [0.3, "#91c7ae"],
              [0.7, "#63869e"],
              [1, "#c23531"],
            ]
          : [
              [0.3, "#67e0e3"],
              [0.7, "#91c7ae"],
              [1, "#c23531"],
            ];

      return {
        name: item.name,
        type: "gauge",
        min: 0,
        max: 100,
        radius: `${86 - index * 14}%`,
        axisLine: {
          lineStyle: {
            width: 10,
            color: colorStops,
          },
        },
        pointer: {
          itemStyle: {
            color: "auto",
          },
        },
        axisTick: {
          distance: -10,
          length: 5,
          lineStyle: {
            color: "#fff",
          },
        },
        splitLine: {
          distance: -10,
          length: 16,
          lineStyle: {
            color: "#fff",
          },
        },
        axisLabel: {
          distance: -20,
          color: "auto",
          fontSize: 12,
        },
        detail: {
          valueAnimation: true,
          formatter: "{value}%",
          color: "auto",
        },
        data: [{ value: item.value, name: item.name }],
        title: {
          offsetCenter: [0, `${-9 + index * 2.5}%`],
        },
      };
    })
    .slice(0, 3); // 最多显示3个仪表盘

  // 设置图表选项
  const option = {
    series: seriesData,
  };

  // 应用配置
  chart.setOption(option);
  return chart;
}
