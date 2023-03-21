#PROGRAMA PARA VERIFICAR CUAL ES EL NUMERO MAS GRANDE
n1 = int(input("Ingrese primero numero: "))
n2 = int(input("Ingrese segundo numero: "))

if n1 > n2:
    print(f'El numero {n1} es mayor a {n2}')
elif n2 > n1:
    print(f'El numero {n2} es mayor a {n1}')
else:
    print("Los dos numeros son iguales")