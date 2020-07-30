label yuri_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    "我很想和 Yuri 再多聊聊..."
    "但是打搅到她看书就不太好了。"
    "我瞥了一眼她的书的封面。"
    "好像就是她借给我的那本..."
    "不仅如此，她好像还在看最开始的几页。"
    play music t6 fadeout 1.0
    show yuri 4a at t11 zorder 2
    y "啊..."
    "淦--"
    "她似乎注意到我在看她了..."
    "她又偷偷看了我一眼，我们视线有那么一瞬间交汇上了。"
    y 4b "..."
    "可她却把头埋进书里，埋得更深了。"
    mc "抱歉..."
    mc "我只是在发呆..."
    "我喃喃地说着，觉得自己是不是让她感觉不舒服。"
    $ achievement.grant("眉 飞 色 舞")
    # why: special notify
    #if persistent.ddmm_mode:
    #    $ ddmm_earn_achievement("")
    show screen notify("达成成就：眉 飞 色 舞（不信你就挂机一下再回来看）")
    y oneeye "哦..."
    y "没事的..."
    y "要是我注意力集中的话，那我一开始也就不会注意到了。"
    y "不过我只是在重读这本，所以..."
    mc "这是你给我的那本，对吧？"
    y "嗯哼。"
    y "我只是想重读一部分而已。"
    y 2q "并没有什么特别的原因啦...！"
    mc "我只是好奇地问下，你怎么会有两本一样的书呢？"
    y "啊..."
    y "嗯，昨天我去书店的时候--"
    y 3o "啊，我不是那个意思..."
    y "我是说--"
    y 1w "我...只是正好买了两本而已。"
    mc "啊，好吧。"
    "显然 Yuri 并没有告诉我实情，但我决定不再追问了。。"
    mc "我一定会尽快开始读的！"
    y 2u "那挺好的..."
    y "一旦你开始读了，恐怕你就再也停不下来了。"
    y 2c "这是个非常紧凑精致的故事。"
    mc "这样吗..."
label yuri_exclusive2_1_ch22:
    mc "话说，它大概是讲什么的呢？"
    y 1f "Well..."
    y "emm..."
    "我看了看书的封面。"
    "这本书叫《Portrait of Markov》（马卡洛夫的肖像）。"
    "封面上还有一个恐怖的眼睛符号。"
    y 1a "总地来说，这本书讲的是一个宗教阵营变成了人/体/实/验/监/狱..."
    y "困在里面的人有个特点，他们都变成了嗜/血的杀/人/机/器。"
    y 1m "但是设施里还有更阴暗的一面，他们开始选择性的肢/解人体并把它们接到--"
    y 1q "哦-哦，这好像有点剧透了..."
    y 3q "但是，我-我真的沉浸于此了！"
    y 3n "...我的意思是，我很喜欢这本书！"
    y 3q "不-不是关于肢///解什么的..."
    mc "这 TM 有点--！"
    "有点黑暗，对吧？"
    "Yuri 的语气让我觉得它像是一个愉快的故事，可情节却十分暗黑。"
    y 1s "啊..."
    y "你是不是不太喜欢这种故事啊，[player]？"
    mc "不，那倒也不是..."
    mc "我是说，这种小说我也可以读下去啦，不要担心。"
    y 2u "但愿吧..."
    "是啊...我完全忘记了一件事，Yuri 很喜欢这类黑暗深邃的故事。"
    "她看起来害羞又孤僻，但思维却好像完全不同。"
    y "这只不过是一类故事啦..."
    y 1a "这种类型会挑战你，让你从一种新奇的角度去看待生活。"
    $ style.say_dialogue = style.normal
    y "恐怖事件的起因，有时候并不仅仅只是有人想要作恶..."
    $ style.say_dialogue = style.edited
    y "而是因为世界上全是恶人，活着反正也没有任何价值。"
    y "突然rrrrrrrrrrrrrrrrrrrrrrrrrr rrrrrrrrrrr{nw}"
    $ style.say_dialogue = style.normal
    y 3v "我...我刚刚是不是在扯淡...？"
    y "下次绝不..."
    y 4b "抱歉..."
    mc "嘿，不用道歉的...！"
    mc "我没有丧失兴致啊。"
    y "Well..."
    y "那就好..."
    y 4a "但是我觉得，最好还是让你了解一下我的这个问题...."
    $ style.say_dialogue = style.normal
    y "当我沉浸在书籍或者写作的世界里的时候..."
    $ gtext = fujaowee(24)
    $ style.say_dialogue = style.edited
    y "我全身都会超级 [gtext]{nw}"
    $ style.say_dialogue = style.normal
    # $ _history_list.pop()
    y "我有时候可能会忽略周边的人..."
    y 3t "所以如果我又说了什么奇怪的话，真的很抱歉！"
    y "如果我又开始讲个不停，拜托阻止我一下！"
    mc "其实--"
    mc "我真的不觉得你应该担心这个..."
    mc "只是说明你对阅读有着莫大的热情罢了。"
    mc "至少我还可以在一旁听着。"
    mc "毕竟这里是文学部嘛..."
    y 4a "啊--"
    y "好像..."
    y "好吧，确实是这样..."
    mc "其实..."
    mc "我也该开始读这本书了，对吧？"
    play sound "sfx/glitch3.ogg"
    call grant_achievement_all("七 龙 珠", "")#todo
    y dragon "吼-吼哇！！GKD！"
    y 3n "我-我的意思是，你也不是非要读它，但是...！"
    mc "啊哈哈，你在说些什么啊？"
    y 3o "..."
    mc "我先把它拿出来..."
    "我迅速将那本书从包里拿了出来。"
    mc "好了...我坐在这里没问题吧？"
    "我小心地在 Yuri 旁边的位置坐下。"
    y 3n "啊...！"
    y "可以..."
    mc "你认真的吗？"
    mc "你好像有点不安的亚子..."
    y "那只是..."
    y 4b "抱歉..."
    y "不是我不希望你坐在这里！"
    y "只是我还不是很习惯..."
    y "...有人陪我看书。"
    mc "这样啊..."
    mc "嗯，如果我让你分心了的话，你直接告诉我就好。"
    y "好-好的..."
    show yuri at thide zorder 1
    hide yuri
    "我翻开书、读起了序章。"
    "我很快就明白了 Yuri 所说的，有人陪着阅读是怎样的体验了。"
    "我在阅读的时候，似乎可以感受到她就在我的肩头。"
    "这倒也不是什么坏事。"
    "虽然可能会让人分心，不过还是挺舒服的。"
    "Yuri 就在我视线的角落里。"
    "我意识到她并没有在看自己的书。"
    "我瞟了过去。"
    "好像她在读我的这本--"
    show yuri 3n at t11 zorder 2
    y "抱-抱歉！"
    $ style.say_dialogue = style.normal
    y "我只是--！{nw}"
    $ style.say_dialogue = style.edited
    y "我只是{fast}沉浸在你的体温wwwwwwwwwwwwwwww温 温wwwwwwwww体iiiiiiiiiiiiiiiiiiii{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()

    mc "Yuri，你道歉得实在太多啦。"
    y "是...是吗？"
    y 4a "我不是故意的..."
    y "抱歉..."
    y 4c "我是说--！"
    mc "啊哈哈。"
    mc "来，这样可以了吧？"
    "我把桌子靠到 Yuri 的桌子上，然后把我的书捧在了两张桌子中间。"
    y 2v "啊..."
    y "我-我觉得可以..."
    "Yuri 羞涩地合上了她自己的那本书。"
    "两个人都稍稍倾斜一点的话，肩膀就几乎要碰到了。"
    "似乎我的左臂挡住了她的视线，所以我开始用我的右手拿书。"
    mc "唔，这样的话我翻书就有点困难了..."
    y "这样..."
    $ persistent.clear[2] = True
    scene y_cg1_base with dissolve_cg
    "Yuri 拿起左手，用拇指与食指拿住了书的左半边。"
    mc "啊..."
    "我学着她的样子用右手拿住了书的右半部分。"
    "这样一来，我每翻过一页，Yuri 就把那页扣在拇指下。"
    "但是这样拿书的话..."
    "我们比之前挤得更近了。"
    "这完全就是干扰...！"
    "我都可以感受到 Yuri 脸颊的温暖，而且她就在我视线的一旁..."
    show y_cg1_exp1 at cgfade
    y "...你准备好了吗？"
    mc "诶？"
    y "准备好翻页了吗..."
    mc "啊...抱歉！"
    mc "我刚刚走神了..."
    "我再次望向 Yuri 的脸，我们的视线交汇了。"
    "我不知道自己怎么样才能跟上她的节奏..."
    y "啊..."
    show y_cg1_exp2 at cgfade
    y "没关系的。"
    y "你平常不太读书吧？"
    y "如果你要多读一会的话，我等你一下也没问题..."
    y "毕竟你对我这么有耐心..."
    y "我也耐心等等你是最起码的..."
    mc "好-好吧..."
    mc "谢谢。"
    hide y_cg1_exp1
    hide y_cg1_exp2
    "我们继续阅读。"
    "Yuri 没再问过我要不要翻页。"
    "于是我就默认她读得比我快，在自己看完时就直接翻页了。"
    "我们就这样一言不发地读完了第一章。"
    "即使不说话，每次翻页也都像是一次亲密交流..."
    "我的拇指轻柔地放出纸页，飞向 Yuri，而 Yuri 也用拇指接下它。"
    mc "嘿，Yuri..."
    mc "这样想可能有点傻，不过..."
    mc "我在主角身上看到了一些你的影子。"
    show y_cg1_exp3 at cgfade
    y "诶-诶？？"
    y "不-不可能，我和她一点也不像！"
    y "绝对不像！"
    mc "真的吗...？"
    mc "我只是觉得她会反复思考一些事的习惯，之类的..."
    show y_cg1_exp1 at cgfade
    y "啊-啊..."
    y "你是在说这个啊..."
    hide y_cg1_exp3
    hide y_cg1_exp1
    show y_cg1_exp2 at cgfade
    y "抱歉..."
    y "我以为你是指...她另外的一些方面。"
    mc "另外的方面...？"
    hide y_cg1_exp2
    show y_cg1_exp3 at cgfade
    y "别-别管了！"
    y "我们都还没读到那里呢..."
    y "所以我也不知道为什么我会这样想..."
    y "啊哈哈！"
    mc "Yuri，你还好吧？"
    hide y_cg1_exp3
    show y_cg1_exp1 at cgfade
    y "诶--？"
    "从开始读书那时起，Yuri 就显得有些坐立不安..."
    mc "你要是觉得不太舒服，那可以先休息一下。"
    mc "你的呼吸有点..."
    y "我的呼吸...？"
    hide y_cg1_exp1
    "Yuri 将手搭在了胸前，似乎在感受自己的心跳。"
    y "我-我都...没注意..."
    show y_cg1_exp3 at cgfade
    y "...不过，我没事的！"
    y "我只是想喝点水...！"
    mc "好吧...别勉强自己。"
    scene bg club_day
    with dissolve_cg
    "Yuri 起身仓促地跑出了教室。"
    mc "发生啥事...？"
    show monika 1d at t11 zorder 2
    m "[player]？"
    m "刚刚是不是发生了什么？"
    mc "呃？"
    mc "不知道..."
    mc "Yuri 大概有点反常吧..."
    m 1r "所以你也什么都不清楚..."
    mc "抱歉，我是真的没头绪。"
    mc "你在担心她吗？"
    m 1a "哦...倒也没有。"
    m "我只是想确认一下你有没有对她做什么。"
    mc "怎-怎么可能！"
    m 5 "啊哈哈，别担心...我相信你，小傻瓜。"
    m "Yuri 有时候是会这样，没什么可怕的。"
    mc "好吧...如你所想。"
    m 2b "总之，我们是不是该开始相互分享我们的诗了？"
    mc "诶？"
    mc "我们不等 Yuri 了吗？"
    m 2a "嗯，她也许还要一会儿，所以我已经决定就这样开始吧。"
    m "不过这样真的没问题吗？"
    mc "好吧，我只是问问..."
    "我站了起来。"
    "我大概记了下自己读到哪里后，把书放回了包里。"
    $ y_ranaway = True
    return

label yuri_exclusive2_2:
    $ y_exclusivewatched = True
    play music t6 fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    mc "嘿，Yuri。"
    show yuri 2f at t11 zorder 2
    y "诶？"
    mc "啊..."
    "我突然注意到 Yuri 正在读的是另一本书，而不是我们一起读的那本。"
    mc "抱歉！打扰你了..."
    y 2m "啊，没事..."
    y "我其实也是在等你..."
    show yuri 2a
    mc "喔，那这样的话..."
    mc "那我们开始吧？"
    y 2c "嗯，好啊！"
label yuri_exclusive2_2_ch22:
    y 3a "事实上，我有一个请求..."
    y "...我可以先沏一些茶吗？"
    mc "没问题。"
    y 1c "谢谢你。"
    y 1a "如果世上有什么可以让我的阅读时光更加完美，那么它一定就是一杯温润的茶了。"
    y "更何况是自己给自己沏的茶。"
    show yuri at thide zorder 1
    hide yuri
    "Yuri 站了起来，走向储藏间。"
    "我在后面跟着，看着她从书架上取出了那种带滤网的小茶壶。"
    show yuri 1f at t11 zorder 2
    y "你能拿一下这个吗？"
    mc "行..."
    "Yuri 把茶壶递给我，自己则拿了个电热水壶。"
    y "我去把这个插到讲台那边，然后我会去盛水。"
    show yuri at thide zorder 1
    hide yuri
    "她从我身边走过，给水壶通上了电。"
    "我则只是站着看她走来走去。"
    "很惊讶的是，她的走路姿态与她平时的讲话习惯间有着惊人的反差。"
    "尤其是配合她那修长的腿，显得十分端庄高雅。"
    show yuri 1f at t11 zorder 2
    y "好啦，可以把茶壶给我吗？"
    y 1a "谢谢，我马上回来。"
    mc "啊，我也许可以和你一起去..."
    y 1q "不-不用的！"
    y "你待在这里就好..."
    y "不会太久的。"
    show yuri at thide zorder 1
    hide yuri
    "Yuri 拿着茶壶，快步走出了教室。"
    show monika 2i at t11 zorder 2
    m "啊..."
    m "優里又留下你一个人出去了？"
    mc "不，这次和上次不一样。"
    mc "她只是用茶壶去盛用来沏茶的水而已。"
    m 5 "哦，好吧！"
    m "抱歉，误会了～"

    scene bg club_day
    with wipeleft_scene

    "..."
    "十分钟过去了。"
    "Yuri 明明说了不会太久的啊..."
    "有什么事情耽搁了吗？"
    "干等着实在有些无聊，所以我决定出去找找她。"
    scene bg corridor
    with wipeleft_scene
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 10.893>bgm/6o.ogg"
    mc "让我康康..."
    "从逻辑上来讲，Yuri 应该是在最近的饮水机那里..."
    $ y_name = "Yuri"
    "我沿着走廊走去。"
    $ y_name = "???"
    y "哈啊.....哈啊...."
    y "....哈啊.....哈啊...."
    "...这啥声音啊？"
    "是从那边的角落里传来的..."
    "听上去像呼吸声。"
    y "嘶--"
    "突然发出了尖锐的吸气声，像是有人在咬着牙吸气。"
    "那很痛吗...？"
    "我走到了转角，四处看了看。"
    mc "Yuri...？"
    $ y_name = "Yuri"
    if persistent.alt_safe_mode:
        show yuri 2n at t11 zorder 2
    else:
        show yuri cuts at t11 zorder 2
    y "噫啊--！"

    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>bgm/6r.ogg"
    if persistent.disable_awful_music:
        show screen notify("为营造游戏气氛，我不能放正常版 BGM，抱歉（（（")
    play music t6r
    show yuri at thide zorder 1
    hide yuri
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    show layer master at rewind
    $ y_name = "???"
    mc "{cps=*3}Yuri...？{/cps}{nw}"
    "{cps=*3}我走到了转角，四处看了看。{/cps}{nw}"
    "{cps=*3}那很痛吗...？{/cps}{nw}"
    "{cps=*3}突然发出了尖锐的吸气声，像是有人在咬着牙吸气。{/cps}{nw}"
    y "{cps=*3}嘶--{/cps}{nw}"
    "{cps=*3}听上去像呼吸声。{/cps}{nw}"
    "{cps=*3}是从那边的角落里传来的...{/cps}{nw}"
    "{cps=*3}...这啥声音啊？{/cps}{nw}"
    y "{cps=*3}....哈啊.....哈啊....{/cps}{nw}"
    y "{cps=*3}哈啊.....哈啊....{/cps}{nw}"
    $ y_name = "Yuri"
    "{cps=*3}我沿着走廊走去。{/cps}{nw}"
    "{cps=*3}从逻辑上来讲，Yuri 应该是在最近的饮水机那里...{/cps}{nw}"
    mc "{cps=*3}让我康康...{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    show layer master at rewind
    "{cps=*3}干等着实在有些无聊，所以我决定出去找找她。{/cps}{nw}"
    "{cps=*3}有什么事情耽搁了吗？{/cps}{nw}"
    "{cps=*3}Yuri 明明说了不会太久的啊...{/cps}{nw}"
    "{cps=*3}十分钟过去了。{/cps}{nw}"
    "{cps=*3}...{/cps}{nw}"

    $ del _history_list[-37:]
    if poemwinner[0] == "yuri" and chapter == 3:
        jump yuri_exclusive2_2_ch23
    $ currentpos = 90.528 - (get_pos() * 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    play music t6r
    hide noise
    hide vignette
    show layer master
    show yuri 1a at t11 zorder 2
    y "我回来了。"
    y "感谢你的耐心等待。"
    y "[player]，你喜欢乌龙茶吗？"
    mc "啊，是的。"
    mc "随便吧。"
    y "很好。"
    "Yuri 将电热水壶的温度设定到了 200℉（约 93℃）。"
    y 1f "是时候去把茶壶拿来了。"
    mc "你沏茶好正式啊。"
    y 1u "当然啦..."
    y "为别人沏茶时，我只会更用心的。"
    mc "即使我不是很懂茶艺也...？"
    y 2m "嚯嚯。"
    y 2a "那样的话，你只会更惊叹我的技艺。"
    mc "嗯...肯定会的！"
    show yuri at thide zorder 1
    hide yuri
    "Yuri 拿过茶壶，开始量取茶叶。"
    "出乎我的意料，她甚至轻轻地哼起了歌。"
    show yuri 1c at t11 zorder 2
    mc "你现在的心情一定很好吧..."
    y 1a "是吗？"
    y "我在试着让情绪流露..."
    y "而你注意到了。"
    y 2u "我刚刚想了想..."
    y "我决定试着多表达一点自己的感情。"
    y "事实证明，这对我来说并不太难..."
    y 1c "只要在我身边的人是你。"
    show yuri 1a
    mc "啊..."
    mc "Yuri，那太棒了！"
    mc "只是别太勉强自己就行了。"
    y 3u "[player]，你总是在为我着想..."
    y "这真的很招人喜欢。"
    mc "这..."
    "Yuri 是认真的..."
    "我都不知道自己能不能跟上她的节奏了...!"
    "我看着 Yuri 为我们两人各沏了一杯茶。"
    y 1a "[player]，我还有一个想法。"
    y "你介意我们今天坐在地板上读书吗？"
    mc "诶？为什么？"
    y 1h "我的背会好受一些..."
    y "背靠着墙会比弯在座位上更舒服一些。"
    mc "啊，抱歉，昨天我都没有意识到。"
    y 1a "没关系。"
    y "只是我很容易背痛，所以得多小心一点。"
    mc "是吗？"
    mc "为什么会背痛呢..."
    y 1f "可能是因为我的--"
    y 1n "啊--"
    y 1o "我-我的..."
    mc "你的阅读姿势，对吧？"
    mc "总是趴在桌子上读书..."
    y 2p "对！"
    y 2q "我的阅读姿势很糟！"
    y "所以我们应该坐到地上。"
    mc "有道理。"
    mc "那我先去那边拿书。"
    show yuri at thide zorder 1
    hide yuri
    "我把书从包里抽了出来。"
    mc "啊，我还有一些巧克力..."
    "这是一包巧克力糖。"
    "配茶也许很不错，所以我就拿了出来。"
    "Yuri 和我背靠着墙坐下了，而茶杯放在了一边。"
    "我们默契地恢复了与昨天相同的阅读姿势，分别握住书的一边。"
    "只是这次..."
    "我们靠得更近了。"
    show yuri 2h at t11 zorder 2
    y "我有点看不清..."
    mc "--！"
    show yuri 2e at d11
    "Yuri 又靠近了一点，以至于我们的肩膀都挨住了。"
    "这样我还怎么专心看书啊喂...？！"
    "Yuri 平时已经足够可爱了，但..."
    "只要她稍微放下心防，她就可爱到让我无法承受了！"
    y 2f "你的茶杯..."
    "Yuri 把我的茶杯递了过来。"
    "我用空着的手接过茶杯，现在的姿势让我越来越难以专注了。"
    "因为现在我还要注意，自己的手会不会碰到 Yuri 的欧派...！"
    "同时，Yuri 却好像什么都没注意。"
    "她维持着和往常一样热切的阅读表情。我猜她已经将书中世界以外的事抛在脑后了。"
    "我勉力保持着阅读的专注。"
    "..."
    "几分钟后，我终于可以放松一点了。"
    "我把茶杯放在了腿间，试着打开巧克力的包装纸。"
    mc "啊，对不起..."
    "为了打开包装，我的手短暂地离开了书。"
    mc "你想吃多少都行。"
    y 2s "啊这..."
    y "谢谢了，但我还是不吃了..."
    mc "诶？确定吗？"
    mc "诶？确定吗？"
    y "手粘上巧克力的话，书页会被弄脏的..."
    mc "啊，有道理..."
    mc "我都没考虑到这些呢。"
    mc "我的锅..."
    y 2a "没必要道歉的。"
    y "我来拿着书吧，可以吗？"
    mc "你确定吗...？"
    y "当然。"
    $ persistent.clear[3] = True
    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    "Yuri 用双手撑开了书。"
    "让她举着反而不会对我的阅读造成什么麻烦。"
    "但是正因如此，她的左臂几乎搭在了我的腿上。"
    mc "呃，那..."
    "Yuri 又已经完全沉浸进去了。"
    "我将一块巧克力丢进了嘴里。"
    "然后，我拿起了另一块..."
    "递到了 Yuri 的面前。"
    "她眼神都没离开过书。"
    "只是自然地张开了嘴，好像这是很正常的行为。"
    "但这样的话，我就只能直接喂了！"
    hide y_cg2_nochoc
    "我小心地将巧克力放进了她的嘴里。"
    "Yuri 配合地咬住了巧克力。"
    y "诶...？"
    show y_cg2_exp2
    "Yuri 严肃的表情瞬间消失了。"
    y "我..."
    y "我刚刚..."
    "Yuri 看了看我，似乎在确认刚刚发生了什么。"
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    y "emmmmm..."
    y "[player]..."
    mc "抱-抱歉！"
    mc "我不该这样的..."
    stop music
    y "啊-啊..."
    "Yuri 的呼吸开始沉重了起来。"
    y "我..."
    y "我不能..."
    y "[player]..."
    "突然，Yuri 抓住我的胳膊，将我甩开。"
    "我的茶杯也被打翻了。"
    scene bg closet
    show yuri 2t at t11 zorder 2
    with wipeleft
    y "[player]..."
    play sound closet_close
    show dark zorder 100
    with wipeleft
    y "我的心..."
    y 2y6 "我的心不会停止跳动的，[player]..."
    y "我冷静不下来。"
    y "我再也没法专注于任何东西了...!"
    y "[player]，你感觉到了吗？"
    "Yuri 突然把我的手按在她的胸前。"
    play music hb
    show layer master at heartbeat
    y 3t "为什么这会发生在我身上？"
    y "就像失去自我意识..."
    y 3y4 "我停不下来了。"
    y 3y6 "我甚至不想读书了..."
    y "我只想..."
    y 3s "...看着..."
    y "...你。"
    hide yuri
    call grant_achievement_all("Touch", "") # todo
    show yuri eyes
    pause 3.0
    y "...哈啊..."
    pause 3.0
    y "...哈啊..."
    pause 3.0
    y "...哈啊..."
    pause 3.0
    play sound closet_open
    stop music
    show layer master
    hide yuripupils
    show yuri 1n at face
    with None
    show yuri 3n at t32 with None
    hide dark
    show monika 3l at f31 zorder 3
    with wipeleft
    m "emm..."
    m "是时候...分享写的诗了..."



    return

label yuri_exclusive2_2_ch23:
    scene black
    with None
    $ audio.t6g = "<loop 10.893>bgm/6g.ogg"
    if persistent.disable_awful_music:
        play music t6
    else:
        play music t6g
    pause 4.62
    scene bg corridor
    show yuri eyes_base
    call grant_achievement_all("O w O", "") # todo
    pause 1.0
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show yuri glitch at i11
    $ gtext = glitchtext(80)
    $ currentpos = get_pos()
    if not persistent.disable_awful_music:
        play music g1
    y "[gtext]{nw}"
    stop music
    scene bg corridor
    show yuri 2n at i11
    y "emm..."
    y "等等..."
    y 2o "我刚刚..."
    y 2y6 "...抱歉，我只是有种奇怪的熟悉感..."
    y "以前没发生过类似的事情...吧？"
    y 2t "我最近有些恍惚..."
    y 3t "希望没有太明显！"
    y "如果我们才刚刚开始相处你就觉得我古怪的话，我会伤心的..."
    y "我是说..."
    show bg corridor:
        xoffset 0
        parallel:
            0.36
            xoffset 1
            repeat
        parallel:
            0.49
            xoffset 0
            repeat
    show black zorder 5:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat

    play music t9
    y "每个人都会有些奇怪的习惯。"
    y 1v "但是刚见到别人时就分享这些，会显得比较不合群...甚至惹人讨厌。"
    y "至少，这是我的发现。"
    y "我小时候，似乎有点过于强势和认真..."
    y "别人都不太想靠近我。"
    y 2w "所以...我开始恨自己。"
    y "比如，我对某种爱好的过度迷恋。"
    y "还有一旦对某件事感到过于兴奋，我就会失控。"
    y "因此..."
    y 1v "我逐渐不和人说话了。"
    y "如果我认为重要的东西只会让我越来越被人讨厌...。"
    y 1u "...那自闭起来似乎要好点。"
    y 1h "但最近，又出现了问题。"
    y "我不知道为什么。"
    y 2y6 "每次我走进社团，我的心脏就开始狂跳。"
    y "就好像是要撞开胸口的那种感觉。"
    y "无法释放的能量和情感淹没了我。"
    y "这驱使我做奇怪的事。"
    y 2t "我不知道为什么会这样！"
    stop music
    y 1t "[player]..."
    y "最近有点离谱的不只有我，Monika 也一样对吧？"
    y 1v "加入社团以来，她一直都很贴心..."
    y "可最近，只要她在身边，气氛就会谜之尖锐。"
    y 2y4 "我没疯，对吧？"
    y 2y1 "快告诉我，我没疯！"
    y "我前面什么都不能说，因为她一直都在听着！"
    y 2y3 "但是现在，我们终于独处了..."
    y "我们可以在这里多待一会吗？"
    y 1m "好吧..."
    y "..."
    play music hb
    show layer master at heartbeat
    show yuri as yuri_eyes zorder 4:
        "yuri/eyesfull.png"#还是三次元之眼
        i11
        alpha 0.0
        block:
            2.012 * 4 - 1.49
            alpha 1.0
            0.52
            alpha 0.0
            1.49
            repeat
    pause 2.0
    # m0nika 在看着你
    $ ad = 40.0
    $ ac = 1.0
    show monika 1 at malpha(ac / ad) onlayer front
    y 1s "我只想留在这里。"
    $ ac += 0
    show monika 1 at malpha(ac / ad) onlayer front
    y "只有我们两个。"
    $ ac += 0
    show monika 1 at malpha(ac / ad) onlayer front
    y "我们可以留在这里，直到社团活动结束。"
    $ ac += 0
    show monika 1 at malpha(ac / ad) onlayer front
    y 1m "那样我们就能在偌大的部室里独处了。"
    $ ac += 0.5
    show monika 1 at malpha(ac / ad) onlayer front
    y "再也没有人干扰我们的阅读时光。"
    $ ac += 0.5
    show monika 1 at malpha(ac / ad) onlayer front
    y 1y4 "再没有人让我如自///残般痛苦。"
    $ ac += 0.5
    show monika 1 at malpha(ac / ad) onlayer front
    y 1q "啊哈哈..."
    $ ac += 0.5
    show monika 1 at malpha(ac / ad) onlayer front
    y "开个玩笑！"
    $ ac += 0.5
    show monika 1 at malpha(ac / ad) onlayer front
    y "别当真。"
    $ ac += 0.5
    show monika 1 at malpha(ac / ad) onlayer front
    y 1i "其实，我很喜欢刀..."
    $ ac += 0.5
    show monika 1 at malpha(ac / ad) onlayer front
    y "听上去有点怪，但如果你没见过这些刀子有多美，你是不会明白的。"
    $ ac += 0.5
    show monika 1 at malpha(ac / ad) onlayer front
    y 1f "我有个想法。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "你哪时来我家看看如何？"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1y6 "我可以给你看我的刀具收藏。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "那里有不同工匠铸造的各类刀具。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1a "每把刀我都会合理地使用。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1m "它们永远不会感到孤独..."
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1y6 "没有人，生来就该孤独。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1y4 "没有的。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1c "所以，[player]，你能加入文学部，我很开心。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1a "我们永远不会孤独了。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "因为我们拥有彼此。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "每一天都如此。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "这就是我要的。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1y6 "这样吧？"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "干脆我们一起退部。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "我们为什么还要忍受 Monika 的油嘴滑舌。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1y4 "更别提还有一个可悲的小白癡。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1s "我们每天可以一起回家。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "一起阅读。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1m "一起吃饭。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y "一起睡觉。"
    $ ac += 1
    show monika 1 at malpha(ac / ad) onlayer front
    y 1s "是不是很爽啊？"
    $ ac += 2
    show monika 1 at malpha(ac / ad) onlayer front
    y "这就是我想要的一切。"
    $ ac += 2
    show monika 1 at malpha(ac / ad) onlayer front
    y 1a "难道这不就是你最开始加入社团的理由吗？"
    $ ac += 2
    show monika 1 at malpha(ac / ad) onlayer front
    y "这就是命啊！" # @极限挑战
    $ ac += 2
    show monika 1 at malpha(ac / ad) onlayer front
    y "命运让我们在一起了！"
    $ ac += 2
    show monika 1 at malpha(ac / ad) onlayer front
    y "现在我终于迎来了我等了几个世纪的 Happy Ending。"
    $ ac += 2
    show monika 1 at malpha(ac / ad) onlayer front
    y "[player]，你会陪我一起吗？"
    $ ac += 2
    show monika 1 at malpha(ac / ad) onlayer front
    $ gtext = glitchtext(200)
    y "你hui{space=60}[gtext]{nw}"
    hide monika onlayer front
    window hide(None)
    $ poemsread = 0
    $ y_gave = False
    play music t5
    scene bg club_day
    window show(None)
    window auto

    return
