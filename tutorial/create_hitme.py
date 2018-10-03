#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' test module '

__author__ = 'Liangjun Jia'

import tkinter as tk

#创建窗口
window=tk.Tk()
#设置窗口属性
window.title('my title')
window.geometry('400x200')

#对字符串类型的封装，常用在button上，其内容改变，button上的值也随之改变
var=tk.StringVar()


'''
#建立标签  建立于窗口上，输入文字'This is Tk'，颜色gray，字体，长宽为字符长度
l=tk.Label(window,text='This is Tk，你好',bg='gray',font=('Arial',12),
           width=15,height=2)
'''
#建立标签  建立于窗口上，输入文字'This is Tk'，颜色gray，字体，长宽为字符长度
l=tk.Label(window,textvariable=var,bg='gray',font=('Arial',12),
           width=15,height=2)

#放置标签
l.pack()

on_hit=False#是否点击了按钮
#定义下文中command命令所需函数hit_me
#注意这里的hit_me是点击按钮之后触发，因此var这个变量一开始是’‘按下之后，触发第一次
def hit_me():
    global on_hit
    if not on_hit:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')


#放置按钮button  最后一个command的命令带入的是一个函数，表示按这个按钮会触发的函数
b=tk.Button(window,text='hit me 点我',width=20,height=4,command=hit_me)
b.pack()

#窗口主循环
window.mainloop()