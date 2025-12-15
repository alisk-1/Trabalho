
usuarios = [["admin", "123", "ADM"], ["cliente", "123", "CLIENTE"]]
produtos = []
servicos = []
compras = []
agendamentos = []

opcao_principal = ''

while opcao_principal != '3':
    print('        PETSHOP PetSertão ')
    print('1 - Login (ADM ou CLIENTE)')
    print('2 - Cadastrar novo usuário')
    print('3 - Sair')
    opcao_principal = input('Escolha uma opção: ')


    # CADASTRAR NOVO USUÁRIO

    if opcao_principal == '2':
        print('   CADASTRAR USUÁRIO ')
        nome = input('Nome de usuário: ')
        senha = input('Senha: ')
        tipo = input('Tipo (ADM ou CLIENTE): ').upper()
        usuarios.append([nome, senha, tipo])
        print('Usuário cadastrado com sucesso!')


    # LOGIN

    elif opcao_principal == '1':
        print(     'LOGIN' )
        nome = input('Usuário: ')
        senha = input('Senha: ')

        logado = False
        tipo_usuario = ''
        for u in usuarios:
            if nome == u[0] and senha == u[1]:
                logado = True
                tipo_usuario = u[2]
                break

        if logado == False:
            print('Usuário ou senha errados')
        else:
            print('Login realizado com sucesso')

            # MENU ADMINISTRADOR

            if tipo_usuario == 'ADM':
                opcao_adm = ''
                while opcao_adm != '6':
                    print('     MENU ADMINISTRADOR')
                    print('1 - Cadastrar produto')
                    print('2 - Listar produtos')
                    print('3 - Remover produto')
                    print('4 - Cadastrar serviço')
                    print('5 - Listar serviços')
                    print('0 - Sair do menu ADM')
                    opcao_adm = input("Escolha: ")

                    # CADASTRAR PRODUTO
                    if opcao_adm == '1':
                        nome_produto = input('Nome do produto: ')
                        preco = float(input('Preço: '))
                        produtos.append([nome_produto, preco])
                        print('Produto cadastrado')

                    # LISTAR PRODUTOS
                    elif opcao_adm == '2':
                        print('   PRODUTOS CADASTRADOS ')
                        if len(produtos) == 0:
                            print("Nenhum produto cadastrado.")
                        else:
                            for i in range(len(produtos)):
                                print(f'{i+1}. {produtos[i][0]} - R$ {produtos[i][1]:}')

                    # REMOVER PRODUTO
                    elif opcao_adm == '3':
                        if len(produtos) == 0:
                            print('Nenhum produto para remover.')
                        else:
                            for i in range(len(produtos)):
                                print(f'{i+1}. {produtos[i][0]}')
                            num = int(input('Número do produto para remover: '))
                            if 1 <= num <= len(produtos):
                                produtos.pop(num - 1)
                                print('Produto removido')
                            else:
                                print('Número inválido!')

                    # CADASTRAR SERVIÇO
                    elif opcao_adm == '4':
                        nome_servico = input('Nome do serviço: ')
                        preco_servico = float(input('Preço: '))
                        servicos.append([nome_servico, preco_servico])
                        print('Serviço cadastrado')

                    # VER SERVIÇOS
                    elif opcao_adm == '5':
                        print('   SERVIÇOS CADASTRADOS ')
                        if len(servicos) == 0:
                            print('Nenhum serviço cadastrado.')
                        else:
                            for i in range(len(servicos)):
                                print(f'{i+1}. {servicos[i][0]} - R$ {servicos[i][1]:}')

                    elif opcao_adm == '0':
                        print('Saindo do menu do ADM')

                    else:
                        print('Opção inválida!')


            # MENU CLIENTE

            elif tipo_usuario == 'CLIENTE':
                opcao_cliente = ''
                while opcao_cliente != '5':
                    print(f'      MENU CLIENTE ({nome}) ')
                    print('1 - Comprar produto')
                    print('2 - Agendar serviço')
                    print('3 - Ver minhas compras')
                    print('4 - Ver meus agendamentos')
                    print('0 - Sair do menu CLIENTE')
                    opcao_cliente = input('Escolha: ')

                    # COMPRAR PRODUTO
                    if opcao_cliente == '1':
                        if len(produtos) == 0:
                            print('Nenhum produto disponível.')
                        else:
                            print( '    PRODUTOS DISPONÍVEIS ')
                            for i in range(len(produtos)):
                                print(f'{i+1}. {produtos[i][0]} - R$ {produtos[i][1]:}')
                            num = int(input('Digite o número do produto para comprar: '))
                            if 1 <= num <= len(produtos):
                                produto = produtos[num - 1]
                                compras.append([nome, produto[0], produto[1]])
                                print(f'Você comprou {produto[0]} por R$ {produto[1]:}')
                            else:
                                print('Número inválido')

                    # AGENDAR SERVIÇO
                    elif opcao_cliente == '2':
                        if len(servicos) == 0:
                            print('Nenhum serviço disponível.')
                        else:
                            print('      SERVIÇOS DISPONÍVEIS ')
                            for i in range(len(servicos)):
                                print(f'{i+1}. {servicos[i][0]} - R$ {servicos[i][1]:}')
                            num = int(input('Digite o número do serviço para agendar: '))
                            if 1 <= num <= len(servicos):
                                servico = servicos[num - 1]
                                horario = input('Digite o horário desejado (ex: 10h): ')
                                agendamentos.append([nome, servico[0], horario])
                                print(f'Serviço {servico[0]} agendado para {horario}.')
                            else:
                                print('Número inválido')

                    # ver compras, facilitar para usuarios
                    elif opcao_cliente == '3':
                        print('    SUAS COMPRAS ')
                        achou = False
                        for c in compras:
                            if c[0] == nome:
                                print(f'{c[1]} -  {c[2]:}')
                                achou = True
                        if not achou:
                            print('Nenhuma compra registrada.')

                    # ver agendamentos facilitar para clientes
                    elif opcao_cliente == '4':
                        print('       AGENDAMENTOS ')
                        achou = False
                        for a in agendamentos:
                            if a[0] == nome:
                                print(f'Serviço: {a[1]} | Horário: {a[2]}')
                                achou = True
                        if not achou:
                            print('Sem agendamento.')

                    elif opcao_cliente == '0 ':
                        print('Saindo do menu do cliente...')

                    else:
                        print('Opção inválida!')

    # SAIR DO SISTEMA
    elif opcao_principal == '3':
        print('Saind...o')

    else:
        print('Opção inválida')
