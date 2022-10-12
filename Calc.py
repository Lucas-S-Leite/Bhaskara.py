import math

a = float (input( ' Insira A '))
b = float (input( ' Insira B '))
c = float (input( ' Insira C '))

d = (b * b)-(4 * a * c)

print (f'Delta={d}')

if d>0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f'X1 ={x1:.2f} X2={x2:.2f}')

else:
    print('Solução Inexistente')