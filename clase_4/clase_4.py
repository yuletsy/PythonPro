mi_lista = [1,2,5,6,9, 10, 15, 0,11,12, 22, 32]
result = [2,4,10,12,18, 2,14,12,9, 10] 
# mi_lista2 = []
def function_multi(element):
    return element*2

# print(mi_lista[1])


result_prueba = []
multip = 2 
    #for numero in mi_lista:
    # result_prueba.append(element*multi)
# result_prueba= list(map(lambda x: x * 2, mi_lista))
result_prueba = [element*multip for element in mi_lista]
    # result = 2 * mi_lista
print(f"{result_prueba=}")
#print(f"{result=}") 


# slice notation
print(f"{mi_lista=}")
print(f"{mi_lista[1]=}")
print(f"{mi_lista[1:5]=}")
print(f"{mi_lista[1:5:2]=}")
print(f"{mi_lista[7:1:-2]=}")
print(f"{mi_lista[1::2]=}")
print(f"{mi_lista[:8:2]=}")

print(f"{mi_lista[:len(mi_lista):-1]=}")
print(f"{mi_lista[::-1]=}") # imprimir una lista al reves
print(f"{mi_lista=}")

 
palindromo = "anita lava la tina"
palindromo_sin_espacios = palindromo.replace(" ","")
print(f"{palindromo=}")
print(f"{palindromo_sin_espacios=}")

print(palindromo == palindromo[::-1])
print(palindromo_sin_espacios == palindromo_sin_espacios[::-1])


pal_lista = list(palindromo)
pal_lista.reverse()
print(pal_lista)