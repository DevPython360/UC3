#Crie um programa que:
#Armazena usuários (nome, email) em um arquivo.
#lista todos os usuários.
#Permita excluir um usuário

def adicionar_usuario():
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    with open('dados.txt', 'a') as arquivo:
        arquivo.write(f"{nome},{email}\n")
    print("Usuário adicionado com sucesso!\n")


def listar_usuarios():
    print("\nUsuários cadastrados:")
    try:
        with open('dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if linhas:
                for linha in linhas:
                    nome, email = linha.strip().split(',', 1)
                    print(f"Nome: {nome} | Email: {email}")
            else:
                print("Nenhum usuário cadastrado.")
    except FileNotFoundError:
        print("Arquivo de dados ainda não existe.")
    print()


def remover_usuario():
    nome = input("Digite o nome do usuário a remover: ").strip().lower()
    email = input("Digite o email do usuário a remover: ").strip().lower()
    try:
        with open('dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        removido = False
        with open('dados.txt', 'w') as arquivo:
            for linha in linhas:
                nome_arquivo, email_arquivo = linha.strip().split(',', 1)
                if nome_arquivo.strip().lower() != nome or email_arquivo.strip().lower() != email:
                    arquivo.write(linha)
                else:
                    removido = True

        if removido:
            print("Usuário removido com sucesso!\n")
        else:
            print("Usuário não encontrado.\n")
    except FileNotFoundError:
        print("Arquivo de dados ainda não existe.\n")


def menu():
    while True:
        print("=== Menu de Usuários ===")
        print("1. Adicionar usuário")
        print("2. Listar usuários")
        print("3. Remover usuário")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            remover_usuario()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


menu()

