label ch21_y_end:
    jump ch1_y_end

label ch22_y_end:
    stop music fadeout 2.0
    call showpoem(poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s")
    call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
    if _return:
        call showpoem(poem_y22_chs, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s")

    y 2q "啊哈哈..."
    y "内容其实不是关键。"
    y "我的思维最近超级活跃，所以我就用了你的笔把它写下来。"
    y 2o "啊--"
    y 2q "这...只是昨天从你书包里掉出来的笔，所以为了保管，我就把它带回家了..."
    y "我，emm..." # 实际上注意刚刚写诗的纸，已经有奇怪的液体了
    y 2y6 "我只是...很喜欢...这支笔...的手感。"
    y "所以我就...用它...写了这首诗。"
    y "而现在你在摸着它..."
    y 2y5 "啊哈哈。"
    y 3p "我-我没事！！"
    y 3o "我刚刚..."
    y "..."
    y 4c "...就当无事发生吧。"
    y "你也可以留着这首诗..."
    return
label ch23_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem(poem_y23, track="bgm/5_yuri2.ogg", revert_music=False, paper="mod_assets/poem_y2_alt.jpg", img="yuri eyes", where=truecenter)
    # 现在稿纸已经是血与液的赞歌了，BGM 也诡异了起来
    y "喜欢吗？？"
    y "这可是我为你而写的！"
    $ gtext = fujaowee(80)
    show yuri 1b at i11
    y "怕你不知道，先说一下，这首诗是关于 [gtext]"
    y 1y6 "更重要的是，我给它赋予了我的专属气味。"
    y "看吧，我是不是俱乐部里最体贴的人？"
    play sound "sfx/glitch2.ogg"
    show yuri glitch
    pause 0.2
    stop sound
    show yuri 3y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "..."
    y 4d "让..."
    y "让我先...吐一会儿。"
    show yuri at lhide
    hide yuri
    pause 1.0
    return
label ch21_n_end:
    jump ch1_n_end
label ch22_n_end:
    if n_appeal >= 2:
        jump ch22_n_end2
    else:
        call showpoem(poem_n2)
        call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
        if _return:
            call showpoem(poem_n2_chs)
        n 2a "还行吧？"
        mc "这比昨天那首长多了。"
        n 2w "昨天那首确实挺短..."
        n "但我只是热身啊！"
        n 2c "希望你不会以为那就是我的上限。"
        mc "不，当然不会..."
        n 2a "不管怎么说，这首诗的主旨还是相当直白的。"
        n "恐怕都不需要解释了。"
        n 2g "比如说，所有人都会认同这首诗的主题是一个愚昧的 baka..."
        n "所有人都有某种奇怪的爱好，或者说一种内疚的快乐。"
        n 5q "某种你害怕别人发现、并且因此取笑或是看轻你的东西。"
        n 1e "...但是这只会让人变得愚蠢！"
        n "只要他们没有伤害到任何人，并且从中得到了快乐，谁在乎他们喜欢什么呢？"
        n 1q "我觉得人们真的需要学会尊重别人的僻好..."
        n 1x "...比如说就在这个社团里的两个女生，我就不说出她们的名字了。"
        n 1s "讽刺的是，即便是在我感觉舒服的地方，也没有人尊重我..."
        n 1u "...天哪，你搞得我抱怨得太多了！"
        "{i}（我刚刚做了什么吗？）{/i}"
        mc "其实，我是尊重你的..."
        n 1h "那么--"
        n "谢谢了..."
        n 1s "...但很明显，你更 '尊重' Yuri，所以..."
        n 42c "算了...既然我们分享完了，那你现在可以走了。"
    return
label ch22_n_end2:
    call showpoem(poem_n2b, revert_music=False)
    call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
    if _return:
        call showpoem(poem_n2b_chs, revert_music=False)
    $ style.say_dialogue = style.edited
    n "[player]..."
    n "为什么你今天不陪我一起看书？"
    n 1m "我一直在等着你。"
    n "我等你等得很久了！"
    n "这是我今天唯一期待的事情。"
    n "你为什么要毁了它？？"
    n "难道你更喜欢 Yuri？"
    n 1k "我强烈建议你远离她。"
    n "喂，你有在听吗？"
    if not persistent.alt_safe_mode:
        show darkred zorder 5:
            alpha 0.0
            easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)

    if not persistent.alt_safe_mode:
        show n_rects_ghost1 zorder 4
        show n_rects_ghost2 zorder 4
        show n_rects_ghost3 zorder 4
    if persistent.sthu:
        n ghost1 "Yuri 就只会无理智地追你到底而已。"
    else:
        n ghost1 "Yuri 就 TM 一死病娇。"
    n "现在这一点特别明显了。"
    n "所以还是陪我玩吧。"
    n "好伐？"
    n "[player]，你不恨我吧？"
    n "你恨我吗？"
    if not persistent.alt_safe_mode:
        show natsuki_ghost_blood zorder 3
    if persistent.sthu:
        n "难道你想让这么{i}可爱{/i}的我哭着回家？"
    else:
        n "难道你 TM 想让这么{i}可爱{/i}的我哭着回家？"
    n "文学部是我唯一感觉安全的地方。"
    n "不要毁了它。" # 实际上间接希望文学部有事，，，，
    n "千万不要毁了它。"
    n "求你了。"
    n "不要再和 Yuri 聊天了。"
    n "要陪我玩。"
    n "我要说的就这么多了..."
    n "陪我玩。"
    stop music
    hide n_rects_ghost3
    n ghost2 "快来陪我玩！！！"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    if not persistent.alt_safe_mode:
        show n_rects_ghost4 onlayer front zorder 4
        show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 at i11 onlayer front
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    show end:
        xzoom -1
    with dissolve_cg
    pause 2.0
    scene black
    with None
    call grant_achievement_all("陪我玩！！！！","PLAY_WITH_ME") # todo

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    return
label ch23_n_end:
    $ natsuki_23 = True
    $ style.say_dialogue = style.normal
    call showpoem(poem_n23, revert_music=False)
    call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
    if _return:
        call showpoem(poem_n23_chs, revert_music=False)
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    stop music
    hide screen tear
    show natsuki ghost_base
    n "我改变想法了。"
    n "忘掉你刚刚看到的一切吧。"
    n "试着做任何事情都是没用的。"
    n "Yuri 被人讨厌都是她自己的锅。"
    n "[player]，听得见我说话吗？"
    n "如果你多陪陪 Monika，问题就消失了。"
    n "对于如此完美的您来说，Yuri 和我实在不合你的口味。"
    n "从现在开始，Just Monika." # 请不要翻译 Just Monika.
    n "Just Monika."
    hide natsuki
    $ style.say_dialogue = style.edited
    "Just Monika."
    menu:
        "Just Monika."
        "Just Monika.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "Just Monika.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "Just Monika." with Dissolve(0.5, alpha=True)
    pause 1.0
    play music t5
    $ skip_transition = True

    return

label ch21_m_end:
    call showpoem(poem_m21)
    call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
    if _return:
        call showpoem(poem_m21_chs)
    jump ch1_m_end2
label ch22_m_end:
    call showpoem(poem_m22, revert_music=False)
    call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
    if _return:
        call showpoem(poem_m22_chs, revert_music=False)
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    pause 2
    show screen tear(20, 0.3, 0.3, 0, 40)
    pause 0.5
    hide screen tear
    play music t5c
    m 5 "抱歉，我知道这有那么一点点抽象。"
    m "我只是想...emm..."
    m 1r "emm，没事。"
    m "这也没什么解释的必要了。"
    m 1i "那么..."
    m 3b "这里是 Monika's Writing Tip of the Day！" # 不要翻译 Monika's Writing Tip of the Day
    m "有时你会遇到选择困难..."
    m "此时不要忘记存档哦！"
    m 3k "你也不知道...emm..."
    m 3i "...等等，我在跟谁说话？"
    m "你听得到吗？"
    m 3g "告诉我，你听得到吗？"
    m "给个反应啊。"
    $ renpy.call_screen("dialog", "请一定要帮我啊。", ok_action=Return())
    m 3k "...今天的 Tip 就到这里！"
    m "感谢聆听~"
    return
label ch23_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen: # todo: >= 6.3.???? < Win10 1511+
        $ mouse_visible = False
        scene bsod
        pause 3.0
        show screen notify("是的，你电脑蓝屏了（x）")
    else:
        show black zorder 1
        pause 2.0
    window show(None)
    show monika 1d at i11 zorder 11
    $ quick_menu = True
    $ mouse_visible = True
    m "woc，吓到我了！{fast}"
    window auto
    m "emmm..."
    m 1m "emm，我可能把“写”这首诗这件事...搞砸了。"
    m "我只是想..."
    m 1i "...没事。"
    m "咱继续吧..."
    stop music
    return


label ch21_n_bad:
    jump ch1_n_bad

label ch21_n_med:
    jump ch1_n_med

label ch21_n_good:
    jump ch1_n_good

label ch22_n_bad:
    #Didn't like last poem or this one
    if n_poemappeal[0] < 0:
        n 1r "..."
        n "呵，果不其然..."
        mc "...？"
        n 2w "[player]，听着。"
        if persistent.sthu:
            n "我可不是什么笨蛋。"
        else:
            n "我可不是什么白癡。"
        n 2h "我知道你在 Yuri 身上花了多少时间..."
        n "很明显，你更希望给她留下深刻印象，而不想提高写作水平。"
        n 2w "这属实可悲啊。"
        n 4h "[player]，你为什么会出现在这个社团里？"
        n "老实说..."
        n "我本以为新加入一个成员可以让大家更多地参与到一起。"
        n 4s "而不是变本加厉地彼此排斥。"
        if persistent.sthu:
            n 1u "结果啊，我真是错的离谱..."
            n 12c "...听着，今天我心情不好，而且现在不想说话。"
            n "所以，你赶紧走开吧。"
        else:
            n 1u "结果啊，这真 TM 傻逼至极..."
            n 12c "...听着，老子今天心情不好，而且现在不想说话。"
            n "所以，你赶紧爬吧。"
        $ skip_poem = True
        return
    
    #Liked the last poem but not this one
    else:
        n 1k "...emm。"
        n "我更喜欢你上一首诗。"
        mc "诶？真的吗？"
        n 2c "是啊。我能看出来你这首大胆了一些。"
        n "但是你在这方面还是不够好。它没达到效果。"
        mc "你说的也许没错，不过我只是想要尝试不同的东西。"
        mc "我还在摸索过程中。"
        jump ch22_n_med_shared2

label ch22_n_med:
    #Likes this one better than the last one
    if n_poemappeal[0] < 0:
        n "...emm。"
        n 2k "好吧，它比上一首更好。"
        n "很高兴能看到你的努力。"
        mc "那就好..."
        label ch22_n_med_shared:
            n 2c "只要确保你能从每个人身上找到一点影响就行了。"
            n "我觉得你至少有些受到了 Yuri 的影响，对吧？"
            n 5q "我是说，我知道你一直，比如说..."
            n "和她待在一起，或是别的..."
            n 1w "但是你知道的，Monika 和我也跟 Yuri 一样好！"
            n 1q "我-我说的是，在诗词方面！"
            n 1h "所以你真的应该试着学些什么，否则你永远都不会进步的！"
            n "那么这是我写的..."
            n "你一定能从中学到什么的。"
            return

    #Likes this one the same amount
    elif n_poemappeal[0] == 0:
        n "...emm。"
        n 2k "好吧，它不比你上一首差。"
        n "但我也不能说它比上一首好。"
        mc "phew..."
        n 2c "哈？'phew' 个啥呢？"
        mc "啊...只要不是那么不堪，我都会当作是胜利。"
        mc "而且我觉得你大概是最挑剔的。"
        n 1p "嘿-嘿！你哪来的--"
        n 1q "{i}（等等，刚刚那句也许是表扬...？）{/i}"
        n 4y "啊-啊哈！真高兴看到有人意识到我的阅历了！"
        n "那么，只要你继续练习，也许有一天你也会像我一样好的！"
        mc "那...呃..."
        "我怀疑 Natsuki 把我的意思误解透了。"
        jump ch22_n_med_shared

    #Likes the last one better
    else:
        n "...emm。"
        n 2c "好吧，它还不算太糟。"
        n "不过在看过你的上一首诗之后，这首还是相当让人失望的。"
        n 2s "话又说回来，如果这首诗跟你上一首一样好，那我会气疯的。"
        mc "好吧，我只是想这次尝试些稍微不同的东西。"
        label ch22_n_med_shared2:
            n 2c "很合理。你还是新手，所以我也不会指望你一下子就找到自己的风格。"
            n "我是说，社团里的每个人的写作方式都大不相同..."
            n "可能你会受到我们的一些影响。"
            n 2q "比如说..."
            n 5q "我注意到你今天和 Yuri 待了一会儿..."
            n "并不是说我在乎你和谁待在一起。"
            n 5w "毕竟我一直都被教育着，永远不要期待从任何人身上得到任何东西。"
            n 5s "所以我也不是在等你什么的。"
            n 5h "不过，你也至少应该看看我的诗..."
            n "你应该可以从中学到些什么。"
            return

label ch23_n_bad:
    if y_gave:
        jump ch23_n_ygave
    #Didn't like the last two poems
    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        n 5x "我再也不想看你那种为 Yuri 写的屑诗。"
        n 5s "但你还是要读我的。"
        n "这是有原因的。"
        n 5x "其实我也不想..."
        n "但不幸的是，我是被逼的。"
        n 5h "你...就好好读吧，OK？"
        if persistent.sthu:
            n "看完你就可以走了。"
        else:
            n "看完你就可以滚了。"
        return
    #Liked one of the other two but not this one
    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n 2c "...咩啊。"
        n "看样子你啥都没学到啊。"
        n "老实说，我不知道自己为什么当初会抱有希望。"
        label ch23_n_bad_shared:
            n 42c "这明显是受到了 Yuri 的影响..."
            n "我才发现你这么容易被影响啊。"
            n "在社团里和她成天待在一起..."
            n "现在又试着像她那样写诗..."
            n 1s "傻逼至极啊。"
            n "至少 Monika 欣赏我的诗..."
            n 1r "...呃。"
            n 1q "好吧...我猜现在该把我的诗给你看了。"
            n "其实我也不想这么做。"
            n "但不幸的是，我是被逼的。"
            n 1h "你...就好好读吧，OK？"
            n "看完你就可以走了。"
            return
    #Didn't dislike either of the others but doesn't like this one
    else:
        n "..."
        n 2r "Awwwww, man..."
        n "大倒退啊。"
        mc "诶？？"
        n 2c "我还是喜欢之前你写的那两首。"
        jump ch23_n_bad_shared

label ch23_n_med:
    if y_gave:
        jump ch23_n_ygave
    #Didn't like the last two poems
    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch23_n_bad
    elif n_poemappeal[1] < 0:
        n "..."
        n 2k "...这个还行。"
        mc "还行？"
        n "对，至少比昨天的好。"
        label ch23_n_shared:
            n 2c "我还是不知道你有多在乎写作，不过没事，你的表现还行。"
            n 4r "即便除了 Yuri 外，你基本不和其他人待在一起..."
            n 4h "我还是觉得，有大家都能参与的活动会好一点。"
            n 4w "所以一定要继续努力啊！"
            n "我是说..."
            n 1h "我知道我不是部长或者副部长之类的..."
            n "但是这并不意味着你可以让我失望，懂？"
            n 1q "那么，现在也读一读我的诗吧。"
            n "但是你要清楚一点..."
            n 1h "这首诗...对我有很大的意义。"
            n "所以一定要仔细读，好吗？"
            return
    else:
        n "..."
        n 2k "...这个还行。"
        mc "还行？"
        n "嗯，对。"
        n "大概和昨天的差不多。"
        jump ch23_n_shared

label ch23_n_ygave:
    n 1h "纳尼？"
    n "你已经把诗给 Yuri 了？"
    if persistent.sthu:
        n 4x "淦！"
        n "你们两个怎么了？"
    else:
        n 4x "艹！"
        n "你们两个有病是不是？"
    n 1s "哼..."
    n "反正老子也不想读。"
    n 1r "当然，你都不想给我看，这真是让我恼火。"
    n 1x "...呃。"
    n 1q "好吧...不管怎么说，我还是要让你读我的诗。"
    n "我真的很讨厌这种感觉。"
    n "但不幸的是，我是被逼的。"
    n 5h "你...就好好读吧，OK？"
    if persistent.sthu:
        n "看完你就可以走了。"
    else:
        n "看完你就可以滚了。"
    return

label ch23_n_good:
    jump ch23_n_med

label ch21_y_bad:
    jump ch1_y_bad

label ch21_y_med:
    jump ch1_y_med

label ch21_y_good:
    jump ch1_y_good

label ch22_y_bad:
    jump ch22_y_med

label ch22_y_med:
    y 2b "久等了..."
    y "让我看看你写了些什么。"
    y 3m "..."
    "Yuri 微笑着做了个深呼吸。"
    y "这手感很 awesome。"
    mc "...？"
    y 3p "啊，我是说--"
    y "这首诗蛮好！"
    y 3o "它，啊..."
    y 2q "...好吧，还有些你可以继续努力的地方..."
    y "不过问题不大。"
    y 2s "感觉你写的任何东西都是珍宝。"
    y 2d "啊哈哈..."
    y 2o "这有点尴尬..."
    y "我-我们进行下一步吧..."
    y 2t "这是我写的诗。"
    y "你不用勉强自己喜欢，讲真..."
    return


label ch22_y_good:
    #likes this one more than yesterday
    if y_poemappeal[0] < 1:
        y 2b "久等了..."
        y "让我看看你写了些什么。"
        y 2e "..."
        y "......"
        "Yuri 面带惊讶地盯着那首诗。"
        mc "你...喜欢它吗？"
        y "[player]..."
        y "...你是怎么做到这么快上手的？"
        label ch22_y_good_shared:
            y 2v "昨天我还在告诉你那些值得练习的技术..."
            mc "也许这就是原因吧..."
            mc "你解释得很棒。"
            mc "我也很想试着加入更多的意象。"
            show yuri 4b at t11 zorder 2
            "Yuri 明显地咽了下口水。"
            "连她的双手也出汗了。"
            y 4e "啊-啊..."
            y "真的让我很开心啊..."
            y 3y5 "[player]，被重视的感觉真好！"
            y "你写的一切对我来说都是珍宝。"
            y 3m "仅仅是拿着它都会让我 boki..."
            y 3q "啊哈哈..."
            y "我想写一首关于这种感受的诗..."
            y 3y6 "可以吧，[player]？"
            y "我没有表现得很奇怪，对吧？"
            y 3s "我-我现在比平时更难掩饰我的感情..."
            y 3m "我有点窘迫的说。"
            y 3y6 "不过现在，我只想让你看看我的诗。"
            y 3y5 "好伐？"
            return
    #likes both poems a lot
    else:
        y 2b "久等了..."
        y "让我看看你写了些什么。"
        y 2e "..."
        y "......"
        "Yuri 面带惊讶地盯着那首诗。"
        mc "你...喜欢它吗？"
        y "[player]..."
        y 2t "这首比昨天的还要好哇..."
        y "...你是怎么做到这么快上手的？"
        jump ch22_y_good_shared

label ch23_y_bad:
    jump ch23_y_good

label ch23_y_med:
    jump ch23_y_good

# 强制 good

label ch23_y_good:
    y 1d "终于啊..."
    y 3y5 "啊哈哈..."
    show yuri 3m
    "Yuri 把我的诗放到了她的脸上，深深地吸了口气。"
    y 3y6 "我喜欢。"
    y "我喜欢它的一切。"
    y 3y5 "[player]，我想把它带回家。"
    y "可以让我留着它吗？"
    y "拜托了。"
    mc "当然，我不介意..."
    y 2y5 "啊哈哈。"
    y "[player]，你对我真好..."
    y "我从来没有遇到过像你这么好的人。"
    y 2y6 "如果没有你，我会去世..."
    y 3y5 "别-别当真，只不过--！"
    y "我不知道该怎么形容。"
    y "这样的感觉没问题的，对吧？"
    show yuri:
        "yuri 3y4"
        0.4
        "yuri 3y6"
    y "还行，对吧？"
    "Yuri 把我的诗拿到了胸前。"
    y 3m "我要把这首诗拿回家，好好放在房间里保管。"
    y "我希望当你想到我拿着它时，你会感觉开心。"
    $ style.say_dialogue = style.normal
    y 3y5 "我会好好保管的！"
    $ style.say_dialogue = style.edited
    y 3y6 "我还会边反复欣赏，边自我 touch 的！"
    $ _history_list.pop()
    y "我会用纸割开自己，这样你的皮脂就会进入到我的血液中。"
    $ _history_list.pop()
    y 3y1 "啊哈哈哈哈哈哈哈哈哈。"
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    y 2s "你也可以读我的诗。"
    y "你看完后一定也想留着它的。"
    y 2y6 "来，拿去吧。我已经等不及了。"
    y 2y5 "快点读吧！GKD！"
    $ y_gave = True
    return


label ch21_m_start:
    m 1b "嗨，[player]！"
    m "最近过得怎样？"
    mc "啊...还行。"
    m 1k "好！我很高兴听到你这么说！"
    m 4a "顺便，由于你是新来的..."
    m "如果你对社团有什么建议，比如新的活动，或是可以做得更好的事情..."
    m 4b "我都会倾听的！"
    m "不要害怕，好吗？"
    show monika 4a
    mc "好的...我会记住的。"
    "其实我害怕提出问题。"
    "在更融入些之前，我最好还是随波逐流吧。"
    m 1a "话说回来..."
    m "你想跟我分享一下你的诗吗？"
    mc "虽然有些尴尬，不过我想也只能这么做了。"
    m 5a "啊哈哈哈！"
    m "别担心，[player]！"
    m "我们今天都有一点尴尬，你知道吗？"
    m "但这种障碍很快就能克服的。"
    mc "嗯，确实。"
    "我把我的诗递给了 Monika。"
    m 2a "...嗯？！"
    $ nextscene = "m2_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_3

    m 1a "话说回来，你想现在读我的诗吗？"
    m 1e "别担心，我不是很擅长..."
    mc "对于这么多宣称自己不擅长的人来说，你很有信心啊。"
    m 1j "好吧...也许我需要信心。"
    m 1b "这并不意味着我总有这种感觉，懂吧？"
    mc "懂..."
    mc "好了，那就开始读你的吧。"
    return

label ch22_m_start:
    if y_appeal < 2:
        m 1b "嗨，又见面了，[player]！"
        m "写得怎么样？"
        mc "还行吧，我觉得..."
        m 2k "让我看看。"
        m 2b "只要它不太差。"
        m 2a "我都会为你的努力而开心。"
        m "可能很快你就会想出一篇 Masterpiece！"
        mc "啊哈哈，我就不指望了..."
        m 2a "说不定呢！"
        m "想跟我分享一下你为今天写的东西吗？"
        mc "当然...给。"
        "我把我的诗给了 Monika."
        m "..."
        m "...没问题！"
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_4

    m 1a "不过话说回来..."
    m "想现在读读我的诗吗？"
    m "我还挺喜欢这首诗的表现方式的，所以希望你也喜欢~"
    return

label ch23_m_start:
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_5
    if y_appeal < 3:
        m 1a "话说回来..."
        if y_gave:
            m 1m "我觉得我们不用担心你的诗了..."
            m "Yuri 至少应该有点礼貌，在拿走之前让你写完它。"
            m 1r "...好吧，算了。"
            m "她高兴就好，我也不阻拦她。"
            m 1a "说回来..."
        m 1e "我真的非常...非常用心地写了这首诗，所以..."
        m "我希望它，呃，能让你留下深刻印象。"
        m 1r "来吧..."
    return



label m2_natsuki_1:
    m 2b "[player]，我喜欢！"
    mc "真的...吗？"
    m 2e "它比我想象中的要可爱多了。"
    m 2k "啊哈哈哈！"
    mc "哦，天哪..."
    m 1b "不是，不是！"
    m "它只是有点让我想到 Natsuki 写的东西。"
    m "而她也是个好的作者。"
    m 5a "所以你就当这是表扬吧！"
    mc "啊哈哈..."
    mc "你高兴就好。"
    m "是的呐！"
    m 3b "如果你喜欢 Natsuki，记得随身携带零食哦！"
    m "她会像小狗一样粘着你的。"
    m 3k "啊哈哈！"
    m 1a "Natsuki 的爸爸不给它午饭钱，也不在家留点吃的，所以她经常挑剔..."
    m "不过有时候，她突然失去了所有的力气，变得麻木。"
    m "就像刚刚那样。"
    m 2d "这只是一个猜测，不过我觉得她长得这么小，一定是因为营养不良影响到了青春期的发育..."
    m 2b "...不过，嘿，有些人也喜欢较小的女生，你知道吧？"
    m 5a "抱歉...别想歪！"

    return

label m2_yuri_1:
    m 1a "写得很好，[player]！"
    m "在我读它的时候，我满脑子都是 'OHHHHHHH' 这样的声音。"
    m 1j "真的非常有隐喻性！"
    m 1a "不知道为什么，我从来没想到你会这么深入。"
    m 3b "恐怕我之前低估你了！"
    mc "大家最容易对我保持一个较低的期待值。"
    mc "这样一来，一旦我努力了，反而会变得很明显。"
    m 5a "啊哈哈！这可不太公平啊！"
    m "好吧，不管怎么说，我觉得它还是奏效了。"
    m 2a "你知道 Yuri 喜欢这种文字的，对吧？"
    m "那种充满意象和隐喻的文字。"
    m 2d "有时候我觉得 Yuri 的思想是完全脱离现实的。"
    m "不过我并不是说这样不好。"
    m 2a "但有时我的印象是她完全放弃了对人的信任。"
    m "她花了那么多时间在自己的脑海中，可能对她来说，那里才是更有趣的地方..."
    m 2b "不过这也是为什么，当你亲切地对待她时，她会变得那么开心。"
    m "我不觉得她习惯于被那样惯着。"
    m 2j "她肯定很渴求社交活动，所以也不要因为她表现地过强而责怪她。"
    m 2d "就像之前那样..."
    m "我想如果她太兴奋了，她最终会退缩并去寻找独处的时间的。"
    "突然，门开了。"
    m 2b "Yuri！"
    show monika 2a
    show yuri 1s at f31 zorder 3
    y "我回来了..."
    y "我有错过什么吗？"
    show yuri at t31 zorder 2
    show monika at f32 zorder 3
    m 2a "没什么..."
    m "嗯，我们刚开始彼此分享诗。"
    show monika at t32 zorder 2
    show yuri at f31 zorder 3
    y 2t "诶？"
    y "已经开始了吗？"
    y 2v "抱-抱歉我迟到了..."
    show yuri at t31 zorder 2
    show monika at f32 zorder 3
    m 2j "不用道歉！"
    m 2a "我们还有很多时间，你可以慢慢来。"
    show monika at t32 zorder 2
    show yuri at f31 zorder 3
    y 1s "好吧..."
    y "谢谢你，Monika。" # 其实更想直接保留 Thanks, Monika 的，歌词梗（
    y "我想我现在应该去拿我的诗了。"
    show yuri at thide zorder 1
    hide yuri
    $ y_ranaway = False
    return

label m2_yuri_2:
    m 1i "[player]，我觉得你之前看到了不该看的东西。"
    m "我本来不想告诉你，但是现在别无选择了。"
    m 1r "陪 Yuri 太久其实很危险的说。"
    m 1i "不知道为什么，她看到你总是特别容易兴奋..."
    m 3d "这本身并不是问题。"
    m "不过 Yuri 一旦太兴奋，她就会找个地方躲起来，然后用一把小刀那啥。"
    m 2e "这不就出大事了吗？"
    m "她甚至每天都带一把不同的刀到学校来，似乎她有收藏之类的..."
    m 2d "我的意思是，这肯定不是因为她抑郁之类的！"
    m "我觉得她只是会从中获得快感。"
    m 2m "它可能甚至，就像是，某种东♂西♀一样...咳..."
    m 1i "但关键在于，你，某种意义上让她助长了这种意识。"
    m 1d "我可没说这是你的错！"
    m 1a "但是我觉得，这就是为什么我需要向你解释这一切..."
    m "所以我在想，如果你跟她保持距离，那么对她而言可能是最好的。"
    m 5 "与此同时，你也可以多花一些时间陪我啊..."
    m "坦白地说，至少我有在脑海中考虑过...我也知道该如何对待我的社团成员。"
    return

label m2_yuri_3:
    stop music
    m 1i "[player]，不要说我没有警告过你。" # 巨硬翻译梗（
    # call screen dialog("你居然爱一个疯子...呵呵。（（（",Return())
    $ skip_poem = True
    return
