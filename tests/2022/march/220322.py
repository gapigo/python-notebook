# Testing getting only not alphabetic characters
# in an array of strings

li = ['a23', '-a52', ' 4']
for i in range(len(li)):
    old = li[i]
    li[i] = ''
    for char in old:
        li[i] += char if not char.isalpha() else ''
    if li[i] == '':
        li[i] = 1
print(li)
#
# print(li)

# li = ['z', 'a', 'g']
# # li.sort()
# a = ['a' for i in range(len(li)) if (i + 1 != len(li))]
# print(a)
# # print(a)

# x = [1, 2, 3, 4, 5]
# y = [a for a in x]
# print(y)
