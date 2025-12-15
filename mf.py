def menu(print):
    print('           MENU')
    print('         PetSertão')
    print()
    print('1 - Login (ADM) OU (CLIENTE) ')
    print('2 - Cadrastar Usuario ')
    print('0 - Sair')





def cadastrar_usuario(usuarios):
        print('cadastrar usuario')

        nome_existe = True
        while nome_existe:  # Repetir
            nome_existe = False
            nome = input('Digite seu nome:')
            for usuario in usuarios:  # Verificar
                if usuario[0] == nome:
                    print('Nome existente')
                    nome_existe = True
                    break

        login = input('Digite seu login:')
        senha = input('Digite sua senha: ')
        tipo = input('Qual tipo deseja cadastrar (ADM) OU (CLIENTE):').lower
        usuarios.append([nome, login, senha, tipo])
        print('Usuario Cadastrado')


def menu_adm(print):
    print('       Menu ADM')
    print('1-Cadastrar produto')
    print('2-Buscar produto cadastrados')
    print('3-Remover produto')
    print('4-Cadastar serviços')
    print('5-Ver serviços')
    print('6-Remover serviços')
    print('7-quantidade de produtos em estoque')
    print('8- Fazer backup')
    print('9- Importar usuarios')
    print('10- Ver lista de usuarios, produtos, serviços')
    print('0-Sair do Menu adm')


def produto(produtos):
    produto = input('Digite o nome do produto:')
    preco = int(input('Digite valor:'))
    produtos.append([produto, preco])
    print('Produto Cadastrado')


def cadastrado(produtos):
    print('  Produtos Cadastrdos')
    if len(produtos) == 0:
        print('Nem um produto encontrado')
    else:
        for i in range(len(produtos)):
            print(f'{i + 1}. {produtos[i][0]} - valor {produtos[i][1]}')


def remover(produtos):
    if len(produtos) == 0:
        print('Nem um produto para remover')
    else:
        for i in range(len(produtos)):
            print(f'{i + 1} {produtos[i][0]}')
            num = int(input('Digite o numero do produto para remover:'))
            if 1 <= num <= len(produtos):
                produtos.pop(num - 1)
                print('Produto removido')
                con = input('Continuar removendo?').lower
                if con == 'nao':
                    break
                else:
                    continue

            else:
                print('Produto não encontrado')


def servico(servicos):
    nome_servico = input('nome do serviço:')
    preco_servico = float(input('Valor:'))
    servicos.append([nome_servico, preco_servico])
    print('Serviço Cadastrado')



def prorcurar(servicos):
    print('Serviços')
    if len(servicos) == 0:
        print('Ainda não a serviços')
    else:
        for i in range(len(servicos)):
            print(f'{i + 1}, {servicos[i][0]}, valor:{servicos[i][1]:}')



def remover(servicos):
    if len(servicos) == 0:
        print('Nem um serviço para remover')
    else:
        for i in range(len(servicos)):
            print(f'{i + 1}-{servicos[i][0]}-{servicos[i][1]}')

            num = int(input('Digite o numero do serviço para remover:'))
            if 1 <= num <= len(servicos):
                servicos.pop(num - 1)
                print('Serviço removido')
            else:
                print('Serviço não encontrado')



def estoque(produtos, quantidades):
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

def backup(usuarios,produtos,servicos):
    arq_usuario = open('usuarios.txt', 'w')
    for user in usuarios:
        arq_usuario.write(user[0] + '-' + user[1] + '-' + user[2] + '\n')
        print('usuarios salvos')
    arq_usuario.close()

    arq_produtos = open('produtos.txt', 'w')
    for pdt in produtos:
        arq_produtos.write(pdt[0] + '-' + pdt[1] + '\n')
        print('Produtos salvos')
    arq_produtos.close()

    arq_servicos = open('servicos.txt', 'w')
    for s in servicos:
        arq_servicos.write(s[0] + '-' + s[1] + '\n')
        print('Serviços salvos')
    arq_servicos.close()

def importar(usuarios, produtos, servicos):
    arq1 = open('usuarios.txt', 'r')
    linhas = arq1.readlines()
    for li in linhas:
        dados = li.split('-')
        usuarios.append([dados[0], dados[1], dados[2].replace('\n', '')])
    arq1.close()

    arq2 = open('produtos.txt', 'r')
    linhas1 = arq2.readlines()
    for linhas in linhas1:
        dados1 = linhas.split('-')
        produtos.append([dados1[0], dados1[1].replace('\n', '')])
    arq2.close()

    arq3 = open('servicos.txt', 'r')
    linhas2 = arq3.readlines()
    for linha in linhas2:
        dados2 = linha.split('-')
        servicos.append([dados2[0], dados2[1].replace('\n', '')])
    arq3.close()


def listar(usuarios, produtos, servicos):
    print(usuarios)
    print(produtos)
    print(servicos)


def menu_cliente(print, nome):
    print(f'Bem vindo ao menu do Cliente Sr.(a){nome}')
    print()
    print('1- Comprar produto')
    print('2- Agendar serviços ')
    print('3- Ver lista de compras')
    print('4- Agendamentos')
    print('5- adicionar foto do pet')
    print('0- Sair do menu Cliente')



def prod_clien(produtos, compras, nome):
    if len(produtos) == 0:
        print('Nem um produto disponível')
    else:
        print('    Produtos Disponíveis')
        for i in range(len(produtos)):
            print(f'{i + 1}. {produtos[i][0]} valor: {produtos[i][1]}')
            num = int(input('Insira o numero do produto para comprar:'))
            if 1 <= num <= len(produtos):
                produto = produtos[num - 1]
                compras.append([nome, produto[0], produto[1]])
                print(f'você comprou o produto {produto[0]} por {produto[1]}')

            else:
                print('Número invalido')
                break


def servi_clien(servicos, agendamentos, nome):
    if len(servicos) == 0:
        print('Nem um serviço disponivel')
    else:
        print('    Serviços disponiveis')
        for i in range(len(servicos)):
            print(f'{i + 1} {servicos[i][0]} valor{servicos[i][1]:}')
            num = int(input('Digite o numero do serviço para agendamento:'))
            if 1 <= num <= len(servicos):
                servico = servicos[num - 1]
                horario = input('Qual o horario: (ex:10:00):')
                agendamentos.append([nome, servicos[0], horario])
                print(f'Servico{servicos[0]} Agendado para {horario}')
            else:
                print('Numero inválida')


def compras(compras,nome):
    print('Suas compras')
    for c in compras:
        if c[0] == nome:
            print(f'{c[1]} - {c[2]}')
            achou = True
            if not achou:
                print('Não há compras no momento.')


def agendamentos(agendamentos, nome):
    for a in agendamentos:
        if a[0] == nome:
            print(f'Servviços{a[1]}, Horário{a[2]}')
            achou = True
            if not achou:
                print('Sem agendamentos')
