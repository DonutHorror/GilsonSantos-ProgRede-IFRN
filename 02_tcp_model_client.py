import threading
import socket
from socket_constants import *
User = input('Escolha um Username >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_SERVER, SOCKET_PORT))


def client_receive(BUFFER_SIZE, CODE_PAGE):
    while True:
        try:
            message = client.recv(BUFFER_SIZE).decode(CODE_PAGE)
            if message == "Username?":
                client.send(User.encode(CODE_PAGE))
            else:
                print(message)
        except:
            print('Erro!')
            client.close()
            break


def client_send():
    while True:
        message = f'{User}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive, args=(BUFFER_SIZE, CODE_PAGE))
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()


