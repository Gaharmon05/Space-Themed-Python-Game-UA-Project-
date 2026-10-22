import utilities


# Asks user if they want to replay the tutorial for Alien Duel, performs an action based on the user's input

def ask_replay_tutorial():
    start_tutorial = input(
        "Do you want to replay the tutorial for Alien Duel? yes or no: ")
    if start_tutorial.lower() == "yes":
        alien_duel()
    elif start_tutorial.lower() == "no":
        utilities.clear_screen()
        utilities.delay_print("Starting Alien Duel...", 2)
        utilities.clear_screen()
        utilities.pygame.mixer.music.set_volume(
            0.1 * (utilities.menu_music_volume / 100))
        utilities.play_music('File008.mp3')
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please answer yes or no", 2)
        return ask_replay_tutorial()


# Rolls player dice, updates player score, and displays rolled dice values and current score
# Also displays the values rolled and the player's current score

def roll_player_dice():
    utilities.clear_screen()
    if utilities.number_of_player_rolls < 2:
        utilities.delay_print("It's your turn to roll the dice", 2)
        utilities.delay_print("Dice are rolling...", 2)
        rolled_dice_value = utilities.random.randint(0, 9)
        rolled_dice_value2 = utilities.random.randint(0, 9)
        utilities.number_of_player_rolls += 2

        if rolled_dice_value == 0:
            rolled_dice_value = 10

        if rolled_dice_value2 == 0:
            rolled_dice_value2 = 10

        utilities.player_score = utilities.player_score + \
            rolled_dice_value + rolled_dice_value2

        utilities.delay_print(
            f"You rolled a {rolled_dice_value} and a {rolled_dice_value2}", 2)

    else:
        utilities.delay_print("It's your turn to roll the die", 2)
        utilities.delay_print("Die is rolling...", 2)
        rolled_dice_value = utilities.random.randint(0, 9)

        if rolled_dice_value == 0:
            rolled_dice_value = 10

        utilities.delay_print(f"You rolled a {rolled_dice_value}", 2)

        utilities.player_score = utilities.player_score + rolled_dice_value

    utilities.delay_print(
        f"Your current score is {utilities.player_score}", 3)


# Rolls the computer's dice and updates the computer's score based on the values rolled
# Also displays the values rolled and the computer's current score

def roll_computer_dice():
    utilities.clear_screen()
    if utilities.number_of_computer_rolls < 2:
        utilities.delay_print("It's my turn to roll the dice", 2)
        utilities.delay_print("Dice are rolling...", 2)
        rolled_dice_value = utilities.random.randint(0, 9)
        rolled_dice_value2 = utilities.random.randint(0, 9)
        utilities.number_of_computer_rolls += 2

        if rolled_dice_value == 0:
            rolled_dice_value = 10

        if rolled_dice_value2 == 0:
            rolled_dice_value2 = 10

        utilities.computer_score = utilities.computer_score + \
            rolled_dice_value + rolled_dice_value2

        utilities.delay_print(
            f"I rolled a {rolled_dice_value} and a {rolled_dice_value2}", 2)

    else:
        utilities.delay_print("It's my turn to roll the die", 2)
        utilities.delay_print("Die is rolling...", 2)
        rolled_dice_value = utilities.random.randint(0, 9)

        if rolled_dice_value == 0:
            rolled_dice_value = 10

        utilities.delay_print(f"I rolled a {rolled_dice_value}", 2)

        utilities.computer_score = utilities.computer_score + rolled_dice_value

    utilities.delay_print(
        f"My current score is {utilities.computer_score}", 3)


# Responsible for playing music and calling all functions related to the alien duel tutorial
# Handles repeated player and computer dice rolls
# Handles score comparison and energy crystal rewards and losses based on the outcome of the tutorial

def alien_duel():

    # Music and energy crystal cost to play the game

    utilities.pygame.mixer.music.set_volume(
        0.09 * (utilities.menu_music_volume / 100))
    utilities.play_music('File0018.mp3')

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

    # Reset player and computer scores and number of rolls before starting the game

    utilities.player_score = 0
    utilities.computer_score = 0
    utilities.number_of_computer_rolls = 0
    utilities.number_of_player_rolls = 0

    player_bet = input("Bet an amount of energy crystals: ")

    # Error checking for player bet input (a real number)

    try:
        player_bet = int(player_bet)

    except ValueError:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please enter a number", 2)
        utilities.energy_count += 5
        return alien_duel()

    roll_player_dice()
    keep_rolling = ""

    # Allows player to keep rolling until they either bust or choose to stop rolling

    while utilities.player_score <= 21 and keep_rolling != "no":
        keep_rolling = input("Do you want to keep rolling? yes or no: ")
        if keep_rolling.lower() == "yes":
            roll_player_dice()

        elif keep_rolling.lower() == "no":
            utilities.clear_screen()
            utilities.delay_print(
                f"Your final score is {utilities.player_score}", 4)
        else:
            utilities.delay_print("Invalid input, try again", 2)
    # End While Loop

    # Handles player bust and ends game if player score exceeds 21

    if utilities.player_score > 21:
        utilities.clear_screen()
        utilities.delay_print(
            f"Your final score is {utilities.player_score}", 4)
        utilities.clear_screen()
        utilities.delay_print(
            f"Player bust, you lost! The alien scored {utilities.computer_score} points", 2)
        utilities.delay_print(f"You forfeited {player_bet} energy crystals", 2)

        utilities.delay_print(
            f"Remaining Energy Crystals: {utilities.tutorial_energy_count}", 2)
        utilities.time.sleep(5)
        utilities.clear_screen()
        utilities.delay_print("Tutorial complete!", 2)
        utilities.delay_print("Loading...", 2)
        utilities.clear_screen()

        return ask_replay_tutorial()

    computer_stop = 0

    roll_computer_dice()

    # Computer rolls dice until it either busts or reaches a score of 17 or higher and stops rolling

    while utilities.computer_score <= 21 and computer_stop < 1:

        if utilities.computer_score < 17:
            roll_computer_dice()

        elif computer_stop == 0:
            utilities.clear_screen()
            computer_stop += 1
            utilities.delay_print(
                f"My final score is {utilities.computer_score}", 4)
    # End While Loop

    # Score comparison to determine winner and energy crystal rewards and losses based on the outcome of the game

    if utilities.computer_score > 21:
        utilities.clear_screen()
        utilities.delay_print(
            f"My final score is {utilities.computer_score}", 4)

    utilities.clear_screen()

    if utilities.computer_score > 21:
        utilities.player_bet = player_bet * 2
        utilities.energy_count += player_bet
        utilities.delay_print(
            f"Alien bust, you won! You scored {utilities.player_score} points", 2)
        utilities.delay_print(f"You earned {player_bet} energy crystals", 2)

    elif utilities.player_score > utilities.computer_score:
        utilities.player_bet = player_bet * 2
        utilities.energy_count += player_bet
        utilities.delay_print(
            f"You won! You scored {utilities.player_score} points", 2)
        utilities.delay_print(f"You earned {player_bet} energy crystals", 2)

    elif utilities.computer_score > utilities.player_score:
        utilities.delay_print(
            f"You lost! The alien scored {utilities.computer_score} points", 2)
        utilities.delay_print(f"You forfeited {player_bet} energy crystals", 2)

    elif utilities.player_score == 21:
        utilities.player_bet = player_bet * 2
        utilities.energy_count += player_bet
        utilities.delay_print(
            f"Plasma blast, you won! You scored {utilities.player_score} points", 2)
        utilities.delay_print(f"You earned {player_bet} energy crystals", 2)

    else:
        utilities.delay_print(
            f"You lost! The alien scored {utilities.computer_score} points", 2)
        utilities.delay_print(f"You forfeited {player_bet} energy crystals", 2)

    # Shows remaining energy crystals before asking user if they want to replay the game

    utilities.delay_print(
        f"Remaining Energy Crystals: {utilities.tutorial_energy_count}", 2)
    utilities.time.sleep(5)
    utilities.clear_screen()
    utilities.delay_print("Tutorial complete!", 2)
    utilities.delay_print("Loading...", 2)
    utilities.clear_screen()

    return ask_replay_tutorial()
