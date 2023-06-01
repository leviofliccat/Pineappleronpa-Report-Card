## The script of the game goes in this file.
rpy monologue single

## Defining the characters. Using an image attributes allows the use of simpler show/hide sprite functions.

define s = Character("Sean", image= "sean")

define r = Character("player_name", dynamic=True)


## These variables are required/used for the report card screens.
default counter = 1
default current_character = character_names[0]
default selected_level = 0




label start:

    ## For the character name input screen.
    $ player_name = "Pingu"
    show screen enterName
    $ ui.interact()

    label continued:
        $ player_name = player_name.strip()

        if player_name == "":
            $ player_name="Pingu" ## If player types nothing, use this as the player name.

        hide screen enterName
        


    scene bg living room
    with fade

    ## This is the label vital to the function of the report card screen. It updates the information dictionary 
    ## from which the screen function pulls values to have the data of the selected character.
    label character_information:
        
        $ info = characters[counter]
        $ current_character = character_names[counter-1]
        $ level = character_friendship[current_character]
        if renpy.get_screen("report_card"):
            $ ui.interact()
    


    ## The script begins here.    

    # """
    # Some visual novels have extended narration, or multiple blocks of dialogue from the same character. In these cases, typing the name of the character and the quotes multiple times is somewhat redundant. 
    # To cover these cases, Ren'Py supports monologue mode. When dialogue is inside triple-quoted strings, Ren'Py will break the dialogue up into blocks at blank lines. Each block is then used to create its own say statement. Here's an example, with three blocks of narration followed by three lines of dialogue:
    # """




    "The bathroom door squeaks open as Sean wobbles out. He uses his hand on the wall for support."
    
    show sean sad with dissolve

    "{color=#2D70D6}Woah! What happened?{/color}"
    r "A- Are you okay?"
    s shocked "Oh [player_name]! You caught me at a bad time…"
    "{color=#2D70D6}Why is he rubbing his stomach like that?{/color}"
    show sean smirk with vpunch
    s "Phew! I no longer feel like a terrorist threat!"
    r "Are you sure you’re okay?"
    show sean glint with fastblinds
    s "Mee? I’m completely fine! Totally."
    "{color=#2D70D6}I can’t tell if he’s actually okay…{/color}"
    show sean smirk with fastsquares
    s "Actually - hey [player_name], have you ever tried Buldak?"
    r "What’s Booldak?"
    s "Buldak Instant Noodles - Spicy…"
    r "Uhh… I’m not too good with spice…"
    r "I usually pass it on to my dad to finish whenever I have anything spicy…"
    show sean glint with fastblinds
    s "Hmm… In that case - you should get stronger."
    r "What?"
    show sean excited with vpunch
    s "Stronger! Robust! Becoming more powerful!"
    r "What do you mean by that?"
    s explain "In order to become stronger, you need to train!"
    r "Train as in… going to the gym?... Have you been working out too much?"
    "{color=#2D70D6}He sure as hell doesn’t look like it…{/color}"
    s sad "No No No…"
    show sean excited with vpunch   
    s "I’m training my stomach!"
    s "You see… eating spicy food actually makes your stomach resilient and makes your digestive tract able to process other foods easily."
    s "So… I’ve been strengthening my stomach using the epitome of spicy food: {nw}"
    extend sus "Buldak Instant Noodles!"
    "{color=#2D70D6}That logic seems a bit skewed…{/color}"
    "{color=#2D70D6}And why specifically instant noodles?{/color}"
    "{color=#2D70D6}And why specifically this brand??{/color}"    
    s away "There’s the 1x spice - and that’s already really spicy!"
    s ultra "But it can go all the way to 2x and 3x! Rumor has it 4x exists! :o"
    r "…"  
    s smirk "You should train with me. I’ll cook one up for you next time!"
    r "Ah…"
    show sean excited with vpunch 
    s "That’s a yes right? We’ll become stronger together? :)"
    r "H- Hold on… Is that why you came out of the bathroom looking like that?"
    show sean ohshit with hpunch
    s "Uhh…"
    show sean discomfort with Dissolve(0.2)
    s "Ahem. I don’t know what you’re talking about! I was completely fine! Completely and totally fine! I said so - didn’t I?"
    r "I thought it was supposed to make you more resilient to spice?"
    show sean angry with hpunch
    s "Slowly but surely! It’s been a while since I had my last - give me a break!"
    r "Why do you even eat that anyway?"
    show sean excited with vpunch
    s "Because it tastes! All my neurons are activated! I feel alive!"
    show sean explain with Dissolve(0.2)
    s "And to become stronger! I can feel my gut burning up - it’s like birth pains! Birth pains are a good sign - great even!"
    show sean smirk with Dissolve(0.2)
    s "It kinda feels like callouses - but in your stomach!"
    "{color=#2D70D6}Where is he getting these ideas?{/color}"
    r "Haha… As much as I appreciate the offer, I think I’m good…"
    show sean sus with Dissolve(0.2)
    s "Aww… Come on… Just a bit?"
    r "I don’t think I’ll be roasting my insides today for a bit of “training”."
    show sean with Dissolve(0.2)
    s "Hmph - fine… fine…"
    show sean discomfort with hpunch
    "As Sean turns around, a sudden jolt of pain doubles him over, likely originating from the after effects of his recent bathroom break. Clenching his stomach, he awkwardly stumbles away."
    hide sean
    with moveoutright
    r "Don’t overdo it! Your stomach is gonna spill out!"
    "Ignoring the fact that Sean offered me near-lethal volcano noodles, it’s pretty amusing being around him. I feel like I’ve seen a side that not many have seen before."



    # This ends the game.

    return
