import socket
import threading
from socket_constants import *

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
def HandleClient(client):
   while True:
      # Recebe a mensagem do cliente e depois envia ela em broadcast para todos os usuarios conectados
      try:
         message = client.recv(512)
         Broadcast(message)
      # Fecha a Thread e remove o client e seu usuario das listas do server
      except:
         index = Clients.index(client)
         Clients.remove(client)
         client.close()
         User = Usernames[index]
         Broadcast(f'{User} se desconectou!'.encode('utf-8'))
         Usernames.remove(User)
         break

# Função principal para lidar com conexão de novos clientes e criação de threads
def ReceiveConnection():
   while True:
      print('Recebendo Mensagens...\n\n')
      client, address = Server.accept()
      print(f'Conexão com sucesso com {str(address)}')
      client.send('Username?'.encode('utf-8'))
      User = client.recv(512)
      Usernames.append(User)
      Clients.append(client)
      print(f'O username desse cliente é {User}'.encode('utf-8'))
      Broadcast(f'{User} entrou no server!'.encode('utf-8')) 
      client.send('Você está conectado!'.encode('utf-8'))
      thread = threading.Thread(target=HandleClient, args=(client))
      thread.start()
      
ReceiveConnection()