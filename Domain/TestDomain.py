from Domain.librarie import creeaza_librarie, get_id,get_titlu_carte,get_gen_carte,get_pret,get_tip_reducere
from Logic.CRUD import get_by_id


def test_creeaza_librarie():
    assert creeaza_librarie(2, "Amintiri din copilarie", "aventura", 1.2, "None") ==[ 2,'Amintiri din copilarie','aventura', 1.2, 'None']
def test_get_id():
    librarie=creeaza_librarie(2, "Amintiri din copilarie", "aventura", 1.2, "None")
    lista=[librarie]
    assert get_id(get_by_id(lista,2))==2
def test_get_titlu_carte():
    librarie = creeaza_librarie(2, "Amintiri din copilarie", "aventura", 1.2, "None")
    lista=[librarie]
    assert get_titlu_carte(get_by_id(lista,2)) == "Amintiri din copilarie"
def test_get_gen_carte():
    librarie = creeaza_librarie(2, "Amintiri din copilarie", "aventura", 1.2, "None")
    lista=[librarie]
    assert get_gen_carte(get_by_id(lista,2)) == "aventura"
def test_get_pret():
    librarie = creeaza_librarie(2, "Amintiri din copilarie", "aventura", 1.2, "None")
    lista=[librarie]
    assert get_pret(get_by_id(lista,2)) == 1.2
def test_get_tip_reducere():
    librarie = creeaza_librarie(2, "Amintiri din copilarie", "aventura", 1.2, "None")
    lista=[librarie]
    assert get_tip_reducere(get_by_id(lista,2)) == "None"
def test_domain():
    test_creeaza_librarie()
    test_get_tip_reducere()
    test_get_pret()
    test_get_gen_carte()
    test_get_id()
    test_get_titlu_carte()