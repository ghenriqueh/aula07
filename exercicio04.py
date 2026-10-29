print(" --- Lista de números --- ")
numeros=[]
quantidade = int(input("Quantos números quer inserir na lista? "))
for i in range (quantidade):
    numero = int(input(f"{i+1}º número: "))
    numeros.append(numero)

print(f"Numeros da lista: {numeros}")

for i in numeros:
    if i %2 == 1:
        print(f"Números pares: {i}")
    else:
        print(f"Números ímpares: {i}")

numeros.sort()
print(f"Números em ordem crescente: {numeros}")
numeros.sort(reverse=True)
print(f"Números em ordem a decrescente: {numeros}")
numeros.sort(reverse=False)

numero_remove=int(input("Qual número quer remover?"))
numeros.remove(numero_remove)
print(f"Nova lista:{numeros}")
