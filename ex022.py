nome = input('Digite seu nome:')
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
tamanho = len(nome) - nome.count(' ')
nome_dividido = nome.split()
tamanho_primeiro = len(nome_dividido[0])
print(f'O seu nome todo maiusculo é: {nome_maiusculo}')
print(f'O se nome todo minusculo é: {nome_minusculo}')
print(f'O seu nome tem {tamanho} letras')
print(f'O seu primeiro nome é {nome_dividido[0]} e tem {tamanho_primeiro} letras')

