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
# print(type(result))
print(1,2,sum_multi(1,2))
print(3,4,sum_multi(3,4))


nums1 = (1,2,3,4)
nums2 = (1,2,3,4,5,6,7,8,9)

print(f"{len(nums1)=}")
print(f"{len(nums2)=}")

for numero in nums2:
    print(f"{numero=}")


