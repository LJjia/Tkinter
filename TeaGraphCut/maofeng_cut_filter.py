#!/usr/bin/env python
# coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  maofeng_cut.py
#       Author @  Jia LiangJun
#  Create date @  2018/10/10 16:40
#        Email @  LJjiahf@163.com
#  Description @  参阅博客
#                 https://blog.csdn.net/majinlei121/article/details/78933947
# ********************************************************************
import os
import numpy as np
from PIL import Image

# 文件路径
maofeng_path = 'D:/Tea/image/maofeng/'
tieguanyin_path = 'D:/Tea/image/tieguanyin/'
maofengBad_path = 'D:/Tea/image/bad_maofeng/'

maofeng_cut_path1 = 'D:/Tea/image/maofeng_cut1/'
maofeng_cut_path2 = 'D:/Tea/image/maofeng_cut2/'

# 设置图像的宽高
imgsize = 1000
imgwidth = 1000
imgheight = 1000
imgform = 'square'  # square rectangle

# 裁剪步长
cut_step = 200


def fun():
    namelist = [x for x in os.listdir(maofeng_path) if 'jpg' in x]
    namelist.sort(key=lambda x: int(x[:-4]))  # 倒着数第四位'.'为分界线，按照‘.’左边的数字从小到大排序
    img = Image.open(maofeng_path + namelist[0])
    # 先打开一个文件获得图像大小
    w, h = img.size
    print('图像大小为: %sx%s' % (w, h))
    # 图像形状
    if imgform == 'square':
        imgheight = imgsize
        imgwidth = imgsize
    # 根据步长分析

    # 前10个
    for i in namelist[:10]:
        print('filename', i)
        img = Image.open(maofeng_path + i)
        grayimg = img.convert('L')  # 转化为灰度图
        # 行列循环
        count=0
        count_filter = 0
        count_nofilter=0
        for row in range(0, h - imgheight, cut_step):
            for col in range(0, w - imgwidth, cut_step):
                # 裁剪图像
                cut_img = grayimg.crop([col, row, col + imgheight, row + imgheight])  # 从左到右->从上到下
                graynp = np.array(cut_img, dtype=np.uint8)

                # print('save file name',i.split('.')[0] + '_' + str(count))
                # print('图像的平均值%s,方差%s，标准差%s' % (graynp.mean(), graynp.var(), graynp.std()))
                # print('图像的和%s' % graynp.sum())
                # print('图像的最大值%s，最小值%s，取值范围%s，中位数%s' % (graynp.max(), graynp.min(), graynp.ptp(), np.median(graynp)))
                # print()
                '''试验表示 标准差对系统的影响性大一些，这里裁剪宽度1000*1000正方形，标准差大约38以上为好的图片
                因此path1作为不筛选标准差，path2为筛选标准差'''
                #筛选标准差 数值由人工确定也是估算值
                if graynp.std()>38:
                    cut_img.save(maofeng_cut_path2 + i.split('.')[0] + '_' + str(count_filter) + '.jpg', 'jpeg')
                    count_filter += 1
                else:
                    cut_img.save(maofeng_cut_path2 +'maofeng_filter/'+ i.split('.')[0] + '_' + str(count_nofilter) + '.jpg', 'jpeg')
                    count_nofilter += 1
                # 不筛选标准差
                # cut_img.save(maofeng_cut_path1 + i.split('.')[0] + '_' + str(count) + '.jpg', 'jpeg')
                # count += 1


if __name__ == '__main__':
    fun()
