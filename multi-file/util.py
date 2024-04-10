"""
工具模块
"""
from qr.q2 import get_info

def plus(a: int, b: int):
    """加法运算

    Args:
        a (int): a
        b (int): b

    Returns:
        int: a+b
    """
    return a + b

def do_qr(info: str):
    """生成二维码

    Args:
        info (str): qr信息
    """
    print(get_info(info))
