import os
main():
       mostrar_opcoes()

def mostrar_opcoes():
        print("""
    █░░ █▀█ ░░█ ▄▀█ █▀   █▀█ █░█ ▄▀█ █▀█ ▄▀█
    █▄▄ █▄█ █▄█ █▀█ ▄█   █▄█ █▀█ █▀█ █▀▄ █▀█""")


    print('1. Cadastra cliente')
    print('2. Listar cliente')
    print('3. Ativar cliente')
    print('4. Sair\n')

    opcao_escolhida = int(input('escolha uma opção'))

def cadastrar_cliente():
    print("Você escolheu a opção cadastrar cliente")
def listar_cliente():
    print ("Você escolheu a opção listar cliente")
def ativar_cliente():
    print ("Você escolheu a opção ativar cliente")

def finaliza_programa():
    os.system('cls')
    print("Finalizando programa\n")


if opcao_escolhida == 1:
    cadastrar_cliente
elif opcao_escolhida== 2:
    listar_cliente  
elif opcao_escolhida== 3:
    ativar_cliente 
else:
   finaliza_programa

   def main()
    
    if __name__ == "__name__":
       main()