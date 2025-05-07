# gustavoejoao
import random

def rolar_dados(n):
    lista = []
    for i in range(0, n):
        dado = random.randint(1, 6)
        lista.append(dado)
    return lista


def guardar_dado(dados_rolados, dados_guardados, indice):
    dado = dados_rolados[indice]
    del dados_rolados[indice]
    dados_guardados.append(dado)
    return [dados_rolados, dados_guardados]


def remover_dado(dados_rolados, dados_guardados, indice):
    dado = dados_guardados[indice]
    del dados_guardados[indice]
    dados_rolados.append(dado)
    return [dados_rolados, dados_guardados]

def calcula_pontos_regra_simples(dados_rolados):
    pontos_regra_simples = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(len(dados_rolados)):
        pontos_regra_simples[dados_rolados[i]] += dados_rolados[i]
    return pontos_regra_simples


def calcula_pontos_soma(dados_rolados):
    total = 0
    for i in range(len(dados_rolados)):
        total += dados_rolados[i]
    return total

def calcula_pontos_sequencia_baixa(dados):
    for i in range(len(dados)):
        if dados[i] + 1 in dados:
            if dados[i] + 2 in dados:
                if dados[i] + 3 in dados:
                    return 15
    return 0

def calcula_pontos_sequencia_alta(dados):
    for i in range(len(dados)):
        if dados[i] + 1 in dados:
            if dados[i] + 2 in dados:
                if dados[i] + 3 in dados:
                    if dados[i] + 4 in dados:
                        return 30
    return 0

def calcula_pontos_full_house(dados):
    valores = {}
    for d in dados:
        if d in valores:
            valores[d] += 1
        else:
            valores[d] = 1

    if len(valores) == 2:
        a = list(valores.values())
        if (a[0] == 3 and a[1] == 2) or (a[0] == 2 and a[1] == 3):
            total = 0
            for num in dados:
                total += num
            return total

    return 0

def calcula_pontos_quadra(numeros_jogados):
    dados = {}
    for i in range(len(numeros_jogados)):
        valor = numeros_jogados[i]
        if valor not in dados:
            dados[valor] = 1
        else:
            dados[valor] += 1

    total = 0
    for numero in dados:
        if dados[numero] >= 4:
            for j in range(len(numeros_jogados)):
                total += numeros_jogados[j]
            break

    return total


def calcula_pontos_quina(dados_jogados):
    dados = {}
    for i in range(len(dados_jogados)):
        valor = dados_jogados[i]
        if valor not in dados:
            dados[valor] = 1
        else:
            dados[valor] += 1

    total = 0
    for j in dados:
        if dados[j] >= 5:
            total = 50
            break

    return total

def calcula_pontos_regra_avancada(dados):
    quina = calcula_pontos_quina(dados)
    fullhouse = calcula_pontos_full_house(dados)
    quadra = calcula_pontos_quadra(dados)
    soma = calcula_pontos_soma(dados)
    sequencia_alta = calcula_pontos_sequencia_alta(dados)
    sequencia_baixa = calcula_pontos_sequencia_baixa(dados)
    tudo = {
    'cinco_iguais': quina,
    'full_house': fullhouse,
    'quadra': quadra,
    'sem_combinacao': soma,
    'sequencia_alta': sequencia_alta,
    'sequencia_baixa': sequencia_baixa
    }
    return tudo


def faz_jogada(lista, cat, cartela):
    psimples = calcula_pontos_regra_simples(lista)
    pavançado = calcula_pontos_regra_avancada(lista) 
    if cat not in ['1', '2', '3', '4', '5', '6']: 
        cartela['regra_avancada'][cat] = pavançado[cat]
    else:
        categoria = int(cat)
        cartela['regra_simples'][categoria] = psimples[categoria]
    return cartela