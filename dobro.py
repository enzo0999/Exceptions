def dobro(x):
    return float(x) * 2

valor = input("Digite um número: ")
if valor == "":
    valor = None

try:
    print(dobro(valor))
except ValueError:
    print("Valor inválido, informe um número")