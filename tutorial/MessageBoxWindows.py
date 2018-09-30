#!/usr/bin/env python
#coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  MessageBoxWindows.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/30 15:04
#        Email @  LJjiahf@163.com
#  Description @  
# ********************************************************************

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('My window')
window.geometry('400x200')
def hit_me():
    #注意Windows下 error的图标会有些不同
    # tk.messagebox.showinfo(title='Hi',message='This is a messagebox')
    tk.messagebox.showerror(title='Hi', message='This is a messagebox')
    # tk.messagebox.showwarning(title='Hi', message='This is a messagebox')
    #有返回值的弹窗
    print(tk.messagebox.askquestion(title='Hi',message='This'))       # 返回yes和no(字符串类型)
    # print(tk.messagebox.askokcancel(title='Hi',message='This'))     # 返回true和false
    # print(tk.messagebox.askyesno(title='Hi',message='This'))        # 返回true和false
    # print(tk.messagebox.askretrycancel(title='Hi',message='This'))  # 返回true和false


tk.Button(window,text='点我',command=hit_me).pack()

window.mainloop()