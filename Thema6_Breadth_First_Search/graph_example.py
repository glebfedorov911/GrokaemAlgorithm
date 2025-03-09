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
    search_queue = deque()
    search_queue += check_name_in_graph(name)
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            print(f"{person} уже проверена")
            continue

        if is_seller_mango(person):
            print(f"Продавец манго - это {person}")
            return True
        else:
            search_queue += check_name_in_graph(person)
            searched.add(person)
    print("Продавец не найден")
    return False

print(has_mango_seller('gleb'))
print(has_mango_seller('alina'))
print(has_mango_seller('vlad'))
print(has_mango_seller('denis'))
print(has_mango_seller('egor'))