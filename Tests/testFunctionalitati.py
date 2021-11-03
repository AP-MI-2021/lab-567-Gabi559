from Domain.Librarie import getPret, getGen
from Logic.CRUD import getById, adaugaLibrarie
from Logic.functionalitate import discount, modificareGen, commandConsole


def testDiscount():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    lista = discount(lista)

    assert getPret(getById("1", lista)) == 15
    assert getPret(getById("2", lista)) == 19
    assert getPret(getById("3", lista)) == 22.5

def testModificareGen():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    lista = modificareGen("Realism", "Interbelic", lista)

    assert getGen(getById("1", lista)) == "Traditionalism"
    assert getGen(getById("2", lista)) == "Interbelic"
    assert getGen(getById("3", lista)) == "Interbelic"

def testCommandConsole():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)
    lista=commandConsole("add,4,O scrisoare pierduta,Drama,40,none", lista)
    assert len(lista) == 4
    lista = commandConsole("edit,3,O scrisoare pierduta,Drama,40,none", lista)
    assert getGen(getById("3",lista)) == "Drama"
