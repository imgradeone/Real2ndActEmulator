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
        if persistent.recording:
            scene bg club_day
        else:
            scene bg club_day2
        show yuri 2 at i11 zorder 2
    else:
        if persistent.recording:
            scene bg club_day
        else:
            scene bg club_day2
        with dissolve_scene_half
    $ chapter = 3
    play music t6
    show yuri 2y5 at t11 zorder 2
    y "嗨，[player]！"
    y "我一直都在等你呢。"
    y 2d "你准备好继续看书了吗？"
    y "我今天带了最好的茶--"
    show yuri 2f
    show natsuki 4w at f33 zorder 3
    n "Monika！"
    n "我跟你说过--"
    n 1g "emm..."
    n "她是不是又双迟到了？"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 1h "Natsuki，你还是和平常一样自私啊。"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 4c "WTF？"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 1r "难道你就那么喜欢用唧唧歪歪的方式打断我说话吗？"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 1o "你 TN 都在说什么？！"
    n 1q "你认为我每天都这样吗？"
    n "我刚刚真的只是没太注意，我错了。"
    n 4u "说真的...你最近到底怎么了？"
    if n_appeal >= 2:
        n "你听我说..."
        n "我已经反思过昨天的行为了。"
        n 2q "我确实说得有点过分了..."
        n 1q "一定是我当时觉得被吓到了之类的。"
        n 1h "我知道我们都在努力让社团变好。"
        n 1q "再来一两个新成员也不会怎么样，除非他们性格差到爆..."
        n 5w "我觉得这次再来一个女生的话，也挺好的..."
        n 5u "所以..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "Natsuki..."
        $ style.say_dialogue = style.edited
        y 1f "没人在乎的。"
        y "你咋不去钻到售货机底下捡捡硬币呢？"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "--！"
        n 1r "..."
        n 12f "..."
        show natsuki at thide
        hide natsuki
        $ pause(1.0)
        show monika 1g at l31
        m "Awwwww, man..." # 这里结合 Creeper? Aw man 的 meme，所以不要翻译
        m "我又双叒叕是最后一个到的！"
        show yuri zorder 3 at f32
        y 1f "你又去练钢琴了？"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "对的..."
        m "啊哈哈..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "那你的毅力挺强的。"
        y "组织这个社团，还要挤出时间练钢琴..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "嗯，也许不是毅力..."
        m 3a "我觉得是热情驱动着我。"
        m "它也激励着我更努力地准备学园祭呢。"
    else:
        show natsuki at t33 zorder 2
        show yuri at f32 zorder 3
        y 2n "我？"
        y 2o "没-没有吧..."
        show yuri at t32 zorder 2
        show natsuki at f33 zorder 3
        n "..."
        show natsuki at t33 zorder 2
        show yuri at f32 zorder 3
        y 2v "我真的很异常吗...？"
        show yuri at t32 zorder 2
        show natsuki at f33 zorder 3
        n 2m "看到了吗，{i}绝对{/i}有问题。"
        show natsuki at t33 zorder 2
        show yuri at f32 zorder 3
        y 3p "我会克服的！"
        y 3y6 "这都不是什么值得一提的事情..."
        y 3o "我只是觉得有些紧张..."
        y 3n "总-总之，别讨论这个啦！"
        show yuri at t32 zorder 2
        show natsuki at f33 zorder 3
        n 2q "嗯，我只是觉得我需要把这件事讲出来罢了。"
        n 5q "我其实也没那么在意..."
        show natsuki at t33 zorder 2
        show yuri 3e
        show monika 1g at l31
        m "Awwwww, man..." # 这里结合 Creeper? Aw man 的 meme，所以不要翻译
        m "我又双叒叕是最后一个到的！"
        show natsuki at f33 zorder 3
        n 2c "嗯，[player] 也刚刚才来。"
        show natsuki at t33 zorder 2
        show yuri at f32 zorder 3
        y 1f "你又去练钢琴了？"
        show yuri at t32 zorder 2
        show monika at f31 zorder 3
        m 5a "对的..."
        m "啊哈哈..."
        show monika at t31 zorder 2
        show yuri at f32 zorder 3
        y 1m "那你的毅力挺强的。"
        y "组织这个社团，还要挤出时间练钢琴..."
        show yuri 1a at t32 zorder 2
        show monika at f31 zorder 3
        m 1a "嗯，也许不是毅力..."
        m 3a "我觉得是热情驱动着我。"
        m "它也激励着我更努力地准备学园祭，还有..."
        m 3n "emm..."
        show monika at t31 zorder 2
        show natsuki at f33 zorder 3
        n 5s "..."
        show natsuki at t33 zorder 2
        show monika at f31 zorder 3
        m 1l "好吧..."
        m "我-我忘记了些东西..."
        show monika at thide zorder 1
        hide monika
        show yuri at f32 zorder 3
        y 2v "呃，说到这个，Natsuki..."
        y "我们昨天又谈了谈，然后..."
        y 2t "嗯...我们应该支持学园祭的活动。"
        y 2l "不过...！"
        y 2h "我理解你不希望社团改变的感受。"
        y "我们都和你的感受差不多。"
        y 2f "所以只要我们齐心协力，这个社团就永远不会成为我们不喜欢的样子。"
        show yuri at t32 zorder 2
        show natsuki at f33 zorder 3
        n "..."
        show natsuki at t33 zorder 2
        show yuri at f32 zorder 3
        y 2v "emm，顺便..."
        y "如果你也能帮忙来准备学园祭的话..."
        y 3r "...我会买一部新的漫画送给你！"
        show yuri 3t at t32 zorder 2
        show natsuki at f33 zorder 3
        n 5h "..."
        n 2z "啊哈哈哈！"
        n "抱歉，你最后那段话真的很好笑哇。"
        n 2c "不过，你听我说..."
        n "我已经反思过昨天的行为了。"
        n 2q "我确实说得有点过分了..."
        n 1q "一定是我当时觉得被吓到了之类的。"
        n 1h "我知道我们都在努力让社团变好。"
        n 1q "再来一两个新成员也不会怎么样，除非他们性格差到爆..."
        n 5w "我觉得这次再来一个女生的话，也挺好的..."
        n 5e "...但更重要的是，我可不愿意看到学园祭活动只是因为我没有加入才办得很糟！"
        n "你也知道我是个 Pro！"
        n 5c "所以我也会帮忙的，确保万无一失。"
        show natsuki at t33 zorder 2
        show yuri at f32 zorder 3
        y 2s "感谢上帝..."
        y "Monika，是不是很棒啊？"
        show yuri at t32 zorder 2
        show natsuki at f33 zorder 3
        n 2k "...Monika？"
        show natsuki at t33 zorder 2
        show monika 1o at f31 zorder 3
        m "啊--"
        m 1n "对，确实很棒！"
        m "Natsuki，没有你的话，恐怕会更糟呢。"
    m 5 "总之，[player]..."
    m "你今天想要做些什么呢？"
    m "我在想，其实我们可以--"
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 1l "我们今天已经有计划了。"
    show yuri at t32 zorder 2
    show monika at f31 zorder 3
    m 1r "啊..."
    m "是吗，Yuri？"
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 1y6 "对啊。"
    y "[player] 正和我读一本小说，读得贼起劲呢。"
    y 1y5 "我终于引导他进入文学的世界了，Monika，难道你不开心吗？"
    show yuri 1a at t32 zorder 2
    show monika at f31 zorder 3
    m 2l "我..."
    m "我以为..."
    m "只是--"
    m 1r "其实，这不重要的。"
    m 1i "真的没什么的。"
    m "你们想干什么都可以。"
    show monika at t31 zorder 2
    show yuri at hf32 zorder 3
    y 2y1 "{i}（吼哇！）{/i}{w=0.5}{nw}"
    y 2u "emm...Monika，理解万岁。"
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    if persistent.recording:
        scene bg club_day
    else:
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
    if persistent.recording:
        scene bg club_day
    else:
        scene bg club_day2
    show monika 4b at t32 zorder 2
    with wipeleft_scene
    play music t3
    m "好啦，各位！"
    m "是时候分配一下学园祭的准备工作了。"
    m 1i "让我们快点把这事弄完。"
    show natsuki 4q at f31 zorder 3
    n "口意..."
    n "今天气氛咋这么怪啊？"
    n "你看，就连 Yuri 也逃不过。"
    show natsuki at t31 zorder 2
    show yuri 4b at f33 zorder 3
    y "唔..."
    y "死气沉沉的气氛，通常暗示着将要发生可怕的事情..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2r "好啦，能赶快搞定吗？"
    m 2d "我会去准备印刷和装订所有的小诗册。"
    if n_appeal >= 2:
        m 2i "Natsuki，你可以做一些纸杯蛋糕。"
        m "我知道你做这个还挺拿手的。"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Natsuki，我只是说--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "我想做纸杯蛋糕！"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...嗯，好。"
        m "很高兴我们还在同一频道上。"
    m 1m "Yuri，你可以..."
    m 1r "...好吧，没事。"
    m 1i "做你想做的吧，只要你觉得对学园祭有帮助就行了。"
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2h "Monika..."
    y "我又不是废人！"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2p "我-我知道啊！"
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 1l "我已经想好我要做什么了。"
    y 1h "没有合适的气氛，就没办法成功开好一个赏诗大会的。"
    y "所以我会去做些装饰，再去弄一些漂亮的灯光烘托气氛。"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2j "这个看上去..."
    m "是个不错的主意！"
    m 1a "那么现在所有人都有事情做了。"
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2f "诶？"
    y "那 [player] 呢？"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2b "[player] 会来帮我的忙。"
    show monika 2a at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4e "等等，帮你？"
    n "Monika，你的工作最简单啊喂！！！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1i "抱歉，但这就是事实。"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 1f "凭什么？！！"
    n "你 TM 到底想搞什么？"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 3h "我-我觉得 Natsuki 说得没错！"
    y "不仅仅因为你的工作本身就更适合一个人完成..."
    y 3l "而且我的工作更倾向于劳力，所以最需要有人来帮忙打下手。"
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 4c "我的也是！"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 1h "啥？你的纸杯蛋糕？？"
    y "就这啊。"
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 1o "说得好像{i}你{/i} TND 懂一样！" # 爆粗口的 Natsuki 是屑（
    n 1x "你只关心如何把 [player] 拴在你和那本白癡才会看的书旁边吧。"
    n 1f "说的是你，{i}还有{/i} Monika！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 2g "嘿！"
    m "我可什么都没做啊！"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3e "好啊，那就别滥用职权，让 [player] 自己决定去帮谁呗！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1p "我可没有...滥用职权啊。"
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2h "不，Monika，你就是在滥用职权。"
    y "让 [player] 自己选，好吗？"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1r "得，得！"
    m "得！"
    show monika 1h at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3w "口意..."
    n "[player]，我知道你肯定已经受够他们两个了。"
    n 3c "我们可以--"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 2r "Natsuki，你 TM 闭上你的臭嘴，让他自己做决定好吗？" # 爆粗口的 Yuri 是屑（
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 1o "{i}你{/i} TM 才该闭嘴！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1r "哦，我的上帝啊..."
    m 1i "这简直没完没了了。赶快做决定吧，好吗？"
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
    m "这周末就可以在你家见面了。"
    m "这一定会很有趣的。"
    m "所以周日你方便吗？"
    show natsuki 1e at f31 zorder 3
    n "你他娘的在逗我吗？" # 爆粗口的 Natsuki 是屑（
    n "不公平啦！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 2i "Natsuki，这非常公平。"
    m "这就是他自己的选择。"
    show monika at t32 zorder 2
    show yuri 3r at f33 zorder 3
    y "不，这一点都不公平！"
    y "你就是让我们干重活累活，然后自己带上了 [player]。"
    y "厚颜无耻！！！"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2r "Yuri，我都没给你分配工作。"
    m 2i "我都让你自己决定的。"
    m "你现在有一点点不讲道理。"
    stop music
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 2y4 "我又不讲道理了？"
    y 2y3 "啊哈哈哈哈哈！"
    y "Monika，没想到你这么妄自尊大、自私自利！"
    y "每次你只要没能参与进来，就把 [player] 从我身边拖走，次次如此。"
    y 1y1 "你是嫉妒吗？"
    y "还是癫了？"
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
    python:
        try: renpy.file(config.basedir + "/have a nice weekend!")
        except: open(config.basedir + "/have a nice weekend!", "w").write("G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/")
        try: renpy.file(config.basedir + "/have a nice weekend!")
        except: open(config.basedir + "/have a nice weekend!chs", "w").write("5WqB5Tby5Yq65liD5x6v5TvN55+w6GHB5igd5p2w55yF5zPB6LOM6ibH5kKH77yX5TjV55+e6GTT546h5Hzw54D954Wg6INU5bAG5x2P55qP5jnh6DOu77yX5TjV55+e6GTT6W+P5Z676Qnu5YmB5G+D5G2D55yR5Zfm5AOs77gZ6YVr5qqo5ThA5WuJ5HZq77lf")
        try: os.remove(config.basedir + "/hxppy thxughts.png")
        except: pass
        try: os.remove(config.basedir + "/CAN YOU HEAR ME.txt")
        except: pass
        try: os.remove(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        except: pass
    show screen notify("我们是不是刚刚删了点什么...你是不是没注意啊？")

    if persistent.disable_awful_music:
        play music t10
    else:
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
    y 2y6 "不过如果这种感觉真的很好..."
    y 2y4 "那么为什么可怕的事情还是要发生呢？"
    y 2y6 "也许这就是我最初尝试阻止自己的原因..."
    y "但是这种爱慕的感觉特别强烈了。"
    y 3y1 "[player]，即便这样，我也不在乎了！"
    y 3y1 "[player]！"
    y "我一定要告诉你！"
    y 3y4 "我...我疯一般地爱上你了！"
    y "我感觉我身体的每一寸肌肤...还有每一滴血...都在喊着你的名字。"
    y 3y3 "我也不在乎后果了！"
    y "我也不在乎 Monika 有没有在那里偷听了！"
    y 3w "求你了，[player]，请一定要明白我有多爱你啊。"
    y 3m "我特别爱你，甚至一度偷你的笔去自///慰。"
    y 3y4 "我只想拉开你的表//皮，在你的身体里游走。"
    y 3y6 "我想让你永远属于我。"
    y "而我也将只属于你。"
    y "听上去是不是很棒呢？"
    y 3s "所以，[player]，告诉我。"
    y "告诉我你想成为我的爱人。"
    y "你接受我的告白吗？"

    menu:
        "接受。":
            jump yuri_kill
        "不。":
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
        show screen notify("危险动作 关乎生命 请勿模仿")
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
        $ persistent.yuri_kill += 50 # 1440 下是人等的？？？
        if persistent.yuri_kill < 1440:
            $ gtext = fujaowee(renpy.random.randint(8, 80))
            y "进度：[persistent.yuri_kill]/1440 [gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(config.basedir + "/have a nice weekend!")
        except: pass
        try: os.remove(config.basedir + "/have a nice weekend!chs")
        except: pass
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
    $ config.allow_skipping = True
    $ quick_menu = True
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
    m "真是难堪啊。"
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
    "Monika 揭开锡箔纸，从 [gtext] 的托盘里拿走了一个纸杯蛋糕。"
    m 2b "啊，真香！"
    m "我肯定要拿的呐，毕竟这是最后一次了。"
    m 2a "你懂的，在她们彻底消失之前。"
    m "...但怎么说，我真的不能让你再等太久了。"
    m 2j "稍微忍耐一下，好吧？"
    m 2a "一下下就好。"

    $ persistent.cleared = True
    $ persistent.player_level = 1

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    scene black with dissolve_scene_half
    pause 3.0

# TODO: 一刷后初级能力者标识

    return


