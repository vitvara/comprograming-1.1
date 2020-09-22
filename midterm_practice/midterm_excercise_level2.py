import sys
name_list = []


def menu():
    if name_list == []:
        user_input = input("(N)ew (Q)uit : ")
        if user_input.lower() == "n":
            new_add()
        elif user_input.lower() == "q":
            sys.exit()
    else:
        user_input = input("(N)ew (S)how (D)elete (Q)uit : ")
        if user_input.lower() == "n":
            new_add()
        elif user_input.lower() == "s":
            show_name()
        elif user_input.lower() == "d":
            delete_name()
        elif user_input.lower() == "q":
            print("Bye")
            sys.exit()
        else:
            print("Incorrect Menu")


def new_add():
    name = input("Name : ")
    name_list.append(name)
    print(f"{name} added")


def show_name():
    for i in range(len(name_list)):
        print(f"({i+1}) {name_list[i]}")


def delete_name():
    user_delete = input("Number? : ")
    name_list.remove(name_list[int(user_delete)-1])
    show_name()


def play():
    while True:
        menu()


play()
