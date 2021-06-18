lista = []

while True:
	print("""
1 - Inserir um nome na lista
2 - Excluir um nome
3 - Imprimir os elementos da lista
4 - Sair
""")

	opcao = int(input("Insira uma opção: "))
	
	if opcao == 1:
		nome = input("Insira um nome: ")
		lista.append(nome)
	elif opcao == 2:
		nome = input("Insira um nome para remoção: ")
		lista.remove(nome)
	elif opcao == 3:
		print(lista)
	else:
		break

