# UTILIZANDO O SE ENCADEADO - forma raiz
'''
# Dado um número pelo usuário, verificar se ele é positivo, negativo ou nulo

n = int(input("Digite um numero: "))

# Primeiro if
if n > 0:
    # lado verdade do primeiro if
    print("Positivo")
else:
    #lado falso do primeiro if
    # Segundo if
    if n < 0:
        # lado verdade do segundo if
        print("Negativo")
    else:
        # lado falso do segundo if
        print("Nulo")
'''

# UTILIZANDO O SE ENCADEADO - forma utilizando o elif
# Dado um número pelo usuário, verificar se ele é positivo, negativo ou nulo
'''
n = int(input("Digite um numero: "))

if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Nulo")
'''

# EXEMPLO DE MENU
nome = "Maria"
print(f"""
    1 - Cadastro
    2 - Consula
    3 - Aleração
    4 - Exclusao
    0 - sair
    
    Bom dia {nome}
""")

opcao = int(input("Digite uma opção: "))

if opcao == 1:
    print("Executando o cadastro...")
elif opcao == 2:
    print("Executando a consulta...")
elif opcao == 3:
    print("Executando a alteração...")
elif opcao == 4:
    print("Executando a exclusao...")
elif opcao == 0:
    print("Obrigado por utilizar nosso sistema...")
else:
    print("ERRO! Digite um valor entre 0 e 4")