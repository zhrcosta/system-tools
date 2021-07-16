from size_readable_m2 import sizeReadable
import os
import glob

def maxWordLen(word_list):
    num = 0

    for word in word_list:
        if len(word) >= num:
            num = len(word)

    return num

def maxSizeLenBytes(pathlist):
    num = 0

    for file in pathlist:
        size = f'{os.path.getsize(file):,} - Bytes'.replace(',','.')

        if len(size) > num:
            num = len(size)

    return num

def maxSizeLen(pathlist):
    num = 0

    for file in pathlist:
        size = sizeReadable(os.path.getsize(file))

        if len(size) > num:
            num = len(size)

    return num

def sizeByFile(path):

    if os.path.isdir(path):
        if path[-1] != '/':
            path = path + '/'
            file_list = os.listdir(path)
        else:
            file_list = os.listdir(path)
    else:
        print('não é um diretorio')

    file_list = [file for file in file_list if os.path.isfile(f'{path}{file}')]
    file_path = [f'{path}{file}' for file in file_list]

    maxchar = maxWordLen(file_list)
    maxsizeH = maxSizeLen(file_path)

    gap = maxsizeH + maxchar + 5

    maxsizeB = maxSizeLenBytes(file_path)

    print()

    for index, *_ in enumerate(file_list):

        size = f'{os.path.getsize(file_path[index]):,} - Bytes'.replace(',','.')
        size_h = sizeReadable(os.path.getsize(file_path[index]))
        file = file_list[index]
        space_1 = gap - (len(file) + len(size_h))
        space_2 = (maxsizeB + 3) - (len(size))

        print(f'{file}  {space_1 * "."}  {size_h}  {space_2 * "."}  {size}')
    
    print()

sizeByFile('Downloads/')

