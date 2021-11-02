from Tests.testCRUD import testAdaugaLibrarie, testStergeLibrarie, testModificaLibrarie, testGetById
from Tests.testDomain import testLibrarie
from Tests.testFunctionalitati import testDiscount


def runAllTests():
    testLibrarie()
    testAdaugaLibrarie()
    testStergeLibrarie()
    testModificaLibrarie()
    testGetById()
    testDiscount()