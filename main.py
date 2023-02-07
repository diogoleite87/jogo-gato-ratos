from math import inf as infinity
from random import choice
import platform
import time
from os import system

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
        print('\n---------------------------------------')
        for cell in row:
            if cell == +1:
                print('|', 'R', '|', end='')
            elif cell == -1:
                print('|', 'G', '|', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n---------------------------------------')


def verificaVitoriaRato():

    # verifica se o rato(computador) venceu por um deles chegar do outro lado

    for i in range(8):
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


def main():
    imprimeTabuleiro()
    print(verificaVitoriaRato())


if __name__ == '__main__':
    main()
