import os


def recursion_print_filenames(start_dir, step=0):
    for file in os.listdir(start_dir):
        fullpath = os.path.join(start_dir, file)
        if os.path.isfile(fullpath):
            print("Найден файл по пути:", fullpath, "Понадобилось обойти директорий: ", step)
        else:
            recursion_print_filenames(fullpath, step+1)

recursion_print_filenames("Thema7_Tree/test_catalog")