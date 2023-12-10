import requests, json
from funcoes import *

token = "6783809632:AAGbxDBhNSr6hGAl3l3PGNNHXmpWMu9LlRs"
strURL = f"https://api.telegram.org/bot{token}/"
update_id = None

while True:
    try:
        atualizacao = pegar_atualizacao(update_id, strURL)
        mensagens = atualizacao["result"]

        for mensagem in mensagens:
            update_id = mensagem['update_id']
            chat_id = mensagem['message']['from']['id']
            comando = mensagem['message']['text']
            resposta = criar_resposta(comando, chat_id)
            requisicao = f"{strURL}sendMessage?chat_id={chat_id}&text={resposta}"
            requests.get(requisicao)

    except OSError:
        print(f"Ocorreu um erro: ", OSError)
