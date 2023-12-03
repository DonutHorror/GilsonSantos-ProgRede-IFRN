import socket
import threading
from socket_constants import *

print('Recebendo Mensagens...\n\n')

# Criando o socket TCP
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
Server.bind((HOST_SERVER, SOCKET_PORT))

# Máximo de conexões enfileiradas
Server.listen(MAX_LISTEN)

# Lista de clientes e nomes de usuario
Clients = []
Usernames = []

# Função de broadcast
def Broadcast(Message):
   for client in Clients:
      client.send(Message)
   
# Função para lidar com as mensagens do cliente
def HandleClient(client, BUFFER_SIZE, CODE_PAGE):
   while True:
      # Recebe a mensagem do cliente e depois envia ela em broadcast para todos os usuarios conectados
      try:
         message = client.recv(BUFFER_SIZE)
         Broadcast(message)
      # Fecha a Thread e remove o client e seu usuario das listas do server
      except:
         index = Clients.index(client)
         Clients.remove(client)
         client.close()
         User = Usernames[index]
         Broadcast(f'{User} se desconectou!'.encode(CODE_PAGE))
         Usernames.remove(User)
         break
      