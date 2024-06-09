class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = self.__validate_sides(*sides)
        self.__color = self.__validate_color(*color)
        self.filled = False

    def __validate_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            return [r, g, b]
        else:
            return [0, 0, 0]

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __validate_sides(self, *sides):
        if len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides):
            return list(sides)
        else:
            return [1] * self.sides_count

    def __is_valid_sides(self, *sides):
        return len(sides) == len(self.__sides) and all(isinstance(side, int) and side > 0 for side in sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self._Figure__sides[0] / (2 * 3.141592653589793)

    def get_square(self):
        return 3.141592653589793 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        s = sum(self._Figure__sides) / 2
        area = (s * (s - self._Figure__sides[0]) * (s - self._Figure__sides[1]) * (s - self._Figure__sides[2])) ** 0.5
        return 2 * area / self._Figure__sides[0]

    def get_square(self):
        s = sum(self._Figure__sides) / 2
        return (s * (s - self._Figure__sides[0]) * (s - self._Figure__sides[1]) * (s - self._Figure__sides[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) != 1:
            self._Figure__sides = [1] * 12
        else:
            self._Figure__sides = [sides[0]] * 12

    def get_volume(self):
        return self._Figure__sides[0] ** 3

# ПРМЕРЫ ИЗ ДЗ
circle = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle))

# Проверка объёма (куба):
print(cube1.get_volume())
