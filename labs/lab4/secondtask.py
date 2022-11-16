import numpy as np
#номер 6
print ('Введіть розміри матриці:')
n = int(input('n>>'))
m = int(input('m>>'))
A = np.random.randint(-99, 99, (int(n),int(m)))
print('Початкова матриця\n',A)
print('Негативні елементи стовпців:')
for i in range (len(A)):
    count = 0
    print (f'\n{i+1} стовпець: ')
    for j in A[:,i]:
        if j < 0:
            print (j, end = ', ')
            count+=1
    print(f'\nК-ть негативних елементів {i+1} стовпця:', count)
print('\nНегативні елементи рядків:')
for i in range (len(A)):
    count = 0
    print (f'\n{i+1} рядок: ')
    for j in A[i]:
        if j < 0:
            print (j, end = ', ')
            count+=1
    print(f'\nК-ть негативних елементів {i+1} рядка:', count)
