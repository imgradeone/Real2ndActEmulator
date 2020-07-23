label poemresponse_start:
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label poemresponse_start2:
        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""
        if poemsread == 0:
            $ menutext = "首先我该把诗分享给谁看呢？"
        else:
            $ menutext = "接下来要和谁分享我的诗呢？"

        menu:
            "[menutext]"

            "Sayori" if not s_readpoem and persistent.playthrough == 0:
                $ s_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "I'm definitely most comfortable sharing it with Sayori first."
                    "She's my good friend, after all."
                call poemresponse_sayori from _call_poemresponse_sayori
            "Natsuki" if not n_readpoem:
                $ n_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "昨天我说过，我对 Natsuki 的诗很感兴趣。"
                    "所以我应该先和她分享，这样才对。"
                call poemresponse_natsuki from _call_poemresponse_natsuki
            "Yuri" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "Yuri 看上去像个大佬，所以我应该从她开始。"
                    "我相信她的意见是公允的。"
                call poemresponse_yuri from _call_poemresponse_yuri
            "Monika" if not m_readpoem:
                $ m_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "我应该从 Monika 开始。"
                    "她昨天似乎非常想读我的诗，而我也想让她看到我的努力。"
                call poemresponse_monika from _call_poemresponse_monika
        $ poemsread += 1
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop

    # Reset variables for next time
    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label poemresponse_sayori:
    scene bg club_day
    show sayori 1a at t11 zorder 2
    with wipeleft_scene
    $ poemopinion = "med"
    if s_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif s_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_s_" + poemopinion
    call expression nextscene from _call_expression_14
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_s_end"
        call expression nextscene from _call_expression_15
    return

label poemresponse_natsuki:
    scene bg club_day
    show natsuki 1c at t11 zorder 2
    with wipeleft_scene
    $ poemopinion = "med"
    if n_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif n_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_n_" + poemopinion
    call expression nextscene from _call_expression_16
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_n_end"
        call expression nextscene from _call_expression_17
    return

label poemresponse_yuri:
    scene bg club_day
    show yuri 1a at t11 zorder 2
    with wipeleft_scene
    $ poemopinion = "med"
    if y_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif y_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_y_" + poemopinion
    call expression nextscene from _call_expression_18
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_y_end"
        call expression nextscene from _call_expression_19
    return

label poemresponse_monika:
    scene bg club_day
    show monika 1a at t11 zorder 2
    with wipeleft_scene
    if m_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif m_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_m_start"
    call expression nextscene from _call_expression_20
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_m_end"
        call expression nextscene from _call_expression_21
    return

label ch1_y_end:
    call showpoem(poem_y1, img="yuri 3t")
    call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
    if _return:
        call showpoem(poem_y1_chs, img="yuri 3t")
    y 3t "..."
    y "抱-抱歉，我写字写得那么难看！"
    mc "啥？？"
    mc "我可没有这么想..."
    y 2v "但是你花了很久的时间才读完诶..."
    mc "啊--"
    mc "嗯，我只是不怎么读手稿..."
    mc "我其实觉得你的字挺漂亮的。"
    y 2t "诶？"
    y 2u "啊...吓死我了..."
    mc "还有，我也很喜欢你的诗。"
    mc "虽然短，但表达得相当生动。"
    y 2t "这是不是太短了？"
    y "我一般会写长一些的诗..."
    mc "不短啊。"
    y 1m "很...很高兴你能喜欢。"
    y "说实话..."
    y 1a "因为这是我们第一次分享诗，所以我想写得平淡一些。"
    y "或者说是容易消化理解。"
    mc "Yuri，你对幽灵很感兴趣吗？"
    y 1m "呼呼。"
    y "实际上，[player]，这个故事跟幽灵完全没关系。"
    mc "真的吗？"
    mc "我肯定完全理解错了..."
    y 1u "嗯，毕竟你只是浏览了一下..."
    y "不过你要记住，诗人常常会在自己的作品中表达他们的思想、情感以及经历。"
    y 1a "他们通常并不会只讲简单一个的故事，或是描绘出一幅画。"
    y "在这种情况下，或许诗的主题只是在象征意义上比做了幽灵。"
    y 2l "徘徊在她最后的安心之处，无法对过去释怀。"
    y "而且很快就会一无所有..."
    mc "...这样解释的话，诗就严肃了很多。"
    mc "我想都没有想到过..."
    mc "真是令人印象深刻啊。"
    if poemopinion == "good":
        y 2f "诶？"
        y 3v "没-没什么，真的！"
        y "你的诗也非常让人印象深刻，所以..."
        mc "不..."
        mc "恰恰相反，倒是我可以从你身上学到一两点。"
        y 4a "...你是这么想的吗？"
        mc "嗯，当然啦。"
        y "啊..."
        y 2s "你知道的..."
        y "这些事情都会让我非常紧张。"
        y "不过到头来，我自己也很享受。"
        y "我会继续为你尽力的，[player]！"
        mc "啊..."
        mc "我也是。"
    else:
        y 1u "其实真的没什么..."
        y "嗯...你能这么想，我很开心。"
        y 1a "不过你要记得，很快你也会上手这些东西的。"
        mc "嗯，或许你说得没错。"
        mc "我必须要继续努力了。"
        y "我相信你。"
    return

label ch1_n_end:
    call showpoem(poem_n1, img="natsuki 2s")
    call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
    if _return:
        call showpoem(poem_n1_chs, img="natsuki 2s")
    n 2q "嗯..."
    n "我说过你不会喜欢的。"
    mc "我喜欢。"
    n 2h "什么？"
    n "说实话！"
    mc "我真的喜欢。"
    mc "为什么你这么觉得我不喜欢呢？"
    n 5w "好吧--"
    n "因为！"
    n "高中里的所有人都认为，文章应该是复杂丰满的..."
    n 5q "所以大家都不把我的文章当回事。"
    mc "但是，诗的关键不就是要表达自己吗？"
    mc "你的写作风格并不会使主旨逊色一分。"
    n 1k "是的！就是这样！"
    n "我喜欢那些读起来容易，但是又能狠狠触动你的诗。"
    n 1c "就像这首诗一样。"
    n "看着身边的所有人都在做大事，这真是让人沮丧啊..."
    n "所以我就决定将它写下来。"
    mc "嗯，我能理解。"
    n 2a "不过简单地写作还有一个好处，它可以更注重文字游戏。"
    n "比如说，我在每句话末尾设置了韵脚，但随即就押错韵。"
    n "这样就可以帮助我从上一行中的情绪中摆脱出来。"
    mc "所以你这么做..."
    mc "似乎比我意识到的还要更深入一些。"
    n 4y "这就是 Pro！"
    n "很高兴你能学到些东西。"
    n "你没想到会从年纪最小的人这里学到吧？"
    mc "耶...确实。"
    "我决定就这样迁就她一次。"
    "我其实并不在意大家的年纪，不过如果 Natsuki 对此感到自豪的话，那么我也不会说破的。"
    return

label ch1_m_end:
    call showpoem(poem_m1)
    call screen confirm("是否查看中文翻译版？", Return(True), Return(False))
    if _return:
        call showpoem(poem_m1_chs)
label ch1_m_end2:
    m 1a "那么...你觉得怎么样？"
    mc "唔...它非常...自由，如果你想这么称呼的话。"
    mc "抱歉，我真的不是征求反馈意见的合适人选..."
    m 2e "啊哈哈。没关系。"
    m 2b "嗯，这种风格现在已经相当流行了。"
    m "也就是，很多诗会注重强调词和行之间的把握。"
    m 2a "大声朗读出来时，就很有感染力。"
    mc "这首诗背后的灵感是什么？"
    m "啊..."
    m 3d "嗯，我不是很确定我能不能表达好..."
    m 3a "我觉得你可能已经发现我最近有些顿悟了。"
    m "而这也稍微影响到了我的诗。"
    mc "顿悟？"
    m 1a "是的...类似这样的东西。"
    m "我对于谈论这些深层次的东西有些紧张，因为它来得有些强烈..."
    m "也许是在大家成为了更好的朋友之后。"
    m 1j "那么..."
    m 3b "这里是 Monika's Writing Tip of the Day！" # 不要翻译 Monika's Writing Tip of the Day
    m "有时候，当在你写诗，或者是一个故事的时候，你的大脑会过分专注在某个特定点上..."
    m "如果你过于追求完美的话，那么你就永远不会有任何进步。"
    m "只要强迫你自己在纸上写下一些东西，事后再整理就行了！"
    m "还有一种方式："
    m "如果你把钢笔放在某个地方太久，那么你只会得到一个很大的黑色墨点。"
    m "所以只要挥洒起来，顺其自然就行了！"
    m 3k "...今天的 Tip 就到这里！"
    m "感谢聆听~"
    return

label ch1_n_bad:
    n "..."
    mc "...？"
    if persistent.playthrough == 2 and renpy.random.randint(0, 2) == 0:
        $ currentpos = get_pos()
        stop music
        pause 2.0
        show screen notify("达成成就：我 TM 炸开！（物理）")
        play sound "sfx/stab.ogg"
        show n_blackeyes_alt at i11 zorder 3
        show n_eye_alt zorder 3:
            subpixel True
            pos (660,250) xanchor 0.5 yanchor 0.5 zoom 0.8
            parallel:
                linear 2.0 rotate 720
            parallel:
                linear 2.0 xpos 1680
            parallel:
                easein 0.25 ypos 180
                easeout 1.0 ypos 1280
        show n_eye_alt as n_eye2 zorder 3:
            subpixel True
            pos (580,260) xanchor 0.5 yanchor 0.5 zoom 0.8 rotate 180
            parallel:
                linear 2.0 rotate -560
            parallel:
                linear 2.0 xpos -440
            parallel:
                easein 0.10 ypos 240
                easeout 1.0 ypos 1280
        # show blood zorder 3:
        #     pos (645,255)
        # show blood as blood2 zorder 3:
        #     pos (575,260)
        pause 0.75
        hide n_blackeyes_alt
        hide n_eye_alt
        hide n_eye2
        hide blood
        hide blood2
        stop sound
        play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    n 2b "[player]，如果你不想认真对待这个文学部的话，请你直接回家。"
    mc "纳-纳尼？？"
    mc "wdnmd..."
    n 42c "哈？你还以为，我不知道你在瞎写啊？"
    n "你觉得我是白癡吗？"
    mc "我又不是作家！"
    mc "可能它不太好，但是没错，我确实努力了。"
    mc "大家都是从零开始的，对吧？"
    mc "不过，如果你还对{i}你{/i}写的第一首诗非常自豪的话，那么我也很想读一读。"
    n 1o "！！"
    mc "戳到痛处了？"
    n 1r "..."
    n 5q "好吧。"
    n "对不起。"
    n 5c "反正你以后会写得好起来的。"
    n "我会告诉你需要改进什么，不过你最好还是再尝试一次。"
    mc "说得在理..."
    mc "嗯，我觉得，每个人都有选择喜好的权利。"
    n 5q "不管怎么说，我猜现在该由我来分享诗了..."
    n "以我对你的了解，你可能会觉得它很傻。"
    return

label ch1_n_med:
    n "..."
    mc "...？"
    n 2k "...好吧，和我对你这样的人的期待差不多。"
    mc "这说得有些直接了..."
    n 2c "好吧，抱歉。"
    n "我没说它很糟。"
    n "只不过它没有唤起任何感情。"
    mc "所以根本上来说，对你的口味而言，它还不够可爱？"
    n 4f "你想被我锤死？？？"
    mc "当我没说..."
    n 42b "嘶..."
    n 42c "反正无论如何，我还是要给你看看我的。"
    n 4q "恐怕你不会喜欢。"
    return

label ch1_n_good:
    n "..."
    mc "...？"
    n 1t "...好吧，先说一下我不喜欢的地方！"
    n "首先，呃..."
    mc "..."
    "Natsuki 又读了一遍我的诗。"
    n 4c "没-没事。我没有任何意见。"
    mc "诶？那分享又有什么意义呢？"
    mc "我在写它的时间里，本来可以做其它事情的。"
    n 4r "唔..."
    mc "实际上，你还记得我是怎么说我想要读你的诗的吗？"
    mc "这就是我在写这首诗时，脑海中想着的东西。"
    mc "我想要让你对分享你的诗感到安心。"
    mc "就像 Monika 说的那样。"
    n 4x "唔唔唔唔...！"
    n 1h "嗯，要是你的诗很烂的话，我会更安心于分享我的诗！"
    n 1w "你应该给我看一首非常蠢的诗，然后我就可以说 '哈，这可不太行，让我给你看看真正的文学是怎么样的吧！'"
    n 1h "但是你却毁了它！"
    n "希望你开心！"
    mc "..."
    mc "...所以，换句话说，你是在说你喜欢这首诗？"
    n 1o "呃--"
    "Natsuki 的反驳被卡在了喉咙里。"
    n 1x "呜呜呜...你真是太...！"
    n "你...你...什么都不懂，对吧？"
    n 5q "我已经跟你说了，你不需要这样对着全世界宣布，就好像你很高傲一样！"
    mc "我很确定你真的没有说过..."
    "我这句话基本是在对自己说。"
    "Natsuki 肯定很讨厌我了吧。"
    "我不知道她喜欢我的诗，是意味着我的胜利还是失败。"
    mc "不管怎么说...你还是得给我看看你的诗，不是吗？"
    n 5s "呃...好吧。"
    n "反正只是因为 Monika 要求我这么做的。"
    return

label ch1_y_bad:
    y 1g "..."
    y "emm..."
    y "..."
    "Yuri 盯着那首诗。"
    "一分钟过去了，似乎用了太长时间。"
    mc "emm..."
    y "Oh！"
    y 3n "抱-抱歉...！"
    y "我忘记去读了..."
    y "唔-唔！"
    mc "没关系，别强迫自己。"
    y 2v "我没有..."
    y "我只是需要将我的想法变成语言。"
    y "等一下..."
    y "...好了。"
    y 1f "这是你第一次写诗，对吗？"
    mc "呃，是啊..."
    mc "你为什么要问这个？"
    y "我只是确认一下。"
    y "在读完这首诗之后，我就是这么猜的。"
    mc "啊，也就是说它很烂啊。"
    y 2p "不是！！"
    y 2o "...我刚刚是不是太大声了点...？"
    y 4c "唔，抱歉..."
    "Yuri 把脸埋到了手里。"
    "我忍不住，突然注意到，已经好几分钟过去了，而我们一点进展都没有。"
    "Yuri 可能需要一些时间来适应新人..."
    mc "没关系，我都没注意到。"
    mc "你刚刚说了什么？"
    y 2u "好吧...唔..."
    label ch1_y_shared:
        y 1a "只不过诗里有一些能典型见于新手作者的特定写作习惯。"
        y "我也是从新手过来的，所以对于这些习惯都有些熟悉。"
        y 1i "我觉得，新手作者最明显的一点就是，他们会非常谨慎地决定风格。"
        y "换句话说，他们更喜欢剥离主题来选择写作风格，然后再将两者结合起来。"
        y 1a "而最终结果就是，风格和表现力都被削弱了。"
        "Once Yuri finds her train of thought, it's as if her demeanor totally changes."
        "她的磕磕巴巴完全消失了，听起来就像是专家一样。"
        y 1k "Of course, that's not something you can be blamed for."
        y "There are so many different skills and techniques that go into writing even a simple poem."
        y 1a "Not just finding them and building them, but getting them to work together is probably the most challenging part."
        y "It might take you some time, but it all comes with practice, and learning by example, and trying new things."
        y "I also hope that everyone else in the club gives you valuable feedback."
        y 1l "Natsuki can be a little bit biased, though..."
        mc "Biased? How?"
        y 2j "U-Um..."
        y "Well..."
        y "Never mind..."
        y "I shouldn't be talking about people like that..."
        y "Sorry..."
        mc "It's fine."
        "I'm not sure if Yuri is apologizing to herself, to me, or to Natsuki."
        mc "Do you mind if I read your poem now?"
        y 3c "Please do!"
        y "I'd love to share my thought process behind it..."
        "Yuri smiles dreamily, as if that's a rare opportunity for her."
        "Which itself is kind of funny..."
        "...After all, isn't this supposed to be a literature club?"
        return

label ch1_y_med:
    jump ch1_y_bad

label ch1_y_good:
    y 1e "..."
    "As Yuri reads the poem, I notice her eyes lighten."
    y 2f "...大师之作。" # @小罐茶（（（
    mc "诶？什么意思？"
    y "...?"
    y 2n "D-Did I say that out loud...?"
    "Yuri first covers her mouth, but then ends up covering her whole face."
    y 4c "I...!"
    y "Uu..."
    y "{i}（他会讨厌我的...）{/i}"
    mc "Um..."
    mc "You really didn't do anything wrong, Yuri..."
    y 4a "Eh...?"
    y "That's..."
    y 2q "I-I guess you're right..."
    y "What am I getting so nervous for?"
    y "啊-啊哈哈..."
    show yuri 2l at t11
    "Yuri takes a breath."
    y "So..."
    y 1a "What kind of writing experience do you have?"
    y "Your use of imagery and metaphors indicates you've written a lot of poetry before."
    mc "Really...?"
    mc "Wow, that's a huge compliment coming from you."
    mc "This is actually my first time, really."
    y 1e "Huh...?"
    "Yuri stares at me blankly, then looks at my poem again."
    y "..."
    y 2h "...Well, I know that!"
    y "I just meant...u-um..."
    "Yuri trails off, unable to find an excuse."
    "She traces her finger along the words in the poem, as if breaking it down more thoroughly."
    y 2l "...Yeah."
    y "Okay."
    y "This is the reason I was able to tell."
    jump ch1_y_shared


label ch1_m_start:
    m 1b "Hi, [player]!"
    m "Having a good time so far?"
    mc "Ah...yeah."
    m 1k "Good! Glad to hear it!"
    m 4a "By the way, since you're new and everything..."
    m "If you ever have any suggestions for the club, like new activities, or things we can do better..."
    m 4b "I'm always listening!"
    m "Don't be afraid to bring things up, okay?"
    show monika 4a
    mc "Alright...I'll keep that in mind."
    "Of course I'll be afraid to bring things up."
    "I'm much better off just going with the flow until I'm more settled in."
    m 1a "Anyway..."
    m "Want to share your poem with me?"
    mc "It's kind of embarrassing, but I guess I have to."
    m 5a "Ahahaha!"
    m "Don't worry, [player]!"
    m "We're all a little embarrassed today, you know?"
    m "But it's that sort of barrier that we'll all learn to get past soon."
    mc "Yeah, that's true."
    "I hand Monika my poem."
    m 2a "...Mhm!"
    $ nextscene = "m_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_22

    mc "I'm sure I'll end up trying different things a lot."
    mc "It could take a while before I feel comfortable doing this."
    m 1k "That's okay!"
    m 1b "I'd love to see you try new things."
    m "That's the best way to find the kind of style that suits you."
    m 3e "Everyone else might be a little bit biased toward their own kinds of styles..."
    m 3a "But I'll always help you find what suits you the most!"
    m "So don't force yourself to write the way everyone else wants you to write."
    m "It's not like you have to worry about impressing them or anything."
    m 5 "啊哈哈！"
    mc "啊哈哈..."
    m 1a "Anyway, do you want to read my poem now?"
    m 1e "Don't worry, I'm not very good..."
    mc "You sound pretty confident for someone who claims to not be very good."
    m 1j "Well...that's 'cause I have to sound confident."
    m 1b "That doesn't mean I always feel that way, you know?"
    show monika 1a
    mc "I see..."
    mc "Well, let's read it, then."
    return

label m_natsuki_1:
    m 2b "I like it, [player]!"
    mc "Really...?"
    m 2e "It's a lot cuter than I expected."
    m 2k "Ahahaha!"
    mc "Oh jeez..."
    m 1b "No, no!"
    m "It kind of makes me think of something Natsuki would write."
    m "And she's a good writer, too."
    m 5a "So take that as a compliment!"
    mc "啊哈哈..."
    mc "If you say so."
    m "Yep!"
    m 1a "By any chance have you read anything by Shel Silverstein?"
    mc "Eh?"
    mc "Maybe a long time ago..."
    m "He's famous for telling all kinds of stories in just a few simple words."
    m "His poems can be funny, endearing, or even sad..."
    m 3d "And sometimes they're only a few lines long."
    m "They might even feel like they're written for kids, but if you think about them..."
    m "They can express views of the world that would apply to anybody."
    mc "I see..."
    mc "So you're saying that Natsuki is kind of like that?"
    m 2a "Sort of."
    m "Maybe she's not an expert..."
    m "But you probably won't find much filler in her poems."
    m "They might be easy to write, but they're super challenging to get the meaning through."
    m 2b "So I can see why it would be your kind of poem to explore!"
    return

label m_yuri_1:
    m 1a "Great job, [player]!"
    m "I was going 'Ooh' in my head while reading it."
    m 1j "It's really metaphorical!"
    m 1a "I'm not sure why, but I didn't expect you to go for something so deep."
    m 3b "I guess I underestimated you!"
    mc "It's easiest for me to keep everyone's expectations low."
    mc "That way, it always counts when I put in some effort."
    m 5a "Ahaha! That's not very fair!"
    m "Well, I guess it worked, anyway."
    m 2a "You know that Yuri likes this kind of writing, right?"
    m "Writing that's full of imagery and symbolism."
    m 2d "Unlike Sayori, who likes using simple and direct words to describe happiness and sadness..."
    m "Yuri likes it when readers are left to derive their own meaning out of it."
    m 4d "It's very challenging to write like that effectively."
    m "Both allowing people to get something out of it just by feel..."
    m "Or letting them deeply analyze all of the nuances."
    m "It can take years of practice, which I'm assuming Yuri has at this point."
    m 1e "I never really asked, though..."
    mc "I'm sure I'm nowhere near her level yet."
    m 2b "Don't worry so much about that!"
    m "You do your own thing."
    m "Just keep exploring, and learn by trying new things!"
    return

label m_natsuki_2:
    m 1j "It's pretty good~"
    m 1a "You've been spending some time with Natsuki, haven't you?"
    m "You must like her writing style."
    mc "Ah, yeah..."
    mc "I think it's a neat way to tell a story."
    m 2a "Mhm. I don't disagree."
    m "Natsuki's poems may be cute, but they're also meaningful."
    m "I can see why you'd be into the style."
    m "I guess that means you're not as much a fan of Yuri's poems, then?"
    mc "Ah-- I wouldn't say that..."
    mc "I kind of like everyone's poems."
    m 2d "That's true, but I'm sure you like some more than others, right?"
    m "Like Yuri's use of complex words and symbolism..."
    m "Or Sayori's way of expressing happiness or sadness in a more direct way."
    m 2a "You must have some kind of preference, don't you?"
    m 4l "Ah, not that it's a contest or anything!"
    m 4a "I was just curious, that's all."
    return

label m_yuri_2:
    m 2b "This one's good!"
    m "It feels like you're not only getting more comfortable with your style..."
    m "But the imagery is better than the last one I read!"
    m 2a "Just wondering, but have you been finding inspiration in Yuri's writing style?"
    mc "Hmm..."
    mc "I guess so."
    mc "You can't deny that she's talented."
    m 4k "Yeah, totally!"
    m 4a "I think her poems are the most..."
    m "...Romantic."
    m 1a "That's the best way to describe it."
    m 1d "She's like a totally different person when she picks up a pen..."
    mc "I noticed that, too."
    mc "Or when she's talking about literature, it's like a light turns on inside her."
    m 2a "Mhm!"
    m "Sadly, it's hard to get much personal conversation out of her..."
    m 2m "Trust me, I've tried..."
    m "Who knows what goes on in that head of hers?"
    mc "I hope you don't mean that in a bad way."
    m 1g "No, of course not!"
    m "I just meant that I wish she didn't keep so much to herself..."
    m 1e "But still, defending her like that..."
    m 5 "You must be pretty into her..."
    mc "Eh?!"
    mc "You...completely misunderstood!"
    m "Ahaha! Calm down, I'm kidding!"
    m 2a "Besides, I'm pretty sure she's already got a boyfriend..."
    mc "Wait, really?"
    m 2k "Yeah. A fictional one, anyway."
    "Monika kind of whispers that last part to me."
    m 5 "It's just a hunch, but..."
    mc "...Well, there's not really anything wrong with that!"
    m 1n "Oh, well I know...!"
    m "I was just saying~"
    return

label m_natsuki_3:
    m 2j "Sticking with the Natsuki style once more, I see~"
    m 2d "Hmm..."
    m "You really like Natsuki, don't you?"
    mc "Eh? That's--"
    m 5 "Oh, come on, [player]."
    m "It's awfully suspicious, you know?"
    m "Spending time with her in the clubroom every day..."
    m "Pretending to like the manga that she's into..."
    mc "Y-You know how Natsuki is...!"
    mc "If I don't indulge her, she'll end up hating me."
    m 2e "Eh?"
    m 2a "No, I think you're misunderstanding, [player]."
    m "It's not like Natsuki just hates anyone who doesn't give her what she wants."
    m 2d "Yeah, she's assertive, but she's not that selfish..."
    m "In fact, I think you're the only one who's indulged her as much as you have."
    mc "Is that so..."
    "I kind of knew that, but I just didn't want to admit it."
    m "So, I just need to ask one thing of you..."
    m 1e "...Be careful. Please?"
    m "Natsuki is kind of unpredictable."
    m "A lot of times, she doesn't even know what she wants."
    m 1i "After all, she's the youngest one here."
    m "She might not know how to handle her own feelings properly."
    m "What I'm saying is..."
    m 1m "If something bad happens, then it could end up damaging the club, too..."
    m 5 "And you wouldn't do that to me...right?"
    mc "That's--"
    "I'm not sure how to respond to Monika."
    "While I care about her and the club, it's also kind of unfair to bring that up."
    m "Well...you're smart."
    m "I'm sure you'll do the right thing."
    "Monika smiles sweetly."
    return

label m_yuri_3:
    m 2e "Your style's gotten so refined, [player]."
    m "Yuri's been teaching you a lot of things, hasn't she?"
    mc "Well--"
    mc "I guess so."
    m 2a "Yeah... I've been noticing how much time you spend with her."
    m 2d "I think I've heard her say more words these past couple days than she's talked in the whole year."
    m "Not sure how you did it, but that's pretty impressive..."
    mc "Well, she just needs some patience and a way to talk about all the things in her head, I guess..."
    mc "I'm still getting the hang of it, myself."
    m 2a "Hm..."
    m "You're certainly putting in a lot of effort."
    m 2e "You must really like her."
    mc "Eh? That's--"
    m 5 "Ahaha!"
    m "It's awfully suspicious, you know?"
    m "Spending time with her in the clubroom every day..."
    m "Reading that edgy novel with her..."
    mc "Well--!"
    mc "I just...feel bad that she has a hard time socializing."
    mc "It makes me want to make sure she doesn't spend all her time alone."
    mc "Besides, the novel isn't too bad either, you know..."
    m 1k "Alright, alright~"
    m "I get you."
    m 1a "Just...be careful, alright?"
    m "I know that Yuri isn't used to opening herself up..."
    m 2d "So if something bad happens while she's vulnerable..."
    m "Then it could be really hard for her."
    m 2i "Her books aren't a total escape from reality."
    m "They're just a bandage."
    mc "You say that like I'm going to hurt her..."
    m 1l "Sorry, I didn't really mean that~"
    m "If anything, she might accidentally hurt herself."
    return
