n = 4
mat = [[0] * n for i in range(n)]
for row in mat:
    print(' '.join([str(el) for el in row]))

print('-----------')
for i in range(n):
    for j in range(n):
        if i < j:
            mat[i][j] = 0
        elif i > j:
            mat[i][j] = 2
        else:
            mat[i][j] = 1
for row in mat:
    print(' '.join([str(el) for el in row]))



'''
mat = [[1, 0, 2], 
    [0, 2, 1], 
    [2, 1, 0],
    [1, 2, 0]
]
a = 0

for row in mat:
    for el in row:
        a += el
    print(a)
'''




