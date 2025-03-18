#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
面向对象编程基础示例 - Person类
展示类的定义、属性、方法和实例化的基本概念。
"""

class Person:
    """人员类，表示一个具有姓名、年龄和职业的人员 (Person class, represents a person with name, age, and profession)"""
    
    # 类变量（所有实例共享）(Class variable, shared by all instances)
    species = "人类" # 物种 (species)
    
    def __init__(self, name, age, profession=None):
        """
        初始化Person实例
        (Initialize a Person instance)
        
        参数:
            name (str): 姓名
            age (int): 年龄
            profession (str, optional): 职业，可选参数
        """
        # 实例变量（每个实例独有）(Instance variables, unique to each instance)
        self.name = name
        self.age = age
        self.profession = profession
        self._private_attr = "私有属性（通过约定）" # 私有属性（通过约定）(Private attribute by convention)
    
    def introduce(self):
        """
        自我介绍方法
        (Self-introduction method)
        
        返回:
            str: 包含人员信息的介绍
        """
        if self.profession:
            intro = f"我叫{self.name}，今年{self.age}岁，是一名{self.profession}。"
            intro_en = f"My name is {self.name}, I'm {self.age} years old, and I'm a {self.profession}."
        else:
            intro = f"我叫{self.name}，今年{self.age}岁。"
            intro_en = f"My name is {self.name}, I'm {self.age} years old."
        
        return f"{intro}\n({intro_en})"
    
    def celebrate_birthday(self):
        """
        庆祝生日，年龄增加1
        (Celebrate birthday, increase age by 1)
        
        返回:
            str: 生日祝福消息
        """
        self.age += 1
        return f"祝{self.name}生日快乐！现在{self.age}岁了。\n(Happy birthday to {self.name}! Now {self.age} years old.)"
    
    def change_profession(self, new_profession):
        """
        更改职业
        (Change profession)
        
        参数:
            new_profession (str): 新职业
            
        返回:
            str: 确认职业变更的消息
        """
        old_profession = self.profession
        self.profession = new_profession
        
        if old_profession:
            message = f"{self.name}的职业从{old_profession}变更为{new_profession}。"
            message_en = f"{self.name}'s profession changed from {old_profession} to {new_profession}."
        else:
            message = f"{self.name}的职业设置为{new_profession}。"
            message_en = f"{self.name}'s profession is set to {new_profession}."
            
        return f"{message}\n({message_en})"
    
    @classmethod
    def get_species(cls):
        """
        类方法：获取物种
        (Class method: Get species)
        
        返回:
            str: 物种名称
        """
        return cls.species
    
    @staticmethod
    def is_adult(age):
        """
        静态方法：检查年龄是否成年
        (Static method: Check if age is adult)
        
        参数:
            age (int): 要检查的年龄
            
        返回:
            bool: 如果年龄大于等于18则为True，否则为False
        """
        return age >= 18


# 演示如何使用Person类 (Demonstration of how to use the Person class)
if __name__ == "__main__":
    # 创建Person实例 (Create Person instances)
    print("===== 创建Person实例 (Creating Person instances) =====")
    person1 = Person("张三", 25, "工程师")
    person2 = Person("李四", 17)
    
    # 访问实例属性 (Accessing instance attributes)
    print("\n===== 访问实例属性 (Accessing instance attributes) =====")
    print(f"姓名: {person1.name}, 年龄: {person1.age}, 职业: {person1.profession}")
    print(f"(Name: {person1.name}, Age: {person1.age}, Profession: {person1.profession})")
    
    # 调用实例方法 (Calling instance methods)
    print("\n===== 调用实例方法 (Calling instance methods) =====")
    print(person1.introduce())
    print(person2.introduce())
    
    # 修改实例属性 (Modifying instance attributes)
    print("\n===== 修改实例属性 (Modifying instance attributes) =====")
    person2.profession = "学生"
    print(person2.introduce())
    
    # 调用会修改状态的方法 (Calling methods that modify state)
    print("\n===== 调用会修改状态的方法 (Calling methods that modify state) =====")
    print(person1.celebrate_birthday())
    print(person1.change_profession("高级工程师"))
    print(person1.introduce())
    
    # 访问类变量 (Accessing class variables)
    print("\n===== 访问类变量 (Accessing class variables) =====")
    print(f"物种(直接访问): {Person.species}")
    print(f"物种(通过实例): {person1.species}")
    print(f"(Species (direct access): {Person.species})")
    print(f"(Species (via instance): {person1.species})")
    
    # 调用类方法 (Calling class methods)
    print("\n===== 调用类方法 (Calling class methods) =====")
    print(f"物种(类方法): {Person.get_species()}")
    print(f"(Species (class method): {Person.get_species()})")
    
    # 调用静态方法 (Calling static methods)
    print("\n===== 调用静态方法 (Calling static methods) =====")
    print(f"张三是成年人吗？{Person.is_adult(person1.age)}")
    print(f"李四是成年人吗？{Person.is_adult(person2.age)}")
    print(f"(Is Zhang San an adult? {Person.is_adult(person1.age)})")
    print(f"(Is Li Si an adult? {Person.is_adult(person2.age)})")
    
    # 也可以通过实例调用静态方法，但不是推荐的做法
    # (Can also call static methods through instances, but not recommended)
    print(f"通过实例调用静态方法: {person1.is_adult(person1.age)}")
    print(f"(Calling static method via instance: {person1.is_adult(person1.age)})")
    
    print("\n程序执行完毕! (Program execution completed!)") 