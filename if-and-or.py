"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro ')
if numero.isdigit():    
    numero_inteiro = int(numero)
    resto_numero_por2 = numero_inteiro%2
    if numero_inteiro and resto_numero_por2 == 0:
        print('Seu número é par')
    elif numero_inteiro and resto_numero_por2 != 0:
        print('Seu número é impar')
else:
    print('Não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são? Digite um numero entre 0 e 23: ')
if hora.isdigit():    
    horario_int = int(hora)
    if horario_int >= 0 and horario_int <= 11:
        print('Bom dia')
    elif horario_int >= 12 and horario_int <= 17:
        print('Boa tarde')
    elif horario_int >= 13 and horario_int <= 23:
        print('Boa noite')
    else:
        print('Não conheço esse horario')
else:
    print('Não é um horario válido')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Escreva seu primeiro nome ')
if nome:
    quant_letras = len(nome)
    if quant_letras <= 4:
        print('Seu nome é curto')
    elif quant_letras == 5 or quant_letras == 6:
        print('Seu nome é normal')
    else: 
        print('Seu nome é muito grande')
else: 
    print('Nome não digitado')