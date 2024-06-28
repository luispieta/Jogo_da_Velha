import os
tabuleiro = list(range(0, 9)) 

def estrutura(tabuleiro):
    print(f"  {tabuleiro[6]}  |  {tabuleiro[7]}  |  {tabuleiro[8]}  ")
    print('-----+-----+-----')
    print(f"  {tabuleiro[3]}  |  {tabuleiro[4]}  |  {tabuleiro[5]}  ")
    print('-----+-----+-----')
    print(f"  {tabuleiro[0]}  |  {tabuleiro[1]}  |  {tabuleiro[2]}  ")

def possiveis(tabuleiro):
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
        return tabuleiro[0]

    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
        return tabuleiro[0]

    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
        return tabuleiro[0]

    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        return tabuleiro[2]

    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
        return tabuleiro[2]

    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        return tabuleiro[1]
    
    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
        return tabuleiro[3]

    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
        return tabuleiro[6]

    return False

jogador1 = input('Seu nome jogador 1 (X): ')
jogador2 = input('Seu nome jogador 2 (O): ')
print('\n')
    
def posicao(tabuleiro):
    numero = 0  
    estrutura(tabuleiro)
            
    while True:
        print(f'=-=-=Vez do jogador {jogador1.capitalize() if numero % 2 == 0 else jogador2.capitalize()}=-=-=')
        posicao = int(input('Digite a posição que você deseja: '))
        tabuleiro[posicao] = 'X' if numero % 2 == 0 else 'O'

        print('\n')
        os.system('cls')
        estrutura(tabuleiro)
        numero += 1 

        possivel = possiveis(tabuleiro)
        if possivel == tabuleiro[posicao] == 'X': 
            print(f'Fim de jogo \n Jogador {jogador1.capitalize()} ganhou!')
            exit()

        if possivel == tabuleiro[posicao] == 'O': 
            print(f'Fim de jogo \n Vencedor {jogador2.capitalize()}')
            exit()

        temNumero = False
        for pos in tabuleiro:
            if pos != "O" and pos != "X":
                temNumero = True


        empate = possivel == False and not temNumero
        if empate:
            print('Fim de jogo \n Ninguém ganhou!')
            exit()
while True: 
    posicao(tabuleiro)