try:
    import requests
except ModuleNotFoundError:
    print("Erro: O módulo 'requests' não está instalado.")
    print("Instale com: pip install requests")
    exit()

nome = input("Digite o nome ou número do pokemon: ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    
    dados = resposta.json()
    print("Nome:", dados["name"])

except requests.exceptions.HTTPError:
    print("Erro: Pokémon não encontrado.")

except requests.exceptions.ConnectionError:
    print("Erro: Problema de conexão com a internet.")

except requests.exceptions.RequestException:
    print("Erro inesperado na requisição.")

## Instale o módulo requests
## No terminal, execute: pip install requests