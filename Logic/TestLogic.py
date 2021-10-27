from Logic.CRUD import add_librarie, stergere_librarie


def test_add_librarie():
    lista = []
    assert add_librarie(1, "TREI IEZI", "poveste", 2.5, "silver", lista)


def test_stergere_librarie():
    lista = []
    add_librarie(1, "TREI IEZI", "poveste", 2.5, "silver", lista)
    add_librarie(2, "PATRU IEZI", "poveste", 3.5, "silver", lista)
    stergere_librarie(1, lista)
    assert len(lista) == 1


def test_logic():
    test_stergere_librarie()
    test_add_librarie()