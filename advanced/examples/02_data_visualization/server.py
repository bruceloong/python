#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数据可视化应用服务器
启动后端API服务器并提供静态文件服务
"""

import os
import sys
import webbrowser
from flask import Flask, send_from_directory, redirect
from flask_cors import CORS
import threading
import time
import api

# 创建应用
app = Flask(__name__)
CORS(app)

# 静态文件目录
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# 路由 - 根目录重定向到index.html
@app.route('/')
def index():
    return redirect('/index.html')

# 路由 - 提供静态文件
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(STATIC_DIR, path)

# 在单独的线程中启动API服务器
def run_api_server():
    api.app.run(port=5000, debug=False, use_reloader=False)

# 在单独的线程中启动Web服务器
def run_web_server():
    app.run(port=5001, debug=False, use_reloader=False)

# 在浏览器中打开应用
def open_browser():
    # 等待服务器启动
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:5001')

if __name__ == '__main__':
    print("正在启动数据可视化应用...")
    
    # 检查是否需要在浏览器中打开应用
    should_open_browser = '--no-browser' not in sys.argv
    
    # 启动API服务器线程
    api_thread = threading.Thread(target=run_api_server)
    api_thread.daemon = True
    api_thread.start()
    print("API服务器已启动 (端口5000)")
    
    # 如果需要，打开浏览器
    if should_open_browser:
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
    
    # 启动Web服务器（主线程）
    print("Web服务器已启动 (端口5001)")
    print("访问 http://127.0.0.1:5001 打开应用")
    app.run(port=5001, debug=False, use_reloader=False) 