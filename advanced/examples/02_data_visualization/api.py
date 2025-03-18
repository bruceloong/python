#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数据可视化 - 后端API

这个文件提供了用于数据可视化的RESTful API，生成各种类型的数据集，
包括时间序列、分类数据、地理数据等，用于前端可视化展示。
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.datasets import make_blobs, make_moons
from datetime import datetime, timedelta
import random
import json
import os

# 创建Flask应用
app = Flask(__name__)
# 启用CORS，允许前端跨域请求
CORS(app)

# 生成时间序列数据
def generate_time_series(days=90):
    """生成随机时间序列数据"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # 创建时间索引
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # 生成多个指标的数据
    metrics = {
        'sales': np.random.randint(100, 500, len(date_range)) + np.sin(np.arange(len(date_range))/7) * 50,
        'traffic': np.random.randint(1000, 3000, len(date_range)) + np.sin(np.arange(len(date_range))/7) * 300,
        'users': np.random.randint(500, 1500, len(date_range)) + np.cos(np.arange(len(date_range))/14) * 200
    }
    
    # 转换为DataFrame
    df = pd.DataFrame(metrics, index=date_range)
    
    # 转换为JSON友好格式
    result = []
    for date, row in df.iterrows():
        result.append({
            'date': date.strftime('%Y-%m-%d'),
            'sales': round(float(row['sales']), 2),
            'traffic': round(float(row['traffic']), 2),
            'users': round(float(row['users']), 2)
        })
    
    return result

# 生成分类数据
def generate_category_data():
    """生成不同类别的数据"""
    categories = ['电子产品', '服装', '食品', '家居', '书籍', '健康', '玩具']
    metrics = ['销售额', '利润', '客户数']
    
    result = []
    for category in categories:
        sales = round(random.uniform(10000, 100000), 2)
        # 利润是销售额的一个比例
        profit = round(sales * random.uniform(0.1, 0.3), 2)
        customers = int(sales / random.uniform(50, 150))
        
        result.append({
            'category': category,
            '销售额': sales,
            '利润': profit,
            '客户数': customers
        })
    
    return result

# 生成地理数据
def generate_geo_data():
    """生成中国各省份的示例数据"""
    provinces = [
        '北京', '上海', '广东', '江苏', '浙江', '山东', '河南', '四川', '湖北', '湖南',
        '河北', '福建', '陕西', '辽宁', '江西', '安徽', '黑龙江', '广西', '内蒙古', '山西',
        '吉林', '云南', '贵州', '重庆', '天津', '甘肃', '新疆', '青海', '西藏', '宁夏', '海南'
    ]
    
    result = []
    for province in provinces:
        result.append({
            'name': province,
            'value': random.randint(100, 1000),
            'extraData': {
                'gdp': round(random.uniform(1000, 10000), 2),
                'population': random.randint(500, 5000) * 10000
            }
        })
    
    return result

# 生成散点图数据
def generate_scatter_data(n_samples=200):
    """生成散点图数据"""
    X, y = make_blobs(n_samples=n_samples, centers=4, cluster_std=1.0, random_state=42)
    
    result = []
    for i in range(len(X)):
        result.append({
            'x': float(X[i][0]),
            'y': float(X[i][1]),
            'category': int(y[i])
        })
    
    return result

# 生成网络图数据
def generate_network_data():
    """生成网络关系图数据"""
    # 节点
    nodes = []
    for i in range(20):
        category = random.randint(0, 3)
        size = random.randint(20, 50)
        nodes.append({
            'id': f'node{i}',
            'name': f'节点{i}',
            'category': category,
            'value': size,
            'symbolSize': size
        })
    
    # 边/关系
    links = []
    for i in range(30):
        source = random.randint(0, len(nodes)-1)
        target = random.randint(0, len(nodes)-1)
        # 避免自环
        while target == source:
            target = random.randint(0, len(nodes)-1)
        
        links.append({
            'source': f'node{source}',
            'target': f'node{target}',
            'value': random.randint(1, 10)
        })
    
    return {
        'nodes': nodes,
        'links': links
    }

# 生成仪表盘数据
def generate_gauge_data():
    """生成仪表盘数据"""
    metrics = ['CPU使用率', '内存使用率', '磁盘使用率', '网络负载', '电池电量']
    
    result = []
    for metric in metrics:
        if metric == '电池电量':
            value = random.randint(10, 100)
            result.append({
                'name': metric,
                'value': value,
                'target': 100
            })
        else:
            value = random.randint(30, 95)
            result.append({
                'name': metric,
                'value': value,
                'target': 80
            })
    
    return result

# API路由
@app.route('/api/data/time-series', methods=['GET'])
def time_series_data():
    """获取时间序列数据"""
    days = request.args.get('days', default=90, type=int)
    return jsonify(generate_time_series(days))

@app.route('/api/data/categories', methods=['GET'])
def category_data():
    """获取分类数据"""
    return jsonify(generate_category_data())

@app.route('/api/data/geo', methods=['GET'])
def geo_data():
    """获取地理数据"""
    return jsonify(generate_geo_data())

@app.route('/api/data/scatter', methods=['GET'])
def scatter_data():
    """获取散点图数据"""
    samples = request.args.get('samples', default=200, type=int)
    return jsonify(generate_scatter_data(samples))

@app.route('/api/data/network', methods=['GET'])
def network_data():
    """获取网络图数据"""
    return jsonify(generate_network_data())

@app.route('/api/data/gauge', methods=['GET'])
def gauge_data():
    """获取仪表盘数据"""
    return jsonify(generate_gauge_data())

@app.route('/api/data/all', methods=['GET'])
def all_data():
    """获取所有类型的样本数据"""
    return jsonify({
        'timeSeries': generate_time_series(30),
        'categories': generate_category_data(),
        'geo': generate_geo_data(),
        'scatter': generate_scatter_data(100),
        'network': generate_network_data(),
        'gauge': generate_gauge_data()
    })

# API根路径
@app.route('/api', methods=['GET'])
def api_root():
    """API根路径，返回可用端点信息"""
    return jsonify({
        'message': '数据可视化API',
        'version': '1.0',
        'endpoints': {
            'time-series': '/api/data/time-series?days={days}',
            'categories': '/api/data/categories',
            'geo': '/api/data/geo',
            'scatter': '/api/data/scatter?samples={samples}',
            'network': '/api/data/network',
            'gauge': '/api/data/gauge',
            'all': '/api/data/all'
        }
    })

# 主程序
if __name__ == '__main__':
    # 启动应用
    app.run(debug=True, port=5000) 