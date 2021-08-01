import time

#baza tabelaryczna
names = []
items = []

#dodaje rekord do bazy tabelarycznej
def add_to_standard_database(name, item):
    names.append(name)
    items.append(item)

def print_standard_database():
    print('standard database:')
    i = 0
    while i < len(names):
        print(str(names[i]) + ', ' + str(items[i]) + '\n')
        i = i + 1

def select_count_standard(item):
    return items.count(item)

#baza grafowa
graph = {}

#dodaje rekord do bazy grafowej, jęsli wierzcholek nie istnial tworzy go
def add_to_graph_database(name, item):
    if name in graph:
        graph[name].append(item)
    else:
        start_array = []
        start_array.append(item)
        graph[name] = start_array

def print_graph_database():
    print('graph database:')
    print(graph)

def select_count_graph(item):
    counter = 0
    for vertex in graph:
        temp_array = graph[vertex]
        counter += temp_array.count(item)
    return counter




if __name__ == '__main__':
    maximum = 10000000

    for i in range(0, maximum):
        add_to_standard_database('mati', 'pizza')
        add_to_standard_database('mati', 'limoncello')
        add_to_standard_database('klaudia', 'limoncello')
        add_to_standard_database('robert', 'pasta')
    start_time = time.time()
    print(select_count_standard('limoncello'))
    print("--- %s seconds ---" % (time.time() - start_time))

    for i in range(0, maximum):
        add_to_graph_database('mati', 'pizza')
        add_to_graph_database('mati', 'limoncello')
        add_to_graph_database('klaudia', 'limoncella')
        add_to_graph_database('robert', 'pasta')
    start_time = time.time()
    print(select_count_graph('limoncello'))
    print("--- %s seconds ---" % (time.time() - start_time))