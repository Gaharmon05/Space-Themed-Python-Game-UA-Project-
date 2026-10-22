import utilities


# Displays settings menu and allows user to select a settings menu option

def settings_menu():
    utilities.pygame.mixer.music.set_volume(
        0.12 * (utilities.menu_music_volume / 100))
    utilities.play_music(utilities.menu_music_choice)
    utilities.clear_screen()
    print("   -   Settings   -   ")
    print()
    print("1. Change Menu Music")
    print("2. Change Music Volume")
    print("3. Autosave Options")
    print("4. Reset Settings to Default")
    print("5. Exit settings")
    print()
    return input("Choose option: ")


# Matches user selected settings menu option to appropriate action

def settings_menu_option_match(settings_menu_option):
    match settings_menu_option:
        case "1":
            return change_menu_music()

        case "2":
            return change_music_volume()

        case "3":
            return autosave_options()

        case "4":
            return reset_settings()

        case "5":
            utilities.clear_screen()
            utilities.delay_print("Returning to main menu...", 2)
            return utilities.menu_option_match(utilities.menu())

        case _:
            utilities.clear_screen()
            utilities.delay_print(
                "Invalid input, please choose a valid option", 2)
            return settings_menu_option_match(settings_menu())


# Displays menu music options and allows user to select a menu music option, then changes the menu music based on the user's selection

def change_menu_music():
    utilities.pygame.mixer.init()
    utilities.clear_screen()

    # displays options

    print("  -  Menu Music Options  -  ")
    print()
    print("1. Alternative Dance (Default)")
    print("2.  Alternative Hip Hop")
    print("3. Jazzy Hip Hop")
    print("4. Return to Settings")
    print()
    menu_music_choice = input("Choose option: ")

    # Error checking for user menu music choice input

    if menu_music_choice != "1" and menu_music_choice != "2" and menu_music_choice != "3" and menu_music_choice != "4":
        utilities.clear_screen()
        utilities.delay_print(
            "Invalid input, please choose a valid option", 1)
        utilities.delay_print("Enter a number between 1 and 4 ...", 3)
        return change_menu_music()

    # match users user's menu music choice to appropriate menu music file

    match menu_music_choice:
        case "1":
            utilities.menu_music_choice = "File003.mp3"
            utilities.clear_screen()
            utilities.delay_print("- Alternative Dance selected -", 2)

        case "2":
            utilities.menu_music_choice = "File0033.mp3"
            utilities.clear_screen()
            utilities.delay_print("- Alternative Hip Hop selected -", 2)

        case "3":
            utilities.menu_music_choice = "File0028.mp3"
            utilities.clear_screen()
            utilities.delay_print("- Jazzy Hip Hop selected -", 2)

        case "4":
            utilities.clear_screen()
            utilities.delay_print("Returning to settings menu...", 2)
            return settings_menu_option_match(settings_menu())

        case _:
            utilities.clear_screen()
            utilities.delay_print(
                "Invalid input, please choose a valid option", 2)
            return change_menu_music()

    return settings_menu_option_match(settings_menu())


# Asks user to input a menu music volume between 0 and 100%, then changes the menu music volume based on the user's input

def change_music_volume():

    global menu_music_volume

    utilities.clear_screen()
    utilities.delay_print(
        f"Current menu music volume: {utilities.menu_music_volume}%", 2)
    utilities.menu_music_volume = input("Choose menu music volume (0-100): ")

    # Error checking for user menu music volume input

    try:
        utilities.menu_music_volume = int(utilities.menu_music_volume)

    except ValueError:
        utilities.clear_screen()
        utilities.delay_print(
            "Invalid input, please enter a number between 0 and 100", 2)
        return change_music_volume()

    if utilities.menu_music_volume < 0 or utilities.menu_music_volume > 100:
        utilities.clear_screen()
        utilities.delay_print(
            "Invalid input, please enter a number between 0 and 100", 2)
        return change_music_volume()

    return settings_menu_option_match(settings_menu())


# Asks user to enable or disable autosave, then changes the autosave setting based on the user's input

def autosave_options():
    utilities.clear_screen()
    autosave_decision = input(
        "Do you want to enable or disable autosave? (type 'enable' or 'disable'): ").strip().lower()
    if autosave_decision == "enable":
        utilities.auto_save = True
        utilities.clear_screen()
        utilities.delay_print("Autosave enabled...", 2)

    elif autosave_decision == "disable":
        if utilities.auto_save == False:
            utilities.clear_screen()
            utilities.delay_print("Autosave is already disabled...", 2)
        else:
            utilities.auto_save = False
            utilities.delay_print("Autosave disabled...", 2)
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please choose a valid option", 2)
        return autosave_options()

    return settings_menu_option_match(settings_menu())


# Asks user to confirm if they want to reset settings to default, then resets or keeps current settings based on the user's input

def reset_settings():
    utilities.clear_screen()
    reset = input(
        "Are you sure you want to reset all settings to default? (type 'yes' or 'no'): ").strip().lower()

    if reset == "yes":
        utilities.menu_music_choice = "File003.mp3"
        utilities.menu_music_volume = 100
        utilities.auto_save = False
        utilities.clear_screen()
        utilities.delay_print("Settings have been reset to default...", 2)

    elif reset == "no":
        utilities.clear_screen()
        utilities.delay_print("Settings will remain unchanged...", 2)
    else:
        utilities.clear_screen()
        utilities.delay_print("Invalid input, please choose a valid option", 2)
        return reset_settings()
    return settings_menu_option_match(settings_menu())
