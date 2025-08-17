n = int(input())  # linhas
m = int(input())  # colunas

# Cabeçalho
print("  ", end="")
for col in range(1, m + 1):
    print(col, end=" ")
print()

# Linhas do tabuleiro
for linha in range(1, n + 1):
    print(linha, end=" ")
    for _ in range(m):
        print("/", end=" ")
    print()
