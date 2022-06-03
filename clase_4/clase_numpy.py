import numpy as np



mi_lista =np.array([1,2,5]) 
# resultado = np.array([2,4,10])
# multip = 2 
# result_prueba = multip* mi_lista
# print(f"{result_prueba=}")
# print(f"{mi_lista+resultado=}")
# print(f"{mi_lista*resultado=}")
# print(f"{np.dot(mi_lista, resultado)=}")
# print(f"{np.cross(mi_lista, resultado)=}")

unitaria2 = 2 * np.eye(3)
resultado = np.matmul(mi_lista, unitaria2)
print(np.eye(3))
