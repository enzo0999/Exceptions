nome_arquivo = input("Arquivo: ")
try:
    f = open(nome_arquivo, "r", encoding="utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Arquivo não encontrado")
