import os

Clientes = [{'nome':'Pedro Silva','instrumento musical':'clarinete','ativo':True},
           {'nome':'Ana Julia','instrumento musical':'flauta transversal', 'ativo':False},
           {'nome':'Hannay','instrumento musical':'ukulele', 'ativo':True}]
   
def exibir_titulo():
    print("""
█░░ █▀█ ░░█ ▄▀█ █▀   █▀█ █░█ ▄▀█ █▀█ ▄▀█
█▄▄ █▄█ █▄█ █▀█ ▄█   █▄█ █▀█ █▀█ █▀▄ █▀█\n""")


def exibir_opcao():
    print('1. Cadastrar Cliente')
    print('2. Listar Cliente')
    print('3. Ativar Cliente')
    print('4. Sair\n')

def escolher_opcao():

    def exibir_subtitulo(texto):
        os.system('cls')
        linha = '-' * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print('') 

    def retorna_menu():
        input(' Digite uma tecla para voltar ao menu principal ')
        main()

    def cadastra_cliente():
        exibir_subtitulo('Cadastrar Cliente')

        Nome_Cliente = input("Digite seu Nome")
        instrumento_cliente = input(f'Qual instrumento musical o {Nome_Cliente} vai comprar: ')
        dados_do_cliente = {'nome':Nome_Cliente, 'instrumento musical':instrumento_cliente, 'ativo':True}
        Clientes.append(dados_do_cliente) 
        print(f'{Nome_Cliente} foi cadastrado com sucesso\n')
        retorna_menu()

    def listar_clientes():
        exibir_subtitulo('Listar Clientes')
        for Cliente in Clientes:
            nome_cliente = Cliente['nome']
            instrumento_cliente = Cliente ['instrumento musical']
            ativo = 'Cadastrado' if Cliente['ativo'] else 'Não Cadastrado'
            print(f' - {nome_cliente.ljust(20)} | {instrumento_cliente.ljust(20)} | {ativo.ljust(20)}')
        retorna_menu()

    def ativar_cliente():
        exibir_subtitulo('Ativar Cliente')
        nome_cliente = input('Digite o nome o cliente que deseja ativar:')
        cliente_encontrado = False

        for Cliente in Clientes:
            if nome_cliente == Cliente['nome']:
                cliente_encontrado = True
                Cliente['ativo'] = not Cliente ['cliente']
                mensagem = f'{nome_cliente} foi ativado com sucesso' if Cliente['ativo'] else f'O cadastro {nome_cliente} não foi realizdo'
                print(mensagem)
        if not cliente_encontrado:
            print('Não Encontrado')

    def finalizar_app():
        os.system('cls')
        print("Finalizando programa")

    def opcao_invalida():
        print("Opçao Inválida")
        input("Aperte um botão para retornar")
        main()


    opcao_escolhida = int(input('Escolha uma opção:'))
    
    try:
        if opcao_escolhida == 1:
            cadastra_cliente()
        elif opcao_escolhida == 2:
            listar_clientes()
        elif opcao_escolhida == 3:
            ativar_cliente()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcao()
    escolher_opcao()

if __name__ == "__main__":
    main()
