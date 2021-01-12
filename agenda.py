AGENDA = {}

AGENDA['Mateus'] = {
    'telefone': '(75)2162-9779',
    'email': 'mateus@gmail.com',
    'endereco': 'Avendia Getulio vargas',
}

AGENDA['Adriele'] = {
    'telefone': '(75)0162-8770',
    'email': 'adrilds@gmail.com',
    'endereco': 'Fazenda Modelo',
}


AGENDA['Mateus Henrique'] = {
    'telefone': '(75)33172-1539',
    'email': 'mathenriquesouzaads@gmail.com',
    'endereco': 'Avendia Getulio Modelo',
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('-------------------------------------------')
    except KeyError:
        print('>>>>> Contato Inexistente!')


def ler_detalhes_contato():
    telefone = input('Digite os números do telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar_agenda()
    print()
    print('>>>>> Contato {} Add/editado com sucesso.  <<<<<'.format(contato))
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar_agenda()
        print()
        print('>>>>> Contato {} excluido com sucesso. <<<<<'.format(contato))
        print()
    except KeyError:
        print('>>>>> Contato Inexistemte!')


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{};{};{};{}\n".format(
                    contato, telefone, email, endereco))
            print('>>>>> Agenda exportada com sucesso.')
    except Exception:
        print('>>>>> Algum erro ocorreu ao exportar os contatos')


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('>>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>>> Algum erro ocorreu')
        print(error)


def salvar_agenda():
    exportar_contatos('database.csv')


def carregar_agenda():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }

        print('>>>>> Database carregado com sucesso')
        print('>>>>> {} contatos carregados'.format(len(AGENDA)))

    except FileNotFoundError:
        print('>>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>>> Algum erro ocorreu')
        print(error)


def imprimir_menu():
    print('-------------------------------------------')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Exclui contato')
    print('6 - Exportar agenda em um arquivo CSV')
    print('7 - Importar agenda CSV')
    print('0 - Fechar agenda')
    print('-------------------------------------------')


# INICIO DO PROGRAMA
carregar_agenda()

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>>> Contato já existente')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>>> Editando Contato: ', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('Contato Inexistente')

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)

    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)

    elif opcao == '0':
        print('>>> Fechando o programa.')
        break

    else:
        print('>>> Opção inválida!')
