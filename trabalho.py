import mf
import teste

usuarios = [['admin','admin','123', 'ADM'], ['cliente','cliente', '123', 'CLIENTE'],['alisk','pk','1234','ADM' ],['joao','jo', '4021','CLIENTE']]
produtos = [['Shampoo', '35.00'],['Racao golden p/ Caes', '149.99'],['anti-pulgas', '66.50'],['Coleira anti-pulga', '175.59'],['Tapete', '70.45']]
quantidades = [10 , 15 , 15 , 50 , 13]
servicos = [['Toza', '50.00'], ['Banho', '35.99'], ['Adestramento', '100.00'], ['Veterinario', '153.45']]
compras = []
agendamentos = [['toza', '10 hrs'], ['Banho', '12 hrs'], ['toza', '14 hrs'],['Toza','14.30']]
imagem = []

print('            Olá, amigo(a)')
print()
print('          Bem vindo ao PetSertão')
print()
inicio = input('Para começar click na tecla enter:')
print()


opcao_principal = ''

while opcao_principal != '3':
    mf.menu(print)
    opcao_menu = input('Escolha uma opcão:')

    if opcao_menu == '2':
       mf.cadastrar_usuario(usuarios)

    elif opcao_menu == '1':
        print('Insira seu login e senha')
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')

        logado = False
        tipo_usuario = ''
        for u in usuarios:
            if login == u[1] and senha == u[2]:
                logado = True
                tipo_usuario = u[3]
                break

        if logado == False:
            print('Login ou senha incorretos')
        else:
            print('Login realizado!')

                        #Menu adm

            if tipo_usuario == 'ADM':
                opcao_adm = ''
                while opcao_adm != '99':
                    mf.menu_adm(print)
                    opcao_adm = input('Escolha uma opção: ')

                    if opcao_adm == '1':
                        mf.produto(produtos)

                    elif opcao_adm == '2':
                       mf.cadastrado(produtos)

                    elif opcao_adm == '3':
                        mf.remover(produtos)

                    elif opcao_adm == '4':
                       mf.servico(servicos)

                    elif opcao_adm == '5':
                        mf.prorcurar(servicos)

                    elif opcao_adm == '6':
                        mf.remover(servicos)

                    elif opcao_adm == '7':
                        mf.estoque(produtos,quantidades)

                    elif opcao_adm == '8':
                        mf.backup(usuarios, produtos, servicos)

                    elif opcao_adm == '9':
                        mf.importar(usuarios, produtos, servicos)

                    elif opcao_adm == '10':
                       mf.listar(usuarios, produtos, servicos)

                    elif opcao_adm == '0':
                        print('Saindo do Menu adm')
                        break
                    else:
                        print('Opção invalida')

            else:
                tipo_usuario == 'CLIENTE'
                opcao_cliente = ''
                while opcao_cliente != '6':
                    mf.menu_cliente(print,login)
                    opcao_cliente = input('Digite uma opção: ')

                    if opcao_cliente == '1':
                        mf.prod_clien(produtos,compras,login)

                    elif opcao_cliente == '2':
                        mf.servi_clien(servicos, agendamentos, login)

                    elif opcao_cliente == '3':
                        achou = False
                        mf.compras(compras,login)

                    elif opcao_cliente == '4':
                        print('     Agendamentos')
                        achou = False
                        mf.agendamentos(agendamentos,login)

                    elif opcao_cliente == '5':
                        teste.tirar_fotos(imagem)
                        break

                    elif opcao_cliente == '0':
                        print('Sair do menu Cliente')
                        break
                    else:
                        print('Opçao invalida')

    elif opcao_menu == '0':
        print('Saindo..')
        break

    else:
        print('Opção invalida')