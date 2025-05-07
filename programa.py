import random
from funcoes import *

def main():
    cartela = {i: -1 for i in range(1, 7)}
    rodadas = 0

    while rodadas < 12:
        dados = [random.randint(1, 6) for _ in range(5)]
        print(f"\nRodada {rodadas + 1}: Dados rolados: {dados}")

        while True:
            acao = input("1-Guardar, 2-Remover, 3-Re-rolar, 4-Ver Cartela, 0-Marcar Pontuação: ")

            if acao == "1":
                dado = int(input("Índice para guardar (0-4): "))
                if 0 <= dado < 5:
                    dados[dado] = -1
            elif acao == "2":
                dado = int(input("Índice para remover (0-4): "))
                if 0 <= dado < 5:
                    dados[dado] = random.randint(1, 6)
            elif acao == "3":
                dados = [random.randint(1, 6) for _ in range(5)]
                print(f"Novos dados rolados: {dados}")
            elif acao == "4":
                imprime_cartela(cartela)
            elif acao == "0":
                combinacao = int(input("Digite a combinação (1-6): "))
                if cartela.get(combinacao, -1) == -1:
                    cartela[combinacao] = regra_simples(combinacao, dados)
                    break
            else:
                print("Opção inválida.")

        rodadas += 1

    imprime_cartela(cartela)
    print(f"Pontuação total: {sum(v for v in cartela.values() if v != -1)}")

if __name__ == "__main__":
    main()