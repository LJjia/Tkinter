#!/usr/bin/env python
#coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  List.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/29 20:10
#        Email @  LJjiahf@163.com
#  Description @  ListBox
# ********************************************************************



import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x400')
'''注意了，这里使用pack，个个对象是依次pack进去的，因此如果窗口设置的过小，
而pack的内容过多，会导致有些对象在窗口中看不到'''

var1 = tk.StringVar()
#创建一个Label
l=tk.Label(window,bg='yellow',width=10,textvariable=var1)
l.pack()



def print_selection():
    #获取光标选择的值为value
    value=lb.get(lb.curselection())
    var1.set(value)


#command 传入的参数为点击按钮时执行的函数
b = tk.Button(window, text='print selelction',  height=2, command=print_selection)
b.pack()


var2=tk.StringVar()
#var2.set(2)
var2.set([11,22,33,44,55])
#创建ListBox 其listvariable的输入参数可以是一个 值，list，tuple
lb=tk.Listbox(window,listvariable=var2)
#当然lb这个Listbox也可以调用insert方法，与之前的文本框类似
lb.insert('end',[1,2,3,4])
for i in ['t1','t2','t3']:
    lb.insert('end',i)
lb.insert(1,'first')
lb.insert(2,'second')
#删除
lb.delete(2)
lb.pack()

window.mainloop()
