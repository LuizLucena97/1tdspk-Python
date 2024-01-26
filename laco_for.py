# laço enquanto - while
'''
n = 1
soma = 0

while n != 0:
    n = int(input("Digite um numero: "))
    soma = soma + n

print(f"Soma = {soma}")
'''

# laço Repita - while True
'''
soma = 0

while True:
    n = int(input("Digite um numero: "))
    soma = soma + n
    if n == 0:
        break

print(f"Soma = {soma}")
'''


# for volta in range(10, 1 - 1, -1):
#     print(volta, ' ', end = '')
'''
soma = 0
for volta in range(1, 5 + 1, 1):
    n = int(input(f"Digite o {volta}.o um numero: "))
    soma = soma + n

print(f"Soma = {soma}")

soma = 0
volta = 1
while volta <= 5:
    n = int(input(f"Digite o {volta}.o um numero: "))
    soma = soma + n
    volta = volta + 1

print(f"Soma = {soma}")
'''

# 1. Dados 10 numeros pelo usuário, exibir quantos são pares e quantos sao impares
'''
qtd_par = qtd_impar = 0

for volta in range(1, 11, 1):
    # ler os 10 numero (sim)
    num = float(input("Numero: "))
    # verificar e contar os pares e impares (sim)
    if num % 2 == 0:
        qtd_par = qtd_par + 1
    else:
        qtd_impar = qtd_impar + 1

# exibir as quantidades (nao)
print(f"""
    Pares {qtd_par}
    Impares {qtd_impar}
""")
'''


# 2. Dados  numeros pelo usuário, exibir quantos são positivos e quantos sao negativos
# a condicao de saida será digitar zero

qtd_positivo = qtd_negativo = 0

while True:
    num = float(input("Numero: "))
    # verificar e contar os pares e impares (sim)
    if num > 0:
        qtd_positivo = qtd_positivo + 1
    elif num < 0:
        qtd_negativo = qtd_negativo + 1
    else:
        break
print(f"""
    Positivo {qtd_positivo}
    Negativo {qtd_negativo}
""")




