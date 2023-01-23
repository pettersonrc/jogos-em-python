def jogar_forca():
    import forcaFunções
    from time import sleep

    while True:
        print('-=' * 15)
        # CABEÇALHO
        nome = forcaFunções.nome_do_jogador()

        forcaFunções.titulo(f'BEM VINDO AO JOGO DE FORCA {nome}!')
        forcaFunções.cabecalho_de_opcoes()

        # Opções lógica
        arquivo = forcaFunções.escolher_opcao()

        # Colocar as palavras do arquivo em uma lista
        palavras = forcaFunções.organizar_palavras(arquivo)

        # Randomizar a palavra criando a lista de acertos
        palavra_secreta = forcaFunções.randomizar_palavra(palavras)

        # Criando lista de acertos
        letras_acertadas = forcaFunções.lista_de_acertos(palavra_secreta)

        # Variáveis
        errou = 0
        chutados = list()

        # Lógica do jogo
        while True:
            for c in letras_acertadas:
                print(f'{c}', end=' ')
            print()

            # Pedindo o chute
            chute = forcaFunções.pedindo_chute()

            # Se o chute já foi
            if chute in chutados:
                print(f'\033[31mA letra {chute} ja foi digitada! Por favor digite outra letra.\033[m')
                continue
            # Se não foi
            else:
                # Se acertou
                if chute in palavra_secreta:
                    letras_acertadas = forcaFunções.acertou_a_letra(chute, palavra_secreta, letras_acertadas)

                # Se errou
                else:
                    errou += 1
                    print(f'Ops, você errou! Faltam {7 - errou} tentativas.')
                    forcaFunções.desenha_forca(errou)

            # Mostrando letras chutadas
            chutados.append(chute)
            print('Letras chutadas: ', end='')
            for letra in chutados:
                print(f'{letra}', end=' ')
            print()
            print('-=' * 15)

            # Se perdeu
            if errou == 7:
                forcaFunções.imprime_mensagem_perdedor(palavra_secreta, nome)
                break
            # Se ganhou
            if '_' not in letras_acertadas:
                forcaFunções.imprime_mensagem_vencedor(palavra_secreta, nome)
                break

        # Continuar ou não
        resp = ' '
        while resp not in 'SN':
            resp = str(input('\033[33mGostaria de jogar novamente? [S/N] \033[m')).upper().strip()[0]
        if resp == 'N':
            break

    # Finalização
    print('\033[36m-=' * 15)
    print('Finalizando...')
    sleep(1)
    print('-' * 30)
    print('Obrigado por jogar!!!\033[m')


jogar_forca()

