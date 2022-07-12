def class_homework():
    b = bytearray([10,20,60,40,50])
    print(f'Before: {b}')
    b[2] = 50
    print(f'Later: {b}')
    print(b[2])
    print()
    #print(str(int(b[2], 16)))
    


class_homework()

import os
def class_file_example():
    path = 'C:/Users/Vi Tiet/Desktop/Ryerson/PythonProblems'
    
    for file in os.listdir(path):
        if os.path.isfile(file):
            # fn, fe = os.path.splitext(file)
            # if fe == '':
            #     fe = 'undefined'
            # print(f'file name: {fn}')
            # print(f'file extension: {fe}')
            print(os.path.abspath(file))
    
    # for file in os.scandir(path):
    #     file_size = round((file.stat().st_size / 1024))
    #     print(f'file name: {file.name}')
    #     print(f'     size: {file_size} MB')


class_file_example()