print('Scientific Computing with Python - FreeCodeCamp')
print('Project: Polygon Area Calculator')

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, num):
        self.width = num

    def set_height(self, num):
        self.height = num

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** (1/2)

    def get_picture(self):
        new = []
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            while len(new) < self.height:
                new.append('*' * self.width)
            new.append('')
            return '\n'.join(new)

    def get_amount_inside(self, another_shape):
        return int(self.get_area() / another_shape.get_area())

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width, height=width)

    def set_side(self, num):
        self.width = num
        self.height = num

    def __str__(self):
        return f'Square(side={self.width})'
