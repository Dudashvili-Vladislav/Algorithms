from collections import deque 
#-------------------------------------------------
# Поиск в ширину
#-------------------------------------------------

""" Реализация графов """
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []




def person_is_seller(name): #Функция для критерия поиска
    return name[-1] == "m"
    

def search(name):
  search_queue = deque() #Создаем очередь для проверки с помощью функции duque
  search_queue += graph[name] #Добавляем все графы в очередь для поиска 
  searched = [] #Массив для отслеживания проверенных данных

  while search_queue: #Цикл работает пока очередь не будет пуста
      person = search_queue.popleft() #Из очереди извлекается первый элемент
      if not person in searched: #Продолжается проверка только если в массиве searcehed данные не засвечены
          print(f'Searching {person}') #Смотрим путь до искомого элемента
          if person_is_seller(person): #Проверяем является ли этот объект тем,что мы ищем
              print(person + " " + "is a mango seller ")
              return True
          else:
              search_queue += graph[person] # Данные отмечаются как проверенные 
              searched.append(person) #Данные добавляются в массив searched
  return False
