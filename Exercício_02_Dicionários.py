# Aluno = CARLOS EDUARDO KOHN

# 1) Primeiro, faça uma lista chamada "mantimentos" com os valores "banana", "laranja" e "melao".
# Defina estes dois dicionários:
# estoque = {"banana": 6, "melao": 0, "laranja": 32, "pera": 15}
# precos = {"banana": 4, "melao": 2, "laranja": 1.5, "pera": 3}

# 2) Defina uma função calcular_conta que aceita um argumento "lista_de_mantimentos" como entrada.
# Na função, crie uma variável total com um valor inicial zero.
# Para cada item da lista de mantimentos, adicione o preço desse item ao total.
# Finalmente, retorne o total.
# Ignore se o item que você está faturando está ou não em estoque.
# Observe que sua função deve funcionar para qualquer lista de mantimentos.

# 3) Agora, faça as seguintes alterações na função calcular_conta:
# Enquanto você percorre cada item da lista de mantimentos,
# adicione apenas o preço do item ao total se a contagem de estoque do item for maior que zero.
# Se o item estiver em estoque, depois de adicionar o preço ao total,
# subtraia um da contagem de estoque do item.


lista_de_mantimentos = ['banana', 'laranja', 'melao']
estoque = {'banana': 6, 'melao': 0, 'laranja': 32, 'pera': 15}
precos = {'banana': 4, 'melao': 2, 'laranja': 1.5, 'pera': 3}

def calcular_conta(lista_de_mantimentos):
    total = 0
    for item in lista_de_mantimentos:
        if estoque[item] > 0:
            total += precos[item]
            estoque[item] -= 1

    print(total)

calcular_conta(lista_de_mantimentos)
