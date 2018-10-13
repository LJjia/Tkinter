#!/usr/bin/env python
#coding=utf-8
__author__ = 'Jia Liangjun'
# *******************************************************************
#     Filename @  tool1.py
#       Author @  Jia Liangjun
#  Create date @  2018/10/3 19:43
#        Email @  LJjiahf@163.com
#  Description @  Excel工具
# ********************************************************************


import os
import xlwt
import xlrd
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from xlrd import xldate_as_tuple
import webbrowser#超链接
'''pyinsatller 工具可以多个参数一起使用，如下，但是需注意顺序。
以下例子是采用xlicon.ico 图标包装 Python文件CreatTools.py，并且生成单个可执行文件
pyinstaller -F -i xlicon.ico CreatTools.py'''

'''读取文件目录的函数'''
def ReadAllfile():
    #输入为一个字符串，读取当前目录下文件夹名
    print('当前目录：',os.path.abspath('.'),'找到文件')
    global namelist
    namelist=[x  for x in os.listdir('.') if ('xls' in x) and ('~' not in x) and ('file' not in x)]
    for x in namelist:
        print(x)
    return len(namelist)

'''Excel写入格式的函数'''
def stylish():
    # 设置字体
    font = xlwt.Font()  # Create Font
    # font.height = 20 * 12  # 字体大小
    # 创建单元格对其格式
    alignment = xlwt.Alignment()  # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER  # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    # 创建单元格边框
    borders = xlwt.Borders()  # Create Borders
    borders.left = xlwt.Borders.THIN  # DASHED虚线 NO_LINE没有 THIN实线
    # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40

    style = xlwt.XFStyle()  # Create Style
    style.alignment = alignment  # Add Alignment to Style
    style.borders = borders  # Add Borders to Style
    style.Font = font
    return style

'''读取Excel并且转换的函数'''
def start_xls():
    category=ChooseCategory.get()
    ifnot_name = 1
    if category=='序号':
        ifnot_name=0

    column=ChooseColumn.get()
    column=int(column)
    column-=1

    creatfile=CreateFilename.get()

    userData = {}  # 字典形式存储用户数据

    # 解析第一个文件，方便之后多次循环提高效率
    filename=namelist[1]
    data = xlrd.open_workbook(filename)#后面一个参数可以读取合并单元格
    table = data.sheet_by_index(0)  # 通过索引顺序获取
    nrows = table.nrows
    ncols = table.ncols  # 获取行数列数

    for i in range(nrows):
        if table.cell(i,column).value=='姓名' or table.cell(i,column).value=='序号':
            ModelLine=i#第i行为模板 则下一行为数据  这里不支持多行数据
            UserDataLine=i+1
            if i+2<nrows:
                print('多行数据，无法打印')
                return
    #读第一个文件，先写一个模板

    #读是否有合并单元格
    if_mergecell=table.merged_cells
    if if_mergecell:#非空
        mergecell=if_mergecell[0]#合并格式为 若是(0,1,2,9) 0行和1行 2列和9列合并
    mergecell_value=table.cell(mergecell[0], mergecell[2]).value
    #print('发现合并单元格,内容为',mergecell,)

    #读模板
    # try:
    #     for col in range(ncols):
    #         userData[table.cell(ModelLine, col).value] = table.cell(UserDataLine, col).value
    # except Exception as e:
    #     print(e)
    # print(userData,'模板')
    ModelKind=list(table.cell(ModelLine, col).value for col in range(ncols) )#模板类别，使用元组保存
    # 查找序号和姓名在列表中的索引
    order_1=0
    order_position=0
    if '序号' not in ModelKind:
        ModelKind.insert(0,'序号')#默认第一项为序号
        order_1=1
    order_position=ModelKind.index('序号')



    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    sheet1 = workbook.add_sheet('Sheet1',cell_overwrite_ok = True)#可以重复写入的表单

    style=stylish()

    #写合并单元格
    sheet1.write_merge(mergecell[0],mergecell[1]-1,mergecell[2],mergecell[3]-1,mergecell_value,style=style)
    #写模板单元格
    for col in range(ncols):
        #print(table.cell(ModelLine, col).value)
        sheet1.write(ModelLine,col,ModelKind[col],style=style)

    writefileLine = UserDataLine
    #写数据
    print('用户数据为:')
    for filename in namelist:
        data = xlrd.open_workbook(filename)
        table = data.sheet_by_index(0)  # 通过索引顺序获取
        #table = data.sheet_by_name(u'Sheet1')  # 通过名称获取Sheet1
        '''
        考虑下这里数据如何读取成文本形式 ，因为有些日期数字会出错
        '''
        #字典存储数据
        try:
            for col in range(ncols):
                ctype = table.cell(UserDataLine, col).ctype  # 表格的数据类型
                cell = table.cell_value(UserDataLine, col)
                #python读取excel中单元格的内容返回的有5种类型，即上面例子中的ctype:
                # ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error 如果是string形式就不转换
                if ctype == 2 :  # 如果是整形
                    cell = int(cell)
                elif ctype == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    #cell = date.strftime('%Y/%d/%m %H:%M:%S')#不需要年月日+时分秒的形式
                    cell = date.strftime('%Y/%d/%m')#年月日的形式
                elif ctype == 4:
                    cell = True if cell == 1 else False
                userData[table.cell(ModelLine, col).value] = cell
                #userData[table.cell(ModelLine,col).value]=table.cell(UserDataLine,col).value
                sheet1.write(writefileLine, col+order_1, userData[ModelKind[col]], style=style)
            #序号重新写 且默认第一个类别是序号
            sheet1.write(writefileLine, order_position, writefileLine-UserDataLine+1, style=style)
            writefileLine += 1
        except Exception as e:
            print(e)
        print(userData)


    workbook.save(creatfile+'.xls')


'''用户界面点击触发的函数'''
def Generate():

    filenum=ReadAllfile()
    genstart=tk.messagebox.askyesno(message='共发现文件%d个，确认是否启动统计？'%filenum)
    if genstart:#启动转换
        start_xls()
        #window.destroy()#便于用户观察显示数据，不摧毁窗口
    else:
        return



'''图形界面部分'''


#创建图形化界面
window = tk.Tk()
window.title('Excel 汇总工具v1.0')
window.geometry('350x200')
ChooseCategory=tk.StringVar()
ChooseCategory.set('姓名')
tk.Label(window,font=('Arial', 10),text='选择 姓名 或 序号 (将会以此类别为依据进行查找)',anchor='w').place(x=10,y=10)
rName=tk.Radiobutton(window,text='姓名',variable=ChooseCategory,value='姓名').place(x=10,y=30)
rOrder=tk.Radiobutton(window,text='序号',variable=ChooseCategory,value='序号').place(x=80,y=30)

tk.Label(window,font=('Arial', 10),text='输入该类别所在Excel中列数(数字)',anchor='w',).place(x=10,y=50)
ChooseColumn=tk.StringVar()
ChooseColumn.set('3')
tk.Entry(window,textvariable=ChooseColumn,width=10).place(x=10,y=70)
tk.Label(window,font=('Arial', 10),text='输入要生成的文件名',anchor='w').place(x=10,y=90)
CreateFilename=tk.StringVar()
CreateFilename.set('file')
tk.Entry(window,textvariable=CreateFilename,width=20).place(x=10,y=110)

gener=tk.Button(window, text='开始汇总', width=15, command=Generate).place(x=110,y=140)

tk.Label(window,font=('Arial', 10),text='Designed by LJjia').place(x=30,y=180)
#超链接
text = tk.Text(window,width=30,font=('Arial', 10),height=1,bg='Silver')#银灰

text.place(x=140,y=180)
text.insert(tk.INSERT,"欢迎一起学习,源码可以参见网址")

text.tag_add("link","1.11","1.15")#后面两个参数的意思是 1行4列 到 1行8列为超链接  即最后四个字超链接
text.tag_config("link",foreground="blue",underline=True)

def click(event):
    webbrowser.open("https://github.com/LJjia/Tkinter/tree/master/tutorial/Excel_tools")
text.tag_bind("link","<Button-1>",click)

if __name__ == '__main__':
    window.mainloop()