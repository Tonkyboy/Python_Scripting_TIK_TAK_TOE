import ascii_tik_tak_toe

logo = ascii_tik_tak_toe.logo


print(logo + "\n\n")
BASIC_FIELDS = ascii_tik_tak_toe.BASIC_FIELDS


def print_field(fields):
    print("Gamefield:\n"
          "\n"
          "     |     |     \n"
          f"  {fields[0]}  |  {fields[1]}  |  {fields[2]}  \n"
          "_____|_____|_____\n"
          "     |     |     \n"
          f"  {fields[3]}  |  {fields[4]}  |  {fields[5]}  \n"
          "_____|_____|_____\n"
          "     |     |     \n"
          f"  {fields[6]}  |  {fields[7]}  |  {fields[8]}  \n"
          "     |     |     \n"
          )


def player_one():
    placement = int(input("Player one place your next X on an empty field: "))
    return placement


def player_two():
    placement = int(input("Player two place your next O on an empty field: "))
    return placement


def check_for_win(fields):
    if fields[0] == fields[1] == fields[2]:
        return fields[0]
    elif fields[3] == fields[4] == fields[5]:
        return fields[3]
    elif fields[6] == fields[7] == fields[8]:
        return fields[6]
    elif fields[0] == fields[3] == fields[6]:
        return fields[0]
    elif fields[1] == fields[4] == fields[7]:
        return fields[1]
    elif fields[2] == fields[5] == fields[8]:
        return fields[2]
    elif fields[0] == fields[4] == fields[8]:
        return fields[0]
    elif fields[2] == fields[4] == fields[6]:
        return fields[2]


def start_new():
    restart = input("Want to start a new Game? Type Y or N: ").capitalize()
    if restart == "Y":
        return True
    elif restart == "N" or restart != "Y":
        return False



def run_game():
    # BASIC_FIELDS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #fields = BASIC_FIELDS
    fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if start_new():
        print_field(fields=fields)
        counter = 0
        while counter < 9:
            if counter % 2 == 0:
                placement_number = player_one()
                if type(fields[placement_number - 1]) == int:
                    fields[placement_number - 1] = "X"
                    print_field(fields=fields)
                    if check_for_win(fields=fields) == "X":
                        print("Player One won the Game!")
                        run_game()
                else:
                    print("This field already in use, try another one!")
                    counter -= 1

            elif counter % 2 != 0:
                placement_number = player_two()
                if type(fields[placement_number - 1]) == int:
                    fields[placement_number - 1] = "O"
                    print_field(fields=fields)
                    if check_for_win(fields=fields) == "O":
                        print("Player Two won the Game!")
                        run_game()
                else:
                    print("This field already in use, try another one!")
                    counter -= 1
            counter += 1
        else:
            print("Game finished!")
            run_game()

    else:
        print("Bye! Have a nice day.")


run_game()
