#!/usr/bin/env python
# coding=utf-8
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  unified.py
#       Author @  Jia LiangJun
#  Create date @  2018/10/11 11:08
#        Email @  LJjiahf@163.com
#  Description @  
# ********************************************************************
import os
import numpy as np
from PIL import Image

# 文件路径
maofeng_path = 'D:/Tea/image/maofeng/'
tieguanyin_path = 'D:/Tea/image/tieguanyin/'
maofengBad_path = 'D:/Tea/image/bad_maofeng/'

maofeng_cut_path = 'D:/Tea/image/maofeng_cut/'
tieguanyin_cut_path = 'D:/Tea/image/tieguanyin_cut/'
testpath = 'D:/Tea/image/test_cut'

# 设置图像的宽高
imgsize = 1000
imgwidth = 1500
imgheight = 1500
imgform = 'square'  # square rectangle

# 裁剪步长
cut_step = 200

# 滤波器默认开启
def fun(foldername, teaname, stdvaule,cutsize, filter=1):
    if teaname == 'tieguanyin':
        sourfile_path = tieguanyin_path
    elif teaname == 'maofeng':
        sourfile_path = maofeng_path
    else:
        pass
    namelist = [x for x in os.listdir(sourfile_path) if 'jpg' in x]
    namelist.sort(key=lambda x: int(x[:-4]))  # 倒着数第四位'.'为分界线，按照‘.’左边的数字从小到大排序
    img = Image.open(tieguanyin_path + namelist[0])
    # 先打开一个文件获得图像大小
    w, h = img.size
    print('图像大小为: %sx%s' % (w, h))
    # 图像形状
    if cutsize:
        imgsize=cutsize
    if imgform == 'square':
        imgheight = imgsize
        imgwidth = imgsize
    # 创建目录文件夹
    if teaname == 'tieguanyin':
        save_unuse_path = tieguanyin_cut_path + 'unuse_'+'tgy_' + foldername + '/'
        save_use_path = tieguanyin_cut_path + 'use_' + 'tgy_' + foldername + '/'
    if teaname == 'maofeng':
        save_unuse_path = maofeng_cut_path + 'unuse_' + 'mf_' + foldername + '/'
        save_use_path = maofeng_cut_path + 'use_' + 'mf_' + foldername + '/'
    print(save_unuse_path, save_use_path)
    # 如果不存在则创建目录# 创建目录操作函数 创建目录时末尾也可以有/
    if not os.path.exists(save_unuse_path):
        os.makedirs(save_unuse_path)
    if not os.path.exists(save_use_path):
        os.makedirs(save_use_path)
    # 不开启滤波器
    if filter == 0:
        temppath = testpath
    # 前10个
    all_count=0
    all_count_filter=0
    for i in namelist[:10]:
        print('filename', i)
        img = Image.open(sourfile_path + i)
        grayimg = img.convert('L')  # 转化为灰度图
        # 行列循环
        count = 0
        count_filter = 0
        count_nofilter = 0
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
                # 筛选标准差 数值由人工确定也是估算值
                # if graynp.std() > stdvaule:
                #     cut_img.save(save_use_path + '/' + i.split('.')[0] + '_' + str(count_filter) + '.jpg', 'jpeg')
                #     count_filter += 1
                if graynp.std() > stdvaule:
                    cut_img.save(save_use_path + '/' + str(all_count) + '.jpg', 'jpeg')
                    all_count += 1
                else:
                    cut_img.save(save_unuse_path + '/' + str(all_count_filter) + '.jpg', 'jpeg')
                    all_count_filter += 1
                # 不筛选标准差
                # cut_img.save(temppath + i.split('.')[0] + '_' + str(count) + '.jpg', 'jpeg')
                # count += 1


if __name__ == '__main__':

    # for i in range(25, 56, 4):
    #     for j in range(1000, 2001, 250):
    #         fun(foldername=str(j) + 'x' + str(j) + 'std' + str(i), cutsize=j,stdvaule=i, teaname='tieguanyin',)
    #
    # for i in range(30, 51, 4):
    #     for j in range(1000, 2001, 250):
    #         fun(foldername=str(j) + 'x' + str(j) + 'std' + str(i),cutsize=j, stdvaule=i, teaname='maofeng',)
    fun(foldername=str(1000) + 'x' + str(1000) + 'std' + str(38), cutsize=1000, stdvaule=38, teaname='maofeng', )
    fun(foldername=str(1000) + 'x' + str(1000) + 'std' + str(38), cutsize=1000, stdvaule=40, teaname='tieguanyin', )