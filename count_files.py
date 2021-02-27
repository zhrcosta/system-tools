

def countFiles(path):

    import os
    import glob

    
    type_count = []

    folder = glob.glob(path + "/*")

    file_list = []

    folders_amount = 0

    for file_type in folder:

        if os.path.isfile(file_type):
            file_list.append(file_type)

        else:
            if os.path.isdir(file_type):
                folders_amount += 1

    ext = [file.split(".")[-1] for file in file_list]

    for type in set(ext):
        type_count.append((ext.count(type), type.upper()))

    type_count = sorted(type_count)[::-1]
    type_count.append((folders_amount, "FOLDERS"))

    for type in type_count:
        extension = type[1]
        amount = type[0]
        space = 30 - (len(extension) + len(str(amount)))
        print(f'{extension} {space * "."} {amount}')


countFiles("test")
