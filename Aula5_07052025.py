# Atividade Prática: Sistema de uma Biblioteca
#Contexto:
#Você foi contratado para desenvolver um sistema de gerenciamento de biblioteca usando POO em Python.
#O sistema deve modelar livros, usuários e empréstimos, com funcionalidades básicas de cadastro, consulta e operações.

#Requisitos:
#O sistema deve permitir o cadastro de livros, usuários e empréstimos.
#O sistema deve permitir a consulta de livros cadastrados.
#O sistema deve permitir a consulta de usuários cadastrados.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar(self):
        return f"{self.titulo} - {self.autor}"


class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario

    def mostrar(self):
        return f"{self.livro.titulo} emprestado para {self.usuario.nome}"


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def adicionar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))

    def adicionar_usuario(self, nome, cpf):
        self.usuarios.append(Usuario(nome, cpf))

    def emprestar_livro(self, titulo_livro, cpf_usuario):
        for livro in self.livros:
            if livro.titulo == titulo_livro:
                for usuario in self.usuarios:
                    if usuario.cpf == cpf_usuario:
                        self.emprestimos.append(Emprestimo(livro, usuario))
                        print("Empréstimo feito com sucesso!")
                        return
        print("Livro ou usuário não encontrado.")

    def mostrar_livros(self):
        for livro in self.livros:
            print(livro.mostrar())

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.mostrar())

    def mostrar_emprestimos(self):
        for emprestimo in self.emprestimos:
            print(emprestimo.mostrar())


def menu():
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro("Drácula", "Bram Stoker")
    biblioteca.adicionar_livro("Frankenstein", "Mary Shelley")
    biblioteca.adicionar_livro("O Iluminado", "Stephen King")
    biblioteca.adicionar_livro("It: A Coisa", "Stephen King")
    biblioteca.adicionar_livro("A Volta do Parafuso", "Henry James")
    biblioteca.adicionar_livro("O Exorcista", "William Peter Blatty")
    biblioteca.adicionar_livro("Coraline", "Neil Gaiman")
    biblioteca.adicionar_livro("O Médico e o Monstro", "Robert Louis Stevenson")
    biblioteca.adicionar_livro("O Chamado de Cthulhu", "H.P. Lovecraft")
    biblioteca.adicionar_livro("A Assombração da Casa da Colina", "Shirley Jackson")
    biblioteca.adicionar_livro("VHS", "Cesar Bravo")
    biblioteca.adicionar_livro("O Colecionador", "John Fowles")
    biblioteca.adicionar_livro("O Morro dos Ventos Uivantes", "Emily Brontë")
    biblioteca.adicionar_livro("Pet Sematary", "Stephen King")

    biblioteca.adicionar_usuario("Isis Rita Pires", "697.964.138-76")
    biblioteca.adicionar_usuario("Caio Anderson Lima", "995.753.927-28")
    biblioteca.adicionar_usuario("Elisa Andreia Julia Gomes", "794.380.541-03")
    biblioteca.adicionar_usuario("Mateus Noah Barros", "216.932.381-36")
    biblioteca.adicionar_usuario("Mirella Tatiane Rezende", "538.506.118-25")
    biblioteca.adicionar_usuario("Isabel Lavínia Almeida", "870.228.624-60")
    biblioteca.adicionar_usuario("Mariane Luana Catarina Assunção", "527.374.095-94")
    biblioteca.adicionar_usuario("Mariane Carolina Viana", "710.455.039-91")
    biblioteca.adicionar_usuario("Elisa Regina Emanuelly Bernardes", "186.042.386-89")

    while True:
        print("\n1 - Adicionar Livro")
        print("2 - Adicionar Usuário")
        print("3 - Emprestar Livro")
        print("4 - Ver Livros")
        print("5 - Ver Usuários")
        print("6 - Ver Empréstimos")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            biblioteca.adicionar_livro(titulo, autor)
        elif escolha == "2":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            biblioteca.adicionar_usuario(nome, cpf)
        elif escolha == "3":
            titulo = input("Título do livro: ")
            cpf = input("CPF do usuário: ")
            biblioteca.emprestar_livro(titulo, cpf)
        elif escolha == "4":
            biblioteca.mostrar_livros()
        elif escolha == "5":
            biblioteca.mostrar_usuarios()
        elif escolha == "6":
            biblioteca.mostrar_emprestimos()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()