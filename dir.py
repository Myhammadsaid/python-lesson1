# Метод dir() — это встроенная функция Python, которая возвращает список имен (атрибутов и методов), доступных у объекта.

number = 5
print(dir(number))

string = 'Hello'
print(dir(string))

boolean = True
print(dir(boolean))

array = [1,2,3,4,5,6]
print(dir(array))

object = {'1': 4, "2": 12, '3':745}
print(dir(object))