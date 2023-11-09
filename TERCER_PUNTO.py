import time

# Fibonacci Simple
def fibonacci_simple(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Fibonacci Recursivo Cola
def fibonacci_recursivo_cola(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fibonacci_recursivo_cola(n-1, b, a+b)

# Medir el tiempo de ejecución para Fibonacci Simple
inicia_tiempo = time.time()
resultado_simple = fibonacci_simple(30)
fin_tiempo = time.time()
print(f"Tiempo de ejecución para Fibonacci Simple: {fin_tiempo - inicia_tiempo} segundos")
print(f"Fibonacci Simple: {resultado_simple}")

# Medir el tiempo de ejecución para Fibonacci Recursivo Cola
inicia_tiempo = time.time()
resultado_recursivo_cola = fibonacci_recursivo_cola(30)
fin_tiempo = time.time()
print(f"Tiempo de ejecución para Fibonacci Recursivo Cola: {fin_tiempo - inicia_tiempo} segundos")
print(f"Fibonacci Recursivo Cola: {resultado_recursivo_cola}")
