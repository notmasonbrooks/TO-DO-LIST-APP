to_do_list = []

while True:
    try:
        print("\n---TO-DO LIST---")
        print("1. Add")
        print("2. View")
        print("3. Delete")
        print("4. Quit")

        user_input = int(input("\nPlease Select an Option:\n"))

        def add_item(item):
            to_do_list.append(item)
            print(f"\n{item} added to list.")

        def view_list():
            print(f"\nTO-DO LIST:")
            for item in to_do_list:
                print(f"- {item}")

        def delete_item(item):
            if item in to_do_list:
                to_do_list.remove(item)
                print(f"\n{item} deleted from the list.")
            else:
                print(f"\n{item} not found in list.")

        if user_input == 1:
            item_to_add = input("\nPlease enter the task you would like to add:\n")
            add_item(item_to_add)
        elif user_input == 2:
            view_list()
        elif user_input == 3:
            item_to_delete = input(
                "\nPlease enter the task you would like to delete:\n"
            )
            delete_item(item_to_delete)
        elif user_input == 4:
            break
        else:
            print("\nInvalid input. Please enter a valid number from the menu.")
    except ValueError:
        print("\nPlease enter a valid number from the menu.")
