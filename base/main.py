"""
基本演示 只有一个文件
"""
import os

def get_current_dir():
    return os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    print("当前路径", get_current_dir())
