#!/usr/bin/env python
# coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  Example1.py
#       Author @  Jia LiangJun
#  Create date @  2018/9/30 15:54
#        Email @  LJjiahf@163.com
#  Description @  制作登陆窗口
# ********************************************************************

import tkinter as tk
from tkinter import messagebox
import pickle

window = tk.Tk()
window.title('Login in Window')
window.geometry('500x480')  # 宽500高480

# 背景图
canvas = tk.Canvas(window, height=200, width=500)
BackDataPath_laptop = 'D:/PythonCode/PyCharmCode/Code/Data/'
image_file = tk.PhotoImage(file=BackDataPath_laptop + 'LoginBg.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)  # 把图片放置于画布上
canvas.pack(side='top')

# 输入用户名和密码 布局
tk.Label(window, text='User Name:', anchor='w').place(x=50, y=250)
tk.Label(window, text='Password:', anchor='w').place(x=50, y=290)

var_user_name = tk.StringVar()  # 这个变量是默认存在于输入框中，用以提示作用的
var_user_name.set('example@163.com')
var_user_passport = tk.StringVar()  # 用于存储输入的密码
# 建立两个Entry
entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=150, y=250, width=200, anchor='nw')
entry_user_passport = tk.Entry(window, textvariable=var_user_passport, show='·')
entry_user_passport.place(x=150, y=290, width=200, anchor='nw')


# 按钮对应的函数
def user_login():
    global BackDataPath_laptop  # 获取数据地址
    # 获取用户输入的username 和 passort
    user_name = var_user_name.get()

    '''对于错误的用户名处理，这里该怎么做？
    其实这里不需要，因为这里只是根据输入的用户名找，如果用户名出错，会一律回归为没有找到对应用户名'''

    user_pwd = var_user_passport.get()
    # 第一次执行的时候，由于文件不存在，会报错，因此在这里设置异常捕获
    # 因此往往需要先注册，创建文件，然后再登陆
    try:
        with open(BackDataPath_laptop + 'user_info.pickle', 'rb') as user_file:
            user_Dict = pickle.load(user_file)
    except FileNotFoundError:  # 如果没有发现文件，就执行如下语句
        # 创建写文件  写入初始管理员账号和密码
        with open(BackDataPath_laptop + 'user_info.pickle', 'wb') as user_file:
            user_Dict = {'admin': 'admin'}
            pickle.dump(user_Dict, user_file)
        '''pickle的作用仅限于Python内部保存处理数据，可以讲数据固化成字典的形式，便于后续查阅
        但是对于其他的平台，则无法通用，不能相互传递数据'''

    # 获取到用户名和密码后和保存的数据集 user_Dict对比。对正确和错误的密码分别对待
    if user_name in user_Dict:  # 找到用户名
        if user_pwd == user_Dict[user_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you?' + user_name)
        else:  # 错误的密码
            tk.messagebox.showerror(message='Error!your passort is wrong,try again')
    else:  # 没有找到用户名
        is_sign_up = tk.messagebox.askyesno(title='Error,Don\'t find the user', message='Do you want'
                                                                                        ' to sign up Now?')  # 返回True False
        if is_sign_up:
            user_sign_up()  # 调用下面的注册函数
        else:
            return
            #如果此处是user_login()那么就是再次调用自己，也就是说按了否之后，串口仍再起开启，一直关不掉


def user_sign_up():
    def sign2email():
        # 获取新窗口输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        # 判断两次输入的密码是否相同
        if np!=npf:
            tk.messagebox.showerror(title='Error',message='Passort Must be Same')
            return
        try:
            #打开记录的数据文件，将数据读入
            with open(BackDataPath_laptop+'user_info.pickle','rb') as user_file:
                exist_user_info=pickle.load(user_file)
        #类似的，在这里也是如果一开始没有数据库文件，先建立一个数据库，存储管理员
        except FileNotFoundError:
            with open(BackDataPath_laptop+'user_info.pickle','wb') as user_file:
                user_Dict={'Admin':'Admin'}
                pickle.dump(user_Dict,user_file)

        #读取到了exist_user_info
        if nn in exist_user_info:#用户已存在
            tk.messagebox.showerror(title='Error',message='User has already signed up')
        else:#输入正确
            exist_user_info[nn]=np#创建新用户
            with open(BackDataPath_laptop+'user_info.pickle','wb') as user_file:
                pickle.dump(exist_user_info,user_file)
            tk.messagebox.showinfo(title='Hi',message='You have successfully signed up')
            window_sign_up.destroy()#关闭这个注册子窗口





    # 这句话的含义是在window基础上再生成一个优先级(置于最前)的窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('400x300')
    window_sign_up.title('Sign up window')
    # 获取新窗口中输入的一些 变量 Label 和 Entry
    new_name = tk.StringVar()
    new_name.set('example@163.com')
    new_pwd = tk.StringVar()
    new_pwd_confirm = tk.StringVar()

    tk.Label(window_sign_up, text='User name').place(x=10, y=10)
    tk.Label(window_sign_up, text='Passort').place(x=10, y=50)
    tk.Label(window_sign_up, text='Confirm passort').place(x=10, y=90)

    tk.Entry(window_sign_up, textvariable=new_name, show=None).place(x=150, y=10)  # 用户名
    tk.Entry(window_sign_up, textvariable=new_pwd, show='·').place(x=150, y=50)  # 第一次输入密码
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='·').place(x=150, y=90)  # 验证密码

    # 创建Button
    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign2email).place(x=150, y=130)


# 创建按钮布局
# 登陆按钮
btn_login = tk.Button(window, text='login in', width=15, command=user_login)
btn_login.place(x=80, y=320)
# 注册按钮
btn_sign_up = tk.Button(window, text='sign up', width=15, command=user_sign_up)
btn_sign_up.place(x=220, y=320)


if __name__=='__main__':
    window.mainloop()
