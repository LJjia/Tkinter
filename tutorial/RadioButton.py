#!/usr/bin/env python
#coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  RadioButton.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/29 20:56
#        Email @  LJjiahf@163.com
#  Description @  选择按钮
# ********************************************************************


import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x400')

var = tk.StringVar()
l=tk.Label(window,bg='yellow',text='empty',height=2,width=20)
#如果不输入width参数 label的宽度也会随着输入自负串长度自动改变
l.pack()

def print_selection():
    #config可以修改Label中的内容
    l.config(text='you choose selection '+var.get())

#这句话的含义是点击这个选择则这个按钮之后，将'A'赋值给var这个StringVar
#并且执行print_selection这个函数
rA=tk.Radiobutton(window,text='Option A',
                  bg='blue',
                  variable=var,value='A',
                  command=print_selection)
rA.pack()
rB=tk.Radiobutton(window,text='Option B',
                  variable=var,value='B',
                  command=print_selection)
rB.pack()
rC=tk.Radiobutton(window,text='Option C',
                  variable=var,value='C',
                  command=print_selection)
rC.pack()

window.mainloop()
