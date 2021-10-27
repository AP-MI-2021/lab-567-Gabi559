from Domain.librarie import creeaza_librarie, get_id


def add_librarie(id,titlu_carte,gen_carte,pret,tip_reducere,lista):
    """
    adauga librarie in lista de librari
    :param id: id librarie adaugata
    :param titlu_carte: titlul_carte librarie adaugata
    :param gen_carte: gen_carte librarie adaugata
    :param pret: pret librarie adaugata
    :param tip_reducere: tip_redicere librarie adaugata
    :param lista: lista cu librariile
    :return: lista cu noua librarie adaugata
    """
    librarie=creeaza_librarie(id,titlu_carte,gen_carte,pret,tip_reducere)
    lista.append(librarie)
    return lista
def get_by_id(lista,id):
    """

    :param librarie:
    :return:returneaza librarie dupa id
    """
    for librarie in lista:
        if get_id(librarie) == id:
            return librarie
    return None
def stergere_librarie(id,lista):
    lista_noua=[]
    for x in lista:
        if get_id(lista[x]) != id:
            lista_noua.append(lista[x])
    return lista_noua
def modificare_lista(id,lista):
    lista_noua=[]
    for librarie in lista:
        if get_id(librarie) == id:
            librarie_noua=creeaza_librarie(id,titlu_carte,gen_carte,pret,tip_reducere)
            lista_noua.append(librarie_noua)
        else:
            lista_noua.append(librarie)
    return lista_noua
