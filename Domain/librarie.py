def creeaza_librarie(id,titlu_carte,gen_carte,pret,tip_reducere):
    """
    :param id: int
    :param titlu_carte: string
    :param gen_carte:string
    :param pret:float
    :param tip_reducere: int
    :return: un dictionar cu id,titlu_carte,gen_carte,pret,tip_reducere
    """
    return {
    "id":id,
    "titlu_carte":titlu_carte,
    "gen_carte":gen_carte,
    "pret":pret,
    "tip_reducere":tip_reducere
    }
def get_id(librarie):
    return librarie["id"]
def get_titlu_carte(librarie):
    return librarie["titlu_carte"]
def get_gen_carte(librarie):
    return librarie["gen_carte"]
def get_pret(librarie):
    return librarie["pret"]
def get_tip_reducere(librarie):
    return librarie["tip_reducere"]
