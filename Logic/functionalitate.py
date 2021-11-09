from Domain.Librarie import getId, creeazaLibrarie, getGen, getTitlu, getPret, getReducere
from Logic.CRUD import adaugaLibrarie, getById, modificaLibrarie, stergeLibrarie


def discount(lista):
    """
    da un discount de 5% respectiv 10% pentru toate cartiile ce au tipul de reducere silver respectiv gold
    :param lista: lista de carti
    :return: lista de carti cu preturile modificate
    h
    """
    listaNoua=[]
    for librarie in lista:
        if getReducere(librarie)=="silver":
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                getGen(librarie),
                getPret(librarie)  - (0.05 * getPret(librarie)),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        elif getReducere(librarie)=="gold":
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                getGen(librarie),
                getPret(librarie) - (0.1 * getPret(librarie)),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua

def modificareGen(numeOriginal, noulGen, lista):
    """
    modifica genul unei carti care are titlul dat
    :param numeOriginal:
    :param noulGen:
    :param lista:
    :return:
    """
    listaNoua = []
    for librarie in lista:
        if numeOriginal == getTitlu(librarie):
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                noulGen ,
                getPret(librarie),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua
def commandConsole(comand,lista):
    list_comand=comand.split(",")
    for x in range(len(list_comand)):
        if list_comand[x] == "add":
            try:
                if getById(list_comand[x+1], lista) is not None:
                 raise ValueError("Id-ul "+list_comand[x+1]+" exista deja")
                lista=adaugaLibrarie(list_comand[x+1], list_comand[x+2], list_comand[x+3], list_comand[x+4], list_comand[x+5], lista)
            except ValueError as ve:
                print("Error: {}".format(ve))
        if list_comand[x] == "show all":
            from UI.console import showAll
            showAll(lista)
        if list_comand[x] == "delete":
            lista=stergeLibrarie(list_comand[x+1], lista)
        if list_comand[x] == "edit":
            try:
                if getById(list_comand[x+1], lista) is None:
                    raise ValueError("Nu exista o librarie cu id-ul "+list_comand[x+1])
                lista=modificaLibrarie(list_comand[x+1], list_comand[x+2], list_comand[x+3], list_comand[x+4], list_comand[x+5], lista)
            except ValueError as ve:
                print("Error: {}" .format(ve))
    return lista
def modificareGen(numeOriginal, numeSchimbat, lista):
    listaNoua = []
    for librarie in lista:
        if getTitlu(librarie) == numeOriginal:
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                numeSchimbat ,
                getPret(librarie),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua
def pretMinim(lista):
    rezultat = {}
    for librarie in lista:
        gen = getGen(librarie)
        pret = getPret(librarie)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen]=pret
        else:
            rezultat[gen]=pret
    return rezultat
def nrTitluriPeGen(lista):
    rezultat = {}
    aux=[]
    for librarie in lista:
        gen = getGen(librarie)
        ok=0
        titlu = getTitlu(librarie)
        for p in aux:
            if titlu == p:
                ok = 1
        aux.append(titlu)
        if gen in rezultat and ok == 0:
            rezultat[gen] = rezultat[gen] + 1
        else:
            rezultat[gen] = 1
    return rezultat

def ordonareDupaPret(lista):
    return sorted(lista, key = lambda librarie: getPret(librarie))