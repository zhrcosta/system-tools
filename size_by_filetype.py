from size_readable_m2 import sizeReadable
import os
import glob

def sizeByFileType(path):
    
    if os.path.isdir(path):
        if path[-1] != '/':
            path = path + '/'
            folder = glob.glob(path + '*')
    else:
        print('não é um diretorio')

    file_list = [file for file in folder if os.path.isfile(file)]

    ext_list = [file.split(".")[-1] for file in file_list]

    type_count = []

    for ext in set(ext_list):
        exttype = ext.upper()
        amount = 0
        size = 0

        for file_path in file_list:
            if file_path.split(".")[-1] == ext:
                amount += 1
                size += os.path.getsize(file_path)

        type_count.append((size, amount, exttype))

    type_count = sorted(type_count)[::-1]

    print('\n')

    for index, values in enumerate(type_count):
        size = f'{values[0]:,} - Bytes'.replace(',','.')
        size_h = sizeReadable(values[0])
        amount = values[1]
        ext = values[2]

        space_1 = 10 - (len(str(amount))+ len(ext))
        space_2 = 20 - len(size_h)
        space_3 = 30 - len(size)
        print(f'{ext} {space_1 * "."} {amount} {space_2 * "."} {size_h} {space_3 * "."} {size}')

    print('\n')
sizeByFileType()
