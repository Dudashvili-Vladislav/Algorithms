""" Реализация графов """
graph = {}
graph["start"] = {} 
graph["start"] ["a"] = 5
graph["start"] ["e"] = 2

graph["a"] = {}
graph["a"] ["b"] = 4
graph["a"] ["d"] = 2
graph["e"] = {}
graph["e"] ["a"] = 8
graph["e"] ["d"] = 7
graph["b"] = {}
graph["b"] ["fin"] = 3
graph["b"] ["d"] = 6
graph["d"] = {}
graph["d"] ["fin"] = 1
graph["fin"] = {}



infinity = float("inf") #Бесконечность
costs = {}
costs["start"] = 0



parents = {}
parents["a"] = "start"
parents["e"] = "start"
parents["in"] = None



#-------------------------------------------------
# Функция для нахождения минимальной стоимости узла
#-------------------------------------------------

def find_lowest_cost_node(costs):
    lowest_cost = float("inf") #Бесконечность 
    lowest_cost_node = None #Вернет None если ничего не передать
    for node in costs: #Перебираем все узлы
        cost = costs[node]  #Получаем стоимость соседей от узла 
        if cost < lowest_cost and node not in processed: #Если стоимость полученного узла меньше стоимости уже найденного узла и узел с новой стоимостью еще не проверялся 
            lowest_cost = cost #Изменяется стоимость узла на новую
            lowest_cost_node = node #Изменяется узел на новый
    return lowest_cost_node #Возращаем узел с наименьшей стоимостью



#Заполняем все не посещённые ещё узлы бесконечной стоимостью
for k in graph:
    if k not in costs:
        costs[k] = infinity



processed = [] #Массив для обработанных данных 
node = find_lowest_cost_node(costs) #Нахождение узла с наименьшей стоимостью среди необработанных
while node is not None: #Если обработанны все узлы - цикл завершен
    cost = costs[node] #Получаем стоимость соседей от узла которого нашли ранее (узел с наименьшей стоимостью)
    neighbors = graph[node] #Получаем соседей от узла которого нашли ранее (узел с наименьшей стоимостью)
    for n in neighbors.keys(): #Перебираем всех соседей текущего узла
        new_cost = cost + neighbors[n] #Вычисляем сколько времени потребуется для достижения данного узла через самый дешевый путь
        if costs[n] > new_cost: #Сравниваем стоимость дохождения до данного узла 
            costs[n] = new_cost #Если новый путь дешевле мы обновляем стоитьсть дохождения до данного узла
            parents[n] = node #Так как мы нашли новый путь, соответственно у найденного нами  узла мы обновим родителя
    processed.append(node) #Узел отмечается как отработанный и помещается в отдельный массив 
    node = find_lowest_cost_node(costs) #Ищем следующий узел для обработки



print(costs)
