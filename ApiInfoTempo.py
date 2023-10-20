import requests
import json

cidade = str(input("Digite a sua cidade: "))
chaveAPI = 'Sua chave API'
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chaveAPI}"

requisicao = requests.get(link)

requisicao = requisicao.json()

nomeCidade = requisicao['name']

paisCidade = requisicao['sys']['country']

pressaoCidade = requisicao['main']['pressure']

temperaturaCidade = requisicao['main']['temp'] - 273

umidadeCidade = requisicao['main']['humidity']

velocidadeVentoCidade = requisicao['wind']['speed'] * 1.609

print(f"\nCidade: {nomeCidade}\nPaís: {paisCidade}\nTemperatura: {temperaturaCidade:.2f} C°\nUmidade: {umidadeCidade} %\nVelocidade do vento: {velocidadeVentoCidade:.2f} km/h\nPressão: {pressaoCidade} hPA")