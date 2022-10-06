import math

a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))

d = (b**2) - (4*a*c)

x1 = (-b+math.sqrt(d))/(2*a)
x2 = (-b-math.sqrt(d))/(2*a)
deter = pow(b, 2)+(4*a*c)
print('Solusinya adalah {0} dan {1}'.format(x1, x2))
print("Determinanya adalah", deter)
