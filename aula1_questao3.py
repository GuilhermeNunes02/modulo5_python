total = 0

print("Digite 10 números positivos:")
for i in range(10):
    num = int(input())
    total += num

media = total / 10
print(f"A média dos valores digitados é {media:.2f}")
