# 假二周目开头
label fakeintro:
    $ delete_all_saves() # 炸档使我快乐
    show screen notify("存档已删除。")
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48) # 删 Sayori 使我快乐
    stop music
    $ config.window_hide_transition = None
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2
    $ s_name = glitchtext(12)

    s "[gtext]"
    "我看见一个吵吵闹闹的女孩不断挥着手向我跑来，仿佛要把全世界的注意力都聚焦在她身上一样。"
    "她叫 [s_name]，我的邻居，也是我的儿时玩伴。"
    "你能理解，你不一定会和她交朋友，但你们俩在一起太久了，很多事情就这样顺其自然了的感觉吗？"
    "我们以前经常这样一起上学，但上了高中以后她睡懒觉的频率就越来越高，之后我也就有点懒得等她了。"
    "但她这样狂追不舍，弄得我好想逃跑。"
    "不过，我也别无选择，只好叹了口气在路口等着好让 [s_name] 赶上我。"

    show sayori glitch at t11 zorder 2
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves() # 记忆清除
    show screen notify("存档已删除。您现在已经进入真正的二周目。")
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat

    jump ch20_from_ch10