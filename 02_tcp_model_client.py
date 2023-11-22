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

def HostConnection(SERVER):
    while True:
        try:
            tcp_socket.connect((SERVER))
            print("Servidor Online. Conexão com sucesso.")
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                print("Digite [!EXIT] para terminar a conexão")
                Message = HostMessageSend(CODE_PAGE)
                if Message == "!EXIT": 
                    tcp_socket.close()
                    exit()
                continue
        except ConnectionRefusedError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Server Offline... Tentando reconexão em 10 segundos...")
            time.sleep(10)
            continue            
    
def HostMessageSend(CODE_PAGE):
    Message = input("Digite uma mensagem: ")
    if Message == "!EXIT": 
        return Message      
    try: 
        Message = Message.encode(CODE_PAGE)
        tcp_socket.send(Message)
        os.system('cls' if os.name == 'nt' else 'clear')
    except socket.error as message:
        print("A mensagem não pode ser enviada. Tente denovo ou termine a conexão...")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

# Pega informações do HOST
HostInf = GetHostInfo()    

# Ligar 
while True:
    State = input("Conectarse ao servidor? [YES/NO]\n").upper()
    if State == "YES": break
    if State ==  "NO": exit()
    continue

# Cria um socket e uma Thread para tentar se conectar com o servidor
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    HostConnection(SERVER)

# ConnectionThread = threading.Thread(target = HostConnection, args = [(SERVER)], daemon= True).start()


