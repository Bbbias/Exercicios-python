nome = 'Beatriz'
tamanho_nome = len(nome)
nova_string = ''
indice = 0
while indice < tamanho_nome:
    nova_string += f'.{nome[indice]}.'
    indice += 1

print(nova_string)

