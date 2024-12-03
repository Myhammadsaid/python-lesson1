# nums = [1,2,3,True,4.5,'hello',[6,7]]
# nums[3] = 4
# print(nums)

# print(nums[-1][1])

numbers = [1,2,3]
# numbers.append(4)
# numbers.insert(1,True)
# a = [7,6,5]
# numbers.extend(a)
# numbers.sort()
# numbers.reverse()
# numbers.pop()
# numbers.remove(3)
print(numbers)

# print(numbers.count(3))
# print(len(numbers))

# nums = [3,4,5, '50', False]
# for el in nums:
# 	el *= 2
# 	print(el)

n = int(input('Enter length: '))
user_list = []
i = 0
while i < n:
	string = 'Enter element #' + str(i + 1) + ': '
	user_list.append(input(string))
	i += 1

print(user_list)