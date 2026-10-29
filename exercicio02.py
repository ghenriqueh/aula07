print(" O usuário escolhe os números")
numeros = []
quantidade =int(input("Quantos números você quer nessa lista? "))
for i in range (quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero) #para acrescentar numeros na lista
print(f"Números digitados: {numeros}")

#mostrar somente os numeros pares
print("\n Somente os numeros pares")
for i in numeros:
    if i %2 == 0:
        print(i)