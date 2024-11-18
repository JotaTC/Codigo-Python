from ATV_Gerenciamento_de_restauranteC import ItemMenu, PratoPrincipal, Sobremesa, Restaurante
motorizados = []
verificar = int(input("Você quer adicionar uma comida?\n1- Sim\n2- Não\n"))
restaurante = Restaurante()

while verificar == 1:
    nome = input("Digite o nome da Comida: ")
    preco = float(input("Digite o preço da comida: "))

    print("1- Adicionar Prato Principal\n2- Adicionar Sobremesa")
    verificar2 = int(input("Resposta: "))

    if verificar2 == 1:
        descricao = input("Digite a descrição do prato principal: ")
        itens = PratoPrincipal(nome, preco, descricao)
    elif verificar2 == 2:
        tipo = input("Digite o tipo de sobremesa: ")
        itens = Sobremesa(nome, preco, tipo)
    else:
        print("Opção inválida. Tente novamente.")
        continue

    restaurante.adicionar_item_menu(itens)
    verificar = int(input("Você quer adicionar outra comida?\n1- Sim\n2- Não\n"))

restaurante.listar()