# -*- coding: utf-8 -*-
import datetime
import xlwings
import copy_write_excel as copy
from copy_open_excel import read
from function import copy_data


def job(src, src_sheet_name, target, target_sheet_name, config, type):
    (find_col, set_col) = copy_data(config)
    starttime = datetime.datetime.now()
    app = xlwings.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    rdstarttime = datetime.datetime.now()
    src_data = read(src, src_sheet_name, app, find_col)
    rdendtime = datetime.datetime.now()
    wtstarttime = datetime.datetime.now()
    if type == 'search':
        write_data = copy.write_search(target, target_sheet_name, src_data, app, set_col)
    else:
        write_data = copy.write_copy(target, target_sheet_name, src_data, app, set_col)
    wtendtime = datetime.datetime.now()
    if write_data:
        app.quit()
        print "Done!"
    endtime = datetime.datetime.now()
    print "读取用时：", (rdendtime - rdstarttime).seconds, "秒"
    print "写入用时：", (wtendtime - wtstarttime).seconds, "秒"
    print "总用时：", (endtime - starttime).seconds, "秒"

# import copy_job.do_copy_job as copy_job
#
# if __name__ == '__main__':
#     conf_file = './testdata/copy_setting.txt'
#     src_file = ['./testdata/src.xls']
#     src_sheet = u'テスト'
#     target_file = './testdata/target.xls'
#     target_sheet = u'hello'
#     type = 'search' #search or copy
#     copy_job.job(src_file, src_sheet, target_file, target_sheet, conf_file, type)

