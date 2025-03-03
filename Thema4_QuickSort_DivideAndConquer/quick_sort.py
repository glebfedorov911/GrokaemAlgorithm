import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr)-1)
    pivot = arr[pivot_index]
    less = [arr[x] for x in range(0, len(arr)) if x != pivot_index and arr[x] <= pivot]
    greather = [arr[x] for x in range(0, len(arr)) if x != pivot_index and arr[x] > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greather)

arr = [-5838, -1, 0, 1, 1, 1, 2, 3, 8585, 8585, 12939, 14983295]
print(quick_sort(arr))
print(quick_sort([]))
print(quick_sort([3, 1]))
print(quick_sort([3]))
