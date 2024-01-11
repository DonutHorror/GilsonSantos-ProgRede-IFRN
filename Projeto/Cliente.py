import threading, os, socket, platform

SERVER = 'localhost'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '

def client_conn():
    
    try:
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER, PORT))
        
        print('Conectado com sucesso!')
    except:
        print('Não foi possivel se conectar ao servidor')
        client.close()
        exit()
    
def cliente_info():
    
    USERNAME = input('Insira o nome de usuário: ')
    HOST    = socket.gethostname()
    LOGIN = os.getlogin()
    SO = platform.system()
    IP      = socket.gethostbyname(HOST)
    UserInfo = (f'{USERNAME},{HOST},{LOGIN},{SO},{IP}')
    UserInfo = UserInfo.encode('utf-8')
    try:
        client.send(UserInfo)
    except OSError:
        print('Erro ao enviar informações de usuário para o servidor')
        client.close()
        exit()

def servInteraction():
    msg = b' '
    while msg != b'':
        try:
            msg = client.recv(512)
            print ("\n"+msg.decode('utf-8')+"\n"+PROMPT)
        except:
            msg = b''
    client.close()

def userInteraction():
    msg = ''
    while msg != '!q':
        try:
            msg = input(PROMPT)
            if msg != '': client.send(msg.encode('utf-8'))
        except:
            msg = '!q'
    client.close()

def main():
    
    print('Iniciando o programa...')
   
    # Cliente tenta se conectar com o servidor
    client_conn()
    
    # Cliente tenta enviar informações para o servidor
    cliente_info()
    
    # Thread para o cliente ficar constantemente checando a conexão com o servidor
    tuser = threading.Thread(target=userInteraction, daemon=True)
    tserv = threading.Thread(target=servInteraction, daemon=True)
    
    tserv.start()
    tuser.start()
    
    tuser.join()
    tuser.join()
    
if __name__ == "__main__":
    main()