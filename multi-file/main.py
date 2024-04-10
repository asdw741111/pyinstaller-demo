"""
入口
"""
# 主模块所在文件夹不会被视作package，因此除了主模块外，与主模块处在同个文件夹的模块（也就是同级的模块）也必须使用绝对导入。
from util import plus, do_qr
# 绝对导入
from page.user import get_current_user_name

if __name__ == '__main__':
    print(plus(1, 2))
    print(get_current_user_name())
    do_qr("pyinstaller")
