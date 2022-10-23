# необходимо 3 хеш таблицы: graph, costs, parents

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# переменная бесконечности, создание таблицы costs
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Создание таблицы родителей 
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# список обработанных узлов
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs) #Найти узел с наименьшей стоимостью среди необработанных данных
while node is not None: # Если обработаны все узлы, цикл завершен
    cost = costs[node] 
    neighbors = graph[node]
    for n in neighbors.keys(): # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n] 
        if costs[n] > new_cost: # Если есть путь короче 
            costs[n] = new_cost # обновить цену узла
            parents[n] = node # Этот узел становится новым родителем для соседа
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(graph)
print(parents)
print(costs)