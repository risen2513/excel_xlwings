# -*- coding: utf-8 -*-
def copy_data(file_name):
    set_cols = []  # [[] for i in range(2)]
    file = open(file_name)
    i = 1
    for line in file:
        line = line.strip()
        # print i, ":", line
        if i == 1:
            find_cols = line.split(',')
        if i == 2:
            arr = line.split('#')
            set_cols.append(arr[0].split(','))
            set_cols.append(arr[1].split(','))
        i += 1
    return find_cols, set_cols
