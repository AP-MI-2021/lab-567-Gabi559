from Domain.Librarie import toString
from Logic.CRUD import adaugaLibrarie, stergeLibrarie, modificaLibrarie
from Logic.functionalitate import discount, modificareGen, commandConsole


def printMenu():
    print("1. Adaugare carte")
    print("2. Stergere carte")
    print("3. Modificare carte")
    print("4. Reduceri silver si gold")
    print("5. Inlocuire gen")
    print("a. Afisare carti")
    print("c.Command console")
    print("x. Iesire")


def uiAdaugaLibrarie(lista):
    try:
        id = input("Dati id-ul: ")
        titlu = input("Dati titlul: ")
        gen = input("Dati genul: ")
        pret = float(input('Dati pretul: '))
        reducere = input("Dati tipul de reducere: ")
        return adaugaLibrarie(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeLibrarie(lista):
    try:
        id = input("Dati id-ul cartii de sters: ")
        return stergeLibrarie(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaLibrarie(lista):
    try:
        id = input("Dati id-ul cartii de modificat: ")
        titlu = input("Dati noul titlu: ")
        gen = input("Dati noul gen: ")
        pret = float(input('Dati noul pret: '))
        reducere =input("Dati noul tip de reducere: ")
        return modificaLibrarie(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiDiscount(lista):
    return discount(lista)

def uiModificareGen(lista):
    numeOriginal=input("Dati titlul operei al carei gen se va modifica: ")
    numeSchimbat=input("Dati genul cu care se va inlocui: ")
    return modificareGen(numeOriginal, numeSchimbat, lista)

def showAll(lista):
    for librarie in lista:
        print(toString(librarie))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaLibrarie(lista)
        elif optiune == "2":
            lista = uiStergeLibrarie(lista)
        elif optiune == "3":
            lista = uiModificaLibrarie(lista)
        elif optiune == "4":
            lista = uiDiscount(lista)
        elif optiune == "5":
            lista = uiModificareGen(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "c":
            uiCommandConsole()
            command=input("Dati comenzile despartite prin , :")
            lista=commandConsole(command,lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
def uiCommandConsole():
    print("Ati intrat in consola de tip command line")
    print("Comenzile suportate la momentul actual sunt : add , show all , edit")
