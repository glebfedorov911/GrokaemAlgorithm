'''
Найти первое вхождение элемента
Дан отсортированный массив с возможными повторениями. Найдите индекс первого вхождения числа x.
'''

def binary_search_all_elem(arr: list, item: int) -> int:
    low = 0
    high = len(arr) - 1

    while all([i == item for i in arr[low:high+1]]) or arr[low:high+1] != []:
        mid = (low + high) // 2
        guess = arr[mid]    

        if all(i == item for i in arr[low:high+1]):
            return low
        elif guess >= item:
            high = mid 
        else:
            low = mid + 1


    return -1


print(binary_search_all_elem(arr=[1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8], item=5)) # 4
print(binary_search_all_elem(arr=[2, 3, 4, 5, 6, 7], item=3)) # 1
print(binary_search_all_elem(arr=[2, 3, 4, 5, 6, 7], item=5)) # 3
print(binary_search_all_elem(arr=[2, 3, 4, 5, 6, 7], item=7)) # 5
print(binary_search_all_elem(arr=[2, 2, 3, 4, 5, 6, 7], item=2)) # 0
print(binary_search_all_elem(arr=[2, 3, 3, 4, 5, 6, 7], item=3)) # 1
print(binary_search_all_elem(arr=[2, 3, 4, 5, 6, 6, 6, 7], item=6)) # 4
print(binary_search_all_elem(arr=[2, 3, 4, 5, 6, 6, 6, 7], item=16)) # -1