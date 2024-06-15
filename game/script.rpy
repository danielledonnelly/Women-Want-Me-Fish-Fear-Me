# The script of the game goes in this file.

# Declare characters used by this game.
define s = Character("Shauna")
define m = Character("Molly")
define y = Character("Me")
define n = Character("Enthusiastic Ad Narrator")

# Variables to track profile swiping
init python:
    current_profile = "shauna"  # Track the current profile being displayed

# Function to switch profiles
init python:
    def switch_profile():
        global current_profile
        if current_profile == "shauna":
            current_profile = "molly"
        else:
            current_profile = "shauna"
        print(f"Profile switched to: {current_profile}")
        renpy.jump("display_profile")

# Load images
image beach = "images/beach_background.png"
image phone = "images/app-screen.png"
image shauna-screen = "images/shauna-screen.png"
image shauna_catch = "images/shauna-catch-screen.png"
image molly-screen = "images/molly-screen.png"
image molly_catch = "images/molly-catch-screen.png"

# Label for the beginning of the story
label start:

    # Background image for the scene, if you have one
    # scene bg room with fade
    scene beach with fade
    # Narration and dialogue
    "{i}It all started with a silly little ad I saw online.{/i}"
    n "DO YOU STRUGGLE TO FIND LOVE ON TRADITIONAL DATING APPS?"
    "Yes."
    n "DOES ONLINE DATING MAKE YOU FEEL LIKE A FISH OUT OF WATER?"
    "...Maybe."
    n "DID YOU SIGN UP FOR PLENTY OF FISH THINKING IT WAS A SOCIAL MEDIA PLATFORM FOR FISHING ENTHUSIASTS?"
    "...Oddly specific... but yes."
    n "GET READY TO FIND FELLOW FISH FANATICS WITH AN APP THAT'S WAY MORE REEL-ISTIC…"
    n "FISHERS ONLY: WHERE EVERY 'CATCH' IS A KEEPER!"
    n "FIND LOVE ON A PLATFORM MADE FOR FISHERS, BY FISHERS!" 
    n "SWIPE, CHAT, AND REEL IN THAT SPECIAL SOMEONE!"
    n "DOWNLOAD FISHERS ONLY TODAY!"
    "..."
    "I guess it wouldn't hurt."
    "{i}So I downloaded it and made a profile.{/i}"

    # User inputs their name
    $ player_name = renpy.input("Enter your name: ")
    $ player_name = player_name.strip()  # Remove any leading or trailing whitespace

    # Assign the player's name to character y
    $ y = Character(player_name)

    # Jump to display profile
    jump display_profile

# Label to display the current profile
label display_profile:
    scene beach
    # Show the phone background
    show phone

    # Hide previous images
    hide shauna
    hide molly

    # Show current profile
    if current_profile == "shauna":
        show shauna-screen at Position(xalign=0.5, yalign=0.5)
    elif current_profile == "molly":
        show molly-screen at Position(xalign=0.5, yalign=0.5)

    # Display swipe buttons
    call screen swipe_buttons

    return

# Screen to display swipe buttons
screen swipe_buttons:
    hbox:
        xalign 0.5
        yalign 0.9
        spacing 20

        textbutton "X" action Function(switch_profile)
        textbutton "♥" action Jump("its_a_catch")

label its_a_catch:

    # Show the catch screen based on the current profile
    if current_profile == "shauna":
        hide shauna
        show shauna_catch at Position(xalign=0.5, yalign=0.5)
        $ renpy.pause(2.0)  # Pause to show the catch screen
        jump shauna_route
    elif current_profile == "molly":
        hide molly
        show molly_catch at Position(xalign=0.5, yalign=0.5)
        $ renpy.pause(2.0)  # Pause to show the catch screen
        jump molly_route

    return

# Label for Shauna's route
label shauna_route:
    scene beach
    s "Welcome to my route!"
    # Add more dialogue and scenes for Shauna's route here
    return

# Label for Molly's route
label molly_route:
    scene beach with fade
    m "Welcome to my route!"
    # Add more dialogue and scenes for Molly's route here
    return
