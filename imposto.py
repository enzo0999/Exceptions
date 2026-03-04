try:
    preco = float(input("Preço do produto: "))
    imposto = 1.1
    print("Preço com imposto:", preco * imposto)
except ValueError:
    print("Erro: Digite um valor numérico válido para o preço.")