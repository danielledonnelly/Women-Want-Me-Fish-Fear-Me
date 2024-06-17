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
    y "Yes."
    n "DOES ONLINE DATING MAKE YOU FEEL LIKE A FISH OUT OF WATER?"
    y "...Maybe."
    n "DID YOU SIGN UP FOR PLENTY OF FISH THINKING IT WAS A SOCIAL MEDIA PLATFORM FOR FISHING ENTHUSIASTS?"
    y "...Oddly specific... but yes."
    n "GET READY TO FIND FELLOW FISH FANATICS WITH AN APP THAT'S WAY MORE REEL-ISTIC…"
    n "FISHERS ONLY: WHERE EVERY 'CATCH' IS A KEEPER!"
    n "FIND LOVE ON A PLATFORM MADE FOR FISHERS, BY FISHERS!" 
    n "SWIPE, CHAT, AND REEL IN THAT SPECIAL SOMEONE!"
    n "DOWNLOAD FISHERS ONLY TODAY!"
    y "..."
    y "I guess it wouldn't hurt."
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
    s "Hey, it looks like we're a match."
    s "Nice ass, by the way."
    s "Ugh, autocorrect. I meant *BASS, the one you're holding in your profile picture."
    s "Do you go fishing very often?"
    y "I wouldn't be on Fishers Only if I didn't."
    s "Nice! Where's your favourite spot?"
    menu: 
        "The old wharf by the coastline":
            jump old_pier
        "The pond over near the woodlands":
            jump pond_wood

label old_pier: 
    s "Ooh, I know that one. It's one of my personal favourites, in fact."
    s "I was actually thinking of going there this weekend. Would you like to join me?"
    y "Sure."
    s "Sweet! In the meantime, let's chat about bait... what do you typically use?"
    s "Don't laugh... but I SWEAR I caught a carp with a gummy worm once."
    # Shauna definitely uses gummy worms as bait.
    "We talked for a while after that, sharing fishing stories and getting to know each other."
    "Before I knew it, the weekend was already here."
    jump shauna_date1

label pond_wood: 
    s "Huh, I'm not sure I heard of that one before. Maybe you could take me there sometime!"
    s "I tend to prefer fishing in the ocean, personally. In fact, I was going to head out to a nice little spot on Sunday."
    s "It's an old dock near the coastline."
    y "That sounds nice. I tend to do most of my fishing in ."
    s "Would you like to join me? It's a lot of fun casting a line from the wharf."
    y "Yeah, sounds good."
    s "Awesome! You're going to love it."
    s "Let me tell you about some other great fishing spots, I know a lot of secret ones."
    "We talked for a while after that. I learned a lot about Shauna and her favourite places to fish."
    "Before I knew it, the weekend was already here."
    jump shauna_date1

label shauna_date1:
    scene beach
    s "Hey! Nice to see you in person."
    y "Same to you..."
    "I looked her up and down."
    y "No offense, I don't mean this as an insult or anything..."
    y "But do you always wear a sailor's suit when you go fishing?"
    "Shauna laughed."
    s "Only when the weather's nice and I'm staying grounded on land"
    s "I tend to dress a lot more practical when I'm out on the water."
    s "But I figured since we're just fishing from the coast today, it wouldn't hurt to dress up a little."
    "She smiled."
    s "C'mon, let's get to it!"
    # Fishing minigame goes here

label sdate1_catch:
    "I caught a tuna."
    s "Nice work! That's a pretty big one. The fish around here tend to be small, so that's quite the feat."
    y "Thanks!"
    s "I haven't had a single nip on my line yet, but I have a feeling my luck with change soon."
    "I smiled."
    y "I'm sure it will. It's still only early, right? There's plenty of time."
    "Shauna nodded in agreement and sat down on the dock, her rod still in hand."
    "She glanced up at me and patted the ground beside her, urging me to sit down too."
    "So I did."
    s "Tell me about yourself. How did you get into fishing?"
    y "Ah, it's not much of a story. Kind of silly, really"
    s "I don't mind, tell me anyways."
    y "Well..."
    menu: 
        "It was because of a video games.":
            y "This is embarrassing but..."
            y "I always loved catching fish in video games when I was younger."
            y "I found it really fun waiting for a tug and reeling it in."
            y "At a certain point, I wanted to try it for real."
            y "I figured it would be fun and useful to learn."
            y "And... well, it was."
            "Shauna let out a thoughtful little hum before responding."
            s "That's not embarrassing at all, it's sweet."
            s "Like you said, it's a pretty worthwhile skill to have."
            s "I think it's pretty cool that one hobby managed to get you into another one."
            y "I guess so, I never really thought of it like that."
            s "Do you still play games?"
            y "Yeah, every now and then. Not as much as I used to."
            s "I see."
            s "Maybe I'll have to get you to show me one of these fishing games sometime."
            y "Yeah, maybe you'll have more luck catching virtual fish."
            s "Hey!"
            "Despite her incredulous tone, she couldn't help but smile."
            "I smiled too."
            s "Listen, unlike you, I've been a fisher since birth!"
            s "My dad was a sailor, and my mom's the best angler I know."
            s "So needless to say, fishing is in my blood."
            s "I've been going on seaside adventures ever since I was just a little tot."
            y "When did you first start?"
            s "Hmm... hard to say. Maybe when I was six?"
            s "My parents got me started pretty young."
            "She hugged, glaring down at her rod."
            s "Not that you'd be able to tell!"
        "I lived by the coast, so it was natural.":
            y "I've always lived by the seaside in a rural little village."
            y "With the ocean so close, it seemed like the natural thing to do."
            y "All the other kids I knew growing up would go fishing in the summer."
            y "So I did too. And eventually, I realized it was a lot of fun"
            y "And a nice way to save on groceries, too."
            y "My parents were a big fan of my newfound talent, so we'd spend a lot of suppers eating fried fish together."
            s "Aww, that's sweet."
            s "It was sort of similar for me... my parents were always really supportive."
            y "Yeah? When did you start fishing?"
            s "Oh cod, I don't even know if I remember. I was just a tiny little thing."
            s "My mom used to love fishing when she was younger, and my dad was a sailor."
            s "They were a match made in heaven. You're not gonna believe this, but I swear they got married on a boat."
            s "And not a big yacht or anything fancy! A little canoe, if you can believe it."
            "I wasn't totally certain if I {i}did{/i} believe it, but I continued to listen along anyways."
            s "I can barely remember it, but they must have taught me to fish when I was real young."
            s "Because I've been fishing for as long as I can remember..."
            s "Probably learned how around the same time I learned to tie my shoes, that's how ingrained it feels."
            y "You say that, but I don't see any fish in your bucket..."
            "She elbowed me in the ribs for that, a small smirk on her lips."
            s "Watch it, $player_name! Don't be saucy."
            "Despite her warning, she didn't look too pressed."
            s "Anyways, like I was saying. It was a lifelong passion for me."
            

            y "In the summer, my options were limited to swimmin"
            "The rest of the day passed by remarkably quick."


label sdate1_away:
    "The fish got away..."
    s "Ahh, you almost got it! Don't sweat it, you'll catch the next one."
    s "Oh!"
    "Shauna's eyes widen as her line twitches."
    s "I got a bite, and it feels like a big one."
    "She focuses, sticking her tongue out in concentration as she eagerly reels the fish in."
    "Just when it looks like she has it, the line goes limp."
    s "Damn, so close." 
    "She shrugs, not looking too bothered."
    y "You'll get 'em next time."
    "She smiles at that, leaning against the dock's railing with her rod still in hand."
    s "Maybe we're both just having an off day."
    y "Maybe."
    "It's quiet for a few moments."



# Label for Molly's route
label molly_route:
    m "Welcome to my route!"
    # Add more dialogue and scenes for Molly's route here
    return
