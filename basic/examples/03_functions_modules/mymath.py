#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自定义数学模块 (mymath)
包含一些基本的数学运算函数。

这是一个演示如何创建和使用Python模块的例子。
"""

# 模块级变量 (Module level variables)
PI = 3.14159265359
E = 2.71828182846

def add(a, b):
    """
    计算两个数的和
    (Calculate the sum of two numbers)
    
    参数:
        a (number): 第一个数
        b (number): 第二个数
        
    返回:
        number: 两个数的和
    """
    return a + b

def subtract(a, b):
    """
    计算两个数的差
    (Calculate the difference between two numbers)
    
    参数:
        a (number): 被减数
        b (number): 减数
        
    返回:
        number: a减去b的结果
    """
    return a - b

def multiply(a, b):
    """
    计算两个数的乘积
    (Calculate the product of two numbers)
    
    参数:
        a (number): 第一个数
        b (number): 第二个数
        
    返回:
        number: 两个数的乘积
    """
    return a * b

def divide(a, b):
    """
    计算两个数的商
    (Calculate the quotient of two numbers)
    
    参数:
        a (number): 被除数
        b (number): 除数
        
    返回:
        number: a除以b的结果
        
    异常:
        ZeroDivisionError: 当b为0时抛出
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为零 (Divisor cannot be zero)")
    return a / b

def power(base, exponent):
    """
    计算幂
    (Calculate power)
    
    参数:
        base (number): 底数
        exponent (number): 指数
        
    返回:
        number: 底数的指数次方
    """
    return base ** exponent

def square(x):
    """
    计算平方
    (Calculate square)
    
    参数:
        x (number): 要求平方的数
        
    返回:
        number: x的平方
    """
    return power(x, 2)

def cube(x):
    """
    计算立方
    (Calculate cube)
    
    参数:
        x (number): 要求立方的数
        
    返回:
        number: x的立方
    """
    return power(x, 3)

def factorial(n):
    """
    计算阶乘
    (Calculate factorial)
    
    参数:
        n (int): 要计算阶乘的非负整数
        
    返回:
        int: n的阶乘
        
    异常:
        ValueError: 当n为负数时抛出
    """
    if not isinstance(n, int):
        raise TypeError("n必须是整数 (n must be an integer)")
    if n < 0:
        raise ValueError("n必须是非负数 (n must be a non-negative number)")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """
    判断一个数是否是质数
    (Check if a number is prime)
    
    参数:
        n (int): 要检查的整数
        
    返回:
        bool: 如果n是质数则返回True，否则返回False
    """
    if not isinstance(n, int):
        raise TypeError("n必须是整数 (n must be an integer)")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 函数的别名 (Function aliases)
sum_numbers = add  # 为add函数创建别名 (Create an alias for the add function)

# 当模块被直接运行时执行的代码 (Code that executes when the module is run directly)
if __name__ == "__main__":
    print("mymath模块正在作为脚本运行 (mymath module is running as a script)")
    print(f"PI = {PI}")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 x 7 = {multiply(6, 7)}")
    print(f"20 ÷ 5 = {divide(20, 5)}")
    print(f"2³ = {power(2, 3)}")
    print(f"4² = {square(4)}")
    print(f"3³ = {cube(3)}")
    print(f"5! = {factorial(5)}")
    print(f"17是质数吗？{is_prime(17)}")
else:
    print("mymath模块已被导入 (mymath module has been imported)") 