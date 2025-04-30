from collections import deque
import os


def bfs(start_dir):
    dirs = deque()
    dirs.append([start_dir, 0])

    while dirs:
        dir, step = dirs.popleft()
        for file in sorted(os.listdir(dir)):
            fullpath = os.path.join(dir, file)
            if os.path.isfile(fullpath):
                print(f"Найден файл с названием {file} по пути {fullpath}. Понадобилось пройти директорий: {step}")
            else:
                dirs.append([fullpath, step+1])

bfs("Thema7_Tree/test_catalog")