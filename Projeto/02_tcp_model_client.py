import socket, os, time, threading 
from socket_constants import *

# Valores
ONLINE = False
SERVER = HOST_SERVER, SOCKET_PORT

def GetHostInfo():
    HostName = socket.gethostname()
    HostIp = socket.gethostbyname(HostName)
    HostLogin = os.getlogin()
    HostInfo = HostName, HostIp, HostLogin
    return HostInfo

def HostTryConnection(SERVER):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            tcp_socket.connect((SERVER))
        except ConnectionRefusedError:
            print(f"Server Offline... Tentando reconexão em 10 segundos...")
            time.sleep(10)
            continue            
        else:
            print("Server Online... Conexão com sucesso...")
            time.sleep(5)
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    
def HostMessageSend(CODE_PAGE):
    Message = input("Digite uma mensagem: ")
    if Message == "!EXIT": exit()
    try: 
        Message = Message.encode(CODE_PAGE)
        tcp_socket.send(Message)
        os.system('cls' if os.name == 'nt' else 'clear')
    except socket.error as message:
        print("A mensagem não pode ser enviada. Tente denovo ou termine a conexão...")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

HostInf = GetHostInfo()    
# Ligar 
while True:
    State = input("Conectarse ao servidor? [YES/NO]\n").upper()
    if State == "YES": break
    if State ==  "NO": exit()
    continue
ONLINE = True

# Cria um socket e uma Thread para tentar se conectar com o servidor
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ConnectionThread = threading.Thread(target = HostTryConnection, args = [(SERVER)], daemon= True).start()

# Maneira EXTREMAMENTE INEFICIENTE de checar se a conexão foi estavalecida já que eu não sei como threads retornam valores
while True:
    try:
        Ping = "Ping"
        Ping = Ping.encode(CODE_PAGE)
        tcp_socket.send(Ping)  
        break
    except:   
        time.sleep(10)
        continue

while True:
    print("Digite [!EXIT] para terminar a conexão")
    HostMessageSend(CODE_PAGE)




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