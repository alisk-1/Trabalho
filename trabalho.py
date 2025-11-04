usuarios = [['admin', '123', 'ADM'], ['cliente', '123', 'CLIENTE'],['alisk','1234','ADM' ],['joao','4021','CLIENTE']]
produtos = [['Shampoo', 35.00],['Ração golden p/ Cães', 149.50],['anti-pulgas', 66.50],['Coleira anti-pulga', 175.00],['Tapete', 70.00]]
quantidades = [10 , 15 , 15 , 50 , 13]
servicos = [['Toza', 50.00], ['Banho', 35.99], ['Adestramento', 100.00], ['Veterinario', 153.45]]
compras = []
agendamentos = [['toza', '10 hrs'], ['Banho', '12 hrs'], ['toza', '14 hrs'],['Toza','14.30']]


print('               Olá, amigo(a)')
print()
print('          Bem vindo ao PetSertão')
print()
inicio = input('Para começar click na tecla enter:')
print()

opcao_principal = ''

while opcao_principal != '3':
    print('           MENU')
    print('         PetSertão')
    print()
    print('1 - Login (ADM) OU (CLIENTE) ')
    print('2 - Cadrastar Usuario ')
    print('0 - Sair')
    opcao_menu= input('Escolha uma opcão:')

    if opcao_menu == '2':
        print('cadastrar usuario')

        nome_existe = True
        while nome_existe:  # Repetir se o nome digitado for existente
            nome_existe = False
            nome = input('Digite seu nome:')
            for usuario in usuarios:  # Verificar o nome de cada usuarios
                if usuario[0] == nome:
                    print('Nome existente')
                    nome_existe = True
                    break

        senha = input('Digite sua senha: ')
        tipo = input('Qual tipo deseja cadastrar (ADM) OU (CLIENTE):').upper()
        usuarios.append([nome, senha, tipo])
        print('Usuario Cadastrado')


    elif opcao_menu == '1':
        print('Insira seu login e senha')
        nome = input('Digite seu login: ')
        senha = input('Digite sua senha: ')


        logado = False
        tipo_usuario =''
        for u in usuarios:
            if nome == u[0] and senha == u[1]:
                logado = True
                tipo_usuario = u[2]
                break

        if logado == False:
            print('Login ou senha incorretos')
        else:
            print('Login realizado!')

                        #Menu adm

            if tipo_usuario == 'ADM':
                opcao_adm = ''
                while opcao_adm != '8':
                    print('       Menu ADM')
                    print('1-Cadastrar produto')
                    print('2-Buscar produto cadastrados')
                    print('3-Remover produto')
                    print('4-Cadastar serviços')
                    print('5-Ver serviços')
                    print('6-Remover serviços')
                    print('7-quantidade de produtos em estoque')
                    print('0-Sair do Menu adm')
                    
                    opcao_adm = input('Escolha uma opção')

                    if opcao_adm == '1':
                        produto = input('Digite o nome do produto:')
                        preco = float(input('Digite valor:'))
                        produtos.append([produto, preco])
                        print('Produto Cadastrado')

                    elif opcao_adm == '2':
                        print('  Produtos Cadastrdos')
                        if len(produtos) == 0:
                            print('Nem um produto encontrado')
                        else:
                            for i in range(len(produtos)):
                                print(f'{i+1}. {produtos[i][0]} - valor{produtos[i][1]:}')

                    elif opcao_adm == '3':
                        if len(produtos) == 0:
                            print('Nem um produto para remover')
                        else:
                            for i in range(len(produtos)):
                                print(f'{i+1} {produtos[i][0]}')
                                num = int(input('Digite o numero do produto para remover:'))
                                if 1 <= num <= len(produtos):
                                    produtos.pop(num - 1)
                                    print('Produto removido')
                                else:
                                    print('Produto não encontrado')

                    elif opcao_adm == '4':
                        nome_servico = input('nome do serviço:')
                        preco_servico = float(input('Valor:'))
                        servicos.append([nome_servico, preco_servico])
                        print('Serviço Cadastrado')

                    elif opcao_adm == '5':
                        print('Serviços')
                        if len(servicos) == 0:
                            print('Ainda não a serviços')
                        else:
                            for i in range(len(servicos)):
                                print(f'{i+1}, {servicos[i][0]}, valor:{[servicos[i][1]]:}')


                                        elif opcao_adm == '6':
                        if len(produtos) == 0:
                            print('Nem um serviço para remover')
                        else:
                            for i in range(len(servicos)):
                                print(f'{i+1} {servicos[i][0]}')
                                num = int(input('Digite o numero do serviço para remover:'))
                                if 1 <= num <= len(servicos):
                                    servicos.pop(num - 1)
                                    print('Serviço removido')
                                else:
                                    print('Serviço não encontrado')

                    elif opcao_adm == '7':
                        print('   Estoque')
                        for i in range(len(produtos)):
                            print(f'{produtos[i]} - {quantidades[i]} unidades')
                            item = input('Digite o nome do produto:').lower
                            if item in produtos:
                                for i in range(len(produtos)):
                                    if produtos[i] == item:
                                        print(f'O produto {item}, tem {quantidades[i]} unidades no estoque.')

                        else:
                            print('Item não encontrado')


                    elif opcao_adm == '0':
                        print('Saindo do Menu adm')
                        break
                        
                    else:
                        print('Opção invalida')

            else:
                tipo_usuario =='Cliente':
                opcao_cliente = ''
                while opcao_cliente != '5':
                    print(    f'Bem vindo ao menu do Cliente Sr.(a){nome}')
                    print()
                    print('1- Comprar produto')
                    print('2- Agendar serviços ')
                    print('3- Ver lista de compras')
                    print('4- Agendamentos')
                    print('0- Sair do menu Cliente')
                    opcao_cliente = input('Digite uma opção: ')

                    if opcao_cliente == '1':
                        if len(produtos) == 0:
                            print('Nem um produto disponível')
                        else:
                            print('    Produtos Disponíveis')
                            for i in range(len(produtos)):
                                print(f'{i+1}. {produtos[i][0]} valor: {produtos[i][1]:}')
                                num = int(input('Insira o numero do produto para comprar'))
                                if 1 <= num <= len(produtos):
                                    produto = produtos[num - 1]
                                    compras.append([nome, produto[0], produto[1]])
                                    print(f'você comprou o produto{produto[0]} por {produto[1]}:')
                                else:
                                    print('Número invalido')

                    elif opcao_cliente == '2':
                        if len(servicos) == 0:
                            print('Nem um serviço disponivel')
                        else:
                            print('    Serviços disponiveis')
                            for i in range(len(servicos)):
                                print(f'{i+1} {servicos[i][0]} valor{servicos [i][1]:}')
                                num = int(input('Digite o numero do serviço para agendamento:'))
                                if 1 <= num <= len(servicos):
                                    servico = servicos [num- 1]
                                    horario = input('Qual o horario: (ex:10:00')
                                    agendamentos.append([nome, servicos[0], horario])
                                    print(f'Servico{servicos[0]} Agendado para {horario}')
                                else:
                                    print('Numero inválida')

                    elif opcao_cliente == '3':
                        print('Suas compras')
                        achou = False
                        for c in compras:
                            if c[0] == nome:
                               print(f'{c[1]} - {c[2]}')
                                achou = True
                        if not achou:
                            print('Não há compras no momento.')
                            


                    elif opcao_cliente == '4':
                        print('     Agendamentos')
                        achou = False
                        for a in agendamentos:
                            if a[0] == nome:
                                print(f'Servviços{a[1]}, Horário{a[2]}')
                                achou = True
                        if not achou:
                            print('Sem agendamentos')
                            

                    elif opcao_cliente == '5':
                        print('Sair do menu Cliente')
                        break

                    else:
                        print('Opçao invalida')





    elif opcao_menu == '0':
        print('Saindo..')
        break

    else:
        print('Opção invalida')








