# file = open('data/text.txt', 'w')
# file = open('data/text.txt', 'a')

# file.write('Hello World!\n')
# file.write('My name is John')

# file.close()

# data = input('Ведите текст: ')
# file = open('data/text.txt', 'a')

# file.write(data + '\n')

# file.close()

file = open('data/text.txt', 'r')

print(file.read())
# print(file.read(4))

for line in file:
	print(line)
	print(line, end='')

file.close()