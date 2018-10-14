#!/usr/bin/env python
#coding=utf-8
__author__ = 'Jia Liangjun'
# *******************************************************************
#     Filename @  format_conv.py
#       Author @  Jia Liangjun
#  Create date @  2018/10/12 21:41
#        Email @  LJjiahf@163.com
#  Description @  图片转化格式尝试
# ********************************************************************
from PIL import Image
img=Image.open('1.jpg')
img.save('format.bmp','bmp')
