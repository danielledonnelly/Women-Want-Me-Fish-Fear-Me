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

image shauna cheer = "images/sprites/shauna-cheer.png"
image shauna frown = "images/sprites/shauna-frown.png"
image shauna happy = "images/sprites/shauna-happy.png"
image shauna happy2 = "images/sprites/shauna-happy-2.png"
image shauna neutral = "images/sprites/shauna-neutral.png"
image shauna neutral2 = "images/sprites/shauna-neutral-2.png"
image shauna shout = "images/sprites/shauna-shout.png"
image shauna smile = "images/sprites/shauna-smile.png"
image shauna smile2 = "images/sprites/shauna-smile-2.png"
image shauna surprise = "images/sprites/shauna-surprise.png"
image shauna surprise = "images/sprites/shauna-surprise-2.png"


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
    s "Hey, it looks like we're a match. Or a 'catch', I guess."
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
    show shauna happy
    s "Hey! Nice to see you in person."
    show shauna smile
    y "Same to you. How's it going?"
    show shauna happy
    s "Not bad! The weather's looking great, so I'm excited to get some fishing done today."
    show shauna smile
    "I notice that she has some seats set up at the pier, along with a cooler and a tackle box."
    y "Looks like you came prepared."
    show shauna happy2
    s "I always do! You never know what you'll catch out here."
    s "I've got some snacks in the cooler, too. Help yourself if you get hungry."
    show shauna smile2
    y "Thanks, I appreciate it."
    y "Bring any gummy worms today?"
    show shauna cheer
    "She laughs."
    s "I did, actually. They're one of my go-to fishing snacks."
    show shauna smile2
    s "But I've got plenty of real bait too, don't worry."
    show shauna cheer
    s "C'mon, let's get to it! The fish won't catch themselves."
    show shauna smile
    "The two of us settle in, casting our lines out into the water."
    "Even though there don't seem to be many fish out and around, time flies by."
    "We swap stories and enjoy each other's company, the sun shining down on us ."
    "Eventually, I feel a tug on my line."
    # Fishing minigame goes here

    
    # Run the fishing minigame
    label fishing_minigame:
        $ renpy.run(["python", "fishing.py"])
        if fishing.caught:
            jump sdate1_catch
        else:
            jump sdate1_away


label sdate1_catch:
    show shauna smile
    "I caught a tuna."
    show shauna cheer
    s "Nice work! That's a pretty big one. The fish around here tend to be small, so that's quite the feat."
    show shauna smile2
    y "Thanks!"
    show shauna happy
    s "I haven't had a single nip on my line yet, but I have a feeling my luck with change soon."
    show shauna smile
    "I smiled."
    y "I'm sure it will. It's still only early, right? There's plenty of time."
    "Shauna nodded in agreement, her hands tightening around her rod."

label sdate1_away:
    show shauna surprise
    "The fish got away..."
    s "Ahh, you almost got it! Don't sweat it, you'll catch the next one."
    show shauna shout
    s "Oh!"
    "Shauna's eyes widen as her line twitches."
    show shauna surprise2
    s "I got a bite, and it feels like a big one."
    show shauna frown
    "She focuses, her expression serious as she eagerly reels the fish in."
    "Just when it looks like she has it, the line goes limp."
    show shauna shout
    s "Damn, so close." 
    show shauna frown
    "She shrugs, not looking too bothered."
    show shauna smile
    y "You'll get 'em next time."
    "She smiles at that, leaning against the dock's railing with her rod still in hand."
    show shauna happy
    s "Maybe we're both just having an off day."
    show shauna smile
    y "Maybe."
    "It's quiet for a few moments."
    "I may not have been able to catch anything yet, but I wasn't about to give up yet."

label sdate1_merge:
    show shauna happy2
    s "So tell me about yourself. How did you get into fishing?"
    show shauna smile2
    y "Ah, it's not much of a story. Kind of silly, really."
    show shauna surprise
    s "I don't mind, tell me anyways."
    show shauna smile
    y "Well..."
    menu: 
        "It was because of a video games.":
            y "This is embarrassing but..."
            y "I've always loved catching fish in video games, ever since I was a kid."
            y "I found it really fun waiting for a tug and reeling it in."
            y "At a certain point, I wanted to try it for real."
            y "I figured it would be fun and useful to learn."
            y "And... well, it was."
            show shauna smile
            "Shauna let out a thoughtful little hum before responding."
            show shauna happy
            s "That's not embarrassing at all, it's sweet."
            s "Like you said, it's a pretty worthwhile skill to have."
            show shauna happy2
            s "I think it's pretty cool that one hobby managed to get you into another one."
            show shauna smile
            y "I guess so, I never really thought of it like that."
            show shauna surprise
            s "Do you still play games?"
            show shauna smile
            y "Yeah, every now and then. Not as much as I used to."
            show shauna neutral
            s "I see."
            show shauna happy
            s "Maybe I'll have to get you to show me one of these fishing games sometime."
            show shauna smile
            y "Yeah, maybe you'll have more luck catching virtual fish."
            show shauna cheer
            s "Hey!"
            show shauna smile
            "Despite her incredulous tone, she couldn't help but smile."
            "I smiled too."
            show shauna happy
            s "Listen, unlike you, I've been a fisher since birth!"
            s "My mom was a sailor, and my dad's the best angler I know."
            show shauna happy2
            s "So needless to say, fishing is in my blood."
            s "I've been going on seaside adventures ever since I was just a little tot."
            show shauna smile2
            y "When did you first start?"
            show shauna surprise
            s "Hmm... hard to say. Maybe when I was six?"
            s "My parents got me started pretty young."
            show shauna neutral
            "She sighed, glaring down at her rod."
            show shauna shout
            s "Not that you'd be able to tell!"
        "I lived by the coast, so it was natural.":
            y "I've always lived by the seaside in a rural little village."
            y "With the ocean so close, it seemed like the natural thing to do."
            y "All the other kids I knew growing up would go fishing in the summer."
            y "So I did too. And eventually, I realized it was a lot of fun"
            y "And a nice way to save on groceries, too."
            y "My parents were a big fan of my newfound talent, so we'd spend a lot of suppers eating fried fish together."
            show shauna happy
            s "Aww, that's sweet."
            show shauna happy2
            s "It was sort of similar for me... my parents were always really supportive."
            show shauna smile2
            y "Yeah? When did you start fishing?"
            show shauna surprise
            s "Oh cod, I don't even know if I remember. I was just a tiny little thing."
            show shauna happy
            s "My dad used to love fishing when he was younger, and my mom was a sailor."
            s "They were a match made in heaven. You're not gonna believe this, but I swear they got married on a boat."
            show shauna happy2
            s "And not a big yacht or anything fancy! A little canoe, if you can believe it."
            show shauna smile2
            "I wasn't totally certain if I {i}did{/i} believe it, but I continued to listen along anyways."
            show shauna surprise2
            s "I can barely remember it, but they must have taught me to fish when I was real young."
            s "Because I've been fishing for as long as I can remember..."
            show shauna neutral
            s "Probably learned how around the same time I learned to tie my shoes, that's how ingrained it feels."
            show shauna smile
            y "You say that, but I don't see any fish in your bucket..."
            show shauna shout
            "She elbowed me in the ribs for that, giving me an indignant look."
            s "Watch it, $player_name! Don't be saucy."
            show shauna smile
            "Despite her warning, she didn't look too pressed."
            show shauna happy
            s "Anyways, like I was saying. It was a lifelong passion for me."

label sdate1_ending:
    # REEL HER IN MINIGAME
    show shauna surprise
    "I put my arm around her, and there's a shift in the air."
    show shauna smile
    "A light blush dusts her cheeks, but she doesn't pull away."
    y "You may not have caught anything today, but you definitely reeled me in."
    show shauna cheer
    "She rolls her eyes and laughs at the cheesy line."
    show shauna happy
    s "Yeah well... You're quite the catch yourself."
    "She kisses me on the cheek."
    "Her smile softens as she turns to face the horizon, the sun beginning to dip below the water."  
    "We both sit there in comfortable silence, watching as the sky shifts into hues of pink and orange."  

# Label for Molly's route
label molly_route:
    m "Welcome to my route!"
    # Add more dialogue and scenes for Molly's route here
    return
