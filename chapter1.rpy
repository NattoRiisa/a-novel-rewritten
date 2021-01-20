label start:

    if persistent.mc is None:
        $ mc = renpy.input("What is your name?")
        $ persistent.mc = mc
        "Welcome, [mc]."
    else:
        $ mc = persistent.mc
        "Welcome back, [mc]!"

    "What are your pronouns?"
    menu:

        "He / Him .":
            jump male

        "She / Her .":
            jump female

        "They / Them .":
            jump nonbinary

    label male:

        $ persistent.male = True
        $ persistent.female = False
        $ persistent.nonbinary = False

        jump chapter_1

    label female:

        $ persistent.male = False
        $ persistent.female = True
        $ persistent.nonbinary = False

        jump chapter_1

    label nonbinary:

        $ persistent.male = False
        $ persistent.female = False
        $ persistent.nonbinary = True

        jump chapter_1

label chapter_1:

    if persistent.male:
        "So you use He / Him pronouns?"
        menu:

            "Yes.":
                jump confirm

            "No.":
                jump start

    elif persistent.female:
        "So you use She / Her pronouns?"
        menu:

            "Yes.":
                jump confirm

            "No.":
                jump start

    elif persistent.nonbinary:
        "So you use They / Them pronouns?"
        menu:

            "Yes.":
                jump confirm

            "No.":
                jump start


label confirm:
    "Okay."
    $ persistent.genderchosen = True
    " "
    scene bg
    jump c1start

label debugging:
    show nat angry
    n "Testing."
    show nat angry2
    n "Testing."
    show nat breakdown
    n "Testing."
    show nat closed
    n "Testing."
    show nat closed2
    n "Testing."
    show nat closed3
    n "Testing."
    show nat cry
    n "Testing."
    show nat cry2
    n "Testing."
    show nat curious
    n "Testing."
    show nat curious2
    n "Testing."
    show nat happy
    n "Testing."
    show nat happy2
    n "Testing."
    show nat irritated
    n "Testing."
    show nat natural
    n "Testing."
    show nat natural2
    n "Testing."
    show nat sarcastic
    n "Testing."
    show nat shocked
    n "Testing."
    show nat shocked2
    n "Testing."
    show nat sweat
    n "Testing."
    show nat terrified
    n "Testing."
    show nat terrified2
    n "Testing."
    show nat terrified3
    n "Testing."
    menu:
        n "Did any of my sprites work?"

        "Yes!":
            n "Great!"
        "No.":
            n "Try again!"

    return

label c1start:
    scene room with dissolve
    "I woke up to my bed."
    "Today's Monday, and I've gotta go to college right now. It's 6 AM."
    mc "Ah! I gotta hurry up and arrive!"
    "I said, as I quickly do all my things."
    "I change my clothes to the school uniform and quickly went outside."
    scene neighborhood with dissolve
    "I went out."
    "Then I saw 2 people."
    na "Heyyy [mc]!!"
    na "Hey! Wait up!"
    "The sweet and very friendly girl, Nat, has arrived, with the very friendly, yet a clumsy girl, Sour."
    show nat natural at t2
    n "How's your sleep?"
    mc "Oh come on, don't talk about it too much."
    show nat happy
    n "Ehehe!"
    show nat happy2
    n "But seriously tho, did you sleep well last night?"
    show nat smile
    mc "Uhhhh.."
    show nat shocked at h2
    n "You didn't!?"
    "The girl who worries about me sleeping, is Nat."
    "She was very friendly, but she's ready to fight to protect."
    "We used to be best friends ever since she moved by the time she's 13 with her parents."
    if persistent.male:

        "Nat's 23. While I, a male, is already 20."

    elif persistent.female:

        "Nat's 23. While I, a female, is already 20."

    elif persistent.nonbinary:

        "Nat's 23. While I, a person, is already 20."

    "But the thing is, she protects us alot."
    "Which makes me a bit worried, because I care for her."
    show nat irritated at s2
    n "C'mon! I told you to sleep early!"
    "Of course.."
    mc "Yet I see you on my door at 2 in the morning when I peeked at my window a little."
    show nat shocked at h2
    n "Eh!?"
    show nat shocked at t1
    show sour curious2 at t3
    so "Come on, babe. I know that too. Because I also peeked at my window."
    "The yellow lemon looking girl, is Sour."
    "She's a very interesting 22 year old female who's Nat's very cute waifu."
    "She may be clumsy, but at least she has a very soft spot for the both of us."

    "Well. Here we go. This is just the three of us, living as neighbors."
    "We'll be known as the Purrfect Trios by then."

    "And once Sour finished her sentence."
    "Nat then looked at me with her pretty cute eyes."

    show nat curious
    n "By the way. Where should we go for today?"
    "She said, as I was looking at her back, barely reacting to the eyes outside but on the inside."
    mc "Hmm... No idea."
    mc "Where should we go..? The park?"
    show nat happy2
    n "Or how about we go to the cafe?"
    so "Or instead of going to the cafe, what about going to the beach?"
    show nat irritated
    n "Oh man, all three of them are so good."
    show nat breakdown
    n "What should we do!?"
    "Nat said as she's panicking because she has to pick one of the three places."
    so "Oh no.."
    show nat happy2 at h1
    n "Oh! I have an idea!"
    show nat happy
    n "We should let [mc] pick to make it easier!"
    mc "Eh?"
    n "[mc]! Where do you wanna go?"
    "She said as she's excited to ask me that."
    menu:
        "Where should I go?"

        "The park.":
            $ persistent.park = True
            $ persistent.cafe = False
            $ persistent.beach = False
            $ persistent.house = False
        "The cafe.":
            $ persistent.park = False
            $ persistent.cafe = True
            $ persistent.beach = False
            $ persistent.house = False
        "The beach.":
            $ persistent.park = False
            $ persistent.cafe = False
            $ persistent.beach = True
            $ persistent.house = False
        "How about we just stay at my house?":
            $ persistent.park = False
            $ persistent.cafe = False
            $ persistent.beach = False
            $ persistent.house = True

    if persistent.park:
        mc "Let's go to the park."
        show nat happy at h1
        n "Alright then! Sounds peaceful enough!"
        so "Okay. That'll do."
        "And then all three of us went to the park."
        jump park

    elif persistent.cafe:
        mc "Then we can go to the cafe for a drink."
        show nat happy at h1
        n "Ooh! Can I get a strawberry milkshake once we go there?"
        so "Lemon milkshake as well?"
        mc "Alright, alright."
        n "Yay!"
        so "Yay!"
        "And then all three of us went to the cafe."
        jump cafe

    elif persistent.beach:
        mc "We can swim and play volleyball once we go to the beach!"
        show nat happy at h1
        n "Ooh! I like swimming."
        so "I like volleyball."
        "And then all three of us went to the beach."
        jump beach

    elif persistent.house:
        mc "How about we just stay at my house instead?"
        show nat shocked at h1
        n "E-Eh!?"
        so "R-Really? Is that so?"
        mc "I mean. Why not?"
        n "Hm... Alright!"
        so "I mean. Sure. Your house is beautiful."
        "And then all three of us went to my house. Nat and Sour are looking forward to visit my house right now."
        jump house

label after_choice:
    show nat
    n "Now that's the stuff!"
    if persistent.park:
        n "It was so peaceful in there..."
    elif persistent.cafe:
        n "The food was so delicious!"
    elif persistent.beach:
        n "The fine weather, the sand, everything's amazing!"
    elif persistent.house:
        n "Your house is impressive!"
    if persistent.park or persistent.cafe or persistent.beach:
        mc "Is that so?"
    elif persistent.house:
        mc "Thank you very much!"

        mc "I guess we should go to our own homes to rest.."

    s "Alright!"
    "Pre-Alpha 2"
    return
