l = [4, 5, 6, 7, 8, 9, 3, 2, 1, 23, 123]

print(l.__getitem__(2))

print(l.__len__())

print(range(len(l) -1, 0, -1))


for i in range(len(l) -1, 0, -1):
    for j in range(i):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1], l[j]

print(l)