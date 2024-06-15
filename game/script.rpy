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
    def switch_profile(direction):
        global current_profile
        if direction == "left":
            if current_profile == "shauna":
                current_profile = "molly"
            else:
                current_profile = "shauna"
            print(f"Profile switched to: {current_profile}")
            renpy.restart_interaction()
        elif direction == "right":
            print("Jumping to its_a_catch")
            renpy.jump("its_a_catch")

# Load images
image phone = "images/app-screen.png"
image shauna = "images/shauna-screen.png"
image molly = "images/molly-screen.png"

# Label for the beginning of the story
label start:

    # Background image for the scene, if you have one
    # scene bg room with fade

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

    # Show the phone background
    scene phone

    if current_profile == "shauna":
        show shauna at Position(xalign=0.5, yalign=0.5)
    elif current_profile == "molly":
        show molly at Position(xalign=0.5, yalign=0.5)

    # Display swipe buttons
    call screen swipe_buttons

    return

# Screen to display swipe buttons
screen swipe_buttons:
    hbox:
        xalign 0.5
        yalign 0.9
        spacing 20

        textbutton "X" action SetVariable("current_profile", "molly" if current_profile == "shauna" else "shauna")
        textbutton "♥" action Function(switch_profile, "right")

# Label for "IT'S A CATCH!" screen
label its_a_catch:
    scene phone

    "IT'S A CATCH!"

    # Example of starting a conversation
    if current_profile == "shauna":
        s "I'm so glad we matched!"
        # Continue with Shauna's conversation
    elif current_profile == "molly":
        m "Looks like we have a lot in common!"
        # Continue with Molly's conversation

    return
