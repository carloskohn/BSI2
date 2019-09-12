# Aluno: Carlos Eduardo Kohn

texto = 'Carlos pegou a chave do carro que estava na mesa e \
        saiu pela porta para ir no mercado comprar comida.'

def traduz_para_ingles(texto):
    '''Leia uma string em português com um texto completo e traduza as palavras\
    que encontrar utilizando um dicionário contendo as palavras em inglês'''

    dicionario = {'chave': 'key', 'carro': 'car', 'mesa': 'table', 'porta': 'door',\
                  'mercado': 'marketplace', 'comprar': 'purchase', 'comida': 'food'}
    texto = texto.split()
    novo_texto = []


    for palavra in texto:
        if palavra not in dicionario:
            novo_texto.append(palavra)
        else:
            novo_texto.append(dicionario[palavra])
    print(' '.join(novo_texto))

traduz_para_ingles(texto)