list = [1, 2, 3]  # list with square brakets

print(list.__len__())
print(list)

list = ['string', 32.2, 12, '0']  # different types can be in the list
print(list)

print(len(list))  # len function is a length

my_list = ['one', 'two', 'three', 4, 5]

print(my_list[0])

print(my_list[1:])

print(my_list[:3])

a = 'hello' + 'world'

print(my_list + ['new item'])  # concatinate two lists

my_list = my_list + ['permanent add']

print(my_list)

print(my_list * 2)  # you can multiply your list

l = [1, 2, 3]

l.append('append me!')  # appending

print(l)
print(l.pop(2))

x = print(l.pop(1))  # after popping the element is out of the list

print(x)

##reverse method for list

new_list = ['a', 'e', 'x', 'b', 'c']
print(new_list)
new_list.reverse()
print(new_list)  # and we could not reverse in print calling (print(new_list.reverse()) - it does not work)

new_list.sort()  # sort list by alphabet
print(new_list)

# create matrix and print it
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]

matrix = [l_1, l_2, l_3]

print('matrix is = ' + matrix.__str__())

# print the element of the matrix
print(matrix[2][0])

# get first column of matrix and print it
first_col = [row[0] for row in matrix]
print('first_col in that matrix is = ' + first_col.__str__())


print()
