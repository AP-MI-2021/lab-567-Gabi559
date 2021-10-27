def creeaza_librarie(id, titlu_carte, gen_carte, pret, tip_reducere):
    """
    :param id: int
    :param titlu_carte: string
    :param gen_carte:string
    :param pret:float
    :param tip_reducere: int
    :return: un dictionar cu id,titlu_carte,gen_carte,pret,tip_reducere
    """
    return [
        id,
        titlu_carte,
        gen_carte,
        pret,
        tip_reducere
    ]


def get_id(librarie):
    return librarie[0]


def get_titlu_carte(librarie):
    return librarie[1]


def get_gen_carte(librarie):
    return librarie[2]


def get_pret(librarie):
    return librarie[3]


def get_tip_reducere(librarie):
    return librarie[4]
