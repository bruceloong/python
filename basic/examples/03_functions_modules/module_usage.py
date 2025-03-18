#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模块导入和使用示例
展示Python中不同的模块导入方式和使用方法。
"""

print("===== 模块导入和使用示例 (Module Import and Usage Examples) =====\n")

# 1. 导入整个模块 (Import entire module)
print("1. 导入整个模块 (Import entire module)")
import mymath

# 使用模块中的变量和函数 (Using variables and functions from the module)
print(f"PI值: {mymath.PI}")
print(f"E值: {mymath.E}")
print(f"10 + 5 = {mymath.add(10, 5)}")
print(f"7的平方: {mymath.square(7)}")

# 2. 从模块导入特定功能 (Import specific functionality from a module)
print("\n2. 从模块导入特定功能 (Import specific functionality from a module)")
from mymath import multiply, divide, factorial

# 直接使用导入的函数 (Directly use imported functions)
print(f"8 x 6 = {multiply(8, 6)}")
print(f"100 ÷ 4 = {divide(100, 4)}")
print(f"6! = {factorial(6)}")

# 3. 使用别名导入模块 (Import module with an alias)
print("\n3. 使用别名导入模块 (Import module with an alias)")
import mymath as mm

# 通过别名使用模块 (Use module via alias)
print(f"3的立方: {mm.cube(3)}")
print(f"2的8次方: {mm.power(2, 8)}")

# 4. 使用别名导入特定功能 (Import specific functionality with aliases)
print("\n4. 使用别名导入特定功能 (Import specific functionality with aliases)")
from mymath import is_prime as check_prime, subtract as minus

# 通过别名使用函数 (Use functions via aliases)
print(f"23是质数吗? {check_prime(23)}")
print(f"100 - 45 = {minus(100, 45)}")

# 5. 导入所有功能（不推荐） (Import all functionality (not recommended))
print("\n5. 导入所有功能（不推荐） (Import all functionality (not recommended))")
# from mymath import *  # 这种方式会导入模块中的所有内容，但不推荐使用
# 因为它可能会导致命名冲突，并且使代码的依赖关系不明确
# (This imports everything from the module, but it's not recommended
# because it can cause naming conflicts and makes dependencies unclear)

# 6. 导入标准库模块 (Import standard library modules)
print("\n6. 导入标准库模块 (Import standard library modules)")
import math
import random
import datetime

# 使用标准库函数 (Using standard library functions)
print(f"math.pi: {math.pi}")
print(f"随机数 (Random number) (1-10): {random.randint(1, 10)}")
print(f"当前日期时间 (Current date and time): {datetime.datetime.now()}")

# 7. 条件导入 (Conditional import)
print("\n7. 条件导入 (Conditional import)")
try:
    # 尝试导入可能不存在的模块 (Try to import a module that might not exist)
    import numpy as np
    print("NumPy已安装，版本: (NumPy is installed, version:)", np.__version__)
    print("示例数组 (Example array):", np.array([1, 2, 3, 4, 5]))
except ImportError:
    print("NumPy未安装 (NumPy is not installed)")
    print("可以使用命令安装: pip install numpy (You can install it with: pip install numpy)")

# 8. 导入子模块或包 (Import submodules or packages)
print("\n8. 导入子模块或包 (Import submodules or packages)")
# 例如，从datetime包导入date子模块
# (For example, import the date submodule from the datetime package)
from datetime import date
today = date.today()
print(f"今天是 (Today is): {today}")
print(f"年: {today.year}, 月: {today.month}, 日: {today.day}")
print(f"(Year: {today.year}, Month: {today.month}, Day: {today.day})")

# 9. 相对导入（在包内使用） (Relative imports (used within packages))
print("\n9. 相对导入（在包内使用） (Relative imports (used within packages))")
"""
在包内的模块中，可以使用相对导入引用同一包中的其他模块:
(Within modules in a package, you can use relative imports to reference other modules in the same package:)

from . import module1       # 导入同一目录下的module1 (Import module1 from the same directory)
from .. import module2      # 导入父目录下的module2 (Import module2 from the parent directory)
from ..subpackage import module3  # 导入父目录下subpackage包中的module3 
                            # (Import module3 from subpackage in the parent directory)
"""

# 10. 模块搜索路径 (Module search path)
print("\n10. 模块搜索路径 (Module search path)")
import sys
print("Python查找模块的路径: (Python's module search paths:)")
for path in sys.path:
    print(f"- {path}")

print("\n程序执行完毕! (Program execution completed!)") 