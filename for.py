# for循环遍历数组
magicians = ['leo', 'jack', 'lucy']
for magician in magicians :
	print('Welcome ' + magician.title())
print('haha')

# range()可以生产一些列数字数组,通过for访问
for value in range(1, 6) :
	print(value)

# 让range()成为一个真正的数字列表,使用list()方法
numList = list(range(1,11))
# range()方法可以指定第三参数,为增长步数
evenList = list(range(2, 11, 2))
print(evenList)

# **是幂运算
squareList = []
for value in range(1, 11):
	squareList.append(value**2)

print(squareList)
print(min(squareList))
print(max(squareList))

list1 = list(range(1, 21, 2))
print(list1)

list2 = list(range(3, 31, 3))
for item in list2:
	print(item)

list3 = [value**3 for value in range(1, 11)]
for item3 in list3:
	print(item3)

# 使用[index:lastindex]语法构造切片
list4 = [1,2,3,4,5,6,7,8,9,10]	
cut1 = list4[:4]
cut2 = list4[:]
print(cut1)
print(cut2)
print(a)



