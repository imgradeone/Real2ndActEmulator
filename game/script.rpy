# Entry point
label start:
    if persistent.sayoricursor:
        $ config.mouse = {"default": [
                            ("gui/mouse/s_head.png", 0, 0),
                            ]}
    else:
        $ config.mouse = None

    python hide:
        persistent.special_poems = [0,0,0]
        a = range(1,12)
        for i in range(3):
            b = renpy.random.choice(a)
            persistent.special_poems[i] = b
            a.remove(b)

    $ persistent.seen_eyes = None
    $ persistent.seen_sticker = False

    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # 可以修改女主的名字
    $ s_name = "Sayori" # 可选译名：纱世里（推荐）、莎世里、纱悠里
    $ m_name = "Monika" # 推荐译名：莫妮卡
    $ n_name = "女孩 2" # 可选译名：夏树（推荐）、娜苏琪
    $ y_name = "女孩 1" # 推荐译名：优里

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    

    # 确定好 label，然后改动下面几行
    if persistent.cleared:
        call gameconsole_intro
    else:
        if persistent.playthrough == 0:
            call warning from _call_warning
        elif persistent.playthrough == 1:
            call fakeintro from _call_fakeintro
        else:
            call ch20_main from _call_ch20_main
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
