#Cada numeração corresponde a um programa diferente para que seja desenvolvido. As atividades seguem abaixo:

#1.Filtre produtos com preço > 1000 usando list comprehension;

produtos = [
    {"nome": "Notebook", "preco": 2500},
    {"nome": "Mouse", "preco": 100},
    {"nome": "Monitor", "preco": 1200},
    {"nome": "Teclado", "preco": 200},
    {"nome": "Celular", "preco": 1800}
]

produtos_caros = [produto for produto in produtos if produto["preco"] > 1000]

print("Produtos com preço acima de R$1000:")
for produto in produtos_caros:
    print(f"- {produto['nome']} (R${produto['preco']})")


#2.Conte quantos produtos existem por categoria (usar dicionário);

produtos = [
    {"nome": "Notebook", "preco": 2500, "categoria": "Informática"},
    {"nome": "Mouse", "preco": 100, "categoria": "Periféricos"},
    {"nome": "Monitor", "preco": 1200, "categoria": "Informática"},
    {"nome": "Teclado", "preco": 200, "categoria": "Periféricos"},
    {"nome": "Celular", "preco": 1800, "categoria": "Telefonia"},
    {"nome": "Fone de Ouvido", "preco": 150, "categoria": "Telefonia"}
]

contagem_categorias = {}

for produto in produtos:
    categoria = produto["categoria"]
    if categoria in contagem_categorias:
        contagem_categorias[categoria] += 1
    else:
        contagem_categorias[categoria] = 1

print("Quantidade de produtos por categoria:")
for categoria, quantidade in contagem_categorias.items():
    print(f"- {categoria}: {quantidade}")


#3.Remova duplicatas de uma lista de pedidos usando set.

pedidos = [
    "Pedido001",
    "Pedido002",
    "Pedido003",
    "Pedido001",
    "Pedido004",
    "Pedido002"
]

pedidos_unicos = list(set(pedidos))

print("Lista de pedidos sem duplicatas:")
for pedido in pedidos_unicos:
    print(f"- {pedido}")


#4.Uma empresa contratou seus serviços para armazenar dados de colaboradores em memória e realizar operações como:
'''
Adicionar novos colaboradores.
Buscar colaborador por ID.
Listar colaboradores com salário acima de X.
'''
#Implemente utilizando funções.

colaboradores = []

def adicionar_colaborador(id, nome, salario):
    colaborador = {"id": id, "nome": nome, "salario": salario}
    colaboradores.append(colaborador)
    print(f"Colaborador {nome} adicionado com sucesso.")

def buscar_colaborador_por_id(id):
    for colaborador in colaboradores:
        if colaborador["id"] == id:
            return colaborador
    return None

def listar_colaboradores_com_salario_acima_de(x):
    return [c for c in colaboradores if c["salario"] > x]


adicionar_colaborador(1, "Ana", 3000)
adicionar_colaborador(2, "Bruno", 4500)
adicionar_colaborador(3, "Carla", 2500)

colab = buscar_colaborador_por_id(2)
if colab:
    print(f"\nColaborador encontrado: {colab['nome']} - R${colab['salario']}")
else:
    print("\nColaborador não encontrado.")

print("\nColaboradores com salário acima de R$3000:")
acima = listar_colaboradores_com_salario_acima_de(3000)
for c in acima:
    print(f"- {c['nome']} (R${c['salario']})")
