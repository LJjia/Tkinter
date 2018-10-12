#!/usr/bin/env python
# coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  Convert.py
#       Author @  Jia LiangJun
#  Create date @  2018/10/12 14:40
#        Email @  LJjiahf@163.com
#  Description @  图片转换工具
# ********************************************************************

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image

'''查找文件函数'''
namelist = []


# 获取文件列表
def ReadAllfile():
    global namelist
    namelist = [x for x in os.listdir('.') if ('.jpg' in x) or ('.png' in x)]


# 寻找首个图片文件 jpg或者png都有可能
def GetPhotoName():
    if namelist:
        return namelist[0]
    else:
        return None


# 以下两个函数是根据列表中的文件自动生成文件名以 photo 为前缀
def GetGenerPhoName():
    Format = vFormat.get()
    i = 1
    for x in namelist:
        if 'photo' + str(i) + Format in x:
            i += 1
    return 'photo' + str(i) + Format


def PrtGenName():
    GenerPhotoName.set(GetGenerPhoName())


# 获得图片大小
def GetPhtoSize():
    PhotoName = photoname.get()
    img = Image.open(PhotoName)
    w, h = img.size
    return w, h


# 列表存储裁剪信息
cutphotoInfo = []
# def printValue():
#     global vCut
#     print(vCut.get())

def CutPhoto():
    global cutphotoInfo
    window_resize = tk.Toplevel(window)
    window_resize.geometry('250x200')
    window_resize.title('resize the photo')
    width, heiht = GetPhtoSize()
    tk.Label(window_resize, text='原始图片 高x宽 ' + str(heiht) + 'x' + str(width)).place(x=10, y=10)

    tk.Label(window_resize, text='调整 高x宽 为').place(x=10, y=30)
    vwidth = tk.StringVar()
    vheigth = tk.StringVar()
    tk.Entry(window_resize, textvariable=vheigth, width=5).place(x=100, y=30)
    tk.Label(window_resize, text='x').place(x=140, y=30)
    tk.Entry(window_resize, textvariable=vwidth, width=5).place(x=150, y=30)
    tk.Label(window_resize, text='像素').place(x=190, y=30)

    tk.Label(window_resize, text='是否裁剪图片？').place(x=10, y=50)
    global  vCut
    vCut = tk.StringVar()
    vCut.set(False)
    # tk.Radiobutton(window_resize, text='否', variable=vCut, value=False,command=printValue).place(x=100, y=50)
    # tk.Radiobutton(window_resize, text='是', variable=vCut, value=True,command=printValue).place(x=140, y=50)
    tk.Radiobutton(window_resize, text='否', variable=vCut, value=False).place(x=100, y=50)
    tk.Radiobutton(window_resize, text='是', variable=vCut, value=True).place(x=140, y=50)

ReadAllfile()
'''图形界面部分'''
# 创建图形化界面
window = tk.Tk()
window.title('图片转换工具v1.0')
window.geometry('350x200')
photoname = tk.StringVar()
photoname.set(GetPhotoName())
tk.Label(window, font=('SimHei', 10), text='输入图片名', anchor='w').place(x=10, y=10)
tk.Entry(window, textvariable=photoname, width=10).place(x=150, y=10)

tk.Label(window, font=('SimHei', 10), text='生成格式', anchor='w').place(x=10, y=30)
vFormat = tk.StringVar()
vFormat.set('.jpg')
pFormatJPG = tk.Radiobutton(window, text='jpg', variable=vFormat, value='.jpg', command=PrtGenName).place(x=150, y=30)
pFormatPNG = tk.Radiobutton(window, text='png', variable=vFormat, value='.png', command=PrtGenName).place(x=220, y=30)

tk.Label(window, font=('SimHei', 10), text='输入要生成的文件名', anchor='w').place(x=10, y=55)
GenerPhotoName = tk.StringVar()
GenerPhotoName.set(GetGenerPhoName())
tk.Entry(window, textvariable=GenerPhotoName, width=10).place(x=150, y=55)

tk.Label(window, font=('SimHei', 10), text='是否裁剪或调整大小', anchor='w').place(x=10, y=75)
vResize = tk.StringVar()
vResize.set(False)
tk.Radiobutton(window, text='否', variable=vResize, value=False).place(x=150, y=75)
tk.Radiobutton(window, text='是', variable=vResize, value=True, command=CutPhoto).place(x=220, y=75)

if __name__ == '__main__':
    window.mainloop()
