def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generador_primos_hasta_numero(numero):
    for i in range(2, numero + 1):
        if es_primo(i):
            yield i

# Ejemplo
limite = 20
print(f"Números primos hasta {limite}: {list(generador_primos_hasta_numero(limite))}")
