from Tests.testCRUD import testAdaugaLibrarie, testStergeLibrarie, testModificaLibrarie, testGetById
from Tests.testDomain import testLibrarie
from Tests.testFunctionalitati import testDiscount, testCommandConsole, testModificareGen, testPretMinim, \
    testOrdonareDupaPret, testNrTitluriPeGen
from Tests.testUndoRedo import test_undo_redo


def runAllTests():
    testLibrarie()
    testAdaugaLibrarie()
    testStergeLibrarie()
    testModificaLibrarie()
    testGetById()
    testDiscount()
    testCommandConsole()
    test_undo_redo()
    testModificareGen()
    testPretMinim()
    testOrdonareDupaPret()
    testNrTitluriPeGen()
    test_undo_redo()