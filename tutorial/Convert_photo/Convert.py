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
import webbrowser
'''打包程序，加上新图标，并且不出现命令行（解释器，黑色的窗口）,pyinstaller -F -i pic.ico Convert.py -w'''


'''查找文件函数'''
namelist = []

# 获取文件列表
def ReadAllfile():
    global namelist
    namelist = [x for x in os.listdir('.') if ('.jpg' in x) or ('.png' in x) or ('.bmp' in x)]


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


# 字典存储裁剪信息
cutphotoInfo = {}
#裁剪窗口函数
def CutPhoto():
    global cutphotoInfo
    window_resize = tk.Toplevel(window)
    window_resize.geometry('250x250')
    window_resize.title('resize')
    width, heiht = GetPhtoSize()
    tk.Label(window_resize, bg='LightGrey',width=35,text='原始图片 高x宽 ' + str(heiht) + 'x' + str(width),anchor='c').place(x=0, y=0)
    tk.Label(window_resize, text='是否调整大小？').place(x=10, y=25)
    vresize_yesno=tk.StringVar()
    vresize_yesno.set('no')
    tk.Radiobutton(window_resize, text='否', variable=vresize_yesno, value='no').place(x=100, y=25)
    tk.Radiobutton(window_resize, text='是', variable=vresize_yesno, value='yes').place(x=140, y=25)

    tk.Label(window_resize,bg='LightGrey',height=2,width=40).place(x=0,y=45)
    tk.Label(window_resize, bg='LightGrey',text='调整 高x宽 为').place(x=10, y=54)
    vwidth = tk.StringVar()
    vheigth = tk.StringVar()
    tk.Entry(window_resize, bg='LightGrey',textvariable=vheigth, width=5).place(x=100, y=54)
    tk.Label(window_resize, bg='LightGrey',text='x').place(x=140, y=54)
    tk.Entry(window_resize, bg='LightGrey',textvariable=vwidth, width=5).place(x=150, y=54)
    tk.Label(window_resize, bg='LightGrey',text='像素').place(x=190, y=54)

    tk.Label(window_resize, text='是否裁剪图片？',anchor='nw').place(x=10, y=90)
    vcut_yesno = tk.StringVar()
    vcut_yesno.set('no')
    tk.Radiobutton(window_resize, text='否', variable=vcut_yesno, value='no').place(x=100, y=90)
    tk.Radiobutton(window_resize, text='是', variable=vcut_yesno, value='yes').place(x=140, y=90)

    # 分割
    tk.Label(window_resize, bg='LightGrey', width=40, height=6).place(x=0, y=110)
    tk.Label(window_resize, bg='LightGrey', text='裁剪比例').place(x=10, y=115)
    ResizeRatio = tk.IntVar()
    ResizeRatio.set(16)
    tk.Radiobutton(window_resize, bg='LightGrey', text='16:9', variable=ResizeRatio, value=16).place(x=10, y=145)
    tk.Radiobutton(window_resize, bg='LightGrey', text='4:3', variable=ResizeRatio, value=4).place(x=60, y=145)
    tk.Radiobutton(window_resize, bg='LightGrey', text='1:1', variable=ResizeRatio, value=1).place(x=110, y=145)
    tk.Radiobutton(window_resize, bg='LightGrey', text='自定义尺寸', variable=ResizeRatio, value=0).place(x=160, y=145)
    CustResize_height = tk.StringVar()
    CustResize_width = tk.StringVar()
    tk.Entry(window_resize, bg='LightGrey', textvariable=CustResize_height, width=8).place(x=30, y=170)
    tk.Entry(window_resize, bg='LightGrey', textvariable=CustResize_width, width=8).place(x=110, y=170)
    tk.Label(window_resize, bg='LightGrey', text='高').place(x=5, y=170)
    tk.Label(window_resize, bg='LightGrey', text='宽').place(x=90, y=170)
    tk.Label(window_resize, bg='LightGrey', text='像素').place(x=190, y=170)
    tk.Label(window_resize, bg='LightGrey', text='默认采用居中裁剪').place(x=60,y=195)

    #存储信息到字典中
    def ConfirmSize():
        global cutphotoInfo
        cutphotoInfo['resize_yesno']=vresize_yesno.get()
        cutphotoInfo['width']=vwidth.get()
        cutphotoInfo['height']=vheigth.get()

        cutphotoInfo['cut_yesno']=vcut_yesno.get()
        cutphotoInfo['mode']=ResizeRatio.get()
        cutphotoInfo['cut_height']=CustResize_height.get()
        cutphotoInfo['cut_width']=CustResize_width.get()

        window_resize.destroy()

    tk.Button(window_resize, text='确认', width=5, height=1, command=ConfirmSize).place(x=90,y=220)


#根据字典内容创建图像
def CreatPhoto():
    #得到图像文件名
    sourPhotoname=photoname.get()
    creatPhotoname=GenerPhotoName.get()
    #得到生成格式名
    creatPhotoformat=vFormat.get().strip('.') #得到.jpg 为了方便下面使用，去掉首尾的.字符
    try:
        img = Image.open(sourPhotoname)
    except FileNotFoundError as e:
        tk.messagebox.showerror(title='File Not Found', message='未找到文件')
        return
    #字典中的信息不存在 则证明没有打开裁剪选项框
    if (cutphotoInfo.get('cut_yesno')==None) or (cutphotoInfo.get('resize_yesno')==None):
        savePhoto=img

    #需要调整大小
    elif cutphotoInfo['resize_yesno']=='yes':
        resizew=int(cutphotoInfo['width'])
        resizeh=int(cutphotoInfo['height'])
        savePhoto=img.resize((resizew, resizeh), Image.ANTIALIAS) # resize image 带ANTIALIAS滤镜缩放结果，放大质量高

    #需要裁剪
    elif cutphotoInfo['cut_yesno']=='yes':
        w,h=img.size
        cenw=w/2;cenh=h/2
        max_wh=max(w,h)
        min_wh=min(w,h)
        #对于不同的裁剪方式，使用不同的函数
        if cutphotoInfo['mode']==0:
            savePhoto=img.crop([cenw-int(int(cutphotoInfo['cut_width'])/2),cenh-int(int(cutphotoInfo['cut_height'])/2),
                               cenw+int(int(cutphotoInfo['cut_width'])/2),cenh+int(int(cutphotoInfo['cut_height'])/2)])
        elif cutphotoInfo['mode']==1:
            savePhoto = img.crop([cenw -int( min_wh/2), cenh - int(min_wh/2),
                                 cenw + int(min_wh/2), cenh + int(min_wh/2)])
        elif cutphotoInfo['mode']==4:
            if float(w/h)>float(3/4):
                #图片过宽
                savePhoto = img.crop([cenw - int(h*3/8), 0,#(h*3/4)/2
                                     cenw + int(h*3/8), h])
            else:
                # 图片过高
                savePhoto = img.crop([0 , cenh-int(w*2/3),#(w*4/3 )/2
                                     w , cenh+int(w*2/3)])
        elif cutphotoInfo['mode']==16:
            if float(w/h)>float(9/16):
                #图片过宽
                savePhoto = img.crop([cenw - int(h*9/32), 0,#(h*9/16)/2
                                     cenw + int(h*9/32), h])
            else:
                # 图片过高
                savePhoto = img.crop([0 , cenh-int(w*8/9),#(w*16/9 )/2
                                     w , cenh+int(w*8/9)])
    else:
        savePhoto = img
    #这里jpg的格式有点特殊，文件名后缀jpg ，但输入必须是jpeg
    if creatPhotoformat=='jpg':
        savePhoto.save(creatPhotoname, 'jpeg')
    else:
        savePhoto.save(creatPhotoname,creatPhotoformat)



ReadAllfile()
'''图形界面部分'''
# 创建图形化界面
window = tk.Tk()
window.title('图片转换工具v1.0')
window.geometry('350x170')
photoname = tk.StringVar()
photoname.set(GetPhotoName())
tk.Label(window, font=('SimHei', 10), text='输入图片名', anchor='w').place(x=10, y=10)
tk.Entry(window, textvariable=photoname, width=10).place(x=150, y=10)

tk.Label(window, font=('SimHei', 10), text='生成格式', anchor='w').place(x=10, y=30)
vFormat = tk.StringVar()
vFormat.set('.jpg')
pFormatJPG = tk.Radiobutton(window, text='jpg', variable=vFormat, value='.jpg', command=PrtGenName).place(x=150, y=30)
pFormatPNG = tk.Radiobutton(window, text='png', variable=vFormat, value='.png', command=PrtGenName).place(x=200, y=30)
pFormatJPG = tk.Radiobutton(window, text='bmp', variable=vFormat, value='.bmp', command=PrtGenName).place(x=250, y=30)
pFormatJPG = tk.Radiobutton(window, text='gif', variable=vFormat, value='.gif', command=PrtGenName).place(x=300, y=30)

tk.Label(window, font=('SimHei', 10), text='输入要生成的文件名', anchor='w').place(x=10, y=55)
GenerPhotoName = tk.StringVar()
GenerPhotoName.set(GetGenerPhoName())
tk.Entry(window, textvariable=GenerPhotoName, width=10).place(x=150, y=55)

tk.Label(window, font=('SimHei', 10), text='是否裁剪或调整大小', anchor='w').place(x=10, y=75)
vResize = tk.StringVar()
vResize.set('no')
tk.Radiobutton(window, text='否', variable=vResize, value='no').place(x=150, y=75)
tk.Radiobutton(window, text='是', variable=vResize, value='yes', command=CutPhoto).place(x=220, y=75)

tk.Button(window, text='确认生成',bg='Gainsboro',  height=1, command=CreatPhoto).place(x=140,y=100)

#超链接
tk.Label(window,font=('Arial', 10),text='Designed by LJjia').place(x=15,y=140)
text = tk.Text(window,width=30,font=('Arial', 10),height=1,bg='Silver')#银灰
text.place(x=140,y=140)
text.insert(tk.INSERT,"欢迎一起学习,源码可以参见网址")
text.tag_add("link","1.11","1.15")#后面两个参数的意思是 1行4列 到 1行8列为超链接  即最后四个字超链接
text.tag_config("link",foreground="blue",underline=True)

def click(event):
    webbrowser.open("https://github.com/LJjia/Tkinter/tree/master/tutorial/Convert_photo")
text.tag_bind("link","<Button-1>",click)


if __name__ == '__main__':
    window.mainloop()

