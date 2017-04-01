# -*- coding: utf-8 -*-
def read(src, sheet_name, app, find_col):
    wb = app.books.open(src)
    sheet = wb.sheets[sheet_name]
    src_data = []
    for i in range(len(find_col)):
        src_data.append(sheet.range(find_col[i]).expand('down').value)
    wb.close()
    return src_data

