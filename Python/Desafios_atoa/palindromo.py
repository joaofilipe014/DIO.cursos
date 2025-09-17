def palindromo():
    txt = txt1.lower().replace(' ', '')
    txt_invertido = txt[::-1]
    print("Aqui esta a palavra invertida: ",txt_invertido)
    return txt == txt_invertido

txt1 = input("Digite algo: ")
resultado = palindromo()
print("É um palindromo: ", resultado)