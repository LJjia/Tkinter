#!/usr/bin/env python
# coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  EntryText.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/29 19:16
#        Email @  LJjiahf@163.com
#  Description @  Entry & Text
# ********************************************************************


import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x200')

var = tk.StringVar()

# 创建一个Entry （入口）  其中show的作用是将输入的字符串转化为什么样的类型
# 举例，如果show='*' 则像输密码一样，输入之后，字符全变成******
e = tk.Entry(window, show=None, width=30,bg='gray')
#Entry输入不可限制height这个参数，其值默认为1， 需注意
e.pack()


def insert_point():
    # 直接调用函数获得在Entry中输入的内容
    var = e.get()
    # insert函数，其中第一个参数为插入的方式，
    # 比如可以选择'insert' 在光标处插入
    # 或者'end'  在最后插入
    # 或者2.1 表示插入到第二行第一个位置
    t.insert('insert', var)


def insert_end():
    var = e.get()
    #有点奇怪的时这里0行和1行表示的含义好像完全相同
    #数字x.x表示插入到的位置，比如1.0表示插入到1行0列的位置
    t.insert(1.0, var)


# 创建Text 可输入文本框
t = tk.Text(window, height=4,bg='blue')
t.pack()

#command 传入的参数为点击按钮时执行的函数
b1 = tk.Button(window, text='insert point', width=20, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()

window.mainloop()
