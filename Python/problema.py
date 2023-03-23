#REALICE UN PROGRAMA QUE LLENE UNA MATRIZ 2*2 Y UTILIZANDO UNA FUNCIÓN RETORNE QUE POCENTAJE DE NUMEROS PRIMOS ESTA CONTIENE.#

import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_percentage(matrix):
    count_primes = 0
    for row in matrix:
        for num in row:
            if is_prime(num):
                count_primes += 1
    return (count_primes / 4) * 100

# Llenar matriz 2x2 con números aleatorios
matrix = [[random.randint(1, 100) for j in range(2)] for i in range(2)]
print(matrix)

# Calcular porcentaje de números primos en la matriz
percentage = prime_percentage(matrix)
print(f"La matriz contiene {percentage}% de números primos.")

