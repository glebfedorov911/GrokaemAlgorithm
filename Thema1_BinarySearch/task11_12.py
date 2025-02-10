from math import log2, ceil


def count_step_with_binary_search(arr: list[any], item: any) -> int:
    '''
    Алгоритм бинарного поиска, считающий количество ходов, чтобы найти данный элемент
    '''
    low = 0
    high = len(arr) - 1
    step = 0
    is_founded = False

    while low <= high:
        step += 1

        mid = (high+low) // 2
        guess = arr[mid]

        if guess == item:
            is_founded = True
            break
        elif item > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        
    return step if is_founded else None

print("128 имен, какое максимальное количество ходов возможно: ", 
    count_step_with_binary_search(range(1, 128), 1))

print("256 имен, какое максимальное количество ходов возможно: ",
    count_step_with_binary_search(range(1, 256), 1))

def count_max_step_by_binary_search(arr: list[any]) -> int:
    '''
    Специализированная функция для расчета максимального количества ходов
    по логике алгоритма бинарный поиск
    '''
    
    return ceil(log2(len(arr)))

print("128 имен, какое максимальное количество ходов возможно: ", 
    count_max_step_by_binary_search(range(1, 128)))

print("256 имен, какое максимальное количество ходов возможно: ",
    count_max_step_by_binary_search(range(1, 256)))

def binary_search(arr: list, item: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None

print("Индекс числа 43:", binary_search(range(1, 128), 43))
print("Индекс числа 31:", binary_search(range(1, 128), 31))
print("Индекс числа 88:", binary_search(range(1, 128), 88))