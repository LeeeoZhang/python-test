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