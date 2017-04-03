# -*- coding: utf-8 -*-
def write_search(target, sheet_name, src_data, app, set_col):
    wb = app.books.open(target)
    sheet = wb.sheets[sheet_name]
    search_col = set_col[0][0]
    target_A = sheet.range(search_col).expand('down').value
    start_row = sheet.range(search_col).row
    for irow in target_A:
        if irow in src_data[0]:
            index = src_data[0].index(irow)
            for i in range(len(set_col[1])):
                sheet.range(set_col[1][i]+str(start_row)).value = src_data[i+1][index]
        start_row += 1
    wb.save()
    wb.close()
    return True
