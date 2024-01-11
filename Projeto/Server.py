import socket, threading

SERVER = '0.0.0.0'
PORT = 5678
clientes = {}
socklist = []

def clientmsg(sockConn, addr, user):
    
    msg = b''
    while msg != b'!q':
        try:    
            msg = sockConn.recv(512)
            broadCast(msg, addr, user)
        except:
            msg = b'!q'
    
    socklist.remove ((sockConn, addr))
    clientes.pop(user)
    
    print(f'{addr}: {user} se desconectou.')
    sockConn.close()

def broadCast(msg, addrSource, user):
    msg = f"{addrSource} {user} -> {msg.decode('utf-8')}"
    print (msg)
    for sockConn, addr in socklist:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))

def client_conn(sockConn, addr):
    
    Info = sockConn.recv(512).decode('utf-8')
    Info = Info + f',{addr[1]}'
    Info = Info.split(',')
    
    clientes.update({Info[0]: Info[1:]})
    socklist.append((sockConn, addr))
    
    print(f'{addr}: {Info[0]} se conectou.')
    
    threading.Thread(target=clientmsg, args=(sockConn, addr, Info[0]), daemon=True).start()
 
def client_listen():
    
    while True:   
        sockConn, addr = sock.accept()
        
        print ("Connection from: ", addr)        
        threading.Thread(target=client_conn, args=(sockConn, addr)).start()

def main():
    
    try:
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((SERVER, PORT)) 
        
        print ("Listening in: ", (SERVER, PORT))
        sock.listen(5)       
    except Exception as e:
        print ("Fail: ", e)
    
    threading.Thread(target=client_listen, daemon=True).start()
    
    while True:
        input()
    


if __name__ == "__main__":
    main()