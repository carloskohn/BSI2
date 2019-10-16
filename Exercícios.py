
# Aluno: Carlos Eduardo Kohn


import urllib.request

f = urllib.request.urlopen('http://araquari.ifc.edu.br')
site = str(f.read().decode('utf-8'))
pesquisa = 'Sistemas de Informação'

if site.find(pesquisa) > -1:
    arquivo = open('Resultados.txt', 'w')
    arquivo.write('Hoje tem notícia sobre Sistemas de Informação!')
    arquivo.close
else:
    arquivo = open('Resultados.txt', 'w')
    arquivo.write('Hoje não tem notícia sobre Sistemas de Informação!')
    arquivo.close



