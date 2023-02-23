from os import system
from random import choice
import re
import copy
from math import inf as infinity
import platform

HUMANO = -1
COMP = +1
jogada_inicial = True

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


def imprimeTabuleiro(estado):

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


def verificaVitoriaRato(estado):

    # verifica se o rato(computador) venceu por um deles chegar do outro lado

    for i in range(len(estado)):
        if estado[7][i] == 1:
            return True

    # verifica se o rato(computador) venceu por ter eliminado o gato

    gato_eliminado = True

    for i in estado:
        for j in i:
            if j == -1:
                gato_eliminado = False

    return gato_eliminado


def verificaVitoriaGato(estado):

    # verifica se o gato(humano) venceu por ter eliminado todos os ratos

    for i in estado:
        for j in i:
            if j == 1:
                return False

    return True


def movimentaGato():

    # mostra as possiveis movimentaçoes do gato

    tabuleiro_movimentacao = copy.deepcopy(tabuleiro)
    movimentos_possiveis = []
    contador_movimentos = 0
    movimento_valido = False

    posicao_gato = []

    for i in range(len(tabuleiro_movimentacao)):
        for j in range(len(tabuleiro_movimentacao)):
            if tabuleiro_movimentacao[i][j] == -1:
                posicao_gato = [i, j]

    for i in range(len(tabuleiro_movimentacao)):

        if tabuleiro_movimentacao[posicao_gato[0]][i] != -1 and tabuleiro_movimentacao[posicao_gato[0]][i] != 1:
            tabuleiro_movimentacao[posicao_gato[0]][i] = 2
            contador_movimentos += 1

            str_contador_movimentos: str

            if contador_movimentos < 10:
                str_contador_movimentos = '0' + str(contador_movimentos)
            else:
                str_contador_movimentos = str(contador_movimentos)

            movimentos_possiveis.append(
                ['MG(' + str_contador_movimentos + ')', [posicao_gato[0], i]])

            tabuleiro_movimentacao[posicao_gato[0]
                                   ][i] = movimentos_possiveis[contador_movimentos - 1][0]

        elif tabuleiro_movimentacao[posicao_gato[0]][i] == 1:
            tabuleiro_movimentacao[posicao_gato[0]][i] = 3
            contador_movimentos += 1

            str_contador_movimentos: str

            if contador_movimentos < 10:
                str_contador_movimentos = '0' + str(contador_movimentos)
            else:
                str_contador_movimentos = str(contador_movimentos)

            movimentos_possiveis.append(
                ['KR(' + str_contador_movimentos + ')', [posicao_gato[0], i]])

            tabuleiro_movimentacao[posicao_gato[0]
                                   ][i] = movimentos_possiveis[contador_movimentos - 1][0]

    for i in range(len(tabuleiro_movimentacao)):

        if tabuleiro_movimentacao[i][posicao_gato[1]] != -1 and tabuleiro_movimentacao[i][posicao_gato[1]] != 1:
            tabuleiro_movimentacao[i][posicao_gato[1]] = 2
            contador_movimentos += 1

            str_contador_movimentos: str

            if contador_movimentos < 10:
                str_contador_movimentos = '0' + str(contador_movimentos)
            else:
                str_contador_movimentos = str(contador_movimentos)

            movimentos_possiveis.append(
                ['MG(' + str_contador_movimentos + ')', [i, posicao_gato[1]]])

            tabuleiro_movimentacao[i
                                   ][posicao_gato[1]] = movimentos_possiveis[contador_movimentos - 1][0]

        elif tabuleiro_movimentacao[i][posicao_gato[1]] == 1:
            tabuleiro_movimentacao[i][posicao_gato[1]] = 3
            contador_movimentos += 1

            str_contador_movimentos: str

            if contador_movimentos < 10:
                str_contador_movimentos = '0' + str(contador_movimentos)
            else:
                str_contador_movimentos = str(contador_movimentos)

            movimentos_possiveis.append(
                ['KR(' + str_contador_movimentos + ')', [i, posicao_gato[1]]])

            tabuleiro_movimentacao[i
                                   ][posicao_gato[1]] = movimentos_possiveis[contador_movimentos - 1][0]

    for i in range(len(tabuleiro_movimentacao)):
        print(
            '\n--------------------------------------------------------------------------------')

        for j in range(len(tabuleiro_movimentacao)):
            if tabuleiro_movimentacao[i][j] == 0:
                print('|', '      ', '|', end='')
            elif tabuleiro_movimentacao[i][j] == -1:
                print('|', ' GATO ', '|', end='')
            elif tabuleiro_movimentacao[i][j] == 1:
                print('|', ' RATO ', '|', end='')
            else:
                print('|', tabuleiro_movimentacao[i][j], '|', end='')

    print('\n--------------------------------------------------------------------------------')

    while(movimento_valido == False):

        movimento_posicao = []

        movimento = input(
            '\n\nLegenda:\n\nMR: Matar Rato;\nMG: Movimenta Gato. \n\nInsira o numero do movimento que deseja fazer com o gato:\n --->  ')

        for i in range(len(movimentos_possiveis)):
            aux = movimentos_possiveis[i][0]
            aux = re.sub('[^0-9]', '', aux)

            if int(aux) == int(movimento):
                movimento_valido = True
                movimento_posicao = movimentos_possiveis[i][1]

        if movimento_valido:
            tabuleiro[movimento_posicao[0]][movimento_posicao[1]] = -1
            tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0
            break
        else:
            print('\nMovimento Invalido!')


def localizacaoRatos(estado):

    lista_localizacao = []

    for x in range(len(estado)):
        for y in range(len(estado)):
            if estado[x][y] == 1:
                lista_localizacao.append([x, y])

    return lista_localizacao


def movimentosValidosRatos(estado):

    lista_localizacao = localizacaoRatos(estado)
    lista_movimentos = []

    for item in lista_localizacao:

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

    return lista_movimentos


def movimentosValidosGato(estado):

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

    return lista_movimentos


def posicaoGato(estado):
    posicao_gato = []

    for i in range(len(estado)):
        for j in range(len(estado)):
            if estado[i][j] == -1:
                posicao_gato = [i, j]

    return posicao_gato


def avaliacao(estado):
    if verificaVitoriaRato(estado):
        placar = +1
    elif verificaVitoriaGato(estado):
        placar = -1
    else:
        placar = 0

    return placar


def fimJogo(estado):
    return verificaVitoriaGato(estado) or verificaVitoriaRato(estado)


def limpaConsole():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def retrocedeMovimentoRato(estado, jogada):
    estado[jogada[1][0]][jogada[1][1]] = 0
    estado[jogada[0][0]][jogada[0][1]] = 1

    return estado


def retrocedeMovimentoGato(estado, jogada):
    estado[jogada[1][0]][jogada[1][1]] = 0
    estado[jogada[0][0]][jogada[0][1]] = -1

    return estado


def execJogadaRato(estado, jogada):

    estado[jogada[0][0]][jogada[0][1]] = 0
    estado[jogada[1][0]][jogada[1][1]] = 1

    return estado


def execJogadaGato(estado, jogada):

    estado[jogada[1][0]][jogada[1][1]] = -1
    estado[jogada[0][0]][jogada[0][1]] = 0

    return estado


def minimax(estado, profundidade, jogador):

    if avaliacao(estado) != 0 or profundidade == 0:
        return avaliacao(estado), None

    if jogador == COMP:
        placar = -infinity
        movimentosRatos = movimentosValidosRatos(estado)
        melhorJogada = None

        for jogada in movimentosRatos:
            execJogadaRato(estado, jogada)
            placarAtual, _ = minimax(estado, profundidade - 1, HUMANO)
            retrocedeMovimentoRato(estado, jogada)
            if placarAtual > placar or melhorJogada is None:
                placar = placarAtual
                melhorJogada = jogada
        return placar, melhorJogada
    else:
        placar = +infinity
        movimentosGato = movimentosValidosGato(estado)
        melhorJogada = None

        for jogada in movimentosGato:
            execJogadaGato(estado, jogada)
            placarAtual, _ = minimax(estado, profundidade - 1, COMP)
            retrocedeMovimentoGato(estado, jogada)
            if placarAtual < placar or melhorJogada is None:
                placar = placarAtual
                melhorJogada = jogada

        return placar, melhorJogada


def movimentaRatoIA():

    tabuleiro_minimax = copy.deepcopy(tabuleiro)

    profundidade = 10

    global jogada_inicial

    if jogada_inicial:
        jogada = choice(movimentosValidosRatos(tabuleiro))
        execJogadaRato(tabuleiro, jogada)
        jogada_inicial = False
        return

    print("Calculando movimentação rato...")

    jogada = minimax(tabuleiro_minimax, profundidade, COMP)
    execJogadaRato(tabuleiro, jogada[1])
    return


def main():

    while(fimJogo(tabuleiro) == False):
        imprimeTabuleiro(tabuleiro)
        movimentaRatoIA()

        if fimJogo(tabuleiro) == False:
            movimentaGato()

        limpaConsole()

    if verificaVitoriaGato(tabuleiro):
        imprimeTabuleiro(tabuleiro)
        print("\nGato Venceu!")
    else:
        imprimeTabuleiro(tabuleiro)
        print("\nRato Venceu!")


if __name__ == '__main__':
    main()
