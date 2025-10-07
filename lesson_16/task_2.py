from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:  # лучше сразу сделать float или это не обязательно??
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Square(Shape):

    def __init__(self, side_a: float):
        self.__side_a = side_a

    def area(self) -> float:
        return self.__side_a ** 2

    def perimeter(self) -> float:
        return 4 * self.__side_a


class Circle(Shape):

    def __init__(self, radius: float):
        self.__radius = radius

    def area(self) -> float:
        return 3.14 * (self.__radius ** 2)

    def perimeter(self) -> float:
        return 2 * 3.14 * self.__radius


class Rectangle(Shape):

    def __init__(self, side_a: float, side_b: float):
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self) -> float:
        return self.__side_a * self.__side_b

    def perimeter(self) -> float:
        return 2 * (self.__side_a + self.__side_b)


# создаём наши объекты
shapes = [
    Square(side_a=5.0),
    Circle(radius=3.5),
    Rectangle(side_a=4.0, side_b=8.0),

]

for shape in shapes:
    class_name = shape.__class__.__name__
    calculated_area = round(shape.area(), 2)   # мне подсказали, что надо применять round, если не хочу получить бесконечное число
    calculated_perimeter = round(shape.perimeter(), 2)

    print()
    print(f"Shape: {class_name}")
    print(f" Area: {calculated_area}")
    print(f" Perimeter: {calculated_perimeter}")
    print("-" * 20)