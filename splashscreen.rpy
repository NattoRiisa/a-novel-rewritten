label splashscreen:
    scene black
    with Pause(1)

    "This game is not what you've expected. Do you wish to go further?"

    menu:

        "Yes, I do.":
            jump yes

        "No, I don't.":
            jump no

    label yes:

        "Okay."

        jump done

    label no:

        "Leave."

        $ renpy.quit()
        return

    label done:

        show text "NekoNyandere shows you...." with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)
        return
