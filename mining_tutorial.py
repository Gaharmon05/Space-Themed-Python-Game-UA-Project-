import utilities


# Replays the tutorial for the asteroid mining game if the user wants to replay it, otherwise starts the asteroid mining game

def ask_replay_tutorial():
    start_tutorial = input(
        "Do you want to replay the tutorial for Asteroid Mining? yes or no: ")
    if start_tutorial.lower() == "yes":
        asteroid_mining()
    elif start_tutorial.lower() == "no":
        utilities.clear_screen()
        utilities.delay_print("Preparing to start Asteroid Mining...", 2)
        utilities.pygame.mixer.music.set_volume(
            0.12 * (utilities.menu_music_volume / 100))
        utilities.play_music('File0023.mp3')
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please answer yes or no", 2)
        return ask_replay_tutorial()


# Asks user if they want to start the tutorial version of theasteroid mining game, performs an action based on the user's input

def ask_start_mining():
    global mining_answer

    if mining_answer.lower() == "start":
        start_mining()
    else:
        utilities.clear_screen()
        utilities.delay_print(
            "Invalid input, please type 'start' to begin mining", 2)
        utilities.time.sleep(2)

        mining_answer = input("Type 'start' to begin mining: ")
        return ask_start_mining()

#  Starts the asteroid mining tutorial, which allows the user to play the asteroid mining game without losing energy crystals


def start_mining():
    utilities.clear_screen()
    utilities.delay_print("Mining started...", 2)
    utilities.delay_print("Mining in progress...", 5)
    utilities.clear_screen()

    mining_option = utilities.random.randint(1, 100)

# Performs actions and updates energy crystal count based on random mining outcomes

    match mining_option:
        case mining_option if mining_option <= 40:
            utilities.delay_print("Small crystals found...", 2)
            utilities.delay_print("Large crystals found...", 2)
            utilities.clear_screen()
            utilities.delay_print("You earned 50 energy crystals", 2)

        case mining_option if mining_option >= 95:
            random_value = utilities.random.randint(1, 2)
            if random_value == 1:
                utilities.delay_print("Small crystals found...", 2)
                utilities.delay_print("Large crystals found...", 3)
                utilities.delay_print("You found a rare crystal deposit!", 2)
                utilities.clear_screen()
                utilities.delay_print("You earned 100 energy crystals", 2)
            else:
                utilities.delay_print("Small crystals found...", 2)
                utilities.delay_print("Large crystals found...", 3)
                utilities.delay_print("You found a rare crystal deposit!", 4)
                utilities.delay_print(
                    "You tripped and fell, dropping the energy crystals you discovered into a ravine...", 2)
                utilities.clear_screen()
                utilities.delay_print("You lost 100 energy crystals", 2)

        case mining_option if mining_option >= 40 and mining_option < 60:
            utilities.delay_print("No crystals found...", 3)
            utilities.delay_print(
                "You ran into an alien! You got scared and dropped some small energy crystals while running away.", 2)
            utilities.clear_screen()
            utilities.delay_print("You lost 25 energy crystals", 2)

        case mining_option if mining_option >= 90 and mining_option < 95:
            utilities.delay_print(
                "You hit a dangerous gas pocket while mining...", 3)
            utilities.delay_print(
                "You got burned and dropped all of your energy crystals while running away...", 2)
            utilities.clear_screen()
            utilities.delay_print("You lost all of your energy crystals", 2)

        case mining_option if mining_option >= 60 and mining_option < 90:
            utilities.delay_print("Nothing happened", 2)
            utilities.delay_print(
                "You safely left the mining area...", 2)

    # shows remaining energy crystals

    utilities.delay_print(
        f"Remaining Energy Crystals: {utilities.tutorial_energy_count}", 2)


# Responsible for calling all functions and music related to the asteroid mining tutororial

def asteroid_mining():

    # Handles the game's music and displays tutorial information

    utilities.pygame.mixer.music.set_volume(
        0.09 * (utilities.menu_music_volume / 100))
    utilities.play_music('File0018.mp3')

    utilities.clear_screen()
    utilities.delay_print("Collecting Player Energy Crystals...", 2)
    utilities.clear_screen()
    utilities.delay_print("Loading...", 2)
    utilities.clear_screen()
    utilities.delay_print(
        "Player energy crystals are not deducted during the tutorial...", 4)
    utilities.clear_screen()
    utilities.delay_print(
        f"Remaining Energy Crystals: {utilities.tutorial_energy_count}", 3)
    print()
    utilities.delay_print("Loading Tutorial...", 2)
    utilities.delay_print("Tutorial Initialized...", 1)
    utilities.clear_screen()

    global mining_answer
    mining_answer = input("Type 'start' to begin mining: ")
    ask_start_mining()

    # Asks user if they want to replay the tutorial

    utilities.delay_print("Mining complete.", 2)
    utilities.time.sleep(5)
    utilities.clear_screen()
    utilities.delay_print("Tutorial complete!", 2)
    utilities.delay_print("Loading...", 2)
    utilities.clear_screen()

    return ask_replay_tutorial()
