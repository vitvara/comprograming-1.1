import sys
name_list = []


def menu_text():
    if name_list == []:
        return "(N)ew (Q)uit : "
    else:
        return "(N)ew (S)how (D)elete (Q)uit : "


def new_item():
    name = input("Name : ")
    name_list.append(name)
    print(f"{name} added")


def show_item():
    for i in range(len(name_list)):
        print(f"({i+1}) {name_list[i]}")


def delete_item():
    while True:
        try:
            user_delete = int(input("Number? : "))
        except ValueError:
            print("Not a number")
            continue
        try:
            KeyboardInterrupt
            name_list.remove(name_list[int(user_delete)-1])
            show_item()
            break
        except IndexError:
            print("Not in range")


def play():
    while True:
        user_input = input(menu_text())
        if user_input.lower() == "n":
            new_item()
        elif user_input.lower() == "s" and name_list != []:
            show_item()
        elif user_input.lower() == "d" and name_list != []:
            delete_item()
        elif user_input.lower() == "q":
            print("Bye")
            sys.exit()
        else:
            print("Incorrect Menu")


play()
