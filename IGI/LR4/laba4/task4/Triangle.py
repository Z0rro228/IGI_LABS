import math
from PIL import Image, ImageDraw, ImageFont
from FigureColor import FigureColor
from GeometricFigure import GeometricFigure
from MyMixin import MyMixin


class Triangle(GeometricFigure, MyMixin):
    def __init__(self, a, h, color: FigureColor, text=""):
        self.__a = a
        self.__h = h
        self.__color = color
        self.__b = math.sqrt(math.pow(a, 2) / 4 + math.pow(h, 2))
        self.__text = text
        self.__image = Image.new('RGB', (10, 10), 'white')

    def get_area(self):
        return self.__a * self.__h / 2

    def __str__(self):
        return '{0} shape, color: {1}, a: {2},b: {3}, area: {4}'.format(self.__class__.__name__, self.__color,
                                                                    self.__a,self.__b, self.get_area())

    def draw(self):
        image = Image.new('RGB', (2 * (self.__a + 100), 2 * (self.__h + 100)), 'white')
        draw = ImageDraw.Draw(image)
        font = None
        if __name__ != "__main__":
            font = ImageFont.truetype('OpenSans-Regular.ttf', size=14)

        x1, y1 = self.__a / 2 + 50, 50
        x2, y2 = 50, 50 + self.__h
        x3, y3 = 50 + self.__a, 50 +self.__h

        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=self.__color.color, outline=(0, 0, 0))
        draw.text((7, 7), self.__text, font=font, fill='black')

        image.show()
        self.__image = image

    def save(self):
        self.__image.save('task4.jpg')


if __name__ == "__main__":
    test_color = FigureColor("green")
    square = Triangle(100, 120, test_color, "pupupu")
    square.draw()