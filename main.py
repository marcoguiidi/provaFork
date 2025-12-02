liste = {
    "animali": ["cane", "gatto", "elefante", "leone", "tigre", "orso"],
    "persone": ["giacomo", "mario", "luigi", "anna", "maria", "francesca", "giorgio"]
}

print("Welcome to List Manager!")

choice = input("\n1 - Visualize lists \n"
    "2 - Add an element to a list \n"
    "3 - Search for an element in a list \n"
    "4 - Add a list \n"
    "5 - Remove an element from a list \n"
    "q - Exit\n"
    "Choose an option: ").lower().strip()

while choice != "q":
    if choice == "1":
        for key, value in liste.items():
            print(f"\nList of {key}:")
            for item in value:
                print(f"- {item}")
    elif choice == "2":
        avaiable_options = list(liste.keys()) + ["e"]
        list_choice = input(f"Which list do you want to add an element to? ({', '.join(avaiable_options)} - back ): ").strip().lower()
        while list_choice not in avaiable_options:
            list_choice = input(f"Which list do you want to add an element to? ({', '.join(avaiable_options)} - back): ").strip().lower()
        if list_choice != "e":
            new_element = input("Enter the element to add: ").strip().lower()
            if new_element in liste[list_choice]:
                    print(f"{new_element} is already in the list {list_choice}.")
            else:
                liste[list_choice].append(new_element)
                print(f"{new_element} has been added to the list {list_choice}.")
    elif choice == "3":
        search_el = input("Enter the name of the element to search for: ").strip().lower()
        found = False
        for key, value in liste.items():
            if search_el in value:
                print(f"{search_el} is present in the list {key}.")
                found = True

        if not found:
            print(f"{search_el} is not present in any of the lists.")
    elif choice == "4":
        new_list = input("Enter the name of the new list: ").strip().lower()
        if new_list in liste:
            print(f"The list {new_list} already exists.")
        else:
            liste[new_list] = []
            print(f"The list {new_list} has been created.")
    elif choice == "5":
        avaiable_options = list(liste.keys()) + ["e"]
        list_choice = input(f"From which list do you want to remove an element? ({', '.join(avaiable_options)} - back ): ").strip().lower()
        while list_choice not in avaiable_options:
            list_choice = input(f"From which list do you want to remove an element? ({', '.join(avaiable_options)} - back): ").strip().lower()
        if list_choice != "e":
            print(f"Elements in the list {list_choice}: {', '.join(liste[list_choice])}")
            rem_element = input("Enter the element to remove: ").strip().lower()
            if rem_element in liste[list_choice]:
                liste[list_choice].remove(rem_element)
                print(f"{rem_element} has been removed from the list {list_choice}.")
            else:
                print(f"{rem_element} is not present in the list {list_choice}.")
    else:
        print("Invalid option. Please try again.")

    choice = input("\n1 - Visualize lists \n"
    "2 - Add an element to a list \n"
    "3 - Search for an element in a list \n"
    "4 - Add a list \n"
    "5 - Remove an element from a list \n"
    "q - Exit\n"
    "Choose an option: ").lower().strip()


print("Program terminated.")