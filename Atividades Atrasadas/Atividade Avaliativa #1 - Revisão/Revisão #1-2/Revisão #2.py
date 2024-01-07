import os

AppDir = os.path.dirname(os.path.abspath(__file__))

def ler_arquivo(NomeArquivo):
    try:
        with open(f"{AppDir}/{NomeArquivo}", "r") as Arquivo:
            Lista = []
            for linha in Arquivo:
                Valor = int(linha)
                Lista.append(Valor)
        return True, Lista
    except FileNotFoundError:
        return False, None

def ordena_lista(NomeLista, Metodo):
    if Metodo == "BUBBLE":
        Check, ListaOrdenada = ordena_bubble(NomeLista)
    elif Metodo == "INSERTION":
        Check, ListaOrdenada = ordena_insertion(NomeLista)
    elif Metodo == "SELECTION":
        Check, ListaOrdenada = ordena_selection(NomeLista)
    elif Metodo == "QUICK":
        Check, ListaOrdenada = ordena_quick(NomeLista)
    else:
        print("Método de ordenação inválido.")
        return False, None
    return Check, ListaOrdenada

def ordena_bubble(NomeLista):
    Lista = NomeLista
    Check = False
    for i in range(len(Lista) - 1):
        for j in range(len(Lista) - 1 - i):
            if Lista[j] > Lista[j + 1]:
                Lista[j], Lista[j + 1] = Lista[j + 1], Lista[j]
                Check = True
    return Check, Lista

def ordena_insertion(NomeLista):
    Lista = NomeLista
    Check = False
    for i in range(1, len(Lista)):
        Valor = Lista[i]
        j = i - 1
        while j >= 0 and Lista[j] > Valor:
            Lista[j + 1] = Lista[j]
            j -= 1
        Lista[j + 1] = Valor
        Check = True
    return Check, Lista

def ordena_selection(NomeLista):
    Lista = NomeLista
    Check = False
    for i in range(len(Lista)):
        MinIndice = i
        for j in range(i + 1, len(Lista)):
            if Lista[j] < Lista[MinIndice]:
                MinIndice = j
        Lista[i], Lista[MinIndice] = Lista[MinIndice], Lista[i]
        Check = True
    return Check, Lista

def ordena_quick(NomeLista):
    Lista = NomeLista
    Check = False
    if len(Lista) <= 1:
        return True, Lista
    Pivo = Lista[len(Lista) // 2]
    Menores = []
    Maiores = []
    for Valor in Lista:
        if Valor < Pivo:
            Menores.append(Valor)
        elif Valor > Pivo:
            Maiores.append(Valor)
    Check, MenoresOrdenada = ordena_quick(Menores)
    Check, MaioresOrdenada = ordena_quick(Maiores)
    return Check, MenoresOrdenada + [Pivo] + MaioresOrdenada

def main():
    NomeArquivo = input("Nome do arquivo: ")

    try:
        Check, Lista = ler_arquivo(NomeArquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    if not Check:
        print("Não foi possível ler o arquivo.")
        return

    print("Lista lida:", Lista)
    print("Escolha um metodo: [BUBBLE, INSERTION, SELECTION e QUICK]")
    Metodo = input("Método de ordenação: ").upper()

    Check, ListaOrdenada = ordena_lista(Lista, Metodo)

    if Check:
        print("Lista ordenada:", ListaOrdenada)
    else:
        print("Não foi possível ordenar a Lista.")

main()