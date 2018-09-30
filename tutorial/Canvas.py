#!/usr/bin/env python
#coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  Canvas.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/30 8:49
#        Email @  LJjiahf@163.com
#  Description @  Canvas画布功能
# ********************************************************************

import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x200')

#创建canvas对象  bg为background
canvas=tk.Canvas(window,bg='blue',height=100,width=400)
file_path_laptop='D:/PythonCode/PyCharmCode/Code/Data/'
image_file=tk.PhotoImage(file=file_path_laptop+'15.gif')
#这里10，10表示的是坐标（10,10）像素点，其坐标是以左上角为(0,0)
#向右 向下 增长，而anchor的作用是将图片的某个中心点放置于该(10,10)坐标点上
image=canvas.create_image(10,10,anchor='nw',image=image_file)
x0,y0,x1,y1=150,0,250,90
#创建一条直线
line=canvas.create_line(x0,y0,x1,y1)
#创建一个圆  这种画法是以四个坐标确定一个正方形，在这个正方形中填充圆
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')
#创建一个扇形 start和extend参数为起始角度和扇形旋转角度
arc=canvas.create_arc(x0+100,y0+40,x1+100,y1+40,start=0,extent=180)
#创建一个矩形
rect=canvas.create_rectangle(x0+50,y0+40,x1,y1)
canvas.pack()

def moveit():
    #canvas画布中的矩形向右平移0，向下平移10
    canvas.move(rect,0,10)

b=tk.Button(window,text='move',command=moveit).pack()

window.mainloop()

