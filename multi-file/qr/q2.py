"""q2
"""
# 相对导入
from .q1 import get_q1_info

def get_info(name: str):
    """q2 with q1
    """
    info = get_q1_info()
    return f"this is in qr with {info}, qr name is {name}"
