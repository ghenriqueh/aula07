print("Entre com os nomes e coloque em ordem alfabética crescente")
nomes =[]
quantidade = int(input("Quantos nomes quer inserir na lista? "))
for i in range (quantidade):
    nome = input(f"{i+1}º nome: ")
    nomes.append(nome)
nomes.sort()
print(f"Nomes em ordem alfabética: {nomes}")
nomes.sort(reverse=True)
print(f"Nomes em ordem alfabética decrescente: {nomes}")

nome_remove=input("Qual nome quer remover?")
nomes.remove(nome_remove)
print(f"Nova lista:{nomes}")
