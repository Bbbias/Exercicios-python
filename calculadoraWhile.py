while True:
    primeiro_numero = input('Digite um número ')
    segundo_numero = input('Digite outro número ')
    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
    except:
        print('Um ou os dois numeros não são válidos')
        continue

    operador = input('Digite o operador ')
    operadores_validos = '/*-+'
    while operador in operadores_validos and len(operador) > 1:
        operador = input('Mais de um operador digitado.\nDigite um operador ')
    while operador not in operadores_validos:
        operador = input('Não é um operador válido.\nDigite um operador ')

    if operador == '+':
        resultado = primeiro_numero_float + segundo_numero_float
    elif operador == '/':
        resultado = primeiro_numero_float / segundo_numero_float
    elif operador == '*':
        resultado = primeiro_numero_float * segundo_numero_float
    elif operador == '-':
        resultado = primeiro_numero_float - segundo_numero_float
    
    print(f'Resultado: {primeiro_numero_float} {operador} {segundo_numero_float} = {resultado}')

    sair = input('Você quer sair? digite [s] ').lower()
    if sair.startswith('s') == True:
        break