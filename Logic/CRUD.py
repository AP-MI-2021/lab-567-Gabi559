from Domain.Librarie import creeazaLibrarie, getId


def adaugaLibrarie(id, titlu, gen, pret, reducere, lista):
    """
    adauga o vanzare noua in lista de vanzari
    :param id: id-ul noii carti , int
    :param titlu: titlul noii carti , string
    :param gen: genul noii carti , string
    :param pret: pretul noii carti , float
    :param reducere: reducerea noii carti , string (gold,sliver,none)
    :param lista: lista la care se adauga ,list
    :return:
    """
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    librarie = creeazaLibrarie(id, titlu, gen, pret, reducere)
    return lista + [librarie]

def getById(id, lista):
    for librarie in lista:
        if getId(librarie) == id:
            return librarie
    return None

def stergeLibrarie(id, lista):
    """
    sterge o carte din lista dupa un id dat
    :param id: id-ul cartii care se sterge , int
    :param lista: lista din care se sterge , lista
    :return: lista fara cartea cu id-ul "id"
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista o librarie cu id-ul dat")
    return [librarie for librarie in lista if getId(librarie) != id]

def modificaLibrarie(id, titlu, gen, pret, reducere, lista):
    """
    modifica o carte aleasa
    :param id:id-ul cartii care doriti sa o modificati , int
    :param titlu:noul titlu , string
    :param gen: noul gen , string
    :param pret:noul pret , float
    :param reducere: noul tip de reducere , string (gold,none,silver)
    :param lista: lista cu cartea schimbata
    :return:lista noua
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista o librarie cu id-ul dat")
    listaNoua = []
    for librarie in lista:
        if getId(librarie) == id:
            librarieNoua = creeazaLibrarie(id, titlu, gen, pret, reducere)
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua