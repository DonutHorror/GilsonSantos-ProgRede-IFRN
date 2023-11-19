import socket, os
PORT = 80

# Função para obter o nome do arquivo a partir da url
def obter_nome_arquivo(url):
    UrlDividida = url.split('/')
    return UrlDividida[-1]

try:
    UrlCompleta = input("Digite a URL completa da imagem: ")

    # Separa o host e a imagem
    UrlPartes = UrlCompleta.split('//')
    UrlHost = UrlPartes[1].split('/')[0]
    UrlImagem = '/' + '/'.join(UrlPartes[1].split('/')[1:])

    Arquivo = obter_nome_arquivo(UrlCompleta)
    # Aqui garante que o final do arquivo não venha sem uma formatação adequada
    if '.' not in Arquivo or Arquivo.split('.')[-1] not in ['png', 'jpg', 'jpeg']:
        Arquivo += '.png'

    # Cria o socket da imagem e faz a requisição
    UrlRequest = f'GET {UrlImagem} HTTP/1.1\r\nHost: {UrlHost}\r\n\r\n'
    SocketImage = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SocketImage.connect((UrlHost, PORT))
    SocketImage.sendall(UrlRequest.encode())

    ContentLenght = None
    Imagem = b''

    while True:
        # Recebe os dados em pedaços de 5120 bytes
        Dados = SocketImage.recv(5120)
        if not Dados:
            break
        Imagem = Imagem + Dados

        # Procura pelo cabeçalho "Content-Length"
        ContentLenghtMatch = Imagem.split(b'Content-Length:')
        if len(ContentLenghtMatch) > 1:
            ContentLenght = int(ContentLenghtMatch[1].split()[0])

        # Verifica se todos os dados foram recebidos
        if ContentLenght is not None and len(Imagem) >= ContentLenght:
            break
    SocketImage.close()
    print(f'\nTamanho da Imagem: {ContentLenght} bytes')

    # Separa os cabeçalhos e os dados da imagem
    Delimiter = '\r\n\r\n'.encode()
    Position = Imagem.find(Delimiter)
    Headers = Imagem[:Position]
    DadosBin = Imagem[Position + 4:]

    # Salva a imagem no arquivo
    OutputArquivo = open(Arquivo, 'wb')
    OutputArquivo.write(DadosBin)
    OutputArquivo.close()
except ConnectionError:
    print("Erro de conexão.")
except TimeoutError:
    print("Tempo de espera excedido.")
except Exception as error:
    print(f"Ocorreu um erro inesperado: {error}")

