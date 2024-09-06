# %%

notas = []

for i in range(4):
    n = int(input(f"entre com a nota {i+1}: "))
    notas.append(n)

soma = sum(notas)
print(soma)
# %%