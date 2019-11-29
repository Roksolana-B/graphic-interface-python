u = input("Завдання\Порахувати кількість букв в тексті - 1\посортувати букви в алфавітному порядку - 2\Ваш вибір: ")

def tx(s):
	d = {}
	for i in s:
		if i.isalpha():
			d[i] = d.get(i,0) + 1
	for i in sorted(d):
		print(i + ":" + str(d[i]))

while u == "1":
	print("Ви обрали 1 варіант")
	txx = input("Введіть текст: ")
	tx(txx)
	print("Закінчено")
	print("Для продовження натисніть - A\Завершення програми - B")
	u2 = input("Ваш вибір: ")
	if u2 == "A":
		u == "1"
	elif u2 == "2":
		u == "2"
	elif u2 == "B":
		break
	else:
		print("Невірно")
while u == "2":
	print("Ви обрали 2 варіант")
	ttx = input("Введіть текст: ").replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('&','').replace('*', '').replace('(', '').replace(')', '')
	ttx =ttx
	ttx = sorted(ttx)
	print(ttx)
	print("")
	print("Для продовження натисніть - A\Завершення програми - B")
	u3 = input("Ваш вибір: ")
	if u3 == "A":
		u == "1"
	if u3 == "B":
		break
	else:
		print("Невірно")