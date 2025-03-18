#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
条件语句示例
展示Python中的if-elif-else条件语句结构和使用方法。
"""

# 1. 基本的if语句 (Basic if statement)
print("===== 基本的if语句 (Basic if statement) =====")
age = 18

if age >= 18:
    print("你已成年 (You are an adult)")

# 2. if-else语句 (if-else statement)
print("\n===== if-else语句 (if-else statement) =====")
temperature = 15

if temperature > 20:
    print("天气温暖 (The weather is warm)")
else:
    print("天气凉爽 (The weather is cool)")

# 3. if-elif-else语句 (if-elif-else statement)
print("\n===== if-elif-else语句 (if-elif-else statement) =====")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"分数: {score}, 等级: {grade} (Score: {score}, Grade: {grade})")

# 4. 嵌套的if语句 (Nested if statements)
print("\n===== 嵌套的if语句 (Nested if statements) =====")
user_is_admin = True
user_is_active = True

if user_is_admin:
    if user_is_active:
        print("活跃管理员 (Active administrator)")
    else:
        print("非活跃管理员 (Inactive administrator)")
else:
    if user_is_active:
        print("活跃普通用户 (Active regular user)")
    else:
        print("非活跃普通用户 (Inactive regular user)")

# 5. 条件表达式（三元运算符） (Conditional expressions / Ternary operator)
print("\n===== 条件表达式 (Conditional expressions) =====")
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"年龄: {age}, 状态: {status} (Age: {age}, Status: {status})")

# 6. 逻辑运算符 (Logical operators)
print("\n===== 逻辑运算符 (Logical operators) =====")
has_passport = True
has_visa = False

if has_passport and has_visa:
    print("可以出国旅行 (Can travel abroad)")
else:
    print("不能出国旅行 (Cannot travel abroad)")

if has_passport or has_visa:
    print("至少有一个旅行证件 (Have at least one travel document)")
else:
    print("没有任何旅行证件 (Have no travel documents)")

# not 运算符 (not operator)
is_weekend = False
if not is_weekend:
    print("工作日 (Weekday)")
else:
    print("周末 (Weekend)")

# 7. 真值测试 (Truthy and Falsy values)
print("\n===== 真值测试 (Truthy and Falsy values) =====")
"""
在Python中，以下值被视为False：
- False
- None
- 0（整数）
- 0.0（浮点数）
- 空字符串 ("")
- 空列表 ([])
- 空字典 ({})
- 空元组 (())
- 空集合 (set())

其他所有值都被视为True

(In Python, the following values are considered False:
- False
- None
- 0 (integer)
- 0.0 (float)
- Empty string ("")
- Empty list ([])
- Empty dictionary ({})
- Empty tuple (())
- Empty set (set())

All other values are considered True)
"""

# 空列表测试 (Empty list test)
items = []
if items:
    print("列表不为空 (List is not empty)")
else:
    print("列表为空 (List is empty)")

# 非零数值测试 (Non-zero numeric test)
count = 0
if count:
    print("计数不为零 (Count is not zero)")
else:
    print("计数为零 (Count is zero)")

# 字符串测试 (String test)
name = "Python"
if name:
    print(f"名称是: {name} (Name is: {name})")
else:
    print("名称为空 (Name is empty)")

# 8. 成员测试运算符 (Membership operators)
print("\n===== 成员测试运算符 (Membership operators) =====")
fruits = ["苹果", "香蕉", "草莓"]

fruit = "苹果"
if fruit in fruits:
    print(f"{fruit} 在水果列表中 ({fruit} is in the fruits list)")
else:
    print(f"{fruit} 不在水果列表中 ({fruit} is not in the fruits list)")

fruit = "橙子"
if fruit not in fruits:
    print(f"{fruit} 不在水果列表中 ({fruit} is not in the fruits list)")
else:
    print(f"{fruit} 在水果列表中 ({fruit} is in the fruits list)")

# 9. 身份运算符 (Identity operators)
print("\n===== 身份运算符 (Identity operators) =====")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # 值相等 (Values are equal)
print(f"a is b: {a is b}")  # 但不是同一个对象 (But not the same object)
print(f"a is c: {a is c}")  # a和c是同一个对象 (a and c are the same object)

none_val = None
if none_val is None:
    print("值为None (Value is None)")
else:
    print("值不为None (Value is not None)")

print("\n程序执行完毕! (Program execution completed!)") 