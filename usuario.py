pessoa = {"nome": "João", "idade": 20}

try:
    chave = input("Qual campo quer ver? ")
    print(pessoa[chave])

except KeyError:
    print("Erro: Campo não encontrado. Use 'nome' ou 'idade'.")