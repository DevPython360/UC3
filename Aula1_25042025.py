#Cálculo de IMC (Índice de Massa Corporal) Declare duas variáveis, peso e altura, com valores 70 e 1.75, respectivamente.
#Calcule o IMC usando a fórmula: IMC = peso / (altura ** 2). Imprima o resultado.

class Pessoa:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def IMC(self):
      
        imc = self.peso / (self.altura ** 2)

        # Classificando o IMC
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3"


def obter_dados_usuario():
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        return peso, altura
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return None


def main():
    dados_usuario = obter_dados_usuario()
    if dados_usuario:
        peso, altura = dados_usuario
        pessoa = Pessoa(peso, altura)  
        resultado_imc = pessoa.IMC()  
        print(f"Seu IMC é: {resultado_imc}")
    else:
        print("Dados inválidos. Tente novamente.")

if __name__ == "__main__":
    main()

#Cálculo de Média de Notas: Peça ao usuário que insira 4 notas (de 0 a 10). 
#Calcule a média das notas e exiba o resultado. Se a média for maior ou igual a 7, exiba "Aprovado". Caso contrário, exiba "Reprovado".
    
def obter_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota 
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    notas = []
    for i in range(1, 5):
        notas.append(obter_nota(i))
    media = calcular_media(notas)
    
    print(f"\nA média das notas é: {media:.2f}")
    
    if media >= 7:
        print("Resultado: Aprovado!")
    else:
        print("Resultado: Reprovado!")
if __name__ == "__main__":
    main()
