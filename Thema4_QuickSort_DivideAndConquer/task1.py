"""
Задача: Определить размер самого большого квадратного надела участка размером size_x*size_y
Стратегия разделяй и властвуй, пока не будет кратного max_size % min_size == 0
"""
def divide_field(size_x, size_y):
    max_size = max(size_x, size_y)
    min_size = size_x + size_y - max_size

    if max_size % min_size == 0:
        return (min_size, min_size)

    return divide_field(min_size, max_size - (max_size // min_size) * min_size)

print(divide_field(1680, 640))