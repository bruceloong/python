#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件基本操作示例
展示Python中文件的读取、写入和管理基础操作。
"""

import os
import shutil
import datetime

print("===== 文件基本操作示例 (File Operations Basic Examples) =====\n")

# 创建示例文件夹 (Create example directory)
example_dir = "file_examples"
if not os.path.exists(example_dir):
    os.mkdir(example_dir)
    print(f"创建目录: {example_dir} (Created directory: {example_dir})")
else:
    print(f"目录已存在: {example_dir} (Directory already exists: {example_dir})")

# 获取当前工作目录 (Get current working directory)
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir} (Current working directory: {current_dir})")

# 1. 文件写入 - 基本方法 (File writing - basic method)
print("\n1. 文件写入 - 基本方法 (File writing - basic method)")
file_path = os.path.join(example_dir, "sample.txt")

# 打开文件进行写入 (Open file for writing)
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("这是第一行。\n")  # \n表示换行 (\n means newline)
    file.write("这是第二行。\n")
    file.write("This is the third line.\n")
    file.write("这是包含中文和English的一行。\n")

print(f"文件已写入: {file_path} (File written: {file_path})")

# 2. 文件读取 - 一次性读取全部内容 (File reading - read all content at once)
print("\n2. 文件读取 - 一次性读取全部内容 (File reading - read all content at once)")
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

print("文件内容 (File content):")
print(content)

# 3. 文件读取 - 按行读取 (File reading - read line by line)
print("\n3. 文件读取 - 按行读取 (File reading - read line by line)")
with open(file_path, 'r', encoding='utf-8') as file:
    print("按行读取 (Reading line by line):")
    for i, line in enumerate(file, 1):
        print(f"行 {i}: {line.strip()}")  # strip()删除行尾的换行符 (strip() removes trailing newline)

# 4. 文件读取 - 读取所有行到列表 (File reading - read all lines into a list)
print("\n4. 文件读取 - 读取所有行到列表 (File reading - read all lines into a list)")
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(f"文件包含 {len(lines)} 行 (File contains {len(lines)} lines)")
print(f"行列表: {lines} (List of lines: {lines})")

# 5. 文件追加 (File appending)
print("\n5. 文件追加 (File appending)")
with open(file_path, 'a', encoding='utf-8') as file:
    file.write(f"添加于 {datetime.datetime.now()}\n")
    file.write("这是追加的一行。(This is an appended line.)\n")

print(f"内容已追加到文件 (Content appended to file): {file_path}")

# 查看更新后的文件内容 (View updated file content)
with open(file_path, 'r', encoding='utf-8') as file:
    updated_content = file.read()

print("更新后的文件内容 (Updated file content):")
print(updated_content)

# 6. 文件模式和选项 (File modes and options)
print("\n6. 文件模式和选项 (File modes and options)")
"""
常用文件模式:
- 'r': 读取（默认）
- 'w': 写入（覆盖已有内容）
- 'a': 追加
- 'b': 二进制模式
- 't': 文本模式（默认）
- '+': 读写模式

(Common file modes:
- 'r': read (default)
- 'w': write (overwrites existing content)
- 'a': append
- 'b': binary mode
- 't': text mode (default)
- '+': read and write mode)
"""

# 7. 二进制文件操作 (Binary file operations)
print("\n7. 二进制文件操作 (Binary file operations)")
binary_file_path = os.path.join(example_dir, "binary_sample.bin")

# 写入二进制数据 (Write binary data)
with open(binary_file_path, 'wb') as file:
    # 写入一些整数 (Write some integers)
    for i in range(10):
        file.write(i.to_bytes(4, byteorder='little'))

print(f"二进制文件已写入: {binary_file_path} (Binary file written: {binary_file_path})")

# 读取二进制数据 (Read binary data)
with open(binary_file_path, 'rb') as file:
    # 读取前几个整数 (Read the first few integers)
    print("读取的整数 (Integers read):")
    for _ in range(5):
        data = file.read(4)  # 读取4字节 (Read 4 bytes)
        if data:
            value = int.from_bytes(data, byteorder='little')
            print(value, end=' ')
    print()

# 8. 文件和目录管理 (File and directory management)
print("\n8. 文件和目录管理 (File and directory management)")

# 创建一个子目录 (Create a subdirectory)
subdir_path = os.path.join(example_dir, "subdir")
if not os.path.exists(subdir_path):
    os.mkdir(subdir_path)
    print(f"创建子目录: {subdir_path} (Created subdirectory: {subdir_path})")

# 复制文件 (Copy file)
copied_file_path = os.path.join(subdir_path, "sample_copy.txt")
shutil.copy2(file_path, copied_file_path)
print(f"文件已复制: {file_path} -> {copied_file_path} (File copied: {file_path} -> {copied_file_path})")

# 重命名文件 (Rename file)
renamed_file_path = os.path.join(example_dir, "renamed_sample.txt")
os.rename(file_path, renamed_file_path)
print(f"文件已重命名: {file_path} -> {renamed_file_path} (File renamed: {file_path} -> {renamed_file_path})")

# 检查文件是否存在 (Check if file exists)
print(f"文件是否存在: {os.path.exists(renamed_file_path)} (File exists: {os.path.exists(renamed_file_path)})")
print(f"是否是文件: {os.path.isfile(renamed_file_path)} (Is a file: {os.path.isfile(renamed_file_path)})")
print(f"是否是目录: {os.path.isdir(example_dir)} (Is a directory: {os.path.isdir(example_dir)})")

# 获取文件信息 (Get file information)
file_stats = os.stat(renamed_file_path)
print(f"文件大小: {file_stats.st_size} 字节 (File size: {file_stats.st_size} bytes)")
mod_time = datetime.datetime.fromtimestamp(file_stats.st_mtime)
print(f"最后修改时间: {mod_time} (Last modified: {mod_time})")

# 列出目录内容 (List directory content)
print(f"\n目录内容 ({example_dir}) [Directory content]:")
for item in os.listdir(example_dir):
    item_path = os.path.join(example_dir, item)
    item_type = "文件 (File)" if os.path.isfile(item_path) else "目录 (Directory)"
    print(f"- {item} [{item_type}]")

# 9. 文件路径操作 (File path operations)
print("\n9. 文件路径操作 (File path operations)")
file_path = renamed_file_path  # 使用重命名后的文件 (Use the renamed file)
print(f"完整路径: {file_path} (Full path: {file_path})")
print(f"目录名: {os.path.dirname(file_path)} (Directory name: {os.path.dirname(file_path)})")
print(f"文件名: {os.path.basename(file_path)} (File name: {os.path.basename(file_path)})")
print(f"路径组合: {os.path.join('folder', 'subfolder', 'file.txt')} (Path join: {os.path.join('folder', 'subfolder', 'file.txt')})")

# 分离文件名和扩展名 (Split filename and extension)
filename, extension = os.path.splitext(os.path.basename(file_path))
print(f"文件名（不含扩展名）: {filename} (Filename without extension: {filename})")
print(f"扩展名: {extension} (Extension: {extension})")

# 10. 使用try-except处理文件操作错误 (Using try-except to handle file operation errors)
print("\n10. 使用try-except处理文件操作错误 (Using try-except to handle file operation errors)")
non_existent_file = "this_file_does_not_exist.txt"

try:
    with open(non_existent_file, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"错误: 文件 '{non_existent_file}' 不存在 (Error: File '{non_existent_file}' not found)")
except PermissionError:
    print(f"错误: 没有权限访问文件 '{non_existent_file}' (Error: No permission to access file '{non_existent_file}')")
except Exception as e:
    print(f"发生了其他错误: {str(e)} (An error occurred: {str(e)})")

print("\n程序执行完毕! (Program execution completed!)") 