"""Task 4"""

from countOfUppersAndLowers import countOfLowers
from countOfUppersAndLowers import countOfUppers
from removeStartWithA import removeStartWithA
from findFirstZWord import findFirstZWord

#Задание 4. a)Определить количество строчных и заглавных букв в строке;
#б) найти первое слово, содержащее букву 'z' и его номер;
#в) вывести строку, исключив из нее слова, начинающиеся с 'A'.")
def task4():
    print("Ввведите строку:")
    text = input()
    print(f"Количество строчных букв:{countOfLowers(text)}")
    print(f"Количество заглавных букв:{countOfUppers(text)}")
    pos, word = findFirstZWord(text)
    if(pos == -1):
        print("Слово, содержащее z не найдено")
    else:
        print(f"Позиция первого слова, содержащее v: {pos}, слово:{word}")
    print("Текст после удаления слов, начинающиюхся с буквой a:")
    print(removeStartWithA(text))

task4()