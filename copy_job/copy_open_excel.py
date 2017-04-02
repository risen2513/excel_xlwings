# -*- coding: utf-8 -*-
def read(src, sheet_name, app, find_col):
    src_data = []
    for book in src:
        wb = app.books.open(book)
        sheet = wb.sheets[sheet_name]
        for i in range(len(find_col)):
            src_data.append(sheet.range(find_col[i]).expand('down').value)
        wb.close()
    return src_data

