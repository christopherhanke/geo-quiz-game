import game_functions

def main():
    print("Welcome tho the Geo Quiz Game. \nWhat do you want to do?")
    while True:
        print("[P]lay \n[Q]uit")
        selection = input("Your choice? ").lower()

        if selection == "p":
            game_functions.play_game()
        elif selection == "q":
            print("Goodbye.")
            break
        else:
            print("Please enter a valid option. [P/Q]")


if __name__ == "__main__":
    main()

