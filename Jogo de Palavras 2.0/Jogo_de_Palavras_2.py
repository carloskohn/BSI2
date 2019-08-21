#Aluno: Carlos Eduardo Kohn

import random

print('Este é um jogo onde uma palavra é embaralhada')
print('Você deve tentar acertar esta palavra')
print('Você terá 5 tentativas')
print('Escolha entre \n 1 - Fácil \n 2 - Médio \n 3 - Difícil')
dificuldade = input('Digite o número da opção desejada: ')
entradas_validas = '1, 2, 3'

if dificuldade not in entradas_validas:
    print('Incorreto, reinicie e digite uma opção válida')

else:
    if dificuldade == 1:
        palavras = open('facil.txt').read().splitlines()
        palavra = random.choice(palavras)
        embaralhada = ''.join(random.sample(palavra, len(palavra)))
        tentativas = 0
        contador = 5
        print('Tente acertar esta palavra:', embaralhada)
        frases = open('frases.txt').read().splitlines()
        while tentativas <= 5:
            tentativa = input('Digite a palavra: ')
            tentativas += 1
            contador -= 1
            if tentativa == palavra:
                print('PARABÉNS, você acertou em %d tentativas' % (tentativas))
                break
            else:
                if contador == 0:
                    print('Você não tem mais tentativas, obrigado por participar')
                    print('A palavra correta é', palavra.upper())
                    break
                else:
                    print('Você errou, mas ainda tem %d tentatvas' % (contador))
                    print(random.choice(frases))
    elif dificuldade == 2:
        palavras = open('medio.txt').read().splitlines()
        palavra = random.choice(palavras)
        embaralhada = ''.join(random.sample(palavra, len(palavra)))
        tentativas = 0
        contador = 5
        print('Tente acertar esta palavra:', embaralhada)
        frases = open('frases.txt').read().splitlines()
        while tentativas <= 5:
            tentativa = input('Digite a palavra: ')
            tentativas += 1
            contador -= 1
            if tentativa == palavra:
                print('PARABÉNS, você acertou em %d tentativas' % (tentativas))
                break
            else:
                if contador == 0:
                    print('Você não tem mais tentativas, obrigado por participar')
                    print('A palavra correta é', palavra.upper())
                    break
                else:
                    print('Você errou, mas ainda tem %d tentatvas' % (contador))
                    print(random.choice(frases))
    else:
        palavras = open('medio.txt').read().splitlines()
        palavra = random.choice(palavras)
        embaralhada = ''.join(random.sample(palavra, len(palavra)))
        tentativas = 0
        contador = 5
        print('Tente acertar esta palavra:', embaralhada)
        frases = open('frases.txt').read().splitlines()
        while tentativas <= 5:
            tentativa = input('Digite a palavra: ')
            tentativas += 1
            contador -= 1
            if tentativa == palavra:
                print('PARABÉNS, você acertou em %d tentativas' % (tentativas))
                break
            else:
                if contador == 0:
                    print('Você não tem mais tentativas, obrigado por participar')
                    print('A palavra correta é', palavra.upper())
                    break
                else:
                    print('Você errou, mas ainda tem %d tentatvas' % (contador))
                    print(random.choice(frases))


print('FIM DE JOGO')


