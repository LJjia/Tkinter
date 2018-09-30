#!/usr/bin/env python
#coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  frm.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/30 10:24
#        Email @  LJjiahf@163.com
#  Description @  Frame框架
# ********************************************************************

#Frame框架就像是一个window窗口内的布局，为了让窗口显得更加好看而布局

import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x200')

l1=tk.Label(window,text='on the window').pack()

#在window上创建一个Frame
frm=tk.Frame(window,bg='green')
frm.pack()

#在Frame上创建两个子Frame  不过这里好像无法添加颜色
subFrmLeft=tk.Frame(frm,bg='blue')
subFrmRight=tk.Frame(frm,bg='purple')

#在pack的基础上加上相对位置
subFrmLeft.pack(side='left')
subFrmRight.pack(side='right')

#在子Frame上添加标签
tk.Label(subFrmLeft,text='on the left 1').pack()
tk.Label(subFrmLeft,text='on the left 2').pack()
tk.Label(subFrmRight,text='on the right 1').pack()

window.mainloop()

