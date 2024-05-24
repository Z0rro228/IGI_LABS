from Triangle import Triangle
from FigureColor import FigureColor


def task4():
    try:
              a = int(input("Enter a\n"))
              h = int(input("Enter h\n"))
              color = input("Enter color\n")
              text = input("Enter text\n")
              s_color = FigureColor(color)
              triangle = Triangle(a, h, s_color, text)
              triangle.draw()
              triangle.save()
              print(str(triangle))
    except ValueError:
                print('Incorrect input\n')

task4()