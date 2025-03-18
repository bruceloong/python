#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hello World示例
这是Python学习的第一个程序，展示了Python的基本语法和输出功能。
"""

# 这是单行注释 (This is a single line comment)

"""
这是多行注释
可以跨越多行
(This is a multi-line comment that can span multiple lines)
"""

# 基本输出语句 (Basic print statement)
print("Hello, World!")  # 输出Hello, World!

# 使用变量 (Using variables)
message = "你好，世界！"  # 定义一个变量 (Define a variable)
print(message)          # 输出变量内容 (Print the variable content)

# 字符串连接 (String concatenation)
first_name = "Python"
last_name = "程序员"
full_name = first_name + " " + last_name  # 使用+连接字符串 (Connect strings using +)
print("欢迎, " + full_name + "!")         # 输出连接后的字符串 (Print concatenated string)

# 使用f-strings(Python 3.6+)格式化字符串 (Using f-strings for string formatting)
print(f"欢迎, {first_name} {last_name}!")  # 更现代的字符串格式化方法 (Modern string formatting)

# 数字运算 (Numeric operations)
a = 5
b = 3
print(f"加法: {a} + {b} = {a + b}")  # 加法 (Addition)
print(f"减法: {a} - {b} = {a - b}")  # 减法 (Subtraction)
print(f"乘法: {a} * {b} = {a * b}")  # 乘法 (Multiplication)
print(f"除法: {a} / {b} = {a / b}")  # 除法 (Division)

# 获取用户输入 (Getting user input)
user_name = input("请输入你的名字 (Please enter your name): ")
print(f"你好, {user_name}! 欢迎学习Python! (Hello, {user_name}! Welcome to Python!)")

# 程序结束提示 (Program end notification)
print("程序执行完毕! (Program execution completed!)") 