import random, os

AppDir = os.path.dirname(os.path.abspath(__file__))

def gerar_lista(Quantidade, ValorMinimo, ValorMaximo):
    Lista = []
    for i in range(0,Quantidade):
         Lista.append(random.randint(ValorMinimo, ValorMaximo))  
    return True, Lista

def salvar_lista(NomeLista, NomeArquivo):
    with open(f'{AppDir}/{NomeArquivo}.txt', 'w') as Arquivo:
        for Numero in NomeLista:
            Arquivo.write(str(Numero) + "\n")
    Arquivo.close() 
    return True

def main():
    Quantidade = int(input("Quantidade de valores: "))
    ValorMinimo = int(input("Valor mínimo: "))
    ValorMaximo = int(input("Valor máximo: "))

    try:
        gerado, lista = gerar_lista(Quantidade, ValorMinimo, ValorMaximo)
    except ValueError:
        print("Um dos valores informados não é um inteiro válido.")
        return

    if not gerado:
        print("Não foi possível gerar a lista.")
        return

    NomeArquivo = str(input("Nome do Arquivo: "))
    if salvar_lista(lista, NomeArquivo):
        print("A lista foi salva com sucesso.")
    else:
        print("Não foi possível salvar a lista.")

main()

