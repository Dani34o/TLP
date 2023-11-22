def generar_codigos():
    letras = ['P', 'Q', 'R', 'W', 'X', 'Y', 'Z']
    digitos = ['9', '8', '7', '6', '5']
    especiales = ['_', '#', '&', '%']

    codigos = ['COD-' + digito1 + digito2+ digito3 +letra1 + letra2 + letra3 + especial
               for digito1 in digitos
               for digito2 in digitos
               for digito3 in digitos
               for letra1 in letras
               for letra2 in letras
               for letra3 in letras
               for especial in especiales]

    return codigos

codigos = generar_codigos()
print(codigos)

tamanio_lista = len(codigos)

print("Tamaño de la lista de códigos:", tamanio_lista)

