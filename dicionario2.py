pessoas = []

qtd = int(input("informe a quantidade de pessoas: "))
for i in range(qtd):
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    
    pessoa = {"nome": nome, "idade": idade}
    pessoas.append(pessoa)


print("\nLista de pessoas:")
for pessoa in pessoas:
    print(f"{pessoa['nome'].capitalize()} tem {pessoa['idade']} anos")
