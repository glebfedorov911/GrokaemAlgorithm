# Реализация графа

from collections import deque


graph = {}

def add_to_graph(key: str, values: list) -> None:
    graph[key] = values

add_to_graph('gleb', ["alina", 'marina', 'egor'])
add_to_graph('alina', ['marina', 'vadim', 'vlad'])
add_to_graph('vlad', ['denis', 'alina'])
add_to_graph('denis', ['egor', 'agaim'])

def check_name_in_graph(name):
    if name in graph:
        return graph[name]
    return []

def is_seller_mango(name):
    return name[-1] == 'm'

def has_mango_seller(name):
    print("-="*10)
    searched_queue = deque()
    searched_queue += check_name_in_graph(name)
    searched = set()

    while searched_queue:
        current_name = searched_queue.popleft()
        if current_name in searched:
            print(f"Уже был просмотрен пользователь с именем {current_name}")
            continue

        if is_seller_mango(current_name):
            print(f"{current_name.capitalize()} продавец манго")
            return True
        else:
            print(f"{current_name.capitalize()} не является продавецом манго")
            searched_queue += check_name_in_graph(current_name)
            searched.add(current_name)
        
    print("Продавец манго не был найден")
    return False

print(has_mango_seller('gleb'))
print(has_mango_seller('alina'))
print(has_mango_seller('vlad'))
print(has_mango_seller('denis'))
print(has_mango_seller('egor'))