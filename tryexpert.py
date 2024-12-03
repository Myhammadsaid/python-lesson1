# try:
# 	x = int(input('Ведите число: '))
# 	x += 5
# 	print(x)
# except ValueError:
# 	print('Введите лучше число!')

# x = 0
# while x == 0:
# 	try:
# 		x = int(input('Ведите число: '))
# 		x += 5
# 		print(x)
# 	except ValueError:
# 		print('Введите лучше число!')

sum = int(input('Введите число: '))
try:
	x = 5 / sum
	x = int(input('Введите число: '))
except ZeroDivisionError:
	print('Деление на ноль!')
except ValueError:
	print('Вы ввели что-то не так')
else:
	print('Else')
finally:
	print('Код Закончан!')