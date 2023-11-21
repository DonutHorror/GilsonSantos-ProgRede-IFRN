import socket, os, time, threading 
from socket_constants import *

# Valores
ONLINE = False
EXITREQUEST = False
SERVER = HOST_SERVER, SOCKET_PORT

def GetHostInfo():
    HostName = socket.gethostname()
    HostIp = socket.gethostbyname(HostName)
    HostLogin = os.getlogin()
    HostInfo = HostName, HostIp, HostLogin
    return HostInfo

def HostTryConnection(SERVER):
    while True:
        try:
            tcp_socket.connect((SERVER))
        except ConnectionRefusedError:
            print(f"Server Offline... Tentando reconexão em 10 segundos...")
            time.sleep(10)
            continue
        else:
            break

def HostMessageSend():
    Message = input("Digite uma mensagem: ")
    try: 
        Message = Message.encode(CODE_PAGE)
        tcp_socket.send(Message)
    except WindowsError:
        pass
    

    

# Ligar 
while True:
    State = input("Conectarse ao servidor? [YES/NO]\n").upper()
    if State == "YES": break
    if State ==  "NO": exit()
    continue
ONLINE = True

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ConnectionThread = threading.Thread(target = HostTryConnection, args = [(SERVER)]).start()

while True:
    HostMessageSend()



'''# Digitando a mensagem a ser enviada
mensagem = input('Digite a mensagem: ')

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

# Convertendo a mensagem digitada de string para bytes
mensagem = mensagem.encode(CODE_PAGE)

# Enviando a mensagem ao servidor      
tcp_socket.send(mensagem)

# Fechando o socket
tcp_socket.close()'''