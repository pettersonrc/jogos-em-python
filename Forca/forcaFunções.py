def nome_do_jogador():
    nome = str(input('\033[1;33mQual o seu nome? \033[m')).upper().strip()
    return nome


def titulo(msg):
    linha = '~' * len(msg)
    print(f'\033[36m{linha}')
    print(msg)
    print(f'{linha}\033[m')


def cabecalho_de_opcoes():
    print('''\033[35mESCOLHA O TEMA
[1] FRUTAS
[2] JOGOS
[3] ANIMES\033[m''')


def escolher_opcao():
    while True:
        try:
            print('\033[34m-' * 30)
            opcao = int(input('OPÇÃO: \033[m'))
            while opcao not in range(1, 4):
                print('-' * 30)
                print('\033[31mERRO! digite apenas os números indicados\033[m')
                opcao = int(input('OPÇÃO: '))
            if opcao == 1:
                arquivo = open('frutas.txt', 'r')
            elif opcao == 2:
                arquivo = open('jogos.txt', 'r')
            elif opcao == 3:
                arquivo = open('animes.txt', 'r')
        except:
            print('\033[31mERRO! Tivemos um problema com os tipos de dados que você digitou, tente novamente.\033[m')
        else:
            return arquivo


def organizar_palavras(arq):
    palavras = list()
    for linha in arq:
        palavras.append(linha.strip())
    arq.close()
    return palavras


def randomizar_palavra(palavra):
    from random import randrange
    from time import sleep
    print('-=' * 15)
    numero = randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    print(f'\033[30mEscolhendo palavra...')
    sleep(2)
    print('Pronto escolhi, tente advinhar!')
    palavra_sem_espaco = palavra_secreta.replace(' ', '')
    print(f'A palavra tem {len(palavra_sem_espaco)} letras\033[m')
    print('-=' * 15)
    return palavra_secreta


def lista_de_acertos(palavra_secreta):
    letras_acertadas = list()
    for letra in palavra_secreta:
        if ' ' in letra:
            letras_acertadas.append(' ')
        else:
            letras_acertadas.append('_')
    return letras_acertadas


def pedindo_chute():
    while True:
        try:
            chute = str(input('\033[30mQual letra? \033[m')).upper().strip()
            if len(chute) > 1:
                print('\033[31mERRO!, digite apenas uma letra.\033[m')
                continue
        except:
            print('\033[31mERRO! Tivemos um problema com os tipos de dados que você digitou, tente novamente.\033[m')
            continue
        else:
            print('-' * 30)
            return chute


def acertou_a_letra(chute, palavra_secreta, letras_acertadas):
    for index, letra in enumerate(palavra_secreta):
        if chute == letra:
            letras_acertadas[index] = letra
    return letras_acertadas


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_perdedor(palavra_secreta, nome):
    print(f"\033[37mPutz, você foi enforcado {nome}! X.X")
    print(f"A palavra era {palavra_secreta}!\033[m")


def imprime_mensagem_vencedor(palavra_secreta, nome):
    print(f"\033[32mParabéns, você ganhou {nome}!")
    print(f'A palavra era {palavra_secreta}!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print('PARABÉNS!!!\033[m')


