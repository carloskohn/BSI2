def encriptar_mensagem():
    """Troca as vogais de uma linha de um arquivo\
     de texto por um '*' asterisco."""

    texto = open('mensagem.txt')
    saida = open('cripto.txt', 'w')
    for linha in texto.readlines():
        for letra in linha:
            if letra in 'aeiou':
                saida.write('*')
            else:
                saida.write(letra)
    texto.close()
    saida.close()
# encriptar_mensagem()

def quantas_alice():
    """Conta quantas vezes a palavra 'Alice' aparece no texto."""

    arq = open('alice.txt')
    texto = arq.read()
    texto = texto.lower()
    import string
    for c in string.punctuation:
        texto = texto.replace(c, '')
    texto = texto.split()

    dic = {}
    for palavra in texto:
        if palavra not in dic:
            dic[palavra] = 1
        else:
            dic[palavra] += 1
    arq.close()
    return print('Alice aparece %s vezes' %dic['alice'])

quantas_alice()


