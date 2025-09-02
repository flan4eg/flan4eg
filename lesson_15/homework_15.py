class Rhombus:
    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a

    def __setattr__(self, name, value):
        if name == 'side_a':
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Value 'side_a' should be an integer and more than 0.")

        elif name == 'corner_a':
            if not isinstance(value, int) or not (0 < value < 180):
                raise ValueError("Value 'corner_a' should be an integer in range from 0 till 180 degrees.")

            object.__setattr__(self, 'corner_b', 180 - value)  # мне подсказали, что лучше напрямую вызывать object.__setattr__ для corner_b

        object.__setattr__(self, name, value)


print()
# Создаём валидный объект класса Rhombus
try:
    rhombus_1 = Rhombus(side_a = 5, corner_a = 60)
    print("Object with valid values:")
    print(f"Side A: {rhombus_1.side_a}")
    print(f"Corner A: {rhombus_1.corner_a}°")
    print(f"Corner B: {rhombus_1.corner_b}°")
    print("-" * 80)
    print()
except ValueError as e:
    print(f"Error: {e}")

# Пытаемся установить невалидное значение для side_a
try:
    rhombus_1.side_a = -10
except ValueError as e:
    print(f"Not valid value for side_a: {e}")
print("-" * 80)
print()

# Пытаемся установить невалидное значение для corner_a
try:
    rhombus_1.corner_a = 200
except ValueError as e:
    print(f"No valid value for corner_a: {e}")
print("-" * 80)
print()

# Устанавливаем новое валидное значение для corner_a
try:
    rhombus_1.corner_a = 110
    print("New valid value for corner_a is set:")
    print(f"New Corner A: {rhombus_1.corner_a}°")
    print(f"New Corner B: {rhombus_1.corner_b}°")
except ValueError as e:
    print(f"Error: {e}")