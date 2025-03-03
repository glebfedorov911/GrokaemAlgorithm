"""
4.1 Просуммировать все числа массива рекурсивно
"""

def sum_(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_(arr[1:])

print("Подсчет суммы элементов")
print(sum_([1, 2, 3, 4, 5, 20]))
print(sum_([]))


"""
4.2 Подсчет количества элементов массива
"""

def sum_count(arr):
    if arr == []:
        return 0
    return 1 + sum_count(arr[1:])

print("Подсчет длины")
print(sum_count([1, 2, 3, 4, 5]))
print(sum_count([]))
print(sum_count([1] * 10))


"""
Рекурсивная функция для нахождения наибольшего числа массива
"""

def max_elem(arr):
    if arr == []:
        return 0
    return arr[0] if arr[0] > max_elem(arr[1:]) else max_elem(arr[1:])

print("Максимальный элемент")
print(max_elem([1, 2, 3, 4]))
print(max_elem([12, 75, 1, 94, 8581, 0, -1412]))
print(max_elem([]))
print(max_elem([1, 2]))
print(max_elem([5, 2]))


"""
Рекурсивный бинарный поиск
"""

def standard_binary_search(arr, target):
    print("Отсортированный массив:", arr)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return None

print("Бинарный поиск. Стандарт.")
print(standard_binary_search(
    sorted([1, 3, 8585, 12939, 14983295, 1, 0, -1, -5838, 1, 2]),
    12939    
))

def recursion_binary_search(arr, target, left, right):
    if left > right:
        return None

    mid = (left+right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursion_binary_search(arr, target, mid+1, right)
    else:
        return recursion_binary_search(arr, target, left, mid-1)

print("Бинарный поиск. Рекурсия.")
arr = [-5838, -1, 0, 1, 1, 1, 2, 3, 8585, 12939, 14983295]
print(recursion_binary_search(arr, 3, 0, len(arr) - 1))
print(recursion_binary_search(arr, 4, 0, len(arr) - 1))
print(recursion_binary_search(arr, 12939, 0, len(arr) - 1))