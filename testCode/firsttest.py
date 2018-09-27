from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton(self,text='Hello',command=self.hello)
        self.alertButton.pack()
    # 在GUI中，每个Button、Label、输入框等，都是一个Widget(窗口小部件)
    # Frame(框架)则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
    # 　pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局
    # 在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hellow,%s'% name)


# 实例化Application 并且启动消息循环
app = Application()
# 设置窗口标语
app.master.title('hellow world')
# 主消息循环
app.mainloop()
