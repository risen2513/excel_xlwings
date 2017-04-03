# -*- coding: utf-8 -*-
def read(src, sheet_name, app, find_col):
    src_data = []
    wb = app.books.open(src)
    sheet = wb.sheets[sheet_name]
    # src_data.append(sheet.range(find_col[0]).expand('down').value)
    end_row = sheet.range(find_col[0]).end('down').row
    # end_col = sheet.range(find_col[1]).column#.get_address(False, False)
    # print sheet.range((end_row, end_col)).get_address(False, False)
    # xw.Range((1, 1)).get_address(False, False)
    # print sheet.range(sheet.range(find_col[1])).expand('down').value
    # print sheet.range(find_col[0],sheet.range(find_col[0]).end('down').get_address(False, False)).value
    for i in range(len(find_col)):
        end_col = sheet.range(find_col[i]).column
        end = sheet.range((end_row, end_col)).get_address(False, False)
        src_data.append(sheet.range(find_col[i], end).value)
    wb.close()
    # print src_data[0]
    # print src_data[1]
    # print src_data[2]
    # if u'71-314' in src_data[0]:
    #     index = src_data[0].index(u'71-314')
    #     print src_data[0][index], src_data[1][index],src_data[2][index]
    #
    #
    # app.quit()
    # exit()
    return src_data

