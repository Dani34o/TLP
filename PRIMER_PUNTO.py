def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_hasta_numero(numero):
    return list(filter(es_primo, range(2, numero + 1)))

#Ejemplo
numero_limite = 20
print(f"Números primos hasta {numero_limite}: {primos_hasta_numero(numero_limite)}")
