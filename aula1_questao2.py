
import random
import math

n = int(input("Digite o valor de n: "))
soma = 0

for _ in range(n):
    valor = random.randint(0, 100)  # número aleatório entre 0 e 100
    soma += valor

raiz = math.sqrt(soma)
print(f"A soma foi {soma} e a raiz quadrada é {raiz:.2f}")
