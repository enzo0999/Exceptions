try:
    qtd = int(input("Quantas notas? "))
except ValueError:
    print("Erro: Digite um número inteiro válido.")
else:
    if qtd <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
    else:
        soma = 0
        for _ in range(qtd):
            try:
                soma += float(input("Nota: "))
            except ValueError:
                print("Erro: Digite uma nota válida.")
                break
        else:
            media = soma / qtd
            print("Média:", media)