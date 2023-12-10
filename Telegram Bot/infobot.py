import requests, time

while True:
    token = "6783809632:AAGbxDBhNSr6hGAl3l3PGNNHXmpWMu9LlRs"
    strURL = f"https://api.telegram.org/bot{token}/getUpdates"
    resultado = requests.get(strURL)
    print(resultado.json())
    time.sleep(10)