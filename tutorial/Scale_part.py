#!/usr/bin/env python
# coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  Scale_part.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/29 21:18
#        Email @  LJjiahf@163.com
#  Description @  Scale部件
# ********************************************************************

import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x200')

l = tk.Label(window, bg='yellow', width=30, text='empty')
l.pack()


# 注意这里有个入参v   v默认为是Scale的标签值，也就是当前选择的精度
def print_selection(v):
    l.config(text='you have select ' + v)


'''解释一下Scale中各个参数的含义：
label表示这个Scale的名字，
from，to 分别代表标签的起始值和终止值
orient代表了Scale的方向是水平还是竖直
len表示Scale的长度(以像素为单位),
showvalue代表是否显示当前标签所处位置的值，
tickintrval代表每隔多少值显示一个刻度，
resolution代表值显示的精度，这里为两位小数
最后command代表 拉动 滑块的时候会触发的函数，输入值默认为当前滑块所处位置的值'''
s = tk.Scale(window, label='pull me', from_=5.0, to=11,
             orient=tk.HORIZONTAL, len=800,
             showvalue=False, tickinterval=2, resolution=0.01,
             command=print_selection)
s.pack()

window.mainloop()
