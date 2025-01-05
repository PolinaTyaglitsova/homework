#Дана строка, содержащая предложение
# Напишите программу, которая:
#разделит предложение на отдельные слова
#подсчитает, сколько слов в предложении
sentence = "Python is a powerful and easy-to-learn programmig language"
word = sentence.replace('-', ' ').split(' ')
print('\n'.join(word))
print(len(word))