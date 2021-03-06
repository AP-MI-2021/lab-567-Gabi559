def test_undo_redo():
    from Domain.Librarie import getId
    from Logic.CRUD import adaugaLibrarie

    def test_undo_redo():
        # 1. lista goala
        lista = []
        undo_list = []
        redo_list = []

        # 2. se adauga prima librarie
        rezultat = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
        undo_list.append(lista)
        lista = rezultat

        # 3. se adauga a doua librarie
        rezultat = adaugaLibrarie("2", "Ion", "Realism", 25, "silver", lista)
        undo_list.append(lista)
        lista = rezultat

        # 4. se adauga a treia librarie
        rezultat = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 20, "gold", lista)
        undo_list.append(lista)
        lista = rezultat

        # 5. primul undo scoate ultima librarie adaugata
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
        assert getId(lista[1]) == "2"
        assert getId(lista[0]) == "1"

        # 6. inca un undo scoate penultima librarie adaugata
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1
        assert getId(lista[0]) == "1"
        assert undo_list == [[]]

        # 7. inca un undo scoate prima librarie adaugata
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 0
        assert undo_list == []

        # 8. inca un undo care nu face nimic
        if len(undo_list) > 0:
            redo_list.append(lista)
            lista = undo_list
        assert len(lista) == 0
        assert undo_list == []

        # 9. se adauga trei librarii
        rezultat = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
        undo_list.append(lista)
        lista = rezultat
        redo_list.clear()

        rezultat = adaugaLibrarie("2", "Ion", "Realism", 25, "silver", lista)
        undo_list.append(lista)
        lista = rezultat

        rezultat = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 20, "gold", lista)
        undo_list.append(lista)
        lista = rezultat

        assert len(redo_list) == 0
        assert len(undo_list) == 3
        assert len(lista) == 3

        # 10. se face redo (fara sa faca nimic)
        if len(redo_list) > 0:
            undo_list.append(lista)
            lista = redo_list.pop()
        assert len(redo_list) == 0
        assert len(undo_list) == 3
        assert len(lista) == 3

        # 11. se fac 2 undo-uri
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
        assert getId(lista[1]) == "2"
        assert getId(lista[0]) == "1"

        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1
        assert getId(lista[0]) == "1"
        assert undo_list == [[]]

        # 12. se face redo
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(redo_list) == 1
        assert len(undo_list) == 2
        assert len(lista) == 2

        # 13. se face redo
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(redo_list) == 0
        assert len(undo_list) == 3
        assert len(lista) == 3

        # 14. se fac 2 undo-uri
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
        assert getId(lista[1]) == "2"
        assert getId(lista[0]) == "1"

        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1
        assert getId(lista[0]) == "1"
        assert undo_list == [[]]

        # 15. se adauga a patra librarie
        rezultat = adaugaLibrarie("4", "Moara cu noroc", "Fictiune", 25.50, "none", lista)
        undo_list.append(lista)
        lista = rezultat
        redo_list.clear()

        # 16. se face redo (fara sa faca nimic)
        if len(redo_list) > 0:
            undo_list.append(lista)
            lista = redo_list.pop()
        assert len(lista) == 2
        assert len(undo_list) == 2

        # 17. se face undo
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1
        assert len(undo_list) == 1
        assert len(redo_list) == 1

        # 18. se face undo
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 0
        assert len(undo_list) == 0
        assert len(redo_list) == 2

        # 19. se face 2 redo-uri
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(lista) == 1

        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(lista) == 2
        assert len(redo_list) == 0

        # 20. se face ultimul redo, care nu face nimic
        if len(redo_list) > 0:
            undo_list.append(lista)
            lista = redo_list.pop()
        assert len(lista) == 2
        assert len(redo_list) == 0
        assert len(undo_list) == 2
