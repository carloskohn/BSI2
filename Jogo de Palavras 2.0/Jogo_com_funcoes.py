


def facil():
    palavras = open('facil.txt').read().splitlines()
    palavra = random.choice(palavras)
    return palavra

def medio():
    palavras = open('medio.txt').read().splitlines()
    palavra = random.choice(palavras)
    return palavra

def dificil():
    palavras = open('dificil.txt').read().splitlines()
    palavra = random.choice(palavras)
    return palavra