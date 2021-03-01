def sizeReadable(sizeInBytes):

    byte = 1
    kilobyte = 1024 * byte
    megabyte = 1024 * kilobyte
    gigabyte = 1024 * megabyte
    terabyte = 1024 * gigabyte
    petabyte = 1024 * terabyte

    if sizeInBytes < kilobyte:
        print(f'{sizeInBytes} - B')

    elif sizeInBytes == kilobyte:
        print(f'{sizeInBytes//kilobyte} - KB')

    elif sizeInBytes < megabyte:
        print(f'{sizeInBytes/kilobyte:.2f} - KB')

    elif sizeInBytes == megabyte:
        print(f'{sizeInBytes//megabyte} - MB')

    elif sizeInBytes < gigabyte:
        print(f'{sizeInBytes/megabyte:.2f} - MB')

    elif sizeInBytes == gigabyte:
        print(f'{sizeInBytes//gigabyte} - GB')

    elif sizeInBytes < terabyte:
        print(f'{sizeInBytes/gigabyte:.2f} - GB')

    elif sizeInBytes == terabyte:
        print(f'{sizeInBytes//terabyte} - TB')

    elif sizeInBytes < petabyte:
        print(f'{sizeInBytes/terabyte:.2f} - TB')


sizeReadable(12089206171)
