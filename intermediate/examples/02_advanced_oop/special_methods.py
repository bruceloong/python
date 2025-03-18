#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
高级面向对象编程 - 特殊方法（魔术方法）
展示Python中特殊方法的使用，使类的实例能够支持各种内置操作。
"""

class Vector:
    """表示2D向量的类，演示多种特殊方法 (A class representing a 2D vector, demonstrating various special methods)"""
    
    def __init__(self, x=0, y=0):
        """
        初始化向量
        (Initialize the vector)
        
        参数:
            x (float): x坐标
            y (float): y坐标
        """
        self.x = x
        self.y = y
    
    def __str__(self):
        """
        返回向量的字符串表示，供print()等使用
        (Return string representation of the vector for print(), etc.)
        
        返回:
            str: 向量的字符串表示
        """
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """
        返回向量的"官方"字符串表示，用于调试
        (Return the "official" string representation of the vector for debugging)
        
        返回:
            str: 向量的官方字符串表示
        """
        return f"Vector({self.x!r}, {self.y!r})"
    
    def __abs__(self):
        """
        计算向量的长度（模）
        (Calculate the length (magnitude) of the vector)
        
        返回:
            float: 向量的长度
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __bool__(self):
        """
        判断向量是否为零向量
        (Determine if the vector is a zero vector)
        
        返回:
            bool: 如果向量不是零向量，则返回True
        """
        return bool(abs(self))
    
    def __add__(self, other):
        """
        向量加法
        (Vector addition)
        
        参数:
            other (Vector): 要添加的另一个向量
            
        返回:
            Vector: 两个向量的和
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """
        向量减法
        (Vector subtraction)
        
        参数:
            other (Vector): 要减去的另一个向量
            
        返回:
            Vector: 两个向量的差
        """
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """
        向量乘以标量
        (Vector multiplication by a scalar)
        
        参数:
            scalar (float): 要乘以的标量
            
        返回:
            Vector: 缩放后的向量
        """
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        """
        标量乘以向量（右乘）
        (Scalar multiplication by a vector (right multiplication))
        
        参数:
            scalar (float): 要乘以的标量
            
        返回:
            Vector: 缩放后的向量
        """
        return self.__mul__(scalar)
    
    def __eq__(self, other):
        """
        检查两个向量是否相等
        (Check if two vectors are equal)
        
        参数:
            other (Vector): 要比较的另一个向量
            
        返回:
            bool: 如果两个向量相等，则返回True
        """
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __lt__(self, other):
        """
        检查此向量是否小于另一个向量（基于长度）
        (Check if this vector is less than another vector (based on length))
        
        参数:
            other (Vector): 要比较的另一个向量
            
        返回:
            bool: 如果此向量的长度小于另一个向量的长度，则返回True
        """
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented
    
    def __getitem__(self, index):
        """
        通过索引获取向量坐标
        (Get vector coordinate by index)
        
        参数:
            index (int): 索引（0表示x，1表示y）
            
        返回:
            float: 坐标值
            
        引发:
            IndexError: 如果索引不是0或1
        """
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector索引超出范围")
    
    def __len__(self):
        """
        返回向量维度
        (Return vector dimensions)
        
        返回:
            int: 向量的维度（始终为2，因为这是2D向量）
        """
        return 2
    
    def __iter__(self):
        """
        使向量可迭代
        (Make the vector iterable)
        
        返回:
            iterator: 向量坐标的迭代器
        """
        yield self.x
        yield self.y


# 演示特殊方法的使用 (Demonstrate the use of special methods)
if __name__ == "__main__":
    print("===== 创建向量 (Creating vectors) =====")
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1 = {v1}")      # 使用__str__ (Using __str__)
    print(f"v2 = {v2}")
    print(f"repr(v1) = {repr(v1)}")  # 使用__repr__ (Using __repr__)
    
    print("\n===== 向量操作 (Vector operations) =====")
    print(f"v1 + v2 = {v1 + v2}")    # 使用__add__ (Using __add__)
    print(f"v1 - v2 = {v1 - v2}")    # 使用__sub__ (Using __sub__)
    print(f"v1 * 2 = {v1 * 2}")      # 使用__mul__ (Using __mul__)
    print(f"3 * v2 = {3 * v2}")      # 使用__rmul__ (Using __rmul__)
    
    print("\n===== 向量比较 (Vector comparisons) =====")
    print(f"v1 == v2: {v1 == v2}")   # 使用__eq__ (Using __eq__)
    print(f"v1 != v2: {v1 != v2}")   # 使用__eq__的反面 (Using the opposite of __eq__)
    print(f"|v1| = {abs(v1)}")       # 使用__abs__ (Using __abs__)
    print(f"|v2| = {abs(v2)}")
    print(f"v1 < v2: {v1 < v2}")     # 使用__lt__ (Using __lt__)
    print(f"v1 > v2: {v1 > v2}")     # 基于__lt__的比较 (Comparison based on __lt__)
    
    print("\n===== 使用向量作为布尔值 (Using vectors as boolean values) =====")
    zero_vector = Vector(0, 0)
    print(f"bool(v1): {bool(v1)}")             # 使用__bool__ (Using __bool__)
    print(f"bool(zero_vector): {bool(zero_vector)}")
    print(f"if v1: {'真 (True)' if v1 else '假 (False)'}")
    print(f"if zero_vector: {'真 (True)' if zero_vector else '假 (False)'}")
    
    print("\n===== 索引和迭代 (Indexing and iteration) =====")
    print(f"v1[0] = {v1[0]}")        # 使用__getitem__ (Using __getitem__)
    print(f"v1[1] = {v1[1]}")
    
    print("使用for循环迭代v1的坐标 (Iterating v1 coordinates using for loop):")
    for coord in v1:                # 使用__iter__ (Using __iter__)
        print(f"  {coord}")
    
    print("使用列表解析获取坐标 (Getting coordinates using list comprehension):")
    coords = [c for c in v1]
    print(f"  {coords}")
    
    print(f"len(v1) = {len(v1)}")    # 使用__len__ (Using __len__)
    
    print("\n===== 转换为其他类型 (Converting to other types) =====")
    print(f"tuple(v1) = {tuple(v1)}")  # 使用__iter__将向量转换为元组 (Using __iter__ to convert vector to tuple)
    print(f"list(v2) = {list(v2)}")    # 使用__iter__将向量转换为列表 (Using __iter__ to convert vector to list)
    
    try:
        # 尝试访问无效索引 (Try to access an invalid index)
        print(v1[2])
    except IndexError as e:
        print(f"错误 (Error): {e}")
    
    print("\n程序执行完毕! (Program execution completed!)") 