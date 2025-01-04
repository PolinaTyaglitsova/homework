#Дана строка, содержащая несколько слов. Найдите все уникальные слова в строке и выведите их в алфавитном порядке
# Вывод: ['apple', 'banana', 'kiwi', 'orange']

sentence = "apple banana apple orange banana kiwi"
sentence_set= set(sentence.split()) # set-удалил повтоярющиеся элементы
new_sentence = sorted(sentence_set)
print(new_sentence)