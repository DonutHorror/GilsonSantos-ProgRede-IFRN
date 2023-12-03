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

def ReceiveConnection(CODE_PAGE):
   while True:
      print('Recebendo Mensagens...\n\n')
      client, address = Server.accept()
      print(f'Conexão com sucesso com {str(address)}')
      client.send('Username?'.encode(CODE_PAGE))
      User = client.recv(1024)
      Usernames.append(User)
      Clients.append(client)
      print(f'O username desse cliente é {User}'.encode(CODE_PAGE))
      Broadcast(f'{User} entrou no server!'.encode(CODE_PAGE))
      client.send('Você está conectado!'.encode(CODE_PAGE))
      thread = threading.Thread(target=HandleClient, args=(client,))
      thread.start()
      
