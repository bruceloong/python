#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
循环语句示例
展示Python中的for和while循环结构及其用法。
"""

# 1. for循环基础 (Basic for loop)
print("===== for循环基础 (Basic for loop) =====")

# 遍历列表 (Iterating through a list)
fruits = ["苹果", "香蕉", "橙子", "草莓"]
print("水果列表 (Fruit list):")
for fruit in fruits:
    print(f"- {fruit}")

# 使用range()函数 (Using the range() function)
print("\n使用range()函数 (Using the range() function):")
print("range(5):")
for i in range(5):  # 从0到4 (from 0 to 4)
    print(i, end=" ")
print()  # 换行 (newline)

print("\nrange(1, 6):")
for i in range(1, 6):  # 从1到5 (from 1 to 5)
    print(i, end=" ")
print()

print("\nrange(1, 10, 2):")
for i in range(1, 10, 2):  # 从1到9，步长为2 (from 1 to 9, step 2)
    print(i, end=" ")
print()

# 2. while循环基础 (Basic while loop)
print("\n===== while循环基础 (Basic while loop) =====")
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1  # 增加计数 (increment counter)

# 3. break语句 (break statement)
print("\n===== break语句 (break statement) =====")
print("在遇到'橙子'时中断循环 (Break loop when 'orange' is encountered):")
for fruit in fruits:
    if fruit == "橙子":
        print(f"找到了{fruit}，中断循环 (Found {fruit}, breaking loop)")
        break
    print(f"处理: {fruit} (Processing: {fruit})")

# 使用while循环中的break (break in while loop)
print("\n在while循环中使用break (Using break in while loop):")
num = 0
while True:  # 无限循环 (infinite loop)
    print(f"数字: {num}")
    num += 1
    if num >= 5:
        print("达到5，中断循环 (Reached 5, breaking loop)")
        break

# 4. continue语句 (continue statement)
print("\n===== continue语句 (continue statement) =====")
print("跳过偶数 (Skip even numbers):")
for i in range(1, 10):
    if i % 2 == 0:  # 如果i是偶数 (if i is even)
        continue
    print(i, end=" ")
print()

# 5. else子句 (else clause)
print("\n===== 循环的else子句 (else clause with loops) =====")
print("在循环正常完成时执行else (Execute else when loop completes normally):")
for i in range(3):
    print(f"循环中: {i} (In loop: {i})")
else:
    print("循环正常完成 (Loop completed normally)")

print("\n当循环被break中断时，else不执行 (else not executed when loop is broken):")
for i in range(3):
    print(f"循环中: {i} (In loop: {i})")
    if i == 1:
        print("遇到break，中断循环 (Encountered break, interrupting loop)")
        break
else:
    print("这不会被执行 (This won't be executed)")

# 6. 嵌套循环 (Nested loops)
print("\n===== 嵌套循环 (Nested loops) =====")
print("乘法表 (Multiplication table) (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()  # 换行 (newline)

# 7. 列表推导式 (List comprehensions)
print("\n===== 列表推导式 (List comprehensions) =====")
# 传统方式 (Traditional way)
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(f"平方 (Traditional): {squares}")

# 使用列表推导式 (Using list comprehension)
squares_comp = [x ** 2 for x in range(1, 6)]
print(f"平方 (Comprehension): {squares_comp}")

# 带条件的列表推导式 (List comprehension with condition)
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"偶数的平方 (Even squares): {even_squares}")

# 8. 字典推导式 (Dictionary comprehensions)
print("\n===== 字典推导式 (Dictionary comprehensions) =====")
names = ["Alice", "Bob", "Charlie", "David"]
name_lengths = {name: len(name) for name in names}
print(f"名字长度 (Name lengths): {name_lengths}")

# 9. 集合推导式 (Set comprehensions)
print("\n===== 集合推导式 (Set comprehensions) =====")
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x ** 2 for x in numbers}
print(f"唯一平方 (Unique squares): {unique_squares}")

# 10. 生成器表达式 (Generator expressions)
print("\n===== 生成器表达式 (Generator expressions) =====")
# 使用()代替[]创建生成器而不是列表 (Use () instead of [] to create a generator instead of a list)
sum_of_squares = sum(x ** 2 for x in range(1, 6))
print(f"平方和 (Sum of squares): {sum_of_squares}")

# 11. 循环技巧 (Loop tricks)
print("\n===== 循环技巧 (Loop tricks) =====")

# enumerate() - 同时获取索引和值 (Get index and value simultaneously)
print("\nenumerate() - 获取索引和值 (Get index and value):")
for i, fruit in enumerate(fruits):
    print(f"索引 {i}: {fruit} (Index {i}: {fruit})")

# zip() - 并行迭代多个序列 (Parallel iteration of multiple sequences)
print("\nzip() - 并行迭代 (Parallel iteration):")
colors = ["红色", "黄色", "橙色", "红色"]
for fruit, color in zip(fruits, colors):
    print(f"{fruit} 是 {color} 的 ({fruit} is {color})")

# items() - 迭代字典 (Iterating dictionaries)
print("\nitems() - 迭代字典 (Iterating dictionaries):")
person = {"name": "张三", "age": 30, "city": "北京"}
for key, value in person.items():
    print(f"{key}: {value}")

print("\n程序执行完毕! (Program execution completed!)") 