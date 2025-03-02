

def find_smallest(arr: list) -> int:
    smallest_index = 0
    smallest = arr[smallest_index]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[smallest_index]

    return smallest_index

def selection_sort(arr: list) -> list:
    sorted_array = []
    copy_arr = arr.copy()
    for i in range(len(copy_arr)):
        smallest_index = find_smallest(arr=copy_arr)
        sorted_array.append(copy_arr.pop(smallest_index))

    return sorted_array

array = [5, 3, 8, 10, 16, 25, 14, -1, 0, 1100, 10, 1100, 16, 12, 25]
print(selection_sort(arr=array))