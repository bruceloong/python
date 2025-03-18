#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
函数基础示例
展示Python中函数的定义、参数传递和返回值的用法。
"""

# 1. 基本函数定义 (Basic function definition)
print("===== 基本函数定义 (Basic function definition) =====")

def greet():
    """简单问候函数 (Simple greeting function)"""
    print("你好，世界！(Hello, World!)")

# 调用函数 (Calling the function)
greet()

# 2. 带参数的函数 (Function with parameters)
print("\n===== 带参数的函数 (Function with parameters) =====")

def greet_person(name):
    """
    向指定的人问候
    (Greet a specific person)
    
    参数:
        name (str): 被问候的人的名字
    """
    print(f"你好，{name}！(Hello, {name}!)")

# 调用带参数的函数 (Calling function with parameter)
greet_person("张三")
greet_person("李四")

# 3. 返回值 (Return values)
print("\n===== 返回值 (Return values) =====")

def add_numbers(a, b):
    """
    将两个数相加并返回结果
    (Add two numbers and return the result)
    
    参数:
        a (number): 第一个数
        b (number): 第二个数
    
    返回:
        number: 两个数的和
    """
    return a + b

# 使用函数返回值 (Using function return value)
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# 直接使用返回值 (Directly using return value)
print(f"10 + 20 = {add_numbers(10, 20)}")

# 4. 默认参数值 (Default parameter values)
print("\n===== 默认参数值 (Default parameter values) =====")

def greet_with_title(name, title="先生"):
    """
    使用称谓问候一个人
    (Greet a person with a title)
    
    参数:
        name (str): 人名
        title (str, optional): 称谓. 默认是"先生"
    """
    print(f"你好，{name}{title}！(Hello, {title} {name}!)")

# 使用默认参数 (Using default parameter)
greet_with_title("王五")
# 覆盖默认参数 (Overriding default parameter)
greet_with_title("李娜", "女士")

# 5. 关键字参数 (Keyword arguments)
print("\n===== 关键字参数 (Keyword arguments) =====")

def describe_person(name, age, city):
    """打印人物描述 (Print person description)"""
    print(f"{name}今年{age}岁，住在{city}。")
    print(f"({name} is {age} years old and lives in {city}.)")

# 使用位置参数 (Using positional arguments)
describe_person("张三", 30, "北京")
# 使用关键字参数 (Using keyword arguments)
describe_person(city="上海", name="李四", age=25)
# 混合使用位置和关键字参数 (Mixing positional and keyword arguments)
describe_person("王五", city="广州", age=35)

# 6. 可变数量参数 *args (Variable number of arguments *args)
print("\n===== 可变数量参数 *args (Variable number of arguments *args) =====")

def calculate_sum(*numbers):
    """
    计算任意数量参数的总和
    (Calculate the sum of any number of arguments)
    
    参数:
        *numbers: 任意数量的数字
        
    返回:
        float: 所有数字的总和
    """
    total = 0
    for num in numbers:
        total += num
    return total

# 使用不同数量的参数调用函数 (Calling with different number of arguments)
print(f"总和: {calculate_sum(1, 2, 3)}")
print(f"总和: {calculate_sum(10, 20, 30, 40, 50)}")
print(f"总和: {calculate_sum()}")  # 没有参数 (No arguments)

# 7. 关键字可变数量参数 **kwargs (Variable number of keyword arguments **kwargs)
print("\n===== 关键字可变数量参数 **kwargs (Variable number of keyword arguments **kwargs) =====")

def print_person_info(**info):
    """
    打印一个人的所有信息
    (Print all information about a person)
    
    参数:
        **info: 人物的任意属性和值
    """
    print("人物信息 (Person Information):")
    for key, value in info.items():
        print(f"- {key}: {value}")

# 使用不同的关键字参数调用 (Calling with different keyword arguments)
print_person_info(name="张三", age=30, city="北京", job="工程师")
print_person_info(name="李四", age=25, married=False)

# 8. 多返回值 (Multiple return values)
print("\n===== 多返回值 (Multiple return values) =====")

def get_dimensions(area, ratio=1.5):
    """
    根据面积和比例计算尺寸
    (Calculate dimensions based on area and ratio)
    
    参数:
        area (float): 面积
        ratio (float, optional): 长宽比. 默认是1.5
        
    返回:
        tuple: (宽度, 高度)
    """
    width = (area / ratio) ** 0.5
    height = width * ratio
    return width, height

# 接收多个返回值 (Receiving multiple return values)
width, height = get_dimensions(120)
print(f"宽度: {width:.2f}, 高度: {height:.2f}")
print(f"(Width: {width:.2f}, Height: {height:.2f})")

# 将返回值作为元组接收 (Receiving return values as a tuple)
dimensions = get_dimensions(200, 2)
print(f"尺寸: {dimensions}")
print(f"宽度: {dimensions[0]:.2f}, 高度: {dimensions[1]:.2f}")

# 9. 文档字符串 (Docstrings)
print("\n===== 文档字符串 (Docstrings) =====")

def calculate_circle_area(radius):
    """
    计算圆的面积
    (Calculate the area of a circle)
    
    参数:
        radius (float): 圆的半径
        
    返回:
        float: 圆的面积
        
    示例:
        >>> calculate_circle_area(2)
        12.56637...
    """
    import math
    return math.pi * radius ** 2

# 打印函数的文档字符串 (Print the function's docstring)
print(calculate_circle_area.__doc__)

area = calculate_circle_area(5)
print(f"半径为5的圆的面积: {area:.2f}")
print(f"(Area of a circle with radius 5: {area:.2f})")

# 10. 作用域和命名空间 (Scope and namespaces)
print("\n===== 作用域和命名空间 (Scope and namespaces) =====")

global_var = "全局变量 (global variable)"

def demonstrate_scope():
    local_var = "局部变量 (local variable)"
    print(f"函数内，本地变量: {local_var}")
    print(f"函数内，全局变量: {global_var}")
    
    # 修改全局变量 (Modifying global variable)
    # 注意：这实际上创建了一个同名的局部变量
    # (Note: This actually creates a local variable with the same name)
    # global_var = "修改后的全局变量"  # 取消注释会导致错误 (Uncommenting would cause an error)
    
    # 正确修改全局变量 (Correctly modifying global variable)
    global global_var  # 声明使用全局变量 (Declare using global variable)
    global_var = "修改后的全局变量 (modified global variable)"

# 调用函数 (Call the function)
demonstrate_scope()
print(f"函数外，全局变量: {global_var}")

# 11. 嵌套函数 (Nested functions)
print("\n===== 嵌套函数 (Nested functions) =====")

def outer_function(x):
    """外部函数 (Outer function)"""
    print(f"外部函数收到参数 x = {x} (Outer function received parameter x = {x})")
    
    def inner_function(y):
        """内部函数 (Inner function)"""
        print(f"内部函数收到参数 y = {y} (Inner function received parameter y = {y})")
        return x + y
    
    return inner_function  # 返回内部函数 (Return the inner function)

# 使用嵌套函数 (Using nested functions)
add_five = outer_function(5)  # 创建一个始终加5的函数 (Create a function that always adds 5)
print(f"10 + 5 = {add_five(10)}")
print(f"20 + 5 = {add_five(20)}")

# 12. Lambda函数（匿名函数） (Lambda functions (anonymous functions))
print("\n===== Lambda函数 (Lambda functions) =====")

# 使用常规函数计算平方 (Using regular function to calculate square)
def square(x):
    return x ** 2

# 等效的lambda函数 (Equivalent lambda function)
square_lambda = lambda x: x ** 2

print(f"平方(5) = {square(5)}")
print(f"平方_lambda(5) = {square_lambda(5)}")

# 实际使用lambda的场景 - 排序 (Practical use of lambda - sorting)
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]

# 使用lambda作为排序键 (Using lambda as a sort key)
students_sorted = sorted(students, key=lambda student: student["score"], reverse=True)
print("按成绩排序后的学生 (Students sorted by score):")
for student in students_sorted:
    print(f"{student['name']}: {student['score']}")

print("\n程序执行完毕! (Program execution completed!)") 