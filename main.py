from math import inf as infinity
from random import choice
import platform
import time
from os import system
import re

HUMANO = -1
COMPUTADOR = +1

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


def imprimeTabuleiro():

    # imprime o tabuleiro na tela

    for row in tabuleiro:
        print('\n--------------------------------------------------------------------------------')
        for cell in row:
            if cell == +1:
                print('|', ' RATO ', '|', end='')
            elif cell == -1:
                print('|', ' GATO ', '|', end='')
            else:
                print('|', '      ', '|', end='')
    print('\n--------------------------------------------------------------------------------')


def verificaVitoriaRato():

    # verifica se o rato(computador) venceu por um deles chegar do outro lado

    for i in range(len(tabuleiro)):
        if tabuleiro[7][i] == 1:
            return True

    # verifica se o rato(computador) venceu por ter eliminado o gato

    gato_eliminado = True

    for i in tabuleiro:
        for j in i:
            if j == -1:
                gato_eliminado = False

    if gato_eliminado:
        return True

    return False


def verificaVitoriaGato():

    # verifica se o gato(humano) venceu por ter eliminado todos os ratos

    for i in tabuleiro:
        for j in i:
            if j == 1:
                return False

    return True


def movimentaGato():

    # mostra as possiveis movimentaçoes do gato

    tabuleiro_movimentacao = tabuleiro
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

    while(movimento_valido == False):

        movimento_posicao = []

        movimento = input(
            '\n\nLegenda:\n\nKR: Killer Rato;\nMG: Movimenta Gato. \n\nInsira o numero do movimento que deseja fazer com o gato:\n --->  ')

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


def main():

    while(True):
        imprimeTabuleiro()
        movimentaGato()


if __name__ == '__main__':
    main()
