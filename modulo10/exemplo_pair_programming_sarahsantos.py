import requests


url_api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

resposta = requests.get(url_api)


if resposta.status_code == 200:
    dados = resposta.json()
    print("Conexão estabelecida com sucesso!")
else:
    print(f"Erro na requisição: {resposta.status_code}")
    

cotacao_dolar = dados["USDBRL"]["bid"]
nome_moeda = dados["USDBRL"]["name"]


print(f"Moeda: {nome_moeda}")
print(f"Valor atual de compra: R$ {float(cotacao_dolar):.2f}")