names = ['Leo', 'Jack', 'Lily']

# 使用索引访问数组成员,索引从0开始
print(names[0])
print(names[1])
print(names[2])

print('Hello ' + names[0])
print('Hello ' + names[1])
print('Hello ' + names[2])

# append()向数组末尾添加新元素
names.append('Mark')
print(names)

# insert()向数组指定位置插入新元素
names.insert(0, 'Jason')
print(names)

# 使用del语句删除一个指定位置的数组成员
del names[0]
print(names)

# pop()方法移除数组末尾成员,并返回它(类似于移除栈顶元素)
popName = names.pop()
print(popName)
print(names)

# pop()方法还接受还接受参数,指定弹出某个索引的数组成员
witchPop = names.pop(1)
print(witchPop)
print(names)

# remove()方法可以删除指定value的数组成员
# 注意的是,remove()只删除第一个指定的值,假如数组中有多个相同的值,需要循环遍历判断是否都删除
names.remove('Lily')
print(names)


# 一个无聊的数组练习 ..
inviteList = ['Leo', 'Mike', 'Lucy']
print('Welcome to my party, ' + inviteList[0] + '!')
print('Welcome to my party, ' + inviteList[1] + '!')
print('Welcome to my party, ' + inviteList[2] + '!')
print("Mike can't join in us!")
inviteList[1] = 'John'
print('Welcome to my party, ' + inviteList[0] + '!')
print('Welcome to my party, ' + inviteList[1] + '!')
print('Welcome to my party, ' + inviteList[2] + '!')
print('I find a bigger table!')
inviteList.insert(0, 'Jason')
inviteList.insert(2, 'Vivi')
inviteList.append('Lora')
print(inviteList)
inviteList.pop()
inviteList.pop()
inviteList.pop()
inviteList.pop()
print(inviteList)
del inviteList[0]
del inviteList[0]
print(inviteList)


# sort()方法可以对数组进行永久排序
testArray1 = [1,3,4,2,5,8,9]
print(testArray1)
# 默认sort()方法从小到大排列成员
testArray1.sort()
print(testArray1)
# 传递参数 reverse=True ,从大到小排列
testArray1.sort(reverse=True)
print(testArray1)

# sorted()方法可以对数组进行临时排序,不会改变原数组的排序,具体用法与sort()一样
testArray2 = [1,2,3,4,4,8,1]
print(testArray2)
print(sorted(testArray2))
print(sorted(testArray2, reverse=True))
print(testArray2)

# reverse()方法可以翻转数组排列
# array.reverse()
# len()函数可以获取数组长度
# len(array)