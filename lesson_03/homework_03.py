alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where --" said Alice."\n'
                        '"Then it doesn\'t matter which way you go," said the Cat.\n'
                        '"—— so long as I get somewhere," Alice added as an explanation.\n'
                        '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

print(alice_in_wonderland)
print()

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_sur = 436402
azov_sea_sur = 37800
both_seas_sur = black_sea_sur + azov_sea_sur

print("The common surface of Black sea and Azov sea is " + str(both_seas_sur) + " sq.km.")
print()
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

all_stores = 375291
stores_1_2 = 250449
stores_2_3 = 222950
store_3 = all_stores - stores_1_2
store_1 = all_stores - stores_2_3
store_2 = all_stores - (store_3 + store_1)

print("There are " + str(store_1) + " goods in the first store, " + str(store_2) + " goods in the second store, and " + str(store_3) + " goods in the third store.")
print()

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
months = 18
comp_price = monthly_payment * months

print("The price of new computer is " + str(comp_price) + " hrivnas.")
print()

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print("a = " + str(a))
print("b = " + str(b))
print("c = " + str(c))
print("d = " + str(d))
print("e = " + str(e))
print("f = " + str(f))
print()


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza = 274
middle_pizza = 218
juice = 35
cake = 350
watter_bottle = 21
party_price = (big_pizza * 4) + (middle_pizza * 2) + (juice * 4) + cake + (watter_bottle * 3)

print("For this party Iren will need " + str(party_price) + " hr.")
print()


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos = 232
photos_on_page = 8
full_pages = photos // photos_on_page
part_pages = photos % photos_on_page
album_pages = full_pages
if part_pages > 0:
    album_pages = album_pages + 1

print("Ihor will need " + str(album_pages) + " album pages for all his photos.")
print()

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
gas_per_100km = 9
tank_vol = 48
travel_gas = (distance / 100) * 9
distance_per_tank = (tank_vol / gas_per_100km) * 100
full_tanks = distance // distance_per_tank
part_tank = distance % distance_per_tank
gas_stops = full_tanks
if part_tank > 0:
    gas_stops = gas_stops + 1

print("Family needs " + str(travel_gas) + " litres of gas for this travel")
print("They will need to make " + str(int(gas_stops)) + " gas stops.")
