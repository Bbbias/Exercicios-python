"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
-Você vai propor uma palavra secreta qualquer e vai dar a possibilidade 
para ao usuário digitar uma letra, você vai conferir se a letra digitada
está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
palavra_secreta = "tirante"
tamanho_palavra = len(palavra_secreta)
palavra_escondida = ""
letra_acertada = ""
tentativas = 0

while(palavra_escondida != palavra_secreta):
    while(True):
        letra = input("\nDigite uma letra: ")
        letra_digitada = len(letra)
        if(letra_digitada == 1):
            tentativas += 1
            break
        else:
            print('\nMais de uma letra digitada')
            continue

    letra_acertada += letra
    i = 0

    if letra in palavra_secreta:
        palavra_escondida = ""
        while(i < tamanho_palavra):
            if palavra_secreta[i] in letra_acertada:
                palavra_escondida += palavra_secreta[i]
            else:
                palavra_escondida += "*"
            i += 1
        print(palavra_escondida)
    else:
        print(f'\nA palavra secreta não contem {letra}')


print(f'\nParabéns você acertou\n\nA palavra era {palavra_secreta}\n\nVocê usou {tentativas} tentativas')