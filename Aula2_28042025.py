import random

def jogo_da_forca():
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
    
    while True:
        palavra_secreta = random.choice(palavras)
        letras_corretas = set()
        letras_erradas = set()
        tentativas = 6

        print("\nBem-vindo ao Jogo da Forca!")

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

            if palavra_exibida == palavra_secreta:
                print("Parabéns! Você venceu!")
                break

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
            print(f"Game over! A palavra era: {palavra_secreta}")
        
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar!")
            break
