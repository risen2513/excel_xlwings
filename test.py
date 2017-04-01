# -*- coding: utf-8 -*-
import xlwings as xw
def open_excel(src,target):
    app = xw.App(visible = None, add_book = False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(target)
    sheet = wb.sheets['hello']

    sht = app.books.open(src).sheets[u'テスト']
    src_data = []
    src_A = sht.range('A2').expand('down').value
    src_B = sht.range('B2').expand('down').value
    src_data.append(src_A)
    src_data.append(src_B)

    col = 'A'
    row = 2

    target_A = sheet.range(col+str(row)).expand('down').value
    for irow in target_A:
        for jrow in range(len(src_data[0])):
            if src_data[0][jrow] == irow:
                sheet.range('B'+str(row)).value = src_data[1][jrow]
        row = row + 1

    wb.save()
    wb.close()
    app.quit()




if __name__ == '__main__':
    open_excel('./testdata/src.xls', './testdata/target.xls')
    # open_xls('./testdata/target.xls')
