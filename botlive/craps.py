from random import randint


somas_vencedoras_de_primeira = {7, 11}
somas_perdedoras_de_primeira = {2, 3, 12}
somas_perdedoras = somas_vencedoras_de_primeira | somas_perdedoras_de_primeira


def craps():
    nJogada = 1
    ponto = 0
    while True:
        d1 = randint(1, 7)
        d2 = randint(1, 7)
        soma = d1 + d2
        if nJogada == 1:
            if soma in somas_vencedoras_de_primeira:
                return '2020Pajamas Parabéns!! | Pontos: 999 FortOne  2020Party'
            elif soma in somas_perdedoras_de_primeira:
                return f'Craps - perdeu | Pontos = {ponto} NotLikeThis'
        elif nJogada == 2:
            if soma == 7:
                return f'Craps - perdeu | Pontos = {ponto} SeemsGood'
        elif nJogada > 2:
            if soma in somas_perdedoras:
                return f'Craps - perdeu | Pontos = {ponto} LUL'
        ponto += soma
        nJogada += 1
