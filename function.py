# -*- coding: utf-8 -*-
def copy_data(file_name):
    set_cols = []
    find_cols = []
    file_object = open(file_name)
    i = 1
    for line in file_object:
        line = line.strip()
        if i == 1:
            find_cols = line.split(',')
        if i == 2:
            arr = line.split('#')
            set_cols.append(arr[0].split(','))
            set_cols.append(arr[1].split(','))
        i += 1
    return find_cols, set_cols
def create_conf(file_name, data):
    file_object = open(file_name, 'w')
    file_object.write(data)
    file_object.close()
