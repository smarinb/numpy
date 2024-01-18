import numpy as np 

lista = [1,2,3,4,5,6,7,8,9]

arr = np.array(lista)


print(type(arr))

matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)
print(matriz)


print(arr[0] + arr[5]) # primera posición 0 


print(matriz[0]) # [1,2,3]
print(matriz[0][1]) # 2

print(arr[0:3]) #1,2,3 
print(arr[1:5]) #2,3,4,5

print(arr[2:]) #3,4,5,6,7,8,9

print(arr[::3]) #todo de 3 en 3

print(arr[-1]) #Empezando por el final 9
print(arr[-3]) #7


print(matriz[1:])  # [4,5,6],[7,8,9]
print(matriz[1:,0:2]) #[4,5],[7,8]
print(matriz[1,0:2]) #[4,5]