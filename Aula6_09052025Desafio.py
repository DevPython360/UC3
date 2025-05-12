# 4. DESAFIO: retorne às atividades 2 e 3 e implemente uma metaclasse dentro de seus respectivos contextos.

import json
import re

class RepositoryMeta(type):
    obrigatorios = {'cadastrar', 'remover', 'atualizar', 'buscar_por_email'}

    def __init__(cls, name, bases, namespace):
        faltando = {
            metodo for metodo in RepositoryMeta.obrigatorios
            if not callable(namespace.get(metodo))
        }
        if faltando:
            raise TypeError(f"A classe '{name}' está faltando os métodos obrigatórios: {faltando}")
        super().__init__(name, bases, namespace)

class UsuarioRepository(metaclass=RepositoryMeta):
    def __init__(self, arquivo='usuarios.json'):
        self.usuarios = []
        self.arquivo = arquivo
        self.carregar_do_arquivo()

    def carregar_do_arquivo(self):
        try:
            with open(self.arquivo, 'r') as f:
                self.usuarios = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.usuarios = []

    def salvar_no_arquivo(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.usuarios, f, indent=4)

    def cadastrar(self, usuario):
        if self.buscar_por_email(usuario.get('email')):
            raise ValueError("Email já cadastrado.")
        self.usuarios.append(usuario)
        self.salvar_no_arquivo()

    def listar_todos(self):
        return self.usuarios

    def buscar_por_email(self, email):
        for usuario in self.usuarios:
            if usuario.get('email') == email:
                return usuario
        return None

    def remover(self, email):
        self.usuarios = [usuario for usuario in self.usuarios if usuario.get('email') != email]
        self.salvar_no_arquivo()

    def atualizar(self, usuario):
        for i, u in enumerate(self.usuarios):
            if u.get('email') == usuario.get('email'):
                self.usuarios[i] = usuario
                self.salvar_no_arquivo()
                return True
        return False

    def listar_por_nome(self, nome):
        return [u for u in self.usuarios if u.get('nome') == nome]

    def listar_por_email(self, email):
        return [u for u in self.usuarios if u.get('email') == email]

    def listar_por_nome_e_email(self, nome, email):
        return [u for u in self.usuarios if u.get('nome') == nome and u.get('email') == email]

def email_valido(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

if __name__ == "__main__":
    repo = UsuarioRepository()

    while True:
        print("\n1. Cadastrar usuário")
        print("2. Listar todos os usuários")
        print("3. Buscar usuário por email")
        print("4. Remover usuário")
        print("5. Atualizar usuário")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            if not email_valido(email):
                print("Email inválido.")
                continue
            try:
                usuario = {'nome': nome, 'email': email}
                repo.cadastrar(usuario)
                print(f"Usuário {nome} cadastrado com sucesso.")
            except ValueError as e:
                print(e)

        elif escolha == "2":
            usuarios = repo.listar_todos()
            print("Lista de usuários:")
            for usuario in usuarios:
                print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")

        elif escolha == "3":
            email = input("Digite o email para buscar: ")
            usuario = repo.buscar_por_email(email)
            if usuario:
                print(f"Usuário encontrado: Nome: {usuario['nome']}, Email: {usuario['email']}")
            else:
                print("Usuário não encontrado.")

        elif escolha == "4":
            email = input("Digite o email do usuário a ser removido: ")
            repo.remover(email)
            print(f"Usuário com email {email} removido.")

        elif escolha == "5":
            email = input("Digite o email do usuário a ser atualizado: ")
            usuario = repo.buscar_por_email(email)
            if usuario:
                nome = input(f"Digite o novo nome para {usuario['nome']} (deixe em branco para manter): ")
                email_novo = input(f"Digite o novo email para {usuario['email']} (deixe em branco para manter): ")
                if email_novo and not email_valido(email_novo):
                    print("Novo email inválido.")
                    continue
                if nome:
                    usuario['nome'] = nome
                if email_novo:
                    usuario['email'] = email_novo
                if repo.atualizar(usuario):
                    print(f"Usuário {usuario['nome']} atualizado com sucesso.")
                else:
                    print("Erro ao atualizar o usuário.")
            else:
                print("Usuário não encontrado.")

        elif escolha == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
