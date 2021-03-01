def sizeReadable(sizeInBytes):

    byte = 1
    factor = 1024
    label = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    readable = ''

    for size in range(len(label)):

        if sizeInBytes < 1024**(len(label)-1):

            if sizeInBytes < factor:
                readable = f'{sizeInBytes/(factor/1024):.2f} - {label[size]}'
                return readable
                break

            elif sizeInBytes == factor:
                readable = f'{size // factor} - {label[size+1]}'
                return readable
                break
            else:
                factor *= 1024
        else:
            print("The number is too large")
            break


print(sizeReadable(19992089206171))
