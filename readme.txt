Python 2.7

Installation:
pip install xlwings
Windows需要安装pywin32(32位64位有区分)

APIs：
http://docs.xlwings.org/en/stable/api.html

Todo:
[x]查找替换条件通过List设置
[x]支持写入.xls和.xlsx
[x]可设置操作条件
[ ]生成条件配置文件（5中使用的文本数据库）
[x]数据库关联(文本文件格式)
[ ]根据条件Check文件内容
[x]两个文件：查找指定数据粘贴到另一个文件指定位置
[ ]GUI制作（wxPython or PyQt or Web2py）
[ ]可在程序中运行VBA脚本（通过GUI嵌入脚本）
[ ]封装成可脱离环境独立运行的程序（如：EXE）
[ ]for循环遍历效率低，需改善    ？？？？？


HomeWork：
生成配置文件
标题自定义    文件名为时间戳+随机数
保存到conf文件夹
该文件夹下添加index文本文件
用于存储配置文件标题和文件名
方便以后多配置文件使用
例:xxx业务复制工具，26587863244553
每行一个，读取时插入数组根据下标选择


多文件整合到一个文件
现在的两文件复制的源改成数组，循环读取到数组够再写入
单个源文件只循环一次，效果不变
每次打开文件速度可能很慢，参考vba做法




Usage:

一，两个Excel查找指定ID复制数据到指定列
 xls2xls.py
--------------------------------
# -*- coding: utf-8 -*-
import copy_job.do_copy_job as copy_job
if __name__ == '__main__':
    conf_file = './testdata/copy_setting.txt'
    src_file = ['./testdata/src.xls']
    src_sheet = u'テスト'
    target_file = './testdata/target.xls'
    target_sheet = u'hello'
    copy_job.job(src_file, src_sheet, target_file, target_sheet, conf_file)
--------------------------------

 配置文件：
    copy_setting.txt
 例：
    A2,B2,D2,E2
    A2#B,C,D
 说明：
    第一行是源文件的列（可以指定从哪行开始），第一个值为搜索列，用来与目标文件比较相同行，后面的都是要复制的数据的列
    第二行是目标文件的列，第一个值是搜索列，数据与源文件搜索列数据对比（可以指定从哪行开始）。#号分割符后面的是对应赋值的列（不写行号）

