# script.rpy


# Define characters with images
define hak = Character("Hak", image="characters/hak.jpg")
define yona = Character("Yona", image ="characters/yona.jpg")
define soowon = Character("Soo-Won", image="characters/soowon.jpg")
define creepy = Character("creepy", image="characters/creepy.jpg")


# Define images
define not_my_problem = "not_my_problem.png"
define yona_good_morning = "yona_good_morning.png"
define kids_in_snow ="kids_in_snow.png"
define kids_all_three = "kids_all_three.jpg"
define kind_soo_won_kid= "kind_soowon_kid.jpg"
define yona_hiding_hak = "yona_hiding_hak.jpg"
define yona_looking_at_hairprin = "yona_looking_at_hairpin.jpg"
define hair_pin_scene = "hair_pin_scene.jpg"
define yona_walking_around_castle.jpg = "yona_walking_around_catle.jpg"
define yona_happy_in_mirror = "yona_happy_in_mirror"
define yona_beautiful = "yona_beautiful"
define dissatified_yona_mirror = "dissatified_yona_mirror.jpg" 
define yona_running_to_hak = "yona_running_to_hak.jpg"
define yona_traumatized= "yona_traumatized.jpg"
define soowon_hugging_yona = "soowoon_hugging_yona.jpg"
define soowon_blood ="soowoon_blood.jpg"
define soowon_and_yona_horse ="yona_on_hore.jpg"
define happy_ending = "happy_ending.jpg"
define hak_hugging_yona = "hak_hugging_yona.webp"
define hak_smiling= "hak_smiling.webp"
define hak_concerned = "hak_concerned.jpeg"
define soowon_greeting = "soowon_greeting_yona.webp"
define soowon_pat_yona = "soowon_yona_pat_head.jpg"
define yona_hair = "yona_hair.png"
define all_three_laughing = "all_three_as_adults"
define yona_mirror = "yona_mirror.jpg"
define first_scene= "first_scene.jpg"



init:
    $ renpy.fullscreen = True

label start:
    scene first_scene
    "Once upon a time in the Kingdom of Kouka..."

    # ... (previous code)

    # Key scene: Yona looking into the mirror
    scene yona_mirror 
    yona "Ugh, why does my hair never behave?"

    scene 

    # Change expression to a worried one
    scene yona_hair
    yona "Soowon  will be here soon. I can't look like a mess!"


    # Key scene: Yona excited to see Soo-Won after years
 
    scene  yona_happy_in_mirror  
    yona "Soo-Won is coming! It's been years since I last saw him."

    # Add more expressions and dialogue...

    scene yona_good_morning 
    yona "Good morning Soo-Won!"

    # Key scene: Yona reminiscing about childhood with  Soo-Won
    scene kind_soo_won_kid
    yona "Kind Soo-won who has been there by my side since we were children."


    # Add more expressions and dialogue...

    # Key scene: Yona receives a birthday gift from Soo-Won
    scene soowon_pat_yona
    soowon "Happy birthday, Yona. I got you this."
    scene hair_pin_scene
    yona "A hairpin? Soo-Won, it's lovely! I'll cherish it forever."

    # Add more expressions and dialogue...

    # Key scene: Hak interrupts, and Soo-Won defends Yona
    scene hak_as_teenager_upset
    hak "Well, well, trying to impress Soo-Won with that wild hair again?"
    yona "Hak, not now!"

    soowon "Hak, you know Yona looks beautiful as always."


    #Scene
    scene all_three_laughing
    yona "(thinking: I can't believe Soo-Won called my beautiful)"
    

    # Add more expressions and dialogue...

    # Key scene: Creepy man approaches Yona
    scene creepy_man_approach
    creepy "Hey, beautiful. How about a dance?"


    show not_my_problem
    hak "What do you want?"
    show hak serious
    hak "Need help, Red?"

    # Add more expressions and dialogue...

    # Key scene: Hak pretends to be Yona's boyfriend
    scene hak_pretend
    show hak pretend_bf
    creepy "Oh, sorry! Didn't know she was taken."

    yona  "Hak, pretending to be my boyfriend... my heart is pounding."

    # Add more expressions and dialogue...

    # Key scene: Yona walking around the castle, Soo-Won on a horse
    scene castle_walk
    show yona normal
    yona "Soo-Won!"

    show Soo-Won horse
    soowon "Yona! Want to join me for a ride?"

    yona "(Thinking:)I don't want to embarrass myself, but I can't say no to Soo-Won"

 
