from random import choice
import copy
from math import inf as infinity

HUMANO = -1
COMP = +1
jogada_inicial = True
mov_aceito = ['a', 'f', 'e', 'd']
num_aceito = ['1', '2', '3', '4', '5', '6', '7', '8']
tabuleiro = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [+1, +1, +1, 0, 0, +1, +1, +1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0, 0],
]
tab_gato = [[7, 3]]


def imprimetabuleiro(estado):
    # imprime o tabuleiro na tela

    for row in estado:
        print('\n--------------------------------------------------------------------------------')
        for cell in row:
            if cell == +1:
                print('|', ' RATO ', '|', end='')
            elif cell == -1:
                print('|', ' GATO ', '|', end='')
            else:
                print('|', '      ', '|', end='')
    print('\n--------------------------------------------------------------------------------')


# Realiza verificação se o gato venceu por eliminar todos os ratos
def verificavitoriagato(estado):
    for i in estado:
        for j in i:
            if j == 1:
                return False

    return True


def verificavitoriarato(estado):  # Realiza verificação se o rato venceu

    for i in range(8):
        if tabuleiro[7][i] == 1:
            return True

    gato_eliminado = True

    for i in estado:  # Realiza a verificação da elimicação do gato
        for j in i:
            if j == -1:
                gato_eliminado = False

    return gato_eliminado


# Realiza verificação se o movimento é valido no tabuleiro para o gato
def movimentovalido(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    return False


# Atualiza o tabuleiro com o movimento do gato
def executa_gato(estado, x_destinogato, y_destinogato):
    mov_x, mov_y = tab_gato[0][0], tab_gato[0][1]
    estado[mov_x][mov_y] = 0
    estado[x_destinogato][y_destinogato] = HUMANO
    tab_gato.clear()
    tab_gato.append([x_destinogato, y_destinogato])

    return estado


def move_gato(estado):  # Função para mover gato
    while True:
        gato_ganhou = verificavitoriagato(estado)
        if gato_ganhou:
            imprimetabuleiro(tabuleiro)
            print("\nVitória do GATO!!!!")
            exit()
        imprimetabuleiro(tabuleiro)
        x_gato = tab_gato[0][0]
        y_gato = tab_gato[0][1]
        print("\nMovimentos:\n'e' - esquerda\n'd' - direita\n'f' - frente\n'a' - para trás")
        movimento = input("Digite o movimento desejado: ").lower()
        if movimento not in mov_aceito:
            print("Movimento Inválido!")
            continue
        casas = input("Digite o número de casas desejado: ")
        if not casas.isdigit() or casas not in num_aceito:
            print("Digite somente números até 8")
            continue
        casas = int(casas)
        if movimento == 'e':  # Esquerda
            val = movimentovalido(x_gato, y_gato - casas)
            if not val:
                print("Movimento inválido!")
                continue
            # Verifica se tem um rato no caminho
            if tabuleiro[x_gato][y_gato - casas] != COMP:
                for i in range(y_gato, y_gato - casas, -1):
                    if tabuleiro[x_gato][i] == +1:
                        print("Movimento inválido, o caminho não está livre!")
                        break
                else:
                    executa_gato(estado, x_gato, y_gato - casas)
            else:  # Caso o movimento for numa casa ocupada ele mata o rato
                for i in range(y_gato, -1, -1):
                    if tabuleiro[x_gato][i] == +1:
                        print("Você matou um rato!")
                        tabuleiro[x_gato][i] = 0
                        executa_gato(estado, x_gato, i)
                        break
            break
        if movimento == 'd':  # direita
            val = movimentovalido(x_gato, y_gato + casas)
            if not val:
                print("Movimento inválido!")
                continue
            # Verifica se tem um rato no caminho
            if tabuleiro[x_gato][y_gato + casas] != COMP:
                for i in range(y_gato, y_gato + casas, 1):
                    if tabuleiro[x_gato][i] == +1:
                        print("Movimento inválido, o caminho não está livre!")
                        break
                else:
                    executa_gato(estado, x_gato, y_gato + casas)
                    break
            else:  # Caso o movimento for numa casa ocupada ele mata o rato
                for i in range(y_gato, 8, 1):
                    if tabuleiro[x_gato][i] == +1:
                        print("Você matou um rato!")
                        tabuleiro[x_gato][i] = 0
                        executa_gato(estado, x_gato, i)
                        break
            break
        if movimento == 'f':  # frente
            val = movimentovalido(x_gato - casas, y_gato)
            if not val:
                print("Movimento inválido!")
                continue
            # Verifica se tem um rato no caminho
            if tabuleiro[x_gato - casas][y_gato] != COMP:
                for i in range(x_gato, x_gato - casas, -1):
                    if tabuleiro[i][y_gato] == +1:
                        print("Movimento inválido, o caminho não está livre!")
                        break
                else:
                    executa_gato(estado, x_gato - casas, y_gato)
            # Caso o movimento for numa casa ocupada ele mata o rato
            if tabuleiro[x_gato - casas][y_gato] == COMP:
                for i in range(x_gato, -1, -1):
                    if tabuleiro[i][y_gato] == +1:
                        print("Você matou um rato!")
                        tabuleiro[i][y_gato] = 0
                        executa_gato(estado, i, y_gato)
                        break
            break
        if movimento == 'a':  # atras
            val = movimentovalido(x_gato + casas, y_gato)
            if not val:
                print("Movimento inválido!")
                continue
            # Verifica se tem um rato no caminho
            if tabuleiro[x_gato + casas][y_gato] != COMP:
                for i in range(x_gato, x_gato + casas, 1):
                    if tabuleiro[i][y_gato] == +1:
                        print("Movimento inválido, o caminho não está livre!")
                        break
                else:
                    executa_gato(estado, x_gato + casas, y_gato)
            # Caso o movimento for numa casa ocupada ele mata o rato
            if tabuleiro[x_gato + casas][y_gato] == COMP:
                for i in range(x_gato, 8, 1):
                    if tabuleiro[i][y_gato] == +1:
                        print("Você matou um rato!")
                        tabuleiro[i][y_gato] = 0
                        executa_gato(estado, i, y_gato)
                        break
        break


# Retorna uma lista com a localização dos ratos no tabuleiro
def localizacaoratos(estado):
    lista_localizacao = []

    for x in range(len(estado)):
        for y in range(len(estado)):
            if estado[x][y] == 1:
                lista_localizacao.append([x, y])

    return lista_localizacao


# retorna uma lista contendo os movimentos possiveis
def movimentosvalidosratos(estado):
    lista_localizacao = localizacaoratos(estado)
    lista_movimentos = []

    for item in lista_localizacao:

        if item[0] == 7:
            continue
        else:
            if estado[item[0] + 1][item[1]] == -1:
                continue
            elif item[0] == 1:
                lista_movimentos.append([item, [item[0] + 1, item[1]]])
                lista_movimentos.append([item, [item[0] + 2, item[1]]])
            elif item[0] == 7:
                continue
            else:
                lista_movimentos.append([item, [item[0] + 1, item[1]]])

            if item[0] - 1 >= 0 and item[1] + 1 <= 7:
                if estado[item[0] - 1][item[1] + 1] == -1:
                    lista_movimentos.append([item, [item[0] - 1, item[1] + 1]])
            if item[0] - 1 >= 0 and item[1] - 1 >= 0:
                if estado[item[0] - 1][item[1] - 1] == -1:
                    lista_movimentos.append([item, [item[0] - 1, item[1] - 1]])
            if item[0] + 1 <= 7 and item[1] + 1 <= 7:
                if estado[item[0] + 1][item[1] + 1] == -1:
                    lista_movimentos.append([item, [item[0] + 1, item[1] + 1]])
            if item[0] + 1 <= 7 and item[1] - 1 >= 0:
                if estado[item[0] + 1][item[1] - 1] == -1:
                    lista_movimentos.append([item, [item[0] + 1, item[1] - 1]])

    return lista_movimentos  # primeiro indice localição do rato e o segundo a movimentação


# retorna uma lista contendo os movimentos possiveis
def movimentosvalidosgato(estado):
    posicao_gato = []
    lista_movimentos = []

    for i in range(len(estado)):
        for j in range(len(estado)):
            if estado[i][j] == -1:
                posicao_gato = [i, j]

    for i in range(len(estado)):
        if posicao_gato[1] == i:
            continue
        else:
            lista_movimentos.append([posicao_gato, [posicao_gato[0], i]])

    for i in range(len(estado)):
        if posicao_gato[0] == i:
            continue
        else:
            lista_movimentos.append([posicao_gato, [i, posicao_gato[1]]])

    return lista_movimentos  # primeiro indice localização do gato e o segundo a movimentação


def posicaogato(estado):  # Retorna a posição do gato no tabuleiro
    posicao_gato = []

    for i in range(len(estado)):
        for j in range(len(estado)):
            if estado[i][j] == -1:
                posicao_gato = [i, j]

    return posicao_gato


def avaliacao(estado):  # Verifica o estado do jogo
    if verificavitoriarato(estado):
        placar = +1
    elif verificavitoriagato(estado):
        placar = -1
    else:
        placar = 0

    return placar


def fimjogo(estado):  # Retorna se o rato ou o gato ganhou o jogo
    return verificavitoriagato(estado) or verificavitoriarato(estado)


# Desfaz movimento de teste no minmax
def retrocedemovimentorato(estado, jogada):
    estado[jogada[1][0]][jogada[1][1]] = 0
    estado[jogada[0][0]][jogada[0][1]] = 1

    return estado


# Desfaz movimento de teste no minmax
def retrocedemovimentogato(estado, jogada):
    estado[jogada[1][0]][jogada[1][1]] = 0
    estado[jogada[0][0]][jogada[0][1]] = -1

    return estado


def execjogadarato(estado, jogada):  # Executa movimento do rato
    estado[jogada[0][0]][jogada[0][1]] = 0
    estado[jogada[1][0]][jogada[1][1]] = 1

    return estado


def execjogadagato(estado, jogada):  # Executa movimento do gato
    estado[jogada[1][0]][jogada[1][1]] = -1
    estado[jogada[0][0]][jogada[0][1]] = 0

    return estado


def minimax(estado, profundidade, jogador):  # algoritmo recursivo minimax
    if avaliacao(estado) != 0 or profundidade == 0:  # estado final ou profundidade atingida
        return avaliacao(estado), None

    if jogador == COMP:  # vez do COMP(rato)
        placar = -infinity
        movimentosRatos = movimentosvalidosratos(estado)
        melhorJogada = None

        for jogada in movimentosRatos:  # testa movimentos possiveis dos ratos recursivamente
            execjogadarato(estado, jogada)
            placarAtual, _ = minimax(estado, profundidade - 1, HUMANO)
            retrocedemovimentorato(estado, jogada)
            if placarAtual > placar or melhorJogada is None:  # se jogada atual > anterior
                placar = placarAtual
                melhorJogada = jogada
        return placar, melhorJogada  # retorna melhor jogada do rato
    else:  # vez do HUMANO(gato)
        placar = +infinity
        movimentosGato = movimentosvalidosgato(estado)
        melhorJogada = None

        for jogada in movimentosGato:  # testa movimentos possiveis do gato recursivamente
            execjogadagato(estado, jogada)
            placarAtual, _ = minimax(estado, profundidade - 1, COMP)
            retrocedemovimentogato(estado, jogada)
            if placarAtual < placar or melhorJogada is None:  # se jogada atual < anterior
                placar = placarAtual
                melhorJogada = jogada

        return placar, melhorJogada  # retorna melhor jogada do gato


def movimentaratoia():  # Função que movimenta o rato no tabuleiro
    tabuleiro_minimax = copy.deepcopy(tabuleiro)

    profundidade = 6  # Define a profundidade da arvore no minmax

    global jogada_inicial

    if jogada_inicial:  # Executa o primeiro movimento aleatorio
        jogada = choice(movimentosvalidosratos(tabuleiro))
        execjogadarato(tabuleiro, jogada)
        jogada_inicial = False
        return

    print("Calculando movimentação rato...")

    jogada = minimax(tabuleiro_minimax, profundidade, COMP)
    # Executa movimento retornado do minmax
    execjogadarato(tabuleiro, jogada[1])
    return


def main():
    while not fimjogo(tabuleiro):
        movimentaratoia()
        if verificavitoriarato(tabuleiro):
            imprimetabuleiro(tabuleiro)
            print("\nRato Venceu!")
            exit()
        move_gato(tabuleiro)

    if verificavitoriarato(tabuleiro):
        imprimetabuleiro(tabuleiro)
        print("\nRato Venceu!")
        exit()
    elif verificavitoriagato(tabuleiro):
        imprimetabuleiro(tabuleiro)
        print("\nGato Venceu!")
        exit()


if __name__ == '__main__':
    main()
