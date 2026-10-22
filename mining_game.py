import utilities
import mining_tutorial


# Asks user if they want to replay the asteroid mining game, performs an action based on the user's input

def ask_replay_game():
    start_game = input(
        "Do you want to replay Asteroid Mining (cost = 10 energy crystals)? yes or no: ")
    if start_game.lower() == "yes":
        asteroid_mining()
    elif start_game.lower() == "no":
        utilities.delay_print("Returning to menu...", 2)
        utilities.menu_option_match(utilities.menu())
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please answer yes or no", 2)
        return ask_replay_game()


# Asks user if they want to start the asteroid mining tutorial, performs an action based on the user's input

def ask_start_tutorial():
    start_tutorial = input(
        "Do you want to start the tutorial for Asteroid Mining? yes or no: ")
    if start_tutorial.lower() == "yes":
        mining_tutorial.asteroid_mining()
    elif start_tutorial.lower() == "no":
        utilities.clear_screen()
        utilities.delay_print("Preparing Asteroid Mining...", 2)
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please answer yes or no", 2)
        return ask_start_tutorial()


# Displays the rules of asteroid mining

def print_mining_rules():
    utilities.clear_screen()
    utilities.delay_print("    -    Rules of asteroid mining    -    ", 2)
    print()
    utilities.delay_print("1. You will be asked to start mining", 3)
    utilities.delay_print(
        "2. You must have at least 10 energy crystals to start mining", 3)
    utilities.delay_print(
        "3. Once you start mining, you will have a random chance to earn or lose energy crystals", 4)
    # displays mining rules

    print()
    utilities.delay_print(
        "-    Potential mining outcomes and their probabilities    -", 2)
    print()
    utilities.delay_print("1. Earn 50 energy crystals (40 percent chance)", 3)
    utilities.delay_print(
        "2. Earn 100 energy crystals or lose 100 energy crystals (5 percent chance)", 3)
    utilities.delay_print("3. Lose 25 energy crystals (20 percent chance)", 3)
    utilities.delay_print("4. Lose all energy crystals (5 percent chance)", 3)
    utilities.delay_print("5. Nothing happens (30 percent chance)", 3)
    utilities.time.sleep(5)
    # displays mining outcomes and probabilities

    print()


# Asks user if they want to see the rules of asteroid mining, performs an action based on the user's input

def see_mining_rules():
    see_mining_rules = input(
        "Do you want to see the rules of Asteroid Mining? yes or no: ")
    if see_mining_rules.lower() == "yes":
        print_mining_rules()
    elif see_mining_rules.lower() == "no":
        utilities.clear_screen()
    else:
        print("Invalid input... Restarting Asteroid Mining..")
        utilities.time.sleep(2)
        utilities.energy_count += 10
        asteroid_mining()


# Asks user if they want to start mining (officially playing the game), performs an action based on the user's input

def ask_start_mining():
    global mining_answer

    if mining_answer.lower() == "start":
        start_mining()
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please type 'start'", 2)
        utilities.time.sleep(2)

        see_mining_rules()

        mining_answer = input("Type 'start' to begin mining: ")
        return ask_start_mining()


# Starts the asteroid mining game

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
            utilities.energy_count += 50

            utilities.clear_screen()
            utilities.delay_print("You earned 50 energy crystals", 2)

        case mining_option if mining_option > 95:

            random_value = utilities.random.randint(1, 2)

            if random_value == 1:
                utilities.delay_print("Small crystals found...", 2)
                utilities.delay_print("Large crystals found...", 3)
                utilities.delay_print("You found a rare crystal deposit!", 2)
                utilities.energy_count += 100

                utilities.clear_screen()
                utilities.delay_print("You earned 100 energy crystals", 2)
            else:
                utilities.delay_print("Small crystals found...", 2)
                utilities.delay_print("Large crystals found...", 3)
                utilities.delay_print("You found a rare crystal deposit!", 4)
                utilities.clear_screen()
                utilities.delay_print(
                    "You tripped and fell, dropping the energy crystals you discovered into a ravine...", 2)
                utilities.energy_count -= 100

                utilities.clear_screen()
                utilities.delay_print("You lost 100 energy crystals", 2)

        case mining_option if mining_option > 40 and mining_option <= 60:

            utilities.delay_print("No crystals found...", 3)
            utilities.delay_print(
                "You ran into an alien! You got scared and dropped some small energy crystals while running away.", 2)
            utilities.energy_count -= 25

            utilities.clear_screen()
            utilities.delay_print("You lost 25 energy crystals", 2)

        case mining_option if mining_option > 90 and mining_option <= 95:

            utilities.delay_print(
                "You hit a dangerous gas pocket while mining...", 3)
            utilities.delay_print(
                "You got burned and dropped all of your energy crystals while running away...", 2)
            utilities.energy_count -= utilities.energy_count

            utilities.clear_screen()
            utilities.delay_print("You lost all of your energy crystals", 2)

        case mining_option if mining_option > 60 and mining_option <= 90:

            utilities.delay_print("No crystals found...", 2)
            utilities.delay_print(
                "You safely left the mining area...", 2)

    # Ensures energy crystal count does not drop below 0 and shows remaining energy crystals

    if utilities.energy_count < 0:
        utilities.energy_count = 0

    utilities.delay_print(
        f"Remaining Energy Crystals: {utilities.energy_count}", 2)


# Responsible for playing music and calling all functions related to the asteroid mining game
# Also handles energy crystal cost to play the game

def asteroid_mining():

    # Music and energy crystal cost to play the game

    utilities.pygame.mixer.music.set_volume(
        0.12 * (utilities.menu_music_volume / 100))
    utilities.play_music('File0013.mp3')
    utilities.energy_count -= 10

    utilities.clear_screen()
    utilities.delay_print("Collecting Player Energy Crystals...", 2)
    utilities.clear_screen()
    utilities.delay_print(
        f"Remaining Energy Crystals: {utilities.energy_count}", 3)
    print()
    utilities.delay_print("Loading Asteroid Mining...", 2)
    utilities.delay_print("Asteroid Mining Initialized...", 1)
    utilities.clear_screen()

    see_mining_rules()

    ask_start_tutorial()

    global mining_answer
    mining_answer = input("Type 'start' to begin mining: ")

    ask_start_mining()

    # Asks user if they want to replay the game

    utilities.delay_print("Mining complete.", 2)
    utilities.time.sleep(5)
    utilities.clear_screen()
    ask_replay_game()
