from Logic.CRUD import adaugaLibrarie
from Tests.testAll import runAllTests
from UI.console import runMenu

def main():
    runAllTests()
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)
    runMenu(lista)

if __name__ == '__main__':
    main()