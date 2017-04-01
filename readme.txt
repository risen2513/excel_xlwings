Python 2.7

Installation:
pip install xlwings


APIs：
http://docs.xlwings.org/en/stable/api.html

Todo:
[ ]for循环遍历效率低，需改善
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



Usage:

一，两个Excel查找指定ID复制数据到指定列
 xls2xls.py
 调用do_copy_job() 使用copy_write_excel，open_excel，function的copy_data
 配置文件：
    copy_setting.txt
 例：
    A2,B2,D2,E2
    A2#B,C,D
 说明：
    第一行是源文件的列（可以指定从哪行开始），第一个值为搜索列，用来与目标文件比较相同行，后面的都是要复制的数据的列
    第二行是目标文件的列，第一个值是搜索列，数据与源文件搜索列数据对比（可以指定从哪行开始）。#号分割符后面的是对应赋值的列（不写行号）

