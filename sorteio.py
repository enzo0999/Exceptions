nomes = ["Arthur", "Gabriel", "Enzo", "Julia"]

try:
    i = int(input("Indique um número para sortear uma pessoa? "))
    print("Nome:", nomes[i])

except ValueError:
    print("Erro: Digite um número inteiro válido.")

except IndexError:
    print("Erro: Número fora da faixa permitida (0 a 3).")