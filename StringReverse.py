# reverse a string
string1 = "abcdef"
print('before reverse: ' + string1)
print('after reverse: ')
# using reversed() with join()
print('using reversed:' + ''.join(reversed(string1)))
# using loop
string2 = ''
index = len(string1) - 1
while index >= 0:
    string2 += string1[index]
    index -= 1
print('using while:' + string2)

# using slice operator
print('using slice operator: ' + string1[::-1])

# using for loop
string2 = ''
for i in range(len(string1) - 1, -1, -1):
    string2 += string1[i]
print('using for loop:' + string2)

print(string2[0:2:1])