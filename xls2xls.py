# -*- coding: utf-8 -*-
import copy_job.do_copy_job as copy_job

if __name__ == '__main__':
    conf_file = './testdata/copy_setting_search.txt'
    #src_file = ['./testdata/src.xls', './testdata/src1.xls', './testdata/src2.xls']
    src_file = './testdata/zsrc.xlsx'
    src_sheet = u'Sheet2'
    target_file = './testdata/ztarget.xlsx'
    target_sheet = u'台帳'
    copy_job.job(src_file, src_sheet, target_file, target_sheet, conf_file)
