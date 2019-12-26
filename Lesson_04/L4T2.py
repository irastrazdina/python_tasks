# Не понятно как сделать через инпут, чтобы пользовательно вводил числа через запятую.
# Потому что list.remove() удаляет только первый элемент.
from itertools import combinations
a = [7.89, 7.6, 90, 67, 50]
print(list(a))
data = list(combinations(a, 2))
print(data)
