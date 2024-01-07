import socket, sys
PORT = 80

def nome_url(url):
    url_partes = url.split('/')
    return url_partes[-1]

try:
    Url = input('digite a URL da Imagem: ')

    UrlDiv = Url.split('//')
    UrlHost = UrlDiv[1].split('/')[0]
    UrlImagem = '/' + '/'.join(UrlDiv[1].split('/')[1:])
    FileName = nome_url(Url)
    print (f'{FileName}')
    
    UrlRequest = f'GET {UrlImagem} HTTP/1.1\r\nHost: {UrlHost}\r\n\r\n'
    ImgSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); ImgSock.connect((UrlHost, PORT))
    ImgSock.sendall(UrlRequest.encode())

    ContLen = None
    Imagem = b''
 
    if '.' not in FileName or FileName.split('.')[-1] not in ['png', 'jpg', 'jpeg']:
        FileName += '.png'

    while True:
        Dados = ImgSock.recv(5120)
        if not Dados: break
        Imagem += Dados
        ContLenSearch = Imagem.split(b'Content-Length:')
        if len(ContLenSearch) > 1:
            ContLen = int(ContLenSearch[1].split()[0])
        if len(Imagem) >= ContLen and ContLen is not None: break

    ImgSock.close()
    print(f'\n a Imagem possui {ContLen} bytes')

    delimiter = '\r\n\r\n'.encode();    
    position = Imagem.find(delimiter)
    headers = Imagem[:position];        
    Dadosbin = Imagem[position + 4:]

    file_output = open(FileName, 'wb')
    file_output.write(Dadosbin); file_output.close()

except TimeoutError: print('O tempo de espera foi excedido')
except ConnectionError: print('Erro ao conectar')
except Exception as erro: print(f'ERRO . . . {sys.exc_info()[0]}')