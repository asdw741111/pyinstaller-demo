"""
处理
"""
import os
import traceback
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def add_to_listbox(result):
    """
    将处理结果添加到Listbox中
    :param result: 处理结果字符串
    """
    listbox.insert(tk.END, result)
    listbox.yview(tk.END)  # 滚动到Listbox的底部


def handle_excel(directory: str, file: str):
    print("handle_excel", directory, file)

def process_excel_files(directory):
    """处理目录

    Args:
        directory (_type_): _description_
    """
    handle_size = 0
    for file in os.listdir(directory):
        if file.endswith(('.xls', '.xlsx')):
            handle_size += 1
            try:
                handle_excel(directory, file)
                add_to_listbox(f"处理成功: {file}")
            except Exception as e:
                print("excel列错误", file)
                add_to_listbox(f"excel解析错误: {file} - {e}")
                traceback.print_exc()
    if handle_size == 0:
        add_to_listbox("该目录下未找到xls文件")

SELECTED_DIRECTORY = ""  # 用于存储所选目录的全局变量

def select_directory():
    """选择目录
    """
    global SELECTED_DIRECTORY
    dir_path = filedialog.askdirectory()
    if dir_path:
        SELECTED_DIRECTORY = dir_path  # 更新全局变量
        path_label.config(text=dir_path)  # 更新标签显示所选目录路径

def process_excel():
    """执行
    """
    if SELECTED_DIRECTORY:
        try:
            process_excel_files(SELECTED_DIRECTORY)  # 假设这个函数已经定义好
            # tk.messagebox.showinfo("完成", "处理完成！")
        except Exception as e:
            tk.messagebox.showerror("错误", f"处理过程中出现错误：{e}")
    else:
        tk.messagebox.showwarning("警告", "请先选择一个目录")

def close_app():
    root.destroy()

root = tk.Tk()
root.title("读取excel文件实例")

# 设置窗口的宽度为400像素，高度为500像素
root.geometry("400x500")

# 创建一个Frame作为Listbox和Scrollbar的容器
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)
# 创建一个Scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建Listbox并关联Scrollbar
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
listbox.pack(padx=10, side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)


select_button = tk.Button(root, text="选择目录", command=select_directory)
select_button.pack(pady=20)

path_label = tk.Label(root, text="未选择目录")
path_label.pack(pady=5)

# 使用Frame作为按钮的容器
buttons_frame = tk.Frame(root)
buttons_frame.pack(side=tk.BOTTOM, pady=20)

# 使用ttk.Button并应用自定义样式
process_button = tk.Button(buttons_frame, text="执行", command=process_excel)
process_button.pack(side=tk.LEFT, padx=25)

close_button = tk.Button(buttons_frame, text="关闭", command=close_app)
close_button.pack(side=tk.LEFT, padx=25)

root.mainloop()