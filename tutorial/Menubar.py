#!/usr/bin/env python
# coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  Menubar.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/30 9:51
#        Email @  LJjiahf@163.com
#  Description @  
# ********************************************************************
import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x200')

# l = tk.Label(window, bg='yellow', height=2, text='').pack()
# 以上这种方法在这里不行，因为之后会使用l.config因此如果l是pack()过后的变量，
# pack()之后变为None类型  则无法config
l = tk.Label(window, bg='yellow', height=2,width=20, text='')
l.pack()

counter = 0


def do_job():
    global counter
    l.config(text='You do Job' + str(counter))
    counter += 1


# 创建菜单栏 (横向一行)，可以理解为容器
menubar = tk.Menu(window)
# 定义一个空菜单单元  tearoff代表的是选项是否可以移动
filemenu = tk.Menu(menubar, tearoff=0)
# 将filemenu作为菜单栏中的一个选项，以名称为File添加进去
menubar.add_cascade(label='File', menu=filemenu)
# 向该选项中添加多重选项（选取选项后会展开一个列表）
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # 添加一条分界线
# tk的退出命令
filemenu.add_command(label='Exit', command=window.quit)
# filemenu的子选项中再添加一个可以展开的菜单
file_submenu = tk.Menu(filemenu)
# cascade 串联 倾泻
filemenu.add_cascade(label='Import', menu=file_submenu, underline=0)
file_submenu.add_command(label='Submenu1', command=do_job)

# 同样定义Edit菜单
Editmenu = tk.Menu(menubar, tearoff=0)
# 将filemenu作为菜单栏中的一个选项，以名称为File添加进去
menubar.add_cascade(label='Edit', menu=Editmenu)
# 向该选项中添加多重选项（选取选项后会展开一个列表）
Editmenu.add_command(label='Copy', command=do_job)
Editmenu.add_command(label='Cut', command=do_job)
Editmenu.add_command(label='Paste', command=do_job)
Editmenu.add_separator()  # 添加一条分界线


# 改变window的属性，多一个menu
#这句话需注意，可能会忘记
window.config(menu=menubar)

window.mainloop()
