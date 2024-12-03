class Cat:
	name = None
	age = None
	isHappy = None

	def __init__(self, name = None, age = None, isHappy = None):
		self.set_data(name, age, isHappy)
		self.get_data

	def set_data(self, name = None, age = None, isHappy = None):
		self.name = name
		self.age = age
		self.isHappy = isHappy

	def get_data(self):
		print(self.name, 'age:', self.age, '.\nHappy', self.isHappy)

cat1 = Cat('Адидас', 3, True)
cat2 = Cat('Нике', 2, False)

print(cat1.get_data())
print(cat2.get_data())