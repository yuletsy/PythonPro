# a = 10
# b = 20

# suma = a + b
# multiplicacion = a * b

# print(a, b, suma, multiplicacion)

def sum_multi(numero1, numero2):
    suma = numero1 + numero2
    multiplicacion = numero1 * numero2
    return (suma, multiplicacion)


numero1, numero2 = 10, 20
result = sum_multi(numero1, numero2)
print(result)
print(type(result))