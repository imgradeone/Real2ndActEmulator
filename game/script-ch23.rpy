image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47
# 铁 骨 铮 铮 Sayori（

label ch23_main:
    show screen notify("当前 ch23")
    # 来点更刺激的
    if renpy.random.randint(0,15) == 0:
        show screen notify("达成成就：死 不 瞑 目 沙 师 弟")
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 at i11 zorder 2
    else:
        scene bg club_day2
        with dissolve_scene_half
    $ chapter = 3
    play music t6
    show yuri 2y5 at t11 zorder 2
    y "Hi, [player]!"
    y "I've been waiting for you."
    y 2d "Are you ready to continue reading?"
    y "I brought my best tea today--"
    show yuri 2f
    show natsuki 4w at f33 zorder 3
    n "Monika!"
    n "I told you not to--"
    n 1g "emm..."
    n "她是不是又双迟到了？"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 1h "Inconsiderate as usual, Natsuki."
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 4c "Excuse me?"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 1r "Must you always interrupt my conversations with your incessant yelling?"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 1o "What are you talking about?!"
    n 1q "You say that like I do it on a regular basis or something."
    n "I just wasn't paying attention, okay? I'm sorry."
    n 4u "Seriously... What's gotten into you lately?"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 2n "Me?"
    y 2o "N-Nothing..."
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n "..."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 2v "Is it really that bad...?"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 2m "See, it {i}is{/i} something."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 3p "I'll get over it!"
    y 3y6 "It's not even anything noteworthy..."
    y 3o "I've just been feeling a little on edge lately..."
    y 3n "A-Anyway, we don't need to talk about it!"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 2q "Well, I just felt like I needed to bring it up."
    n 5q "It's not like I really care or anything..."
    show natsuki at t33 zorder 2
    show yuri 3e
    show monika 1g at l31
    m "Awwwww, man..." # 这里结合 Creeper? Aw man 的 meme，所以不要翻译
    m "我又双叒叕是最后一个到的！"
    show natsuki at f33 zorder 3
    n 2c "Well, [player] just walked in too."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 1f "Were you practicing piano again?"
    show yuri at t32 zorder 2
    show monika at f31 zorder 3
    m 5a "Yeah..."
    m "Ahaha..."
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 1m "You must have a lot of determination."
    y "Starting this club, and still trying to make time for piano..."
    show yuri 1a at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Well, maybe not determination..."
    m 3a "But I guess passion."
    m "It motivates me to work hard for the festival and..."
    m 3n "Um..."
    show monika at t31 zorder 2
    show natsuki at f33 zorder 3
    n 5s "..."
    show natsuki at t33 zorder 2
    show monika at f31 zorder 3
    m 1l "Right..."
    m "I-I forgot..."
    show monika at thide zorder 1
    hide monika
    show yuri at f32 zorder 3
    y 2v "Um, about that, Natsuki..."
    y "We were all talking yesterday, and..."
    y 2t "Well...we decided that we would like to support the festival as well."
    y 2l "However...!"
    y 2h "I understand how you feel about not wanting the club to change."
    y "I think we all kind of feel that way."
    y 2f "So as long as we're all working together, this club will never become something we don't want."
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n "..."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 2v "Um, also..."
    y "If you help us out with the festival..."
    y 3r "...Then I'll buy you a new manga!"
    show yuri 3t at t32 zorder 2
    show natsuki at f33 zorder 3
    n 5h "..."
    n 2z "Ahahaha!"
    n "Sorry, that last part was really funny."
    n 2c "Look..."
    n "I did some thinking about yesterday."
    n 2q "I was a little more hostile than I meant to be..."
    n 1q "I guess I really felt threatened or something."
    n 1h "But I know this is something we're doing together."
    n 1q "Another new member wouldn't hurt, as long as they're cool..."
    n 5w "And I guess another girl would be nice this time..."
    n 5e "...But more importantly, I would hate to see the event suck just because I chose to back out!"
    n "I'm a pro, you know!"
    n 5c "So I'm gonna help too, and we'll make sure it's done right."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 2s "Thank goodness..."
    y "Isn't that great, Monika?"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 2k "...Monika?"
    show natsuki at t33 zorder 2
    show monika 1o at f31 zorder 3
    m "Ah--"
    m 1n "Yeah, that's wonderful!"
    m "It wouldn't be the same without you, Natsuki."
    m 5 "Anyway, [player]..."
    m "What do you want to do today?"
    m "I was thinking we could--"
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 1l "We already have plans today."
    show yuri at t32 zorder 2
    show monika at f31 zorder 3
    m 1r "Ah..."
    m "Is that so, Yuri?"
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 1y6 "That's correct."
    y "[player] is already engaged in a novel that we're reading together."
    y 1y5 "Aren't you glad I've already gotten him into literature, Monika?"
    show yuri 1a at t32 zorder 2
    show monika at f31 zorder 3
    m 2l "I..."
    m "I suppose..."
    m "I was just--"
    m 1r "Actually, it doesn't matter."
    m 1i "It really doesn't."
    m "You guys can do whatever you want."
    show monika at t31 zorder 2
    show yuri at hf32 zorder 3
    y 2y1 "{i}（吼哇！）{/i}{w=0.5}{nw}"
    y 2u "emm...Monika，感谢理解。"
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 at t11 zorder 2
    with wipeleft_scene
    call yuri_exclusive2_2_ch22
    if y_appeal >= 3:
        call poemresponse_start2 from _call_poemresponse_start2
    else:
        call poemresponse_start from _call_poemresponse_start_5
    jump ch23_end

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2])
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b at t32 zorder 2
    with wipeleft_scene
    play music t3
    m "Okay, everyone!"
    m "It's time to figure out the festival preparations."
    m 1i "Let's hurry and get this over with."
    show natsuki 4q at f31 zorder 3
    n "Jeez..."
    n "Why is the mood so weird today?"
    n "Look, even Yuri isn't immune to it."
    show natsuki at t31 zorder 2
    show yuri 4b at f33 zorder 3
    y "Uu..."
    y "Stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2r "Look, can we just get this done?"
    m 2d "I'm going to be printing and assembling all the poetry pamphlets."
    m "Natsuki, I was thinking--"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 2d "I want to make cupcakes!"
    show natsuki 2a at t31 zorder 2
    show monika at f32 zorder 3
    m 2a "...Yeah, that."
    m "Glad we're on the same page."
    m 1m "Yuri, you can..."
    m 1r "...Well, it doesn't matter."
    m 1i "Do whatever you want, as long as you think it'll help."
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2h "Monika..."
    y "I'm not useless, you know!"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2p "I-I know that!"
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 1l "I already know what I'd like to do."
    y 1h "We can't run a successful poetry event without having the right atmosphere for the occasion."
    y "So I'm going to make decorations and set up some nice mood lighting."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2j "There, see?"
    m "That's a great idea!"
    m 1a "And that gives us all something to do."
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2f "Eh?"
    y "What about [player]?"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2b "[player] is going to help me."
    show monika 2a at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4e "Wait, you?"
    n "You have the easiest job, Monika!"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1i "Sorry, but that's just how it is."
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 1f "Like hell it is!"
    n "What are you trying to pull?"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 3h "I-I agree with Natsuki!"
    y "Not only is your work already most suitable for one person..."
    y 3l "But my task is laborious enough to benefit from an extra pair of hands."
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 4c "Mine too!"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 1h "What, your cupcakes?"
    y "Please."
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 1o "说得好像{i}你{/i} TND 知道一样！" # 爆粗口的 Natsuki 是屑（
    n 1x "你只关心如何把 [player] 拴在你和那本白癡才会看的书旁边吧。"
    n 1f "说的是你，{i}还有{/i} Monika！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 2g "嘿！"
    m "我可什么都没做啊！"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3e "Okay, then why not let [player] decide who to help instead of abusing your power?"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1p "I'm not...abusing my power."
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2h "Yes you are, Monika."
    y "Just let [player] make the choice, okay?"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1r "Okay, fine!"
    m "好吧。"
    show monika 1h at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3w "Jeez..."
    n "[player], I know how fed up you are with these two by now."
    n 3c "We can just--"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 2r "Natsuki，你 TM 闭上你的臭嘴，让他自己做决定好吗？" # 爆粗口的 Yuri 是屑（
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 1o "{i}你{/i} TM 才该闭嘴！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1r "Jesus christ..."
    m 1i "这肯定没完没了了。赶快做决定吧，好吗？"
    show monika at t32 zorder 2
    show screen notify("我们会强制把你的鼠标挪动 Monika 上。你大可以试试强行选另外两个。")
    python:
        madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Yuri.", "yuri"), ("Monika.", "monika")], screen="rigged_choice")
    # 我们会强制把你的鼠标挪动 Monika 上。你大可以试试强行选另外两个。
    # 下面是后果。
    if madechoice != "monika":
        show screen notify("达成成就：但是我拒绝！")
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10 # Yuri 的三次元之眼正在凝视你
        pause 3.0
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = fujaowee(80)
        window auto
        menu:
            "[gtext]"
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            # JUST MONIKAAAAAAAAAAAAAAAAAAAAAa
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki at thide zorder 1
        show yuri at thide zorder 1
        hide natsuki
        hide yuri

    m 5a "耶，你选我啦！"
    m "We can meet at your house this weekend."
    m "I promise it'll be fun."
    m "Is Sunday okay with you?"
    show natsuki 1e at f31 zorder 3
    n "你他娘的在逗我吗？" # 爆粗口的 Natsuki 是屑（
    n "不公平啦！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 2i "Natsuki，这非常公平。"
    m "这就是他自己的选择。"
    show monika at t32 zorder 2
    show yuri 3r at f33 zorder 3
    y "No, it's not fair!"
    y "Giving us all this work and then taking [player] for yourself."
    y "What a shameful thing to do!"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2r "Yuri, I didn't even give you any work."
    m 2i "我都让你自己决定要做什么。"
    m "你现在有一点点不讲道理。"
    stop music
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2y4 "我又不讲道理了？"
    y 2y3 "啊哈哈哈哈哈！"
    y "Monika，没想到你这么妄自尊大，又自私自利！"
    y "每次你只要没能参与进来，就把 [player] 从我身边拖走，次次如此。"
    y 1y1 "你是嫉妒吧？"
    y "还是疯了？"
    y 1y3 "还是你对自己的憎恨溢了一地，就开始随便往别人身上泼呢？"
    y 1y4 "这边强烈建议你去试下当晴天娃娃呢。"
    y "对你的精神健康会有 hin 大的帮助。"
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 5u "Yuri，你属实吓到我了..."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1r "Natsuki，咱们先撤吧。"
    m 1i "我认为她不想让我们在这里继续待着了。"
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2y3 "看吧，想让你们滚不是很简单嘛。"
    y "我仅仅只是想要和他再多独处那么一会。"
    y "这样的要求很过分吗？"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Yuri 跟在 Monika 和 Natsuki 后面，走到教室门。"
    show monika 5a at t11 zorder 2
    m "嘿，[player]..."
    m "Yuri 真的有点那啥..."
    show monika at thide zorder 1
    hide monika
    "Monika 在欢声笑语中被 Yuri 推出门外。"

    play music t10y
    show yuri 2m at t11 zorder 2
    y "终于啊。"
    y 2y1 "久等了！！！"
    y 2s "这就是我真心想要的！"
    y 1y6 "[player]，没必要和 Monika 度过周末了。"
    y "别听她的。"
    y 1y5 "就来我家吧。"
    y 3y5 "一整天就只有我们两个..."
    y "是不是很完美啊？"
    y 3y1 "啊哈哈哈哈！"
    y 3y4 "哇... 我是不是有毛病...？"
    y "但你知道吗？"
    y 1y3 "老子才不在乎呢！"
    y "我这辈子都没有感到这么爽过。"
    y 1y4 "和你在一起就已经是超乎我想象的极致快乐了。"
    y "你知道吗？"
    y "我对你“上瘾”了。"
    y 3y4 "如果不和你在一起，我就要死了。"
    y 4a "如果有那么关心你的人，那感觉是不是很爽？"
    y "还是那种一辈子都想围着你转的那种。"
    y 2y6 "不过如果这种感觉很好..."
    y 2y4 "那么为什么可怕的事情还是要发生呢？"
    y 2y6 "也许这就是我最初尝试阻止自己的原因..."
    y "但是现在这种爱的感觉特别强烈了。"
    y 3y1 "[player]，即便这样，我也不在乎了！"
    y 3y1 "[player]！"
    y "我一定要告诉你！"
    y 3y4 "我...我彻彻底底地爱上你了！"
    y "我感觉我身体的每一块地方...还有每一滴血...都在喊着你的名字。"
    y 3y3 "我也不在乎后果了！"
    y "我也不在乎 Monika 有没有在那里偷听了！"
    y 3w "求你了，[player]，请一定要明白我有多爱你啊。"
    y 3m "我特别爱你，甚至一度偷你的笔去自///慰。"
    y 3y4 "我只想拉开你的表//皮，在你的身体里游走。"
    y 3y6 "我想让你永远属于我。"
    y "我也将永远属于你。"
    y "听上去是不是很棒呢？"
    y 3s "所以，[player]，告诉我。"
    y "告诉我你想成为我的爱人。"
    y "你接受我的感情吗？"

    menu:
        "是的。":
            jump yuri_kill
        "不！":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    pause 1.0
    # Goodbye
    # Instead of deleting saves, we'll use after_load label to return to Yuri whenever a save is loaded
    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "...啊哈哈哈。"
    y "啊哈哈哈哈哈哈哈！"
    $ style.say_dialogue = style.normal
    y 3y5 "啊哈哈哈哈哈哈哈哈！"
    $ style.say_dialogue = style.edited
    y 3y3 "啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal
    if persistent.alt_safe_mode:
        call screen dialog("为响应“清朗”未成年人暑期网络环境专项整治，\nYuri 的自裁动画已跳过。",Return())
        jump yuri_kill_3
    else:
        play sound "sfx/yuri-kill.ogg" # 去世预警 + 变调版 Play With Me
        pause 1.43
        show yuri stab_1
        pause 0.75
        show yuri stab_2
        show blood:
            pos (610,485)
        pause 1.25
        show yuri stab_3
        pause 0.75
        show yuri stab_2
        show blood:
            pos (610,485)
        show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
        pause 1.25
        show yuri stab_5
        pause 0.70
        show yuri stab_6:
            2.55
            easeout_cubic 0.5 yoffset 300
        show blood as blood2:
            pos (635,335)
        pause 2.55
        hide blood
        hide blood2
        pause 0.25
        play sound fall
        pause 0.25
        scene black
        pause 2.0

        scene black
        show y_kill
        with dissolve_cg
        jump yuri_kill_2
label yuri_kill_2:
    $ quick_menu = True
    python:
        _history_list = []
        m.add_history(None, "", """Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with""")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = fujaowee(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = fujaowee(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "好哇，是学园祭时间！"
    show natsuki 4k at t11 zorder 2
    n "哇，你比我早到？"
    n "我觉得我已经够zao--{nw}"
    show natsuki scream at h11
    n "噫啊！"
    n "啊↑啊↗啊→啊↘啊↓啊↓啊↓啊↓！！！"
    pause 1.0
    show natsuki scream at h11
    pause 0.75
    show natsuki vomit at h11
    pause 1.25
    show natsuki at lhide
    hide natsuki
    "Natsuki 溜了。"
    m "..."
    show monika 2b at t11 zorder 2
    m "我在这呢！"
    m 2d "[player]，刚刚是不是发生了什么？"
    m "Natsuki 刚刚从我身边跑了..."
    m 2i "...哦..."
    m "...口我。"
    m 2r "..."
    m 2l "啊哈哈哈！"
    m "有点遗憾啊。"
    m 2d "等等，[player]，你是不是整个周末都要在这里？"
    m "天哪..."
    m 2g "我都没发现这游戏爆得这么厉害。"
    m "肥肠抱歉！"
    m "这肯定很无聊的说..."
    m 2e "我帮你整理一下，好伐？"
    m "给我一点点时间..."
    $ consolehistory = []
    call updateconsole("os.remove(\"characters/yuri.chr\")", "ACCESS DENIED: No permission in emulator")
    pause 1.0
    call updateconsole("os.remove(\"characters/natsuki.chr\")", "ACCESS DENIED: No permission in emulator")
    pause 1.0

    m 2a "可以了。"
    m 2j "我现在想拿一个纸杯蛋糕了。"
    $ gtext = glitchtext(10)
    "Monika 从 [gtext] 的托盘里拿出箔纸并拿走了一个纸杯蛋糕。"
    m 2b "啊，真香！"
    m "我肯定要拿的呐，毕竟这是最后一次了。"
    m 2a "你懂的，在她们彻底消失之前。"
    m "...但怎么说，我真的不能让你再等下去了。"
    m 2j "就陪我，好吧？"
    m 2a "一下下就好。"

    $ persistent.cleared = True
    $ persistent.player_level = 1

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    scene black
    pause 3.0

# TODO: 一刷后初级能力者标识

    return


