import random
from funcoes import *

def main():
    cartela = {i: -1 for i in range(1, 7)}
    rodadas = 0
    dados_guardados = []

    while rodadas < 12:
        dados = [random.randint(1, 6) for _ in range(5)]
        while True:
            print(f"\nDados rolados: {dados}")
            print("Opções: 1. Guardar dado, 2. Remover dado, 3. Rerrolar, 4. Ver Cartela, 0. Marcar pontuação")
            acao = input("> ")

            if acao == "1":
                dado_escolhido = int(input("Escolha o índice do dado para guardar (0-4): "))
                dados_guardados.append(dados[dado_escolhido])
                dados[dado_escolhido] = -1
            elif acao == "2":
                dado_escolhido = int(input("Escolha o índice do dado para remover (0-4): "))
                if dados[dado_escolhido] != -1:
                    dados[dado_escolhido] = random.randint(1, 6)
            elif acao == "3":
                dados = [random.randint(1, 6) for _ in range(5)]
            elif acao == "4":
                imprime_cartela(cartela)
            elif acao == "0":
                combinacao = input("Digite a combinação desejada (1-6): ")
                if combinacao in ["1", "2", "3", "4", "5", "6"]:
                    numero = int(combinacao)
                    if cartela[numero] == -1:
                        cartela[numero] = regra_simples(numero, dados + dados_guardados)
                    else:
                        print("Essa combinação já foi utilizada.")
                    break
                else:
                    print("Combinação inválida.")
                    break

        rodadas += 1

    imprime_cartela(cartela)

    pontos = 0
    for valor in cartela.values():
        if valor != -1:
            pontos += valor

    print(f"Pontuação total: {pontos}")

if __name__ == "__main__":
    main()