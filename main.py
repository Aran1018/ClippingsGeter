import os
import codecs
# 导入字符编码包codecs用于打开文件，防止出现乱码
from tkinter import *
# 窗口操作模块
import tkinter.messagebox
# 提示窗口模块
from tkinter.filedialog import askdirectory
# 读取文件路径模块
import time

CLIPPINGS_FILE = "origin/clippings.txt"
win = tkinter.Tk()
# 窗口初始化

MY_path = StringVar()


# 定义全局变量用于接收字符串改变


def _open_win():
    Button(win, text="路径选择", command=selectPath).grid(row=0, column=2)
    # 定义路径选择按钮
    Entry(win, textvariable=MY_path).grid(row=0, column=1)
    # 定义文本框用于显示路径
    Button(win, text="生成文件", command=main).grid(row=2, column=0)
    # 定义生成文件按钮
    win.mainloop()
    # 窗口循环


def selectPath():
    path_ = askdirectory()
    # 选择地址后拼接路径
    MY_path.set(path_ + "/clippings.txt")


# =============================逻辑代码部分==========================
def _get_str():
    with codecs.open(MY_path.get(), encoding='utf-8') as f:
        # 获取读取的txt文件的路径 最终返回路径变量strings
        strings = f.read()
    return strings


def _add_memo_to_file(memo, filename):
    if not os.path.exists(filename):
        # 判断路径上有没有这本书
        with codecs.open(filename, mode='a', encoding='utf-8') as f:
            f.write('# {}\n\n'.format(filename.split("/")[-1][:-3]))
        # 如果路径上不存在这本书名则创建这本书在首行上撰写书名[:-3为了去除后面的.md后缀]
    with codecs.open(filename, mode='a', encoding='utf-8') as f:
        # 如果路径上存在这本书名则在文未续写并换行
        f.write('* {}\n'.format(memo))


def main():
    tkinter.messagebox.showinfo(title='警示', message='将要向\"'+MY_path.get()[:-13]+'\"路径写入')
    # 弹出对话框，警告写入开始
    content = _get_str()
    memos = content.split('==========\r\n')
    # 首先分离每本书的结构
    for item in memos:
        i = item.split('\r\n')
        # 在每本书中以换行把主体内容分离出来
        # 睡0.3秒便于查看程序运行效果
        print(i)
        if len(i) > 2:
            # 做数据的比对，看数组长度是否为一条标准数据
            filename = MY_path.get()[:-13] + "/" + i[0] + '.md'
            # i[0]把数组第一位的做标题
            # MY_path.get()[:-13]去除路径中的/clippings.txt
            memo = i[-2]
            # 数组倒数第二位的做内容
            _add_memo_to_file(memo, filename)


if __name__ == '__main__':
    _open_win()
