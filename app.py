import utilities

# Notes -
#
# (EXTRA) Added music (beats that I made myself with various samples scraped from the internet) to the main menu and games
# to improve the user experience
#
# Make sure pygame is installed to run the music within the menu and game, and make sure to have the proper music files
# in the same directory as this code for the music to work
#
# (EXTRA) Created an optional tutorial for each game, so the player can get the hang of
# both games and their rules before playing them and potentially losing crystals
#
# (EXTRA) Added a save and load feature, so the player can save their progress and come back to it later
#
# (EXTRA) Added a settings menu, so the player can change the menu music and adjust the volume of the music


# Start Main

utilities.global_variables()


# Menu Bootup

menu_option = utilities.menu()

while menu_option != "6" and utilities.energy_count > 0 and utilities.energy_count < 300:
    if menu_option != "1" and menu_option != "2" and menu_option != "3" and menu_option != "4" and menu_option != "5":
        utilities.clear_screen()
        utilities.delay_print("Error... invalid menu option", 1)
        utilities.delay_print("Enter a number between 1 and 6 ...", 2)
        menu_option = utilities.menu()
    else:
        utilities.stop_music()
        utilities.menu_option_match(menu_option)
        utilities.time.sleep(2)
        menu_option = utilities.menu()
# End While Loop

if menu_option == "6":
    utilities.stop_music()
    utilities.menu_option_match(menu_option)

# End Main
