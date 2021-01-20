transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*1.25 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.30 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.30
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.30 alpha 1.00 yanchor 1.0 ypos 1.03

# This pulls out the character that is talking and makes them bigger
transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*1.25 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.35 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.35
        parallel:
            easein .15 yoffset 0

# This causes the character to sink down
transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.30 alpha 1.00 subpixel True
    easein .5 ypos 1.06

# This makes the character jump
transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.30 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

# Like hop but for a character that is focused
transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.35 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

# This causes the character to dip down for a second and come back up
transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.30 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

# This causes the character to wobble from side to side and up and down
transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.30 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

# This causes the character to fly in
transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.30 alpha 1.00 subpixel True
    easein .25 xcenter x

transform rightin(x=640, z=0.80):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.30 alpha 1.00 subpixel True
    easein .25 xcenter x

# This hides the character
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*1.25 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000

transform t1:
    tcommon(640)
transform t2:
    tcommon(960)
transform t3:
    tcommon(1280)

transform i1:
    tinstant(640)
transform i2:
    tinstant(960)
transform i3:
    tinstant(1280)

transform f1:
    focus(640)
transform f2:
    focus(960)
transform f3:
    focus(1280)

transform s1:
    sink(640)
transform s2:
    sink(960)
transform s3:
    sink(1280)

transform h1:
    hop(640)
transform h2:
    hop(960)
transform h3:
    hop(1280)

transform hf1:
    hopfocus(640)
transform hf2:
    hopfocus(960)
transform hf3:
    hopfocus(1280)

transform d1:
    dip(640)
transform d2:
    dip(960)
transform d3:
    dip(1280)
    
transform l1:
    leftin(640)
transform l2:
    leftin(960)
transform l3:
    leftin(1280)

# Controls the default dissolve speed
define dissolve = Dissolve(0.25)

# Special dissolves for CGs and Scenes
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

# Dissolves the whole scene
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])


# Dissolves out from black for start of a new scene
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# Fade out to black
define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

# Fade out from black
define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

# Controls `wipeleft`'s wipe
define wipeleft = ImageDissolve("images/wipe/left.png", 0.5, ramplen=64)

# Wipes to black and then to a new scene
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/wipe/left.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/wipe/left.png", 0.5, ramplen=64),
    True])

define tpause = Pause(0.25)
