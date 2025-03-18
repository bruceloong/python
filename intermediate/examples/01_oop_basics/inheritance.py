#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
面向对象编程继承示例
展示类的继承、方法重写和多态的基本概念。
"""

class Animal:
    """动物基类 (Animal base class)"""
    
    def __init__(self, name, species):
        """
        初始化Animal实例
        (Initialize an Animal instance)
        
        参数:
            name (str): 动物名称
            species (str): 物种
        """
        self.name = name
        self.species = species
    
    def make_sound(self):
        """
        发出声音（基类方法，子类应重写）
        (Make sound (base method, should be overridden by subclasses))
        
        返回:
            str: 动物发出的声音
        """
        return "一些通用的动物声音 (Some generic animal sound)"
    
    def info(self):
        """
        获取动物信息
        (Get animal information)
        
        返回:
            str: 包含动物名称和物种的信息
        """
        return f"{self.name}是一只{self.species}\n({self.name} is a {self.species})"


class Dog(Animal):
    """狗类，继承自Animal (Dog class, inherits from Animal)"""
    
    def __init__(self, name, breed):
        """
        初始化Dog实例
        (Initialize a Dog instance)
        
        参数:
            name (str): 狗的名称
            breed (str): 狗的品种
        """
        # 调用父类的初始化方法 (Call the parent class initialization method)
        super().__init__(name, "狗")  # species固定为"狗" (species is fixed as "dog")
        self.breed = breed
        self.is_trained = False
    
    def make_sound(self):
        """
        重写父类的方法：狗叫
        (Override parent method: dog bark)
        
        返回:
            str: 狗叫声
        """
        return f"{self.name}：汪汪！\n({self.name}: Woof woof!)"
    
    def fetch(self, item):
        """
        狗特有的方法：捡东西
        (Dog-specific method: fetch items)
        
        参数:
            item (str): 要捡的物品
            
        返回:
            str: 描述狗捡东西的消息
        """
        return f"{self.name}去捡了{item}并带了回来！\n({self.name} fetched the {item} and brought it back!)"
    
    def train(self):
        """
        训练狗
        (Train the dog)
        
        返回:
            str: 描述训练结果的消息
        """
        self.is_trained = True
        return f"{self.name}已经接受了训练，现在很听话！\n({self.name} has been trained and is now obedient!)"
    
    def info(self):
        """
        重写父类方法，增加品种信息
        (Override parent method, add breed information)
        
        返回:
            str: 包含狗名称、物种和品种的信息
        """
        # 调用父类的info方法，然后添加额外的品种信息
        # (Call parent's info method, then add additional breed information)
        basic_info = super().info()
        return f"{basic_info}，品种是{self.breed}\n(and is a {self.breed} breed)"


class Cat(Animal):
    """猫类，继承自Animal (Cat class, inherits from Animal)"""
    
    def __init__(self, name, color):
        """
        初始化Cat实例
        (Initialize a Cat instance)
        
        参数:
            name (str): 猫的名称
            color (str): 猫的颜色
        """
        super().__init__(name, "猫")  # species固定为"猫" (species is fixed as "cat")
        self.color = color
        self.is_purring = False
    
    def make_sound(self):
        """
        重写父类的方法：猫叫
        (Override parent method: cat meow)
        
        返回:
            str: 猫叫声
        """
        return f"{self.name}：喵喵！\n({self.name}: Meow meow!)"
    
    def purr(self):
        """
        猫特有的方法：打呼噜
        (Cat-specific method: purr)
        
        返回:
            str: 描述猫打呼噜的消息
        """
        self.is_purring = True
        return f"{self.name}开始舒服地打呼噜...\n({self.name} starts purring contentedly...)"
    
    def climb(self):
        """
        猫特有的方法：爬树
        (Cat-specific method: climb tree)
        
        返回:
            str: 描述猫爬树的消息
        """
        return f"{self.name}敏捷地爬上了树！\n({self.name} climbed the tree agilely!)"
    
    def info(self):
        """
        重写父类方法，增加颜色信息
        (Override parent method, add color information)
        
        返回:
            str: 包含猫名称、物种和颜色的信息
        """
        basic_info = super().info()
        return f"{basic_info}，毛色是{self.color}\n(with {self.color} fur)"


# 演示继承和多态 (Demonstrate inheritance and polymorphism)
if __name__ == "__main__":
    # 创建基类和子类实例 (Create base class and subclass instances)
    print("===== 创建动物实例 (Creating animal instances) =====")
    generic_animal = Animal("未知动物", "未知物种")
    dog = Dog("旺财", "金毛寻回犬")
    cat = Cat("咪咪", "橘色")
    
    # 访问和使用基类方法 (Access and use base class methods)
    print("\n===== 基类方法 (Base class methods) =====")
    print(generic_animal.info())
    print(generic_animal.make_sound())
    
    # 展示方法重写 (Demonstrate method overriding)
    print("\n===== 方法重写 (Method overriding) =====")
    print(dog.info())
    print(dog.make_sound())
    print(cat.info())
    print(cat.make_sound())
    
    # 使用子类特有的方法 (Use subclass-specific methods)
    print("\n===== 子类特有方法 (Subclass-specific methods) =====")
    print(dog.fetch("球"))
    print(dog.train())
    print(cat.purr())
    print(cat.climb())
    
    # 演示多态性 (Demonstrate polymorphism)
    print("\n===== 多态性 (Polymorphism) =====")
    animals = [generic_animal, dog, cat]
    
    for animal in animals:
        print(f"\n关于 {animal.name}:")
        print(animal.info())
        print(animal.make_sound())  # 同一方法调用，不同的实现 (Same method call, different implementations)
    
    # 类型检查和转换 (Type checking and conversion)
    print("\n===== 类型检查 (Type checking) =====")
    for animal in animals:
        if isinstance(animal, Dog):
            print(f"{animal.name} 是一只狗，它可以: {animal.fetch('棍子')}")
        elif isinstance(animal, Cat):
            print(f"{animal.name} 是一只猫，它可以: {animal.climb()}")
        else:
            print(f"{animal.name} 是一种基本动物")
    
    print("\n程序执行完毕! (Program execution completed!)") 