# 1. Crie uma classe Conta com:

#Atributo _saldo (privado).
#Getter saldo que retorna o valor formatado (ex: R$1000.00).
#Setter que bloqueia valores negativos.

class Conta:
    def __init__(self, saldo_inicial):
        if saldo_inicial >= 0:
            self._saldo = saldo_inicial
        else:
            self._saldo = 0

    def get_saldo(self):
        return f"R${self._saldo:.2f}"

    def set_saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Erro: saldo não pode ser negativo.")

# 2. Classes Abstratas:
#Crie uma classe abstrata Animal com método comum a todas as classes-filhas.
#Implemente, pelo menos, as classes Cachorro e Gato com 3 métodos para cada uma.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Este é o {self.nome}.")

    def fazer_som(self):
        print("Som genérico de animal.")


class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

    def correr(self):
        print(f"{self.nome} está correndo!")

    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo!")


class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

    def subir_em_movel(self):
        print(f"{self.nome} subiu no armário!")

    def arranhar(self):
        print(f"{self.nome} está arranhando o sofá!")

# 3. Padrão de Acesso a Repositórios

# Crie uma classe UsuarioRepository com os seguintes métodos:

#cadastrar(usuario): cadastra um usuário (dicionário com nome e email).
#listar_todos(): retorna uma lista com todos os usuários cadastrados.
#buscar_por_email(email): retorna o usuário correspondente ao email informado.
#remover(email): remove o usuário correspondente ao email informado. 
#atualizar(usuario): atualiza os dados do usuário correspondente ao email informado.
#listar_por_nome(nome): retorna uma lista com todos os usuários que possuem o nome informado.
#listar_por_email(email): retorna uma lista com todos os usuários que possuem o email informado.
#listar_por_nome_e_email(nome, email): retorna uma lista com todos os usuários que possuem o nome e email informados.

class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def cadastrar(self, usuario):
        self.usuarios.append(usuario)

    def listar_todos(self):
        return self.usuarios

    def buscar_por_email(self, email):
        for u in self.usuarios:
            if u["email"] == email:
                return u
        return None

    def remover(self, email):
        for u in self.usuarios:
            if u["email"] == email:
                self.usuarios.remove(u)
                break

    def atualizar(self, usuario):
        for i in range(len(self.usuarios)):
            if self.usuarios[i]["email"] == usuario["email"]:
                self.usuarios[i] = usuario
                break

    def listar_por_nome(self, nome):
        return [u for u in self.usuarios if u["nome"] == nome]

    def listar_por_email(self, email):
        return [u for u in self.usuarios if u["email"] == email]

    def listar_por_nome_e_email(self, nome, email):
        return [u for u in self.usuarios if u["nome"] == nome and u["email"] == email]
