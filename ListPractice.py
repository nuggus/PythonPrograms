# creating a list

mylist = ['a', 'b', 'c']
for i in range(len(mylist)):
    print(mylist[i])

# adding elements to list at the end
mylist.append('d')
print('after appending d')
for i in range(len(mylist)):
    print(mylist[i])

# adding at the beginning
print('adding at the begin')
mylist.insert(0, 'Z')
for i in range(len(mylist)):
    print(mylist[i])

# deleting element in list
del mylist[0]
print('after deleting first element')
for i in range(len(mylist)):
    print(mylist[i])

# creating list using for loop

forlist = [x for x in range(0, 10)]
for i in range(len(forlist)):
    print(forlist[i])
forlist.sort()
# creating nested list
nestedlist = [[1, 2], [3], [4, 5],[6,7,8,9]]
print('nested list')
for i in nestedlist:
    print(i[0])
