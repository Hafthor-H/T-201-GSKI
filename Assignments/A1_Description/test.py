from dalist import DAList

D = DAList(4)

D.append(1)
D.append(2)
D.append(5)
D.insert(10)
if str(D) == '[1, 2, 5]':
    print('Append works: ', D)

else:
    raise ValueError('Error in append')

D.insert(2, 3)

if str(D) == '[1, 2, 3, 5]':
    print('Insert works: ', D)

else:
    raise ValueError('Error in Insert')

D.insert(3, 4)

if str(D) == '[1, 2, 3, 4, 5]':
    print('Double works: ', D)

else:
    raise ValueError('Error in Double')

D.reverse()

if str(D) == '[5, 4, 3, 2, 1]':
    print('Reverse works: ', D)

else:
    raise ValueError('Error in Reverse')

D.remove(3)

if str(D) == '[5, 4, 2, 1]':
    print('Remove works: ', D)

else:
    raise ValueError('Error in Remove')

k = D.pop(2)

if str(D) == '[5, 4, 1]':
    print('Pop works: ', D)
    print(k)

else:
    raise ValueError('Error in Pop')

C = ['a', 'b', 'c']

D.extend(C)
if str(D) == '[5, 4, 1, a, b, c]':
    print('Extend works: ', D)

else:
    raise ValueError('Error in Extend')

A = D.copy()

if str(D) == str(A):
    print('Copy works: ', D, A)

else:
    raise ValueError('Error in Copy')

f = D.index('a')

if f == 3:
    print('Index works: ', D)
    print(f)

else:
    raise ValueError('Error in Index')

k = D.count('b')
if k == 1:
    print('Count works: ', D)
    print('b: ', k)

else:
    raise ValueError('Error in Count')

A.clear()

if str(A) == "[]":
    print('Clear works: ', A)

else:
    raise ValueError('Error in Clear')

for k in D:
    print(k)

del D[2]

if str(D) == '[5, 4, a, b, c]':
    print('Del works: ', D)

else:
    raise ValueError('Error in Del')

D[2] = 3
D[3] = 2
D[4] = 1

if str(D) == '[5, 4, 3, 2, 1]':
    print('Set_item works: ', D)

else:
    raise ValueError('Error in Set_item')

if D[1] == 4:
    print('Get_item works: ', D)

else:
    raise ValueError('Error in get_item')

if len(D) == 5:
    print('len works: ', D)
else:
    raise ValueError('Error in len')
D[-4] = "bruh"
print(D)