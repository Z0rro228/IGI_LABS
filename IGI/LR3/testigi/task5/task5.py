"""Task 5."""

from findPosMult import findPosMult
from findCustomSum import findCustomSum

#Задание 5. Найти произведение положительных элементов с
#и сумму элементов, расположенных до минимального по модулю элемента
def task5():
    print("Вводите вещественные элементы через пробел (окончание ввода <enter>):")
    text = input()
    lst = []
    for p in text.split(' '):
        try:
            el = float(p)
            lst.append(el)
        except ValueError as er:
            print("Wrong value!!! Try again...")
            return
    print("Вы ввели следующий список:")
    print(lst)
    print("Произведение положительных элементов")
    print(findPosMult(lst))
    print("Сумма элементов, расположенных до минимального по модулю элемента:")
    print(findCustomSum(lst))

task5()