import os, sys, socket

AppDir = os.path.dirname(os.path.abspath(__file__))
FileCSV = os.path.join(AppDir,"protocolos.csv")

try:
    File = open(FileCSV, "r", encoding="utf-8")
except FileNotFoundError:
    print(f"Erro: O arquivo {FileCSV} não está no diretorio atual.")
    sys.exit(1)
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
    sys.exit(1)

LinhasArq = []

for linha in File:
    Itens = linha.split('", "')
    Linhas = []

    for item in Itens:
        ItensArq = item.strip('"\n')
        Linhas.append(ItensArq)
    LinhasArq.append(Linhas)
File.close()

for porta in LinhasArq: porta[0] = int(porta[0]) 
TCP, UDP, TCPUDP = [], [], []

try:
    strHost = input("Nome do host: ")
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
    sys.exit(1)

try:
    ipHost = socket.gethostbyname(strHost)
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
    sys.exit(1)

for linha in LinhasArq: 
    if linha[1] == "TCP,UDP":
        TCPUDP.append(linha[0])
    elif linha[1] == "TCP":
        TCP.append(linha[0])
    elif linha[1] == "UDP":
        UDP.append(linha[0])

for porta in LinhasArq: 
    port = porta[0]

    try: 
        if port in TCP: 
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: TCP: {porta[2]}/ Status: Responde (Aberta)')
            else:
                print(f'Porta {port}: Protocolo: TCP: {porta[2]}/ Status: Não Responde (Fechada)')

        elif port in TCPUDP:
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: TCP: {porta[2]}/ Status: Responde (Aberta)')
            else:
                print(f'Porta {port}: Protocolo: TCP: {porta[2]}/ Status: Não Responde (Fechada)')

            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: UDP: {porta[2]}/ Status: Responde (Aberta)')
            else:
                print(f'Porta {port}: Protocolo: UDP: {porta[2]}/ Status: Não Responde (Fechada)')

        elif port in UDP:
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: UDP: {porta[2]}/ Status: Responde (Aberta)')
            else:
                print(f'Porta {port}: Protocolo: UDP: {porta[2]}/ Status: Não Responde (Fechada)')

        else: 
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: : {porta[2]}/ Status: Responde (Aberta)')
            else:
                print(f'Porta {port}: Protocolo: : {porta[2]}/ Status: Não Responde (Fechada)')
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    finally:
        sock.close()    