from size_readable_m2 import sizeReadable
import os
import glob

def sizeByFile(path):

    if os.path.isdir(path):
        if path[-1] != '/':
            path = path + '/'
            file_list = os.listdir(path)
    else:
        print('não é um diretorio')

    file_list = [file for file in file_list if os.path.isfile(f'{path}{file}')]
    file_path = [f'{path}{file}' for file in file_list]
    
    for index, *_ in enumerate(file_list):

        size = f'{os.path.getsize(file_path[index]):,} - Bytes'.replace(',','.')
        size_h = sizeReadable(os.path.getsize(file_path[index]))
        print(file_list[index])
        print(size)
        print(size_h)
        print()

sizeByFile()

