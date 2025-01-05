#Дана строка, содержащая текст с email-адресами. Напишите программу, которая извлечет все email-адреса из строки, сохранит их в список и выведет результат
text = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru"
pochta = []
symb = "@"
text = text.split(" ")
for i in text:
  #  print(i)
    if symb in i:
        pochta.append(i)
print(*pochta)