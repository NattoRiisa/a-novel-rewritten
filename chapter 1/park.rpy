# - Park! -
label park:
    scene park with dissolve
    "We arrived at the park, looking around peacefully."
    "Nat is just drawing right now."
    "While Sour on the other hand, is reading the manga for today."
    menu:
        "Now who should I talk to?"
        "Nat.":
            "Okay. Nat it is then."
            $ persistent.natchosen1 = True
            $ persistent.sourchosen1 = False
            jump park_nat
        "Sour.":
            "Okay. Sour it is then."
            $ persistent.sourchosen1 = True
            $ persistent.natchosen1 = False
            jump park_sour
        "Try to talk to both of them.":
            "Okay, i'll try to interact with the two of them."
            jump park_both


label park_nat:
    "I walk to Nat, as she's looking at her drawing pad, still drawing herself and someone."
    mc "Hello!"
    show nat smile at t2
    "Nat looked at me with pretty cute eyes."
    n "Hey [mc]!"
    mc "How are you?"
    show nat happy
    n "I'm good! What about you?"
    mc "I'm fine!"
    n "Do you wanna see my drawing?"

    #scene nat_drawing
    "You have reached park_nat pre-alpha phase."
    return
label park_sour:
    "I walk to Sour, as she's looking at her daily MHA manga."
    mc "Hey!"
    "Sour looked at me with very beautiful and sophisticated eyes."
    so "Oh hey [mc]. What's up?"

    "You have reached park_sour pre-alpha phase."
    return
label park_both:
    "I went to the two of them, as they're both drawing and reading manga together, they're both proud."
    mc "Hi!"
    "They both looked at me with nice, fancy, and adorable eyes."
    n "Hey [mc]!"
    so "Oh hello [mc]."
    n "What'cha doing?"

    "You have reached park_both pre-alpha phase."
    return
