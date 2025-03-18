#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
命令行任务管理器
一个简单的命令行界面的任务管理应用，可以添加、查看、标记完成和删除任务。
任务存储在JSON文件中，实现了持久化存储。
"""

import os
import json
import datetime
from colorama import init, Fore, Style

# 初始化colorama，使颜色在Windows命令行中正常工作
# (Initialize colorama for colors to work in Windows command prompt)
init()

class TaskManager:
    """任务管理器类，处理任务的添加、查看、更新和删除 (Task manager class that handles adding, viewing, updating, and deleting tasks)"""
    
    def __init__(self, storage_file="tasks.json"):
        """
        初始化任务管理器
        (Initialize the task manager)
        
        参数:
            storage_file (str): 存储任务的JSON文件路径
        """
        self.storage_file = storage_file
        self.tasks = self._load_tasks()
    
    def _load_tasks(self):
        """
        从文件加载任务
        (Load tasks from file)
        
        返回:
            list: 任务列表，如果文件不存在则返回空列表
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                # 如果文件格式不正确或者找不到文件，返回空列表
                # (If file format is incorrect or file not found, return empty list)
                return []
        else:
            return []
    
    def _save_tasks(self):
        """
        保存任务到文件
        (Save tasks to file)
        """
        with open(self.storage_file, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)
    
    def add_task(self, title, description="", due_date=None, priority="medium"):
        """
        添加新任务
        (Add a new task)
        
        参数:
            title (str): 任务标题
            description (str, optional): 任务描述
            due_date (str, optional): 截止日期，格式为YYYY-MM-DD
            priority (str, optional): 优先级，可以是"low"、"medium"或"high"
            
        返回:
            dict: 新添加的任务
        """
        # 生成任务ID (Generate task ID)
        task_id = 1
        if self.tasks:
            task_id = max(task['id'] for task in self.tasks) + 1
        
        # 创建任务 (Create task)
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date,
            "priority": priority,
            "completed": False
        }
        
        # 添加任务到列表 (Add task to list)
        self.tasks.append(task)
        
        # 保存任务 (Save tasks)
        self._save_tasks()
        
        return task
    
    def get_all_tasks(self):
        """
        获取所有任务
        (Get all tasks)
        
        返回:
            list: 任务列表
        """
        return self.tasks
    
    def get_task_by_id(self, task_id):
        """
        根据ID获取任务
        (Get task by ID)
        
        参数:
            task_id (int): 任务ID
            
        返回:
            dict: 任务，如果找不到则返回None
        """
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def update_task(self, task_id, **kwargs):
        """
        更新任务
        (Update task)
        
        参数:
            task_id (int): 要更新的任务ID
            **kwargs: 要更新的字段和值
            
        返回:
            dict: 更新后的任务，如果找不到则返回None
        """
        task = self.get_task_by_id(task_id)
        if task:
            # 更新提供的字段 (Update provided fields)
            for key, value in kwargs.items():
                if key in task:
                    task[key] = value
            
            # 保存任务 (Save tasks)
            self._save_tasks()
            
            return task
        return None
    
    def mark_completed(self, task_id):
        """
        将任务标记为已完成
        (Mark task as completed)
        
        参数:
            task_id (int): 任务ID
            
        返回:
            dict: 更新后的任务，如果找不到则返回None
        """
        return self.update_task(task_id, completed=True)
    
    def delete_task(self, task_id):
        """
        删除任务
        (Delete task)
        
        参数:
            task_id (int): 要删除的任务ID
            
        返回:
            bool: 如果删除成功则返回True，否则返回False
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self._save_tasks()
            return True
        return False
    
    def get_tasks_by_status(self, completed=False):
        """
        根据状态获取任务
        (Get tasks by status)
        
        参数:
            completed (bool): 是否获取已完成的任务
            
        返回:
            list: 符合条件的任务列表
        """
        return [task for task in self.tasks if task['completed'] == completed]
    
    def get_tasks_by_priority(self, priority):
        """
        根据优先级获取任务
        (Get tasks by priority)
        
        参数:
            priority (str): 任务优先级，可以是"low"、"medium"或"high"
            
        返回:
            list: 符合条件的任务列表
        """
        return [task for task in self.tasks if task['priority'] == priority]


def print_task(task):
    """
    打印任务详情
    (Print task details)
    
    参数:
        task (dict): 要打印的任务
    """
    # 根据任务优先级设置颜色 (Set color based on task priority)
    priority_color = {
        "high": Fore.RED,
        "medium": Fore.YELLOW,
        "low": Fore.GREEN
    }.get(task['priority'], Fore.WHITE)
    
    # 设置状态颜色和文本 (Set status color and text)
    status_color = Fore.GREEN if task['completed'] else Fore.RED
    status_text = "已完成" if task['completed'] else "未完成"
    status_text_en = "Completed" if task['completed'] else "Pending"
    
    # 打印任务详情 (Print task details)
    print(f"\n{priority_color}任务 #{task['id']}: {task['title']}{Style.RESET_ALL}")
    print(f"描述 (Description): {task['description']}")
    print(f"创建时间 (Created): {task['created_at']}")
    
    # 如果有截止日期，则打印 (Print due date if available)
    if task['due_date']:
        print(f"截止日期 (Due date): {task['due_date']}")
        
    print(f"优先级 (Priority): {priority_color}{task['priority']}{Style.RESET_ALL}")
    print(f"状态 (Status): {status_color}{status_text} ({status_text_en}){Style.RESET_ALL}")


def print_task_list(tasks, title):
    """
    打印任务列表
    (Print task list)
    
    参数:
        tasks (list): 任务列表
        title (str): 列表标题
    """
    if not tasks:
        print(f"\n{Fore.CYAN}{title}{Style.RESET_ALL}")
        print("没有任务 (No tasks)")
        return
    
    print(f"\n{Fore.CYAN}{title}{Style.RESET_ALL}")
    for task in tasks:
        # 根据任务优先级设置颜色 (Set color based on task priority)
        priority_color = {
            "high": Fore.RED,
            "medium": Fore.YELLOW,
            "low": Fore.GREEN
        }.get(task['priority'], Fore.WHITE)
        
        # 设置状态标记 (Set status marker)
        status_marker = "✓" if task['completed'] else "✗"
        
        # 打印任务简要信息 (Print task summary)
        print(f"{priority_color}[{status_marker}] #{task['id']} - {task['title']}{Style.RESET_ALL}")


def display_menu():
    """
    显示菜单选项
    (Display menu options)
    """
    print(f"\n{Fore.CYAN}==== 任务管理器菜单 (Task Manager Menu) ===={Style.RESET_ALL}")
    print("1. 查看所有任务 (View all tasks)")
    print("2. 查看待办任务 (View pending tasks)")
    print("3. 查看已完成任务 (View completed tasks)")
    print("4. 添加新任务 (Add new task)")
    print("5. 查看任务详情 (View task details)")
    print("6. 标记任务为已完成 (Mark task as completed)")
    print("7. 删除任务 (Delete task)")
    print("8. 根据优先级查看任务 (View tasks by priority)")
    print("0. 退出 (Exit)")
    return input(f"\n{Fore.CYAN}请输入选项 (Enter your choice): {Style.RESET_ALL}")


def get_task_input():
    """
    获取用户输入的任务信息
    (Get task information from user input)
    
    返回:
        tuple: (标题, 描述, 截止日期, 优先级)
    """
    title = input("任务标题 (Task title): ")
    description = input("任务描述 (可选)(Task description (optional)): ")
    due_date = input("截止日期 (格式: YYYY-MM-DD) (可选)(Due date (format: YYYY-MM-DD) (optional)): ")
    
    # 如果截止日期为空，设为None (If due date is empty, set to None)
    if not due_date:
        due_date = None
        
    # 获取优先级 (Get priority)
    while True:
        priority = input("优先级 (Priority) [low/medium/high]: ").lower()
        if priority in ["low", "medium", "high"] or not priority:
            break
        print(f"{Fore.RED}无效的优先级。请输入 'low'、'medium' 或 'high'。(Invalid priority. Please enter 'low', 'medium', or 'high'.){Style.RESET_ALL}")
    
    # 如果优先级为空，设为默认值 (If priority is empty, set to default value)
    if not priority:
        priority = "medium"
        
    return title, description, due_date, priority


def main():
    """
    主函数，运行任务管理器
    (Main function that runs the task manager)
    """
    # 创建任务管理器实例 (Create task manager instance)
    task_manager = TaskManager()
    
    print(f"{Fore.CYAN}欢迎使用命令行任务管理器！(Welcome to the Command Line Task Manager!){Style.RESET_ALL}")
    
    while True:
        choice = display_menu()
        
        if choice == "0":
            print(f"{Fore.CYAN}谢谢使用，再见！(Thank you for using the Task Manager. Goodbye!){Style.RESET_ALL}")
            break
            
        elif choice == "1":
            # 查看所有任务 (View all tasks)
            tasks = task_manager.get_all_tasks()
            print_task_list(tasks, "所有任务 (All Tasks)")
            
        elif choice == "2":
            # 查看待办任务 (View pending tasks)
            tasks = task_manager.get_tasks_by_status(completed=False)
            print_task_list(tasks, "待办任务 (Pending Tasks)")
            
        elif choice == "3":
            # 查看已完成任务 (View completed tasks)
            tasks = task_manager.get_tasks_by_status(completed=True)
            print_task_list(tasks, "已完成任务 (Completed Tasks)")
            
        elif choice == "4":
            # 添加新任务 (Add new task)
            print(f"\n{Fore.CYAN}添加新任务 (Add New Task){Style.RESET_ALL}")
            title, description, due_date, priority = get_task_input()
            
            if title:
                task = task_manager.add_task(title, description, due_date, priority)
                print(f"{Fore.GREEN}任务已添加成功 (Task added successfully){Style.RESET_ALL}")
                print_task(task)
            else:
                print(f"{Fore.RED}任务标题不能为空 (Task title cannot be empty){Style.RESET_ALL}")
                
        elif choice == "5":
            # 查看任务详情 (View task details)
            try:
                task_id = int(input("请输入任务ID (Enter task ID): "))
                task = task_manager.get_task_by_id(task_id)
                if task:
                    print_task(task)
                else:
                    print(f"{Fore.RED}找不到ID为 {task_id} 的任务 (Task with ID {task_id} not found){Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}请输入有效的数字ID (Please enter a valid numeric ID){Style.RESET_ALL}")
                
        elif choice == "6":
            # 标记任务为已完成 (Mark task as completed)
            try:
                task_id = int(input("请输入要标记为已完成的任务ID (Enter ID of task to mark as completed): "))
                task = task_manager.mark_completed(task_id)
                if task:
                    print(f"{Fore.GREEN}任务已标记为已完成 (Task marked as completed){Style.RESET_ALL}")
                    print_task(task)
                else:
                    print(f"{Fore.RED}找不到ID为 {task_id} 的任务 (Task with ID {task_id} not found){Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}请输入有效的数字ID (Please enter a valid numeric ID){Style.RESET_ALL}")
                
        elif choice == "7":
            # 删除任务 (Delete task)
            try:
                task_id = int(input("请输入要删除的任务ID (Enter ID of task to delete): "))
                confirm = input(f"确定要删除ID为 {task_id} 的任务吗？(y/n) (Are you sure you want to delete task with ID {task_id}? (y/n)): ").lower()
                
                if confirm == 'y':
                    if task_manager.delete_task(task_id):
                        print(f"{Fore.GREEN}任务已成功删除 (Task deleted successfully){Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}找不到ID为 {task_id} 的任务 (Task with ID {task_id} not found){Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}已取消删除 (Deletion cancelled){Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}请输入有效的数字ID (Please enter a valid numeric ID){Style.RESET_ALL}")
                
        elif choice == "8":
            # 根据优先级查看任务 (View tasks by priority)
            priority = input("请输入优先级 [low/medium/high]: ").lower()
            if priority in ["low", "medium", "high"]:
                tasks = task_manager.get_tasks_by_priority(priority)
                print_task_list(tasks, f"{priority.capitalize()}优先级任务 ({priority.capitalize()} Priority Tasks)")
            else:
                print(f"{Fore.RED}无效的优先级 (Invalid priority){Style.RESET_ALL}")
                
        else:
            print(f"{Fore.RED}无效的选项，请重试 (Invalid choice, please try again){Style.RESET_ALL}")
            
        # 按任意键继续 (Press any key to continue)
        input(f"\n{Fore.CYAN}按回车键继续... (Press Enter to continue...){Style.RESET_ALL}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # 处理Ctrl+C (Handle Ctrl+C)
        print(f"\n{Fore.CYAN}程序已中断，谢谢使用！(Program interrupted, thank you for using!){Style.RESET_ALL}")
    except Exception as e:
        # 处理其他异常 (Handle other exceptions)
        print(f"{Fore.RED}发生错误: {str(e)} (An error occurred: {str(e)}){Style.RESET_ALL}") 