/**
 * 数据可视化应用主文件
 * 管理应用状态、处理API请求和UI交互
 */

// API配置
const API_BASE_URL = "http://127.0.0.1:5000/api";

// Vue应用实例
const app = new Vue({
  el: "#app",
  data: {
    // 应用状态
    loading: true,
    error: null,
    currentSection: "dashboard",
    timeRange: 30,

    // 数据存储
    timeSeriesData: [],
    categoryData: [],
    geoData: [],
    scatterData: [],
    networkData: null,
    gaugeData: [],

    // 图表实例
    charts: {},
  },

  // 生命周期钩子
  mounted() {
    // 初始化加载数据
    this.fetchData();

    // 监听窗口大小变化，调整图表大小
    window.addEventListener("resize", this.handleResize);
  },

  beforeDestroy() {
    // 移除事件监听器
    window.removeEventListener("resize", this.handleResize);

    // 销毁所有图表实例
    Object.keys(this.charts).forEach((key) => {
      if (this.charts[key]) {
        this.charts[key].dispose();
      }
    });
  },

  methods: {
    // 切换显示的部分
    switchSection(section) {
      this.currentSection = section;

      // 延迟执行以确保DOM已更新
      this.$nextTick(() => {
        this.handleResize();

        // 根据选择的部分加载相应的图表
        switch (section) {
          case "dashboard":
            this.renderDashboardCharts();
            break;
          case "time-series":
            this.renderTimeSeriesCharts();
            break;
          case "categories":
            this.renderCategoryCharts();
            break;
          case "geo":
            this.renderGeoCharts();
            break;
          case "advanced":
            this.renderAdvancedCharts();
            break;
        }
      });
    },

    // 从API获取所有数据
    fetchData() {
      this.loading = true;
      this.error = null;

      axios
        .get(`${API_BASE_URL}/data/all`)
        .then((response) => {
          // 保存数据
          this.timeSeriesData = response.data.timeSeries;
          this.categoryData = response.data.categories;
          this.geoData = response.data.geo;
          this.scatterData = response.data.scatter;
          this.networkData = response.data.network;
          this.gaugeData = response.data.gauge;

          // 加载完成
          this.loading = false;

          // 渲染当前部分的图表
          this.$nextTick(() => {
            this.switchSection(this.currentSection);
          });
        })
        .catch((error) => {
          this.loading = false;
          this.error = `获取数据时出错: ${error.message}`;
          console.error("获取数据出错:", error);
        });
    },

    // 获取特定时间范围的时间序列数据
    fetchTimeSeriesData() {
      this.loading = true;

      axios
        .get(`${API_BASE_URL}/data/time-series?days=${this.timeRange}`)
        .then((response) => {
          this.timeSeriesData = response.data;
          this.loading = false;

          // 更新图表
          this.$nextTick(() => {
            this.renderTimeSeriesCharts();
          });
        })
        .catch((error) => {
          this.loading = false;
          this.error = `获取时间序列数据时出错: ${error.message}`;
          console.error("获取时间序列数据出错:", error);
        });
    },

    // 渲染仪表板图表
    renderDashboardCharts() {
      // 渲染仪表盘
      this.charts.gauge = renderGaugeChart("gauge-chart", this.gaugeData);

      // 渲染销售概览
      const recentData = this.timeSeriesData.slice(-7); // 最近7天数据
      this.charts.salesOverview = renderSalesOverviewChart(
        "sales-overview-chart",
        recentData
      );

      // 渲染分类数据
      this.charts.categoryOverview = renderCategoryPieChart(
        "category-chart",
        this.categoryData
      );
    },

    // 渲染时间序列图表
    renderTimeSeriesCharts() {
      this.charts.timeSeries = renderTimeSeriesChart(
        "time-series-chart",
        this.timeSeriesData
      );
      this.charts.trend = renderTrendChart("trend-chart", this.timeSeriesData);
    },

    // 渲染分类数据图表
    renderCategoryCharts() {
      this.charts.categoryPie = renderCategoryPieChart(
        "category-pie-chart",
        this.categoryData
      );
      this.charts.categoryBar = renderCategoryBarChart(
        "category-bar-chart",
        this.categoryData
      );
      this.charts.radar = renderRadarChart("radar-chart", this.categoryData);
    },

    // 渲染地理数据图表
    renderGeoCharts() {
      this.charts.geo = renderGeoChart("geo-chart", this.geoData);
    },

    // 渲染高级图表
    renderAdvancedCharts() {
      this.charts.scatter = renderScatterChart(
        "scatter-chart",
        this.scatterData
      );
      this.charts.network = renderNetworkChart(
        "network-chart",
        this.networkData
      );
      this.charts.sankey = renderSankeyChart("sankey-chart", this.networkData);
    },

    // 处理窗口大小变化
    handleResize() {
      // 调整所有当前部分的图表大小
      Object.keys(this.charts).forEach((key) => {
        if (this.charts[key]) {
          this.charts[key].resize();
        }
      });
    },
  },
});
