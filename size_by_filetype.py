from size_readable_m2 import sizeReadable


def sizeByFileType(path):

    import os
    import glob

    folder = glob.glob(path + "/*")

    file_list = []

    ext_list = []

    type_count = []

    for file_path in folder:
        if os.path.isfile(file_path):
            file_list.append(file_path)

    for file in file_list:
        file = file.split(".")[-1]
        ext_list.append(file)

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

    for typef in type_count:

        space_1 = 15 - (len(typef[2]) + len(str(typef[1])))
        size_readable = sizeReadable(typef[0])
        space_2 = 15 - len(size_readable)

        print(
            f'{typef[2]}  {space_1 * "."}  {typef[1]}  {space_2 * "."}  {size_readable}')


sizeByFileType('/media/zhrcosta/10F0F41BF0F4092C/Users/Guilherme/Downloads')
