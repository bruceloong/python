#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python基本数据类型示例
展示Python中的主要数据类型及其基本操作。
"""

# 1. 数字类型 (Numeric Types)
print("===== 数字类型 (Numeric Types) =====")

# 整数 (Integers)
integer_number = 42
print(f"整数 (Integer): {integer_number}, 类型 (Type): {type(integer_number)}")

# 浮点数 (Floating-point numbers)
float_number = 3.14159
print(f"浮点数 (Float): {float_number}, 类型 (Type): {type(float_number)}")

# 复数 (Complex numbers)
complex_number = 1 + 2j
print(f"复数 (Complex): {complex_number}, 类型 (Type): {type(complex_number)}")
print(f"实部 (Real part): {complex_number.real}, 虚部 (Imaginary part): {complex_number.imag}")

# 数值运算 (Numeric operations)
print("\n数值运算 (Numeric operations):")
a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"加法 (Addition): a + b = {a + b}")
print(f"减法 (Subtraction): a - b = {a - b}")
print(f"乘法 (Multiplication): a * b = {a * b}")
print(f"除法 (Division): a / b = {a / b}")  # 结果是浮点数 (Result is float)
print(f"整数除法 (Floor division): a // b = {a // b}")  # 结果是整数 (Result is integer)
print(f"取余 (Modulus): a % b = {a % b}")
print(f"幂运算 (Exponentiation): a ** b = {a ** b}")  # a的b次方 (a raised to power b)

# 2. 字符串 (Strings)
print("\n===== 字符串 (Strings) =====")
single_quoted = 'Python编程'
double_quoted = "Python Programming"
triple_quoted = '''这是一个
多行字符串'''

print(f"单引号字符串 (Single quoted): {single_quoted}")
print(f"双引号字符串 (Double quoted): {double_quoted}")
print(f"三引号字符串 (Triple quoted):\n{triple_quoted}")

# 字符串操作 (String operations)
print("\n字符串操作 (String operations):")
text = "Hello, Python!"
print(f"原始字符串 (Original string): {text}")
print(f"长度 (Length): {len(text)}")
print(f"大写 (Uppercase): {text.upper()}")
print(f"小写 (Lowercase): {text.lower()}")
print(f"替换 (Replace): {text.replace('Hello', '你好')}")
print(f"分割 (Split): {text.split(', ')}")
print(f"索引 (Indexing): text[0] = {text[0]}, text[7] = {text[7]}")
print(f"切片 (Slicing): text[0:5] = {text[0:5]}, text[7:] = {text[7:]}")

# 3. 布尔值 (Booleans)
print("\n===== 布尔值 (Booleans) =====")
true_value = True
false_value = False
print(f"真值 (True value): {true_value}, 类型 (Type): {type(true_value)}")
print(f"假值 (False value): {false_value}, 类型 (Type): {type(false_value)}")

# 布尔运算 (Boolean operations)
print("\n布尔运算 (Boolean operations):")
print(f"与运算 (AND): True and False = {True and False}")
print(f"或运算 (OR): True or False = {True or False}")
print(f"非运算 (NOT): not True = {not True}, not False = {not False}")
print(f"比较运算 (Comparison): 5 > 3 = {5 > 3}, 5 == 3 = {5 == 3}, 5 != 3 = {5 != 3}")

# 4. 列表 (Lists)
print("\n===== 列表 (Lists) =====")
# 列表是有序、可变的集合 (Lists are ordered, mutable collections)
fruits = ["苹果", "香蕉", "橙子", "草莓"]
print(f"水果列表 (Fruit list): {fruits}, 类型 (Type): {type(fruits)}")
print(f"列表长度 (List length): {len(fruits)}")
print(f"第一个水果 (First fruit): {fruits[0]}")
print(f"最后一个水果 (Last fruit): {fruits[-1]}")

# 列表操作 (List operations)
print("\n列表操作 (List operations):")
fruits.append("葡萄")  # 添加元素 (Add an element)
print(f"添加后 (After append): {fruits}")
fruits.insert(1, "梨")  # 插入元素 (Insert an element)
print(f"插入后 (After insert): {fruits}")
fruits.remove("香蕉")  # 移除元素 (Remove an element)
print(f"移除后 (After remove): {fruits}")
popped_fruit = fruits.pop()  # 弹出最后一个元素 (Pop the last element)
print(f"弹出的水果 (Popped fruit): {popped_fruit}")
print(f"弹出后 (After pop): {fruits}")
fruits.sort()  # 排序 (Sort)
print(f"排序后 (After sort): {fruits}")
fruits.reverse()  # 反转 (Reverse)
print(f"反转后 (After reverse): {fruits}")

# 5. 元组 (Tuples)
print("\n===== 元组 (Tuples) =====")
# 元组是有序、不可变的集合 (Tuples are ordered, immutable collections)
dimensions = (1920, 1080)
print(f"屏幕尺寸 (Screen dimensions): {dimensions}, 类型 (Type): {type(dimensions)}")
print(f"宽度 (Width): {dimensions[0]}, 高度 (Height): {dimensions[1]}")

# 尝试修改元组会导致错误 (Trying to modify a tuple will cause an error)
# dimensions[0] = 2560  # 这会引发TypeError (This would raise TypeError)

# 虽然元组本身不可变，但它可以被重新赋值 (Although tuples are immutable, they can be reassigned)
dimensions = (2560, 1440)
print(f"新屏幕尺寸 (New screen dimensions): {dimensions}")

# 6. 字典 (Dictionaries)
print("\n===== 字典 (Dictionaries) =====")
# 字典是无序的键值对集合 (Dictionaries are unordered collections of key-value pairs)
person = {
    "name": "张三",
    "age": 30,
    "city": "北京",
    "skills": ["Python", "JavaScript", "HTML/CSS"]
}
print(f"人物信息 (Person info): {person}, 类型 (Type): {type(person)}")

# 访问字典值 (Accessing dictionary values)
print(f"姓名 (Name): {person['name']}")
print(f"年龄 (Age): {person['age']}")
print(f"技能 (Skills): {person['skills']}")

# 字典操作 (Dictionary operations)
print("\n字典操作 (Dictionary operations):")
person["email"] = "zhangsan@example.com"  # 添加新键值对 (Add a new key-value pair)
print(f"添加后 (After adding email): {person}")
person["age"] = 31  # 修改现有值 (Modify an existing value)
print(f"修改后 (After modifying age): {person}")
del person["city"]  # 删除键值对 (Delete a key-value pair)
print(f"删除后 (After deleting city): {person}")
print(f"字典键 (Dictionary keys): {list(person.keys())}")
print(f"字典值 (Dictionary values): {list(person.values())}")
print(f"字典项 (Dictionary items): {list(person.items())}")

# 7. 集合 (Sets)
print("\n===== 集合 (Sets) =====")
# 集合是无序、不重复的元素集合 (Sets are unordered collections with no duplicate elements)
colors = {"红", "绿", "蓝", "红"}  # 注意重复的"红"会被自动删除 (Note the duplicate "红" will be automatically removed)
print(f"颜色集合 (Color set): {colors}, 类型 (Type): {type(colors)}")

# 集合操作 (Set operations)
print("\n集合操作 (Set operations):")
colors.add("黄")  # 添加元素 (Add an element)
print(f"添加后 (After adding): {colors}")
colors.remove("绿")  # 移除元素 (Remove an element)
print(f"移除后 (After removing): {colors}")

# 集合运算 (Set operations)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"集合1 (Set1): {set1}, 集合2 (Set2): {set2}")
print(f"并集 (Union): {set1 | set2}")  # 或使用 set1.union(set2)
print(f"交集 (Intersection): {set1 & set2}")  # 或使用 set1.intersection(set2)
print(f"差集 (Difference): {set1 - set2}")  # 或使用 set1.difference(set2)
print(f"对称差集 (Symmetric difference): {set1 ^ set2}")  # 或使用 set1.symmetric_difference(set2)

# 8. None类型 (None Type)
print("\n===== None类型 (None Type) =====")
empty_value = None
print(f"空值 (Empty value): {empty_value}, 类型 (Type): {type(empty_value)}")
print(f"是否为None (Is None): {empty_value is None}")

print("\n程序执行完毕! (Program execution completed!)") 