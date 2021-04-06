#-------------------------------------------------
# Быстрая сортировка Хоара через рекурсию
#-------------------------------------------------
import random


def quick_sort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a)-1)]  # случайное пороговое значение (для разделения на малые и большие)
        low = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        hi = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(hi)
        
    return a



#-------------------------------------------------
# Быстрая сортировка с определенным выбором опорного элемента из книги Грокаем алгоритмы
#-------------------------------------------------
def quicksort(array):
    if len(array)< 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        gretter = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(gretter)

