import random

print('Este é um jogo onde uma palavra é embaralhada')
print('você deve tentar acertar que palavra é esta')
print('você terá 5 tentativas')
jogar = input("Deseja continuar? s/n: ")
jogar = str(jogar)
tentativas = 0
contador = 5
palavras = open('palavras.txt').read().splitlines()
palavra = random.choice(palavras)
embaralhada = ''.join(random.sample(palavra, len(palavra)))

if jogar == 'n':
    print('Obrigado mesmo assim, se decidir, pode voltar quando quiser')
else:
    print('Obrigado por aceitar o desafio, vamos começar')
    print('Tente acertar esta palavra:', embaralhada)
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
                break
            else:
                print('Você errou, mas ainda tem %d tentatvas' % (contador))

print('FIM DE JOGO')






