lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

new_lst = []

# пыталась как-то через type(), но не получилось. Гугл подсказал isinstance(). Через type() никак или всё же как-то можно?
for item in lst1:
    if isinstance(item, str):
        new_lst.append(item)

print()
print("Only strings from list:")
print(new_lst)

