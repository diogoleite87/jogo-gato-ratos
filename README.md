# Jogo do Gato e Ratos - Inteligencia Artifical

> Foi utilizado Python e algoritmo de Busca Competitiva Minimax

## O trabalho consiste na aplicação do algoritmo Minimax no contexto do jogo Gato e Ratos, onde o Gato é nós(Humano) quem movimenta e os Ratos é a IA(Computador), na qual escolhe o melhor movimento afim de maximizar suas chances.

## Primeiramente, vamos discutir como executar 🏃‍

```bash

# Antes de tudo, voce precisara da versão mais recente do Python instalada

# Feito isso, clone este repositório
$ git clone https://github.com/diogoleite87/jogo-gato-ratos

# Acessa a pasta raiz no terminal
$ cd jogo-gato-ratos

# Execute a aplicação
$ python3 main.py ou python main.py

# A aplicação iniciará e voce poderá jogar e acompanhar pelo terminal

```

## Regras do Jogo:

### Regras de movimento e captura – para os Ratos:

#### 1. Na sua vez, o jogador com os ratos pode mover apenas um de seus ratos.

#### 2. O rato só pode mover-se para frente.

#### 3. O rato avança uma casa por vez.

#### 4. Apenas em seu primeiro movimento, cada rato pode escolher entre avançar uma ou duas casas.

#### 5. O rato só pode capturar na diagonal.

#### 6. O rato não pode mover-se para trás, nem capturar para trás.

### Regras de movimento e captura – para o Gato:

#### 1. O gato pode mover-se para frente, para trás e para os lados, e pode capturar os ratos nestas direções.

#### 2. O gato não pode mover-se nem capturar na diagonal.

#### 3. O gato pode mover-se quantas casas quiser, desde que o caminho esteja livre.

#### 4. Quando o gato captura um rato, passa a ocupar a casa em que o rato estava.

#### 5. O gato só pode capturar um rato por jogada.

## Minimax:

#### O algoritmo minimax é um método utilizado em jogos de decisão de dois jogadores com informações perfeitas e alternadas, em que cada jogador busca maximizar sua própria pontuação e minimizar a pontuação do oponente. Ele funciona através de uma árvore de jogadas, em que cada nó representa uma configuração do jogo e os ramos representam as ações possíveis para cada jogador. O algoritmo avalia as jogadas possíveis, atribuindo valores para cada nó folha da árvore, e escolhe a melhor jogada possível para o jogador considerando as jogadas do oponente. O minimax é um algoritmo completo e ótimo, mas pode ser computacionalmente exigente em jogos complexos com muitas possibilidades, como no caso em questão do jogo Gato e Ratos.
