# The script of the game goes in this file.

# Declare characters used by this game.
define s = Character("Shauna")
define m = Character("Molly")
define y = Character("Me")
define n = Character("Enthusiastic Ad Narrator")

# Variables to track profile swiping
init python:
    current_profile = "shauna"  # Track the current profile being displayed

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

    # User inputs their name and uploads a picture (this part can be more interactive with image upload mechanics, but we'll simplify for now)
    $ player_name = renpy.input("Enter your name: ")
    $ player_name = player_name.strip()  # Remove any leading or trailing whitespace
    
    # Assign the player's name to character y
    $ y = Character(player_name)

    # Display the dating app screen
    show screen dating_app

    # Label to handle left swipe (X button)
    label swipe_left:
    y "Didn't I just see this profile?"
    jump start  # Go back to start label

    # Label to handle right swipe (Heart button)
    label swipe_right:
    y "It's a catch!"
    jump start_conversation  # Jump to start_conversation label

    # Label to start a conversation after swiping right
    label start_conversation:
    # Start a conversation between characters
    y "Hey there! How's it going?"
    s "Oh, hi! I didn't expect someone like you to swipe right."
    y "Haha, well, here we are. Tell me more about yourself."

    # Define the dating app screen
    screen dating_app():
        # Background image of the phone frame
        add "images/phone_frame.png"  # Adjust path as per your project structure

        # Display profiles on the phone screen
        frame:
            xalign 0.5
            yalign 0.5

        vbox:
            xalign 0.5
            yalign 0.5

            # Profile image
            if current_profile == "shauna":
                add "images/shauna_profile.png"  # Replace with actual profile image
            elif current_profile == "molly":
                add "images/molly_profile.png"  # Replace with actual profile image

        # Buttons for swiping
        hbox:
            xalign 0.5
            yalign 0.8

            # X button (Swipe Left)
            textbutton "X" action Jump("swipe_left")

            # Heart button (Swipe Right)
            textbutton "\u2764" action Jump("swipe_right")

