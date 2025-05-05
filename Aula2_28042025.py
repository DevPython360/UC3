import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogo_da_forca():
    palavras_com_dicas = {
        "python": "Linguagem de programação bastante usada em ciência de dados",
        "programacao": "Ato de escrever códigos para computadores",
        "computador": "Máquina usada para processar informações",
        "algoritmo": "Sequência de passos para resolver um problema",
        "desenvolvimento": "Processo de criar sistemas ou softwares"
    }

    while True:
        limpar_tela()
        print("\nBem-vindo ao Jogo da Forca!")

        escolha = input("Deseja digitar a palavra secreta? (s/n): ").lower()
        if escolha == 's':
            palavra_secreta = input("Digite a palavra secreta (não deixe o outro jogador ver!): ").lower()
            dica = input("Digite uma dica para a palavra: ")
            limpar_tela()
        else:
            palavra_secreta, dica = random.choice(list(palavras_com_dicas.items()))

        letras_corretas = set()
        letras_erradas = set()
        tentativas = 6

        print(f"\nDica: {dica}")

        while tentativas > 0:
            palavra_exibida = ""
            for letra in palavra_secreta:
                if letra in letras_corretas:
                    palavra_exibida += letra
                else:
                    palavra_exibida += "_"

            print("\nPalavra:", " ".join(palavra_exibida))
            print("Letras erradas:", " ".join(sorted(letras_erradas)))
            print(f"Tentativas restantes: {tentativas}")

            if "_" not in palavra_exibida:
                print("Parabéns! Você venceu!")
                break

            tentar_palavra = input("\nVocê quer tentar adivinhar a palavra inteira? (s/n): ").lower()
            if tentar_palavra == 's':
                tentativa_palavra = input("Digite a palavra inteira: ").lower()
                if tentativa_palavra == palavra_secreta:
                    print("Parabéns! Você acertou a palavra!")
                    break
                else:
                    print("A palavra está incorreta. Continue tentando!")

            letra = input("Digite uma letra: ").lower()

            if not letra.isalpha() or len(letra) != 1:
                print("Digite apenas uma letra válida.")
                continue

            if letra in letras_corretas or letra in letras_erradas:
                print("Você já tentou essa letra.")
                continue

            if letra in palavra_secreta:
                letras_corretas.add(letra)
                print("Letra correta!")
            else:
                letras_erradas.add(letra)
                tentativas -= 1
                print("Letra incorreta!")

        else:
            print(f"\nGame over! A palavra era: {palavra_secreta}")
        
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar!")
            break


jogo_da_forca()
