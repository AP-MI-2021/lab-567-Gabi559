from Domain.Librarie import getId, creeazaLibrarie, getGen, getTitlu, getPret, getReducere

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
    :param numeSchimbat:
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