import time
import os
import random
import mining_game
import duel_game
import settings
import pygame
import sys


# Defines global variables that are used across multiple files

def global_variables():
    global energy_count
    global tutorial_energy_count
    global menu_music_choice
    global menu_music_volume
    global auto_save

    auto_save = False
    energy_count = 50
    tutorial_energy_count = "infinite"
    menu_music_choice = "File003.mp3"
    menu_music_volume = 100


# Defines function to clear the console screen

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Defines function to print text with a delay, used for better user experience and pacing of the game

def delay_print(text, delay_time):
    print(text)
    time.sleep(delay_time)


# Defines function to save the game by writing the current energy count to a text file

def save_game():
    with open("save_file.txt", "w") as save_file:
        save_file.write(str(energy_count))


# Defines function to load the game by reading the energy count from a text file, if no save file is found it starts a new game with 50 energy crystals

def load_game():
    global energy_count

    try:
        with open("save_file.txt", "r") as save_file:
            energy_count = int(save_file.read())
            clear_screen()
            delay_print("Save file detected...", 3)
            delay_print("Game loaded!", 2)
    except FileNotFoundError:
        clear_screen()
        delay_print("No save file detected...", 3)
        delay_print("Starting new game...", 2)
        energy_count = 50


# Functions that Load, play, and stop music

def play_music(song):
    pygame.mixer.music.load(song)  # Load your music file here
    pygame.mixer.music.play(-1)  # Play the music in a loop


def stop_music():
    pygame.mixer.music.stop()


# Displays menu and allows user to select a menu option

def menu():
    if auto_save:
        clear_screen()
        delay_print("Autosave enabled, saving game...", 2)
        save_game()
        delay_print("Game saved!", 2)

    # Initializes pygame mixer for music playback and sets the menu music volume based on the user's settings

    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.12 * (menu_music_volume / 100))
    play_music(menu_music_choice)
    clear_screen()

    # Checks for win or lose conditions before displaying menu options

    if energy_count >= 300:
        delay_print(
            "Congratulations, you have collected over 300 energy crystals! You win the game!", 4)
        delay_print("Goodbye...", 2)
        clear_screen()
        sys.exit()

    elif energy_count == 0:
        delay_print(
            "You have run out of energy crystals! THE ALIEN ATE YOU FOR BREAKFAST! Game over...", 4)
        delay_print("Goodbye...", 2)
        clear_screen()
        sys.exit()

    # Displays menu options and prompts user to select a menu option, also displays current energy crystal count

    else:
        print("Current Energy Crystal Count:", (energy_count))
        print()
        print("- Menu Options -")
        print()
        print("1. Play Asteroid Mining - 10 energy crystals required")
        print("2. Play Alien Duel - 5 energy crystals required")
        print("3. Save Game")
        print("4. Load Game")
        print("5. Settings")
        print("6. Exit Menu")
        print()
        return input("Choose option: ")


# Matches user selected menu option to appropriate action (some are defined in other files)

def menu_option_match(menu_option):
    match menu_option:
        case "1":
            if energy_count >= 10:
                mining_game.asteroid_mining()
            else:
                print("Not enough energy crystals")
                menu_option = menu()
                menu_option_match(menu_option)

        case "2":
            if energy_count >= 5:
                duel_game.alien_duel()
            else:
                print("Not enough energy crystals")
                menu_option = menu()
                menu_option_match(menu_option)
        case "3":
            clear_screen()
            save = input(
                "Your previous save will be overwritten. Are you sure you want to save the game? yes or no: ")
            if save.lower() == "yes":
                clear_screen()
                delay_print("Saving game...", 2)
                save_game()
                delay_print("Game saved!", 2)
            elif save.lower() == "no":
                clear_screen()
                delay_print("Save cancelled, returning to menu...", 2)
                menu_option = menu()
                menu_option_match(menu_option)
            else:
                clear_screen()
                delay_print("Invalid input, please answer yes or no", 2)
                return menu_option_match("3")

        case "4":
            clear_screen()
            delay_print("Loading game...", 3)
            load_game()

        case "5":
            settings.settings_menu_option_match(settings.settings_menu())

        case "6":
            clear_screen()
            print("Goodbye...")
            time.sleep(2)
            clear_screen()
