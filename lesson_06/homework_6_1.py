three_men = input("Input your text: ")
unic_symbols = set(three_men)

print()
print('Unic symbols:')
print(unic_symbols)
print()

amount_unic_symbols = len(unic_symbols)
if amount_unic_symbols >= 10:
    print(True)
else:
    print(False)

