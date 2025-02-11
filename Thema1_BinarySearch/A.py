'''
Найти элемент в отсортированном массиве
Дан отсортированный массив и число x. Определите, есть ли x в массиве.
'''


def binary_search(arr: list, item: int) -> bool:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2
        guess = arr[mid]

        if guess == item:
            return True
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return False
