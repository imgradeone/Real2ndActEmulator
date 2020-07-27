label ch21_main:
    $ chapter = 1
    show screen notify("当前 ch21")
    if persistent.recording:
        scene bg club_day
        with dissolve_scene_half
    else:
        scene bg club_day2
        with dissolve_scene_half
    if persistent.disable_awful_music:
        play music t2
    else:
        play music t2g3
    show monika 5 at t11 zorder 2
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "[player]，欢迎回来！"
    m "我还以为你会被我们吓跑呢。哈哈哈！"
    mc "呐，别担心。"
    mc "虽然有些奇怪，但我好歹是个守信的人嘛。"
    show monika at thide zorder 1
    hide monika
    "是的，我回到了文学部。"
    "我到得最晚，而其他人都已经在闲聊了。"
    show yuri glitch2 at t32 zorder 2
    y "谢谢你信守了诺言呢，[player]。"
    y 1a "希望这对你来说，不算一个太过沉重的承诺。"
    y 1u "让你在还不熟悉文学的时候就一头扎进去..."
    show natsuki glitch1 at i33 zorder 2
    n "拜托哦！说得就像是他可以偷懒一样！"
    n 4e "你已经是被 Monika 拉来的了。"
    n "我不知道你是打算过来随便看看的，还是什么别的..."
    n "不过你敢不把我们当回事的话，那你就完蛋了。"
    show monika 2b at l41 onlayer front
    m "有一说一，Natsuki，作为一个在部室私藏漫画的人，你这么说是想等着被禁言？？？"

    n 4o "M-M-M...！！"
    show monika at lhide onlayer front
    hide monika onlayer front
    "Natsuki 在\"Monika\"和\"漫画\"两个词之间卡住了。"
    show natsuki at h33
    n 1v "漫画也是文学！！"
    show natsuki at thide zorder 1
    hide natsuki
    "迅速败下阵来的 Natsuki 跌坐回了她的座位。"
    show yuri 2s at t11 zorder 2
    y "抱歉，[player]..."
    y "我们会尽力让你在社团里感到舒适的，好吗？"
    show yuri 2g
    "Yuri 向 Natsuki 投去了责备的一瞥。"
    y 1a "呃，不管怎样..."
    y "现在既然你已经是社团的正式成员了..."
    y "...也许你会有兴趣挑一本书来读读看？"
    mc "唔..."
    mc "我也没法拒绝，对吧。"
    mc "就像你说的，我已经是自己人了。"
    mc "所以，你说的没错，我是应该开始读点什么了。"
    y 4b "等-等一下..."
    y "我不是那个意思！"
    y "唔..."
    y "如果你真的不喜欢，那就当我没说过，就好吧..."
    mc "啊--不，Yuri，不是那样。"
    mc "我确实想要尽力成为社团的一员。"
    mc "所以即使我现在并不经常读书，我也很乐意听你的建议从现在开始读。"
    y 3t "你-你确定...？"
    y "我只是感觉..."
    y 3u "...呃，作为副部长的话..."
    y "...我大概应该让你从你喜欢的东西入手。"
    "Yuri 从她的包里翻出了一本书。"
    y 1s "我希望你可以更快地融入进来..."
    y "所以我就找了本你可能会喜欢的书。"
    y "故事不长，所以即使你偶尔看看，也应该可以保持你的注意力。"
    y "而且我们可以，嗯..."
    show yuri at sink
    y 4b "如果你想的话...可以一起讨论..."
    "这-这..."
    "这个女孩怎么突然这么可爱呢？"
    "就连我这样不常常看书的人，她都去挑了一本她认为我会喜欢的书给我..."
    mc "谢谢你，Yuri！我一定会读的！"
    "我热情地接过了那本书。"
    show yuri 2m at t11 zorder 2
    y "呼..."
    y 2a "嗯，你可以按照自己的节奏来读。"
    y "期待听到你的想法。"
    show yuri at thide zorder 1
    hide yuri
    show layer master

    #Exclusive scene starts here
    "既然大家都已经适应了，我本以为 Monika 会开始一些为社团安排好的活动。"
    "然而并没有。"
    "Yuri 已经把脸埋进了书里。"
    "我情不自禁地注意到了她那认真的表情，好像她等待这次机会已经很久了。"
    "与此同时，Natsuki 在储藏间里到处翻找着什么。"
    
    #Call exclusive scene
    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene
    call poemresponse_start
    jump ch21_end

    return

label ch21_end:
    stop music fadeout 1.0
    if persistent.recording:
        scene bg club_day
        with wipeleft_scene
    else:
        scene bg club_day2
        with wipeleft_scene
    if persistent.disable_awful_music:
        play music t3
    else:
        play music t3g
        queue music t3g2
    mc "呼..."
    "终于结束了。"
    "我扫视了一下教室。"
    "气氛比我预想中的更压抑一点。"
    "就好像所有人都在审视我那平庸的写作水平..."
    "哪怕她们都很宽容，我的诗还是完全没有办法与她们的作品相提并论。"
    "毕竟，这里是文学部嘛。"
    "我叹了口气。"
    "这就是我不自量力的结果吧。"
    "在教室的另一边，Monika 正在她的笔记本上写着些什么。"
    "我的目光随后转移到了 Yuri 和 Natsuki 身上。"
    show yuri 2g at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "她们慎重地交换了纸张，分享着各自的诗。"
    show yuri 2i at t21 zorder 2
    "在她们一起阅读时，我在一旁注意着她们的表情变化。"
    "Natsuki 的眉头皱了起来。"
    "与此同时，Yuri 苦笑着。"
    show natsuki at f22 zorder 3
    n 1q "{i}（这文笔是什么鬼啊...？）{/i}"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2f "诶？"
    y "emm...你刚刚说了什么吗？"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2c "哦，没什么。"
    "Natsuki 不屑一顾地把诗放回了桌子。"
    n "用词上还蛮不错的。"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2i "啊--谢谢..."
    y "你的诗...挺可爱的..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2h "可爱吗？"
    n 1h "你是不是完全不懂这首诗的寓意？"
    n "很明显它是描写放弃这种感受的。"
    n "所以这怎么可爱了？？？"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3f "我-我当然懂啊！"
    y "我只是说..."
    y 3h "文笔方面，大概..."
    y "我只是想说点好听的..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n "诶？"
    n 4w "你意思是，这首诗对于你来说，就连找点好听的话来形容都那么困难吗？"
    n "我 TM 谢谢你，这实际上一点都不好听！"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1i "唔..."
    y "好吧，我确实有几个建议..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 5x "哼。"
    n "如果我需要建议，那么我就会去找喜欢这首诗的人。"
    n "顺便告诉你，都有谁{i}已经{/i}喜欢这首诗了。"
    n 5e "Monika 喜欢。"
    n "[player] 也喜欢！"
    n "所以基于这些，我也乐意给你一点建议。"
    n "首先--"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2l "等一下..."
    y "你的心意我领了，不过我的写作风格是我花了大量时间建立起来的。"
    y 2h "我不想短时间内改变它，除非我遇到了什么特别激发我灵感的事情。"
    y "但迄今为止还没有。"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1o "嗯...？!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1k "而且 [player] 其实也喜欢我的诗。"
    y "他甚至还跟我说，我的诗给他留下了深刻的印象。"
    stop music fadeout 1.0
    "Natsuki 拍案而起。"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4y "哦？"
    n "Yuri，我才发现你为了取悦我们的新成员，简直费尽了心思。"
    if persistent.disable_awful_music:
        play music t7
    else:
        play music t7a
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1n "诶-诶？！"
    y "我不是那个意..."
    y 1o "唔..."
    y "你...你就是..."
    "Yuri 也拍案而起。"
    y 2r "你就是嫉妒 [player] 更赞同我的建议，而不是你的！"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1e "哈！你又知道他没有更重视{i}我{/i}的建议了？"
    n "你是懂王吗？？？"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3h "我...！"
    y "才没有..."
    y "如果我真的是懂王..."
    y 1r "...那我应该把事情搞得可爱到恶心啊！"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1o "唔唔唔...！"
    n "哼唧，你知道吗？！"
    n "某位女士，自从 [player] 一出现，欧派就多了一个奇怪的零件！！"
    show yuri 3p at h21
    show natsuki at t22 zorder 2
    y "N-Natsuki！！"
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    show monika 3l at l41 behind yuri,natsuki
    m "emm，Natsuki，咱能不能别开c--"
    show monika at h41
    show yuri 3p at f32 zorder 3
    show natsuki 1e at f33 zorder 3
    ny "关你屁事！"
    show monika at lhide
    hide monika
    show yuri 2h at f21 zorder 2
    show natsuki at t22 zorder 2
    if not persistent.disable_awful_music:
        queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise at noisefade(25 + timeleft) zorder 3
    show vignette as flicker at vignetteflicker(timeleft) zorder 4
    show vignette at vignettefade(timeleft) zorder 4
    show layer master at layerflicker(timeleft)
    y "把自己的不安情绪投射到别人身上..."
    y "Natsuki，你啊，还是 too young。"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4o "{i}又是我了？？？{/i}看看现在是谁在逼逼赖赖，你这个欲求不满的死碧池！" # 祖安 Natsuki
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y "死碧池...？欲求不满...？"
    y 2r "很抱歉，相对于你的心理年龄而言，想要理解我的生活方式，可能对你这种人来说太难了！"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4f "看吧？？"
    n "歪打正着！"
    n 4e "大部分人初中毕业后就学会克制自己了，可不像你。"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y "想要教训我的话，你先收起你那四处招惹人的司马态度吧！"
    y "你以为你可以通过自己可爱的穿着和行为，来掩盖你那糟糕的性格吗？"
    y 1k "到最后你唯一看起来可爱的地方就只剩下你可怜地做这种无用功了。"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2y "嚯，Yuri，说这种话的时候小心点，可小心话别太锋利，划伤了自己。"
    n "哦，抱歉...你不是已经在划了吗？"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3n "你-你刚刚是说我在割伤自己吗？？"
    y 3r "你 TM 脑袋里都在想什么？？？"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1e "来啊！继续啊！"
    n "让 [player] 来听听您的真实想法！"
    n "当他听完以后，一定会被您迷得神魂颠倒的咯！"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3n "啊-啊--！！！"
    show yuri at t21 zorder 2
    "突然，Yuri 转向了我，似乎她才注意到我一直站在这里。"
    show yuri at f21 zorder 3
    y 2n "[player]...!"
    y "她--她想让我尬场...！"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4w "你骗人！"
    n "是她先挑起来的！"
    show yuri 1t at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}wdnmd，我当初怎么就被牵扯进来的呢？！{/cps}{nw}"
    "{cps=*2}我对写作一窍不通啊...{/cps}{nw}"
    "{cps=*2}不过，不管我站在谁那边，她对我的评价可能会更高吧！{/cps}{nw}"
    "{cps=*2}那么，肯定是选择...{/cps}{nw}" # 这一段请翻历史查看
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "Natsuki。":
                jump menu_click
            "Yuri。":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 at i11 onlayer front:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('Natsuki。', True), ('Yuri。', True)], interact=False, screen='choice')
    m "..."
    show layer master
    show layer screens
    show monika 1 at i11 onlayer front
    window auto
    $ renpy.display_menu(items=[('Natsuki。', True), ('Yuri。', True)], interact=False, screen='choice')
    m "..."
    $ renpy.display_menu(items=[('Natsuki。', True), ('Yuri。', True)], interact=False, screen='choice')
    m "..."
    show monika 1m at i11 onlayer front
    $ renpy.display_menu(items=[('Natsuki。', True), ('Yuri。', True)], interact=False, screen='choice')
    m "emm..."
    $ renpy.display_menu(items=[('Natsuki。', True), ('Yuri。', True)], interact=False, screen='choice')
    m "嘿，[player]..."
    show monika 1e at i11 onlayer front
    $ renpy.display_menu(items=[('Natsuki。', True), ('Yuri。', True)], interact=False, screen='choice')
    m "咱们要不要先\n出去一下下？"
    $ renpy.display_menu(items=[('Natsuki。', True), ('Yuri。', True)], interact=False, screen='choice')
    m "好伐？"
    scene bg corridor
    hide monika onlayer front
    show monika 1n at t11 onlayer master
    with wipeleft_scene
    $ quick_menu = True
    m "肥肠抱歉..."
    m "她们真的不应该把你也一并牵扯进来的。"
    m 1e "咱还是别搅和吧..."
    m "等她们不吵了我们再回去吧。"
    m 5 "啊哈哈..."
    m "真是个不称职的部长啊...w"
    m 1m "我甚至都没办法正面处理部员的情绪..."
    m "我有时候也希望自己变得更强硬一点。"
    m "但是我实在不擅长反对别人..."
    m 1e "你也懂吧？"
    m "总之..."
    m 1a "如果这能让你少花点时间在她们身上，那就太好了。"
    m 1j "我很乐意多陪陪你..."
    show monika at thide zorder 1
    hide monika
    "突然，Natsuki 跑出了教室。"
    show natsuki 12h at t11 zorder 2
    n "..."
    show natsuki 12f at lhide
    show screen notify("Natsuki 哭了，都是你的错！哼唧（")
    $ pause(0.75)
    hide natsuki
    "她很快跑走了。"
    show monika 1l at t11 zorder 2
    m "天哪..."
    m "...好吧，看来她们吵完了..."
    if persistent.recording:
        scene bg club_day
        with wipeleft_scene
    else:
        scene bg club_day2
        with wipeleft_scene

    y "我不是那个意思..."
    y "我不是那个意思..."
    y "我真的不是那个意思..."
    "Yuri 用手捂着额头，不断地在她的座位前后摇摆着。"
    mc "Yuri...？"
    show yuri 4d at t11 zorder 2
    y "我真的不是那个意思啊！！"
    mc "我-我相信你..."
    "我完全无法想象 Yuri 可能对 Natsuki 讲了些什么。"
    "或者已经说了些什么。"
    y "[player]..."
    y "请不要因为这件事讨厌我。"
    y "千万别啊！"
    y "我从来不是这个样子！"
    y "今天的我一定是哪里出问题了..."
    show monika 1d at f31 zorder 3
    m "没事的，Yuri。"
    m "我们知道你不是那个意思。"
    m 1j "况且，Natsuki 明天就会全忘了的。"
    m 1a "彻彻底底、一干二净的那种。"
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 4b "..."
    show yuri at t32 zorder 3
    show monika at f31 zorder 2
    m "总之，今天的社团活动就到这里吧，你们想回家的话可以回去了。"
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 4a "..."
    show yuri at t32 zorder 2
    "Yuri 看着我，似乎想要说些什么。"
    "但是她也不断瞟着 Monika..."
    show yuri at f32 zorder 3
    y 2v "Monika...你-你可以先走的..."
    y "我想稍微多待一会。"
    show yuri at t32 zorder 2
    show monika at f31 zorder 3
    m 2k "我是部长，所以我才应该是最后离开的那个。"
    m "我会等你弄完的。"
    show monika 2a at t31 zorder 2
    show yuri at f32 zorder 3
    y 4b "..."
    y "..."
    y "呃--我是副部长，所以..."
    y "今天就让我代行这个职责好了。"
    show yuri at t32 zorder 2
    show monika at f31 zorder 3
    m 2i "Yuri，这听起来就像是你想做什么事，但是又不想让我在身边呐。"
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 3p "不-不是你想的那样！"
    y 3o "不是那样..."
    y 3n "我只是..."
    y 3q "我只是都还没来得及和 [player] 讨论我的书..."
    y "你要是在一边听的话...也许会有点尴尬..."
    show yuri at t32 zorder 2
    show monika at f31 zorder 3
    m 1r "{i}*叹气*{/i}"
    m 1d "这样的话，我也没得选了，不是吗？"
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 1t "抱-抱歉给你添麻烦了..."
    $ gtext = glitchtext(20)
    y 1s "但是我真的希望你可以理j{nw}"
    play music g1
    show monika 1 at i31 onlayer front
    y glitch "但是我真的希望你可以理j{fast} [gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    call poem(False)
    jump ch22_main
    return

