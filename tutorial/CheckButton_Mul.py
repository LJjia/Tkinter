#!/usr/bin/env python
#coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  CheckButton_Mul.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/29 21:58
#        Email @  LJjiahf@163.com
#  Description @  CheckButton多选
# ********************************************************************

import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x200')

l = tk.Label(window, bg='yellow', width=30, text='I don\'t  like any one')
l.pack()

def print_selection():
    #根据get得到的var1，var2的值进行判断
    #打印出不同的信息
    if (var1.get()==0) & (var2.get()==0):
        l.config(text='I don\'t  like any one')
    elif (var1.get()==1) & (var2.get()==0):
        l.config(text='I like Python')
    elif (var1.get()==0) & (var2.get()==1):
        l.config(text='I like C++')
    else:
        l.config(text='I like Python and Python')

#初始化两个数值  用作判断
var1=tk.IntVar()
var2=tk.IntVar()

cPython=tk.Checkbutton(window,text='Python',
                       variable=var1,onvalue=1,offvalue=0,
                       command=print_selection)
cCplus=tk.Checkbutton(window,text='C++',
                       variable=var2,onvalue=1,offvalue=0,
                       command=print_selection)
#这里设置了一个左对齐 (多行才有效)，和文本在Label中的位置，比如w center e
#最后一个wraplength则是多少个单位之后发生换行
#具体可参阅博客 https://blog.csdn.net/aa1049372051/article/details/51858904
chooselabel=tk.Label(window,bg='green',width=40,
                     text='Choose the option/language you like',
                     justify='left',anchor='w',wraplength = 180)

chooselabel.pack()
cPython.pack()
cCplus.pack()

window.mainloop()

