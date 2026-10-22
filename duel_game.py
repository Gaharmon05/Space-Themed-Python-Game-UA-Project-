import utilities
import duel_tutorial


# Displays the rules of alien duel

def print_duel_rules():
    utilities.clear_screen()
    utilities.delay_print(
        "       -       Rules of Alien Duel       -       ", 2)
    print()
    utilities.delay_print(
        "1. The player always goes first and takes turns rolling a 10 sided dice with the alien", 3)
    utilities.delay_print(
        "2. Both the player and alien roll 2 dice their first turn and 1 die on every subsequent turn (if they choose to roll again).", 3)
    utilities.delay_print(
        "3. Every value the player or alien rolls gets added to their final score and if their score exceeds 21, they bust", 3)
    utilities.delay_print(
        "4. If the player or alien busts, the they lose. Whoever busts first loses.", 3)
    utilities.delay_print(
        "5. If neither the player or Alien busts, whoever has the highest score wins", 3)
    utilities.delay_print(
        "6. If the player and the alien score a total of 21, the player wins. This is called a Plasma Blast", 3)
    utilities.delay_print("6. Any other tie results in the player's loss", 3)
    utilities.delay_print(
        "7. Try to get the highest score you can without busting, a win results in earning double the energy crystals bet", 5)
    print()


# Asks user if they want to see the rules of alien duel, performs an action based on the user's input

def see_duel_rules():
    utilities.clear_screen()
    see_rules = input(
        "Do you want to see the rules of Alien Duel? yes or no: ")
    if see_rules.lower() == "yes":
        print_duel_rules()
    elif see_rules.lower() == "no":
        utilities.clear_screen()
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input... Please answer yes or no.", 2)
        return see_duel_rules()


# Asks user if they want to replay the alien duel game, performs an action based on the user's input

def ask_replay_game():
    start_game = input(
        "Do you want to replay Alien Duel (cost = 5 energy crystals)? yes or no: ")
    if start_game.lower() == "yes":
        alien_duel()
    elif start_game.lower() == "no":
        utilities.delay_print("Returning to menu...", 2)
        utilities.menu_option_match(utilities.menu())
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please answer yes or no", 2)
        return ask_replay_game()


# Asks user if they want to start the alien duel tutorial, performs an action based on the user's input

def ask_start_tutorial():
    start_tutorial = input(
        "Do you want to start the tutorial for Alien Duel? yes or no: ")
    if start_tutorial.lower() == "yes":
        duel_tutorial.alien_duel()
    elif start_tutorial.lower() == "no":
        utilities.clear_screen()
        utilities.delay_print("Preparing Alien Duel...", 2)
        utilities.clear_screen()
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please answer yes or no", 2)
        return ask_start_tutorial()


# Rolls the player's dice and updates the player's score based on the values rolled
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


# Responsible for playing music and calling all functions related to the alien duel game
# Handles repeated player and computer dice rolls
# Handles score comparison and energy crystal rewards and losses based on the outcome of the game
# Also handles energy crystal cost to play the game

def alien_duel():

    # Music and energy crystal cost to play the game

    utilities.pygame.mixer.music.set_volume(
        0.1 * (utilities.menu_music_volume / 100))
    utilities.play_music('File008.mp3')
    utilities.energy_count -= 5

    utilities.clear_screen()
    utilities.delay_print("Collecting Player Energy Crystals...", 2)
    utilities.clear_screen()
    utilities.delay_print(
        f"Remaining Energy Crystals: {utilities.energy_count}", 3)
    print()
    utilities.delay_print("Loading Alien Duel...", 2)
    utilities.delay_print("Alien Duel Initialized...", 1)
    utilities.clear_screen()

    see_duel_rules()

    ask_start_tutorial()

    utilities.delay_print(
        "Game Starting... Get Ready to bet your energy crystals!", 5)
    utilities.clear_screen()

    # Reset player and computer scores and number of rolls before starting the game

    utilities.player_score = 0
    utilities.computer_score = 0
    utilities.number_of_computer_rolls = 0
    utilities.number_of_player_rolls = 0

    player_bet = input("Bet an available amount of energy crystals: ")

    # Error checking for player bet input (a real number)

    try:
        player_bet = int(player_bet)

    except ValueError:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please enter a number", 2)
        utilities.energy_count += 5
        return alien_duel()

    # Error checking for player bet input (cannot exceed player's current energy crystal count)

    if player_bet > utilities.energy_count:
        utilities.clear_screen()
        utilities.delay_print(
            "Not enough energy crystals... Restarting Alien Duel...", 2)
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
        utilities.energy_count -= player_bet
        utilities.delay_print(
            f"Player bust, you lost! The alien scored {utilities.computer_score} points", 2)
        utilities.delay_print(f"You forfeited {player_bet} energy crystals", 2)

        utilities.delay_print(
            f"Remaining Energy Crystals: {utilities.energy_count}", 2)
        utilities.time.sleep(5)
        utilities.clear_screen()
        utilities.delay_print("Returning to menu...", 2)
        utilities.menu_option_match(utilities.menu())

        return

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
        utilities.energy_count -= player_bet
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
        utilities.energy_count -= player_bet
        utilities.delay_print(
            f"You lost! The alien scored {utilities.computer_score} points", 2)
        utilities.delay_print(f"You forfeited {player_bet} energy crystals", 2)

    if utilities.energy_count < 0:
        utilities.energy_count = 0

    # Shows remaining energy crystals before asking user if they want to replay the game

    utilities.delay_print(
        f"Remaining Energy Crystals: {utilities.energy_count}", 2)
    utilities.time.sleep(5)
    utilities.clear_screen()
    ask_replay_game()
