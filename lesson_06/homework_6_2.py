while True:
    h_word = input("Input word with 'h' letter: ")
    lower_h = h_word.lower()
    if 'h' in lower_h:
        print("Yes, this word has letter 'h'")
        break
    else:
        print("There is no 'h' letter in this word - input another word!")
        print()
