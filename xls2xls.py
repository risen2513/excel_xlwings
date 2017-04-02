# -*- coding: utf-8 -*-
import copy_job.do_copy_job as copy_job

if __name__ == '__main__':
    conf_file = './testdata/copy_setting_copy.txt'
    src_file = ['./testdata/src.xls', './testdata/src1.xls', './testdata/src2.xls']
    src_sheet = u'テスト'
    target_file = './testdata/target2.xls'
    target_sheet = u'hello'
    type = 'copy'
    copy_job.job(src_file, src_sheet, target_file, target_sheet, conf_file, type)
