"""
4.8 Создание таблицы умножения
Пример [2, 3, 7, 8, 10] каждый элемент умножаем на каждый элемент
"""


def multiply_table(arr):
    for i in arr:
        for j in arr:
            print(i*j, end='\t')
        print('\n')

def recursion_multiply_table(arr, i=0, j=0):
    if arr == []:
        return
     
    if j == len(arr):
        print('\n')
        return recursion_multiply_table(arr, i+1, 0)
    if i == len(arr):
        return

    print(arr[i] * arr[j], end="\t")
    return recursion_multiply_table(arr, i, j+1)    

n = [2, 3, 7, 8, 10]
multiply_table(n)
print("-="*10)
recursion_multiply_table(n)