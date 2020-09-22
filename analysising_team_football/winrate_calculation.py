import sys


def menu(filename):
    lines = read_input_text(f"analysising_team_football/{file_name}")
    user_input = input(
        "What do you want to know ? (m)in , ma(x), (o)rder max to min, o(r)der min to max, (q)uit :")
    list_winrate, dict_winrate = calculate_winrate(
        read_input_text(f"analysising_team_football/{file_name}"))

    if user_input.lower() == "x":
        print()
        print(
            f"{dict_winrate[max(list_winrate)]}: got maximum win rate {max(list_winrate):.5f}")
        print()
    elif user_input.lower() == "m":
        print()
        print(
            f"{dict_winrate[min(list_winrate)]}: got minimum win rate {min(list_winrate):.5f}")
        print()
    elif user_input.lower() == "o":
        list_winrate.sort()
        print(f"Total team(s): {len(lines)}")
        for i in range(len(list_winrate)):
            print(
                f"{dict_winrate[list_winrate[i]]}: got win rate {list_winrate[i]:.5f}")
        print()
    elif user_input.lower() == "r":
        list_winrate.sort()
        print(f"Total team(s): {len(lines)}")
        for i in range(len(list_winrate)):
            print(
                f"{dict_winrate[list_winrate[(i+1)*(-1)]]}: got win rate {list_winrate[(i+1)*(-1)]:.5f}")
        print()
    elif user_input.lower() == "q":
        print("Bye")
        sys.exit()


def read_input_text(file_name):
    with open(f"{file_name}", "r") as file_read:
        lines = file_read.readlines()

        return lines


def calculate_winrate(list_team):
    list_team_split = []
    all_team_winrate_name = {}
    all_team_winrate = []
    for i in list_team:
        list_team_split = i.split(",")
        sumtime = int(list_team_split[1]) + int(list_team_split[2])
        winrate = int(list_team_split[1]) / sumtime
        all_team_winrate.append(winrate)
        all_team_winrate_name[winrate] = list_team_split[0]
    return all_team_winrate, all_team_winrate_name


file_name = input("Enter a file name: ")
while True:

    menu(file_name)
