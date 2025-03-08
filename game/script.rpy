# The script of the game goes in this file.

# Declare characters used by this game.
define s = Character("Shauna")
define m = Character("Molly")
define y = Character("Me")
define n = Character("Enthusiastic Ad Narrator")

# Define background music
define audio.bgm = "audio/music.mp3"

# Define styles for menus
style choice_button_text:
    color "#000000"  # Black text for choices

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
image intro = "images/intro-background.png"
image water = "images/water.png"
image pier = "images/pier.png"
image pond = "images/pond.png"
image phone = "images/app-screen.png"
image shauna-profile = "images/shauna-profile.png"
image molly-profile = "images/molly-profile.png"
image shauna_catch = "images/shauna-caught.png"
image molly_catch = "images/molly-caught.png"
image fin = "images/fin.png"

# Button images
image left_button = "images/left.png"
image right_button = "images/right.png"

# Ad images
image ad1 = "images/ad-1.png"
image ad2 = "images/ad-2.png"
image ad3 = "images/ad-3.png"
image ad4 = "images/ad-4.png"
image ad5 = "images/ad-5.png"
image ad6 = "images/ad-6.png"

# Shauna's sprites
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
image shauna surprise2 = "images/sprites/shauna-surprise-2.png"
image shauna blush = "images/sprites/shauna-blush.png"

# Molly's sprites
image molly happy = "images/sprites/molly-happy.png"
image molly smile = "images/sprites/molly-smile.png"
image molly frown = "images/sprites/molly-frown.png"
image molly blush = "images/sprites/molly-blush.png"
image molly neutral = "images/sprites/molly-neutral.png"
image molly surprised = "images/sprites/molly-surprised.png"
image molly thoughtful = "images/sprites/molly-thoughtful.png"

# Label for the beginning of the story
label start:
    # Get the current position of the full song
    $ current_pos = renpy.music.get_pos()
    
    # Switch to instrumental at the same position
    play music ["<from {} loop 0>audio/instrumental.mp3".format(current_pos)] loop

    # Hide the textbox for the ad sequence
    window hide
    
    # Show each ad in sequence
    show ad1 with dissolve
    pause
    show ad2 with dissolve
    pause
    show ad3 with dissolve
    pause
    show ad4 with dissolve
    pause
    show ad5 with dissolve
    pause
    show ad6 with dissolve
    pause
    
    # Show website background for name input
    scene website
    window show
    
    # User inputs their name
    $ player_name = renpy.input("Enter your name: ")
    $ player_name = player_name.strip()  # Remove any leading or trailing whitespace

    # Assign the player's name to character y
    $ y = Character(player_name)

    # Hide textbox before jumping to profile display
    window hide
    jump display_profile

# Label to display the current profile
label display_profile:
    window hide  # Ensure textbox stays hidden
    scene black
    
    # Show current profile
    if current_profile == "shauna":
        scene shauna-profile
    else:
        scene molly-profile
    
    # Display swipe buttons
    call screen profile_buttons
    
    return

# Screen for profile navigation buttons
screen profile_buttons:
    # Left arrow button (switch profiles)
    imagebutton:
        xalign 0.1  # Position on left side
        yalign 0.5  # Center vertically
        idle "images/left.png"
        hover "images/left.png"
        action Function(switch_profile)
    
    # Heart button (using right.png)
    imagebutton:
        xalign 0.9  # Position on right side
        yalign 0.5  # Center vertically
        idle "images/right.png"
        hover "images/right.png"
        action Jump("its_a_catch")

# Define style for profile buttons
style profile_button:
    size 50  # Make buttons larger
    color "#FFFFFF"  # White text
    hover_color "#FF69B4"  # Pink on hover
    background None  # No button background
    padding (20, 20)  # Add padding around the text

label its_a_catch:
    # Show the catch screen based on the current profile
    if current_profile == "shauna":
        scene shauna_catch with dissolve
        $ renpy.pause(2.0)  # Pause to show the catch screen
        jump shauna_route
    elif current_profile == "molly":
        scene molly_catch with dissolve
        $ renpy.pause(2.0)  # Pause to show the catch screen
        jump molly_route

    return

# Label for Shauna's route
label shauna_route:
    scene black
    $ current_message_index = 0
    show screen message_screen
    pause

label shauna_date1:
    scene black
    hide screen message_screen
    scene pier with dissolve
    show shauna happy with dissolve
    s "Hey! Nice to see you in person."
    show shauna smile
    y "Same to you. How's it going?"
    show shauna happy
    s "Pretty good! The weather's looking great and the tide is running in so I'm excited to get fishing!"
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
    "We swap stories and enjoy each other's company, the sun shining down on us."
    "Eventually, I feel a tug on my line."

    # Call the fishing minigame
    $ caught_fish = renpy.call_in_new_context("fishing_minigame")
    
    if caught_fish:
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
    s "I haven't had a single nip on my line yet, but I have a feeling my luck will change soon."
    show shauna smile
    "I smiled."
    y "I'm sure it will. It's still only early, right? There's plenty of time."
    "Shauna nodded in agreement, her hands tightening around her fishing rod."
    jump sdate1_merge

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
    jump sdate1_merge

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
            show shauna smile
            "Shauna let out a thoughtful little hum before responding."
            show shauna happy
            s "That's not embarrassing at all, it's sweet."
            show shauna happy2
            s "Don't you think it's pretty cool that one hobby managed to get you into another one?"
            show shauna smile
            y "I guess so, I never really thought of it like that."
            show shauna surprise
            s "Do you still play video games?"
            show shauna smile
            y "Yeah, every now and then. Not as much as I used to."
            show shauna surprise
            s "I see."
            show shauna happy
            s "Maybe I'll have to get you to show me one of these fishing games sometime."
            show shauna smile
            y "Yeah, maybe you'll have more luck catching virtual fish."
            show shauna cheer
            s "Hey!"
            show shauna smile
            "Despite her incredulous tone, Shauna couldn't help but smile."
            "I smiled too."
            show shauna happy
            s "Listen, unlike you, I've been a fisher since birth!"
            s "My dad was a sailor, and my mom's the best angler I know."
            show shauna happy2
            s "So needless to say, fishing is in my blood."
            s "I've been going on seaside adventures ever since I was just a little tot."
            show shauna smile2
            y "Wow, that's cool. How old were you when you went on your first fishing trip?"
            show shauna surprise
            s "Hmm... hard to say. Maybe when I was three or four?"
            show shauna surprise2
            s "My parents got me started pretty young."
            show shauna neutral
            "She sighed, glaring down at her rod."
            show shauna surprise
            s "Not that you'd be able to tell!"
            show shauna smile
            "I can't help but laugh at that."
            y "Aww... Don't be so hard on yourself. Everyone has their off days."
            "I reach out and wrap my arm around her shoulder, shifting a bit closer to her with a reassuring smile."
            show shauna blush
            "She blushes, and there's a shift in the air. I try to think of what to say to fill the silence."
        "I lived by the coast, so it was natural.":
            y "I've always lived by the seaside in a rural little village."
            y "With the ocean so close, it seemed like the natural thing to do."
            y "All the other kids I knew growing up would go fishing in the summer."
            y "So I did too. And eventually, I realized it was a lot of fun."
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
            s "My mom has always loved fishing in the sea, and my day was a sailor."
            s "They were a match made in heaven. You're not gonna believe this, but I swear they got married on a boat."
            show shauna happy2
            s "And not a big yacht or anything fancy! A little canoe, if you can believe it."
            show shauna smile2
            "I wasn't totally certain if I {i}did{/i} believe it, but I continued to listen along anyways."
            show shauna surprise2
            s "I can barely remember it, but they must have taught me to fish when I was real young."
            s "Because I've been fishing for as long as I can remember..."
            show shauna neutral
            s "Probably learned how to fish around the same time I learned to tie my shoes, that's how ingrained it feels."
            show shauna smile
            y "You say that, but I don't see any fish in your bucket..."
            show shauna shout
            "She elbowed me in the ribs and gave me an indignant look."
            s "Watch it, [player_name]! Don't be saucy."
            show shauna smile
            "Despite her warning, she didn't look too pressed."
            show shauna cheer
            s "Anyways, like I was saying. Fishing is a lifelong passion for me."
            show shauna smile
            y "That's sweet. Honestly, I could listen to you talk about this all day. Your passion is really charming."
            show shauna blush
            "I can't help but smile as I wrap my arm around Shauna's shoulder, shifting a bit closer to her."
            "She blushes, and there's a shift in the air. I try to think of what to say to fill the silence."

label sdate1_ending:
    # REEL HER IN MINIGAME
    
    # reel her in minigame with heart
    $ caught_fish = renpy.call_in_new_context("heart_minigame")
    
    if caught_fish:
        y "You may not have caught anything today, but you definitely reeled me in."
        show shauna cheer
        "She rolls her eyes and laughs. Her smile is infectious."
        show shauna blush
        s "Yeah well... You're quite the catch yourself, you know."
        "She kisses me on the cheek."
        "There's a comfortable silence for a few moments before she speaks again."
        show shauna happy2
        s "Thank you for joining me [player_name], I had an amazing time today. I'd love to go on another fishing date with you sometime soon."
        y "Who says we have to call it a day yet?"
        y "Let's stay here a little longer... See where the day takes us. What do you say?"
        show shauna blush
        "She smiles, her eyes twinkling."
        s "I'd like that."
        "Her fingers intertwine with mine, and her head leans against my shoulder as we watch the sunset together."
        scene black with dissolve
        window hide
        scene fin with dissolve
        pause
        return

    else:
        show shauna frown
        "I try to say something smooth, but the words get jumbled."
        y "You uh… you… fuck. You're kinda like... a fish? I mean..."
        show shauna neutral
        "She makes a face."
        s "Uhh, you good?"
        "I blurt out the worst possible thing."
        y "I just—I feel like I've caught you, you know? Like, I set the bait, and now you're right where I want you."
        show shauna yell
        s "Dude."
        s "...What."
        y "Wait. I didn't mean it like that—"
        s "You scare me, [player_name]."
        "I made a terrible mistake."
        "That day I learned that it's not just fish that fear me."
        "Women now fear me too."
        scene black with dissolve
        window hide
        scene fin with dissolve
        pause
        return

label molly_route:
    scene black
    $ current_message_index = 0
    show screen molly_message_screen
    pause

# Message screen for showing Molly's conversation images in sequence
screen molly_message_screen():
    # Show the current message image, starting from 1
    $ message_number = current_message_index + 1
    if message_number > 0 and message_number <= 6:  # Only show valid images (1-6)
        add "molly-message{}".format(message_number)

    # Add key handling for space and mouse click to advance images
    key "K_SPACE" action [
        SetVariable("current_message_index", current_message_index + 1),
        If(current_message_index >= 5, Jump("molly_date1"))
    ]
    key "mouseup_1" action [
        SetVariable("current_message_index", current_message_index + 1),
        If(current_message_index >= 5, Jump("molly_date1"))
    ]

label molly_date1:
    scene black
    hide screen molly_message_screen
    scene pond with dissolve
    show molly smile with dissolve
    "We chatted for a while about fishing, farming, foraging, and more. Before I knew it, it was time for our date."
    show molly happy
    m "I'm so glad you could make it. I love showing people around my favorite fishing spot."
    y "Thanks for inviting me. This place is beautiful."
    show molly smile
    m "Right? The pond is perfect this time of year. The water's clear and the fish are really active."
    "I notice Molly has a picnic basket and some fishing gear set up nearby."
    show molly happy
    m "I brought some snacks and extra equipment. Have you ever been pond fishing before?"
    
    menu:
        "Yeah, I'm pretty experienced.":
            y "I mostly tend to fish from the coastline, but I've done a fair share of pond fishing as well."
            show molly smile
            m "Oh, that's really interesting. I bet you have a lot of great fishing stories."
            y "I do. I won't get into them now, but maybe on our next date."
            show molly blush
            m "You're so forward. I kind of like it."
            "She seems flustered for a moment before regaining her composure."
        "No, this is my first time.":
            y "Actually, this is my first time. I've only fished in the ocean before."
            show molly happy
            m "Interesting. It shouldn't be too much different, but I'd still be happy to show you the ropes."
    show molly smile
    m "Anyways, for now, why don't we get started? Let's both cast our lines and see what we can catch."
    "I grab some bait from Molly's basket, and we both cast our lines into the pond."
    "For a few moments, the water is still."
    "...Until suddenly, I feel a tug on my line."
    
    # Call the fishing minigame with molly parameter
    window hide
    $ caught_fish = renpy.call_screen("fishing_minigame", game_type="fish", character="molly")
    window show
    
    if caught_fish:
        jump mdate1_catch
    else:
        jump mdate1_away

label mdate1_catch:
    "I caught a carp."
    show molly happy
    m "Wow, nice catch! That's one of the bigger ones I've seen in this pond."
    show molly smile
    y "Thanks! The water's so clear, I could see it coming for the lure."
    m "You're a natural at this. Want to try for another one?"
    jump mdate1_merge

label mdate1_away:
    show molly frown
    "The fish got away..."
    show molly smile
    m "Hey, don't worry about it. That's just how fishing goes sometimes."
    y "Yeah, I guess you're right."
    show molly happy
    m "Besides, the real fun is in the experience, right? Just being out here, enjoying nature..."
    jump mdate1_merge

label mdate1_merge:
    show molly smile
    m "You know, I've been coming to this pond since I was little."
    y "Really? How did you discover it?"
    show molly happy
    m "It's actually a funny story..."
    show molly smile
    m "I used to help my grandmother collect wild herbs and berries. One summer, I wandered off a little too far while looking for the sweetest blackberries."
    show molly blush
    m "Before I knew it, I was completely lost. I was too stubborn to call for help, so I kept walking, hoping I'd recognize something."
    show molly happy
    m "That's when I found this pond. The water was so still, the air smelled like wildflowers... I almost forgot I was lost."
    show molly smile
    m "Eventually, my grandmother found me sitting under an old oak tree, watching the dragonflies dance over the water." 
    m "She just lauged and said, 'Looks like the forest wanted to show you something special today.'"
    show molly happy
    m "And I think she was right."
    show molly smile
    y "What a sweet story. I get why this place is so special to you."
    show molly happy
    m "I come here whenever I need a moment of quiet. Just the water, the wind, the little creatures scurrying around…"
    m "Speaking of which, I saw a heron here the other morning. It was so graceful, standing right at the water's edge. Barely moved at all, just waiting… watching…"
    show molly blush
    m "Kind of like you right now."
    y "Huh?"
    show molly happy
    m "You've been staring at me for a while now. Waiting, watching…" 
    show molly blush
    m "If I didn't know better, I'd say you were trying to reel {i}me{/i} in."
    "A quiet moment settles between you. The sounds of the pond fill the space—gentle ripples on the water, the rustling of leaves in the breeze."
    show molly smile
    m "Well?"
    "The silence lingers. This is your moment."
    # Call the heart minigame with molly parameter
    window hide
    $ caught_fish = renpy.call_screen("fishing_minigame", game_type="heart", character="molly")
    window show
    
    if caught_fish:
        show molly blush
        "I lean in closer, watching as her blush deepens."
        y "You know, I think I caught something better than a fish today."
        m "Oh? And what's that?"
        y "A chance to know you better."
        "She smiles, her eyes sparkling in the afternoon light."
        m "I'd say we both caught something special today."
        "We sit together by the pond, talking and laughing as the sun begins to set, casting golden reflections across the water."
        scene black with dissolve
        window hide
        scene fin with dissolve
        pause
        return
    else:
        show molly frown
        "I attempt to sputter out a cheesy pick-up line, but it fails miserably."
        y "You may have caught- um.. you uh. Shit. Um.."
        m "Are you okay?"
        m "Are you having a stroke?"
        y "No, I'm... FUCK ummm hold on... You... I..."
        m "Oh dear. You really {i}are{/i} having a stroke. Let's get you to the hospital."
        "After a long drive to the hospital in an ambulance, I was diagnosed with a severe case of brain damage."
        "..."
        "There was no second date."
        scene black with dissolve
        window hide
        scene fin with dissolve
        pause
        return
