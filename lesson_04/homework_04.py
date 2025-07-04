adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print("Task 1")
print()

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)
print()

# task 02 ==
""" Замініть .... на пробіл
"""

print("Task 2")
print()

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
print()

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

print("Task 3")
print()

adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
print("!!!")
print(adwentures_of_tom_sawer)
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)
print()
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print("Task 4")
print()

letter_h = adwentures_of_tom_sawer.lower().count("h")
print(f"Буква 'h' встречается в строке {letter_h} раз.")
print()

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

print("Task 5")
print()

separate_words = adwentures_of_tom_sawer.split()
words_count = 0
for word in separate_words:
    if word[0].isupper():
        words_count += 1

print(f"В тексте {words_count} слов начинаются с большой буквы.")
print()

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

print("Task 6")
print()

word_of_interest = "Tom"
word_search = adwentures_of_tom_sawer.find(word_of_interest)
new_start = word_search + len(word_of_interest)
word_search_2 = adwentures_of_tom_sawer.find(word_of_interest, new_start)
print(f"Second time this word appears on {word_search_2} position")
print()

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

print("Task 7")
print()

adwentures_no_end_dot = adwentures_of_tom_sawer.strip(".")
adwentures_of_tom_sawer_sentences = adwentures_no_end_dot.split('.')
print(adwentures_of_tom_sawer_sentences)
print()

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 8")
print()

if len(adwentures_of_tom_sawer_sentences) >= 4:
    sentence_four = adwentures_of_tom_sawer_sentences[4].lower()
    print(sentence_four)
    print()
else:
    print("There are less then 4 sentences in this text")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

print("Task 9")
print()

found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        found = True
        break
if found:
    print("There is a sentence that starts with 'By the time' in this text.")
else:
    print("There is no sentence that starts with 'By the time' in this text.")

print()


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("Task 10")
print()

last_sentence = adwentures_of_tom_sawer_sentences[-1].split()
length = len(last_sentence)
print(f"There are {length} words in the last sentence.")
print()