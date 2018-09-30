#!/usr/bin/env python
#coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  placepart.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/30 15:19
#        Email @  LJjiahf@163.com
#  Description @  
# ********************************************************************


import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x200')
#
#  pack place  grid多种方法放置
#！！但是这多种放置方法不可以混用！！！！否则会报错

# tk.Label(window,text=[1,2,3,4,5],bg='blue').pack(side='left')
# tk.Label(window,text=1,bg='blue').pack(side='right')
# tk.Label(window,text='1',bg='blue').pack(side='top')
# tk.Label(window,text=1,bg='blue').pack(side='bottom')

# for i in range(5):
#     for j  in  range(6):
#         tk.Label(window,text=2,bg='green').grid(row=i,column=j,
#                                                 padx=15,pady=5)
#最后两个padx，pady是用于调整单元格横向，竖向大小的

#anchor默认值就是'nw'
tk.Label(window,text=3,bg='gray').place(x=0,y=0,anchor='nw')


window.mainloop()