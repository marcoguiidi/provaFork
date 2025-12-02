liste = {
    "animali": ["cane", "gatto", "elefante", "leone", "tigre", "orso"],
    "persone": ["giacomo", "mario", "luigi", "anna", "maria", "francesca", "giorgio"]
}

print("Benvenuto nel programma di gestione delle liste!")

choice = input("\n1 - Visualizza le liste \n"
    "2 - Aggiungi un elemento a una lista \n"
    "3 - Cerca un elemento in una lista \n"
    "4 - Aggiungi una lista \n"
    "5 - Rimuovi un elemento da una lista \n"
    "q - Esci\n"
    "Scegli un'opzione: ").lower().strip()

while choice != "q":
    if choice == "1":
        for key, value in liste.items():
            print(f"\nLista di {key}:")
            for item in value:
                print(f"- {item}")
    elif choice == "2":
        avaiable_options = list(liste.keys()) + ["e"]
        list_choice = input(f"A quale lista vuoi aggiungere un elemento? ({', '.join(avaiable_options)} - indietro ): ").strip().lower()
        while list_choice not in avaiable_options:
            list_choice = input(f"A quale lista vuoi aggiungere un elemento? ({', '.join(avaiable_options)} - Indietro): ").strip().lower()
        if list_choice != "e":
            new_element = input("Inserisci l'elemento da aggiungere: ").strip().lower()
            if new_element in liste[list_choice]:
                    print(f"{new_element} è già presente nella lista {list_choice}.")
            else:
                liste[list_choice].append(new_element)
                print(f"{new_element} è stato aggiunto alla lista {list_choice}.")
    elif choice == "3":
        search_el = input("Inserisci il nome dell'elemento da cercare: ").strip().lower()
        found = False
        for key, value in liste.items():
            if search_el in value:
                print(f"{search_el} è presente nella lista {key}.")
                found = True

        if not found:
            print(f"{search_el} non è presente in nessuna delle liste.")
    elif choice == "4":
        new_list = input("Inserisci il nome della nuova lista: ").strip().lower()
        if new_list in liste:
            print(f"La lista {new_list} esiste già.")
        else:
            liste[new_list] = []
            print(f"La lista {new_list} è stata creata.")
    elif choice == "5":
        avaiable_options = list(liste.keys()) + ["e"]
        list_choice = input(f"Da quale lista vuoi rimuovere un elemento? ({', '.join(avaiable_options)} - indietro ): ").strip().lower()
        while list_choice not in avaiable_options:
            list_choice = input(f"Da quale lista vuoi rimuovere un elemento? ({', '.join(avaiable_options)} - Indietro): ").strip().lower()
        if list_choice != "e":
            print(f"Elementi nella lista {list_choice}: {', '.join(liste[list_choice])}")
            rem_element = input("Inserisci l'elemento da rimuovere: ").strip().lower()
            if rem_element in liste[list_choice]:
                liste[list_choice].remove(rem_element)
                print(f"{rem_element} è stato rimosso dalla lista {list_choice}.")
            else:
                print(f"{rem_element} non è presente nella lista {list_choice}.")
    else:
        print("Opzione non valida. Riprova.")

    choice = input("\n1 - Visualizza le liste \n"
    "2 - Aggiungi un elemento a una lista \n"
    "3 - Cerca un elemento in una lista \n"
    "4 - Aggiungi una lista \n"
    "5 - Rimuovi un elemento da una lista \n"
    "q - Esci\n"
    "Scegli un'opzione: ").lower().strip()


print("Programma terminato.")
