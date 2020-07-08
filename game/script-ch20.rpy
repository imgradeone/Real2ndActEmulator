label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    jump ch20_main2

label ch20_main2:
    "今天，一如既往，是个平常的上学日。"
    "早上可以说是最糟糕的，会被周围的现充包围着走到学校。"
    "与此同时，我却总是一个人。"
    "我经常告诉自己，差不多是时候该找一个女朋友之类的了..."
    "但我确实没什么动力去加入什么社团。"
    "可以把空余时间花在游戏和动画上，我其实已经相当满足了。"
    "学校总是会有动画部的，但是那里怎么可能会有女孩啊..."
    
    scene bg class_day
    with wipeleft_scene

    "在学校的日子和往常一样平淡，不知不觉就结束了。"
    "整理完书包，我茫然地盯着墙，完全没有半点动力。"
    mc "社团啊..."
    "真的没什么社团能让我提起兴趣。"
    "除此以外，大部分社团都会安排很多事，这我肯定受不了。"
    "我想我只能试着从动画部开始了..."

    $ m_name = "???"

    m "...[player]？"
    window hide(None)
    show monika g2 at t11 zorder 2
    pause 0.75
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show monika 1 at t11 zorder 2
    mc "...Monika？"
    $ m_name = "Monika"
    m 1b "天哪，我完全没想到会在这里看见你！"
    m 5 "有一段时间没见了，对吧？"
    mc "啊..."
    mc "是的，确实有一段时间了。"
    "Monika 甜甜地笑着。"
    "我们的确互相认识 - 好吧，虽然我们基本没说过话，但在去年还是同班同学。"
    "Monika 可以说是班级里最受欢迎的女生 - 聪明，漂亮，又擅长运动。"
    "基本上，和我是两个世界的人。"
    "所以，看到她这么真诚地对我微笑让我有点..."
    mc "话说，你怎么会来这？"
    m 1a "哦，我只是来找一点我的社团会用得上的东西。"
    m 1d "你知道这里有没有彩纸吗？"
    m "或者马克笔？"
    mc "我觉得你可以看看储藏间里有没有。"
    mc "...你在辩论部，对吧？"
    m 5 "啊哈哈，那个嘛..."
    m "实际上，我退出辩论部了。"
    mc "真的？你退部了？"
    m "对..."
    m 2e "说实话，我无法忍受大社团里的勾心斗角。"
    m "除了争论预算和宣传以及准备活动，感觉都没有别的事情..."
    m "我更愿意选择自己喜欢的东西，并做出一些有意义的事。"
    mc "那你后来加入哪个社团了？"
    m 1b "实际上，我正在组建一个新的！"
    m "是一个文学部！{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m "是一个文学部！{fast}"
    window auto
    mc "文学...？"
    "听起来有点...枯燥的亚子？"
    mc "那么你们现在有多少部员了呢？"
    m 5 "emm..."
    m "啊哈哈..."
    m "有点不好意思讲，不过现在我们只有三个人。"
    m "为这个听上去很无聊的社团寻找新成员真的很难..."
    mc "嗯，我能理解..."
    m 3d "但是这个社团一点也不无聊，真的！"
    m "文学可以是任何东西。阅读，写作，诗歌..."
    m 3e "我的意思是，我们的一个社员甚至把她的漫画收藏拿到了部室..."
    mc "等等...真的吗？"
    m 2k "是的，有点好玩，对吧？"
    m 2e "她总是坚称漫画也是文学的一部分。"
    m "我的意思是，她说得应该也没错..."
    m "况且，成员有一个算一个，对吧？"
    "... Monika 刚刚说了...\"她\"？"
    "emm..."
    m 1a "嘿，[player]..."
    m "就随便问问...你还在找要加入的社团吗？？"
    mc "啊--"
    mc "我，大概...也许...差不多在找，不过..."
    m "这样的话..."
    m 5 "你可以帮我一个大忙吗？"
    m "我不会直接要求你加入，不过..."
    m "如果你能稍微来我的社团参观一下，我会非常开心的。"
    m "可以吗？"
    mc "emm..."
    "嗯，我没法拒绝..."
    "况且，我怎么会拒绝像 Monika 这样的人呢？"
    mc "行，那就去一下吧。"
    m 1k "啊，Awesome!"
    m 1b "你真的很温柔呢，[player]，你知道吗？"
    mc "这-这没什么的，真的..."
    m 1a "那我们走吧。"
    m "我还是下次再来拿材料吧 - 你更重要些。"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "就在今日，我把灵魂出卖给了 Monika 和她那无人可挡的微笑。"
    "我羞怯地跟随着 Monika 穿过学校、上了楼 - 我不常来学校这边, 这里通常是三年级学生和社团活动所使用的地方。"
    "元气满满的 Monika 一口气拉开了教室的门。"

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show screen notify("达成成就：GLITCHHHHHHHHHHHH")
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "我回来啦～！"
    m "而且我还带来了一位客人！"
    show yuri 2t at t33 zorder 2
    if not config.skipping:
        show screen invert(0.15, 0.3)
        # 这么好康你还跳过？？？？？？？
    y "诶？"
    y "一...一个客人？"
    show natsuki 4c at t32 zorder 2
    n "你真的假的？你带了个男生过来？"
    n "太毁气氛了吧。"
    show monika 3m at f31 zorder 3
    m "别这样，Natsuki..."
    m 3b "...但不管怎样，[player]，欢迎来到文学部!"
    show monika 3a at t31 zorder 2
    mc "..."
    "看着眼前这幅景象，我根本说不出话来。"
    "这个社团..."
    "{i}...全都是超级卡哇伊的女孩纸啊啊！！{/i}"

    show natsuki at f32 zorder 3
    n 5c "那么，我来猜一猜..."
    n "你是 Monika 的男朋友，对吧？"
    show natsuki at t32 zorder 2
    mc "啥--"
    mc "不！我没有！"
    show yuri at f33 zorder 3
    y 2l "Natsuki..."
    $ n_name = 'Natsuki'
    "我并不认识这个名叫 Natsuki、看起来脾气很嚣张的女生。"
    "看她那娇小的身材，我觉得她应该是一年级的学妹。"

    show yuri at t33 zorder 2
    show monika at f31 zorder 3
    m 2l "总-总之，这位是 Natsuki，和平常一样充满活力..."
    m 2b "这位是 Yuri，文学部的副部长！"
    $ y_name = 'Yuri'
    show monika 2a at t31 zorder 2
    show yuri at f33 zorder 3
    y 4 "很-很荣幸认识你..."
    "Yuri，看起来更加成熟，但却有点害羞，似乎不太跟得上类似夏树这样的人的节奏。"
    show yuri at t33 zorder 2
    mc "嗯...很高兴认识你们俩。"
    show monika at f31 zorder 3
    m 1a "我正巧在教室里碰到了 [player]，然后他决定来社团看看。"
    m "还不错吧？"
    show monika at t31 zorder 2
    show natsuki at f32 zorder 3
    n 4e "等等！Monika！"
    n "难道我没和你说过，在让其他人加入之前先告诉我的么？"
    n 4q "我正要...好吧，你知道的..."
    show natsuki at t32 zorder 2
    show monika at f31 zorder 3
    m 1e "抱歉，抱歉！"
    m "我没忘，只不过我碰巧遇见他了。"
    show monika at t31 zorder 2
    show yuri at f33 zorder 3
    y 1a "这样的话，我该去沏一些茶吧？"
    show yuri at t33 zorder 2
    show monika at f31 zorder 3
    m 1b "嗯，再好不过了！"
    m "你不过来坐吗，[player]?"
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "女孩们用几张课桌拼成了一张大桌子。"
    "Yuri 走到了房间的角落，打开了储藏间。"
    "与此同时，Monika 和 Natsuki 面对面坐在了桌旁。"
    "我还是觉得有些尴尬，于是就坐在了 Monika 的旁边。"
    show monika 1a at t11 zorder 2
    m "嗯，我知道你其实并没有打算要来这里..."
    m "但是我们会让你感到宾至如归的，好吗?"
    m 1j "作为文学部的部长，我的职责就是要让所有人都能感受到社团的有趣、愉悦！"
    mc "我很惊讶，这里居然只有这么些部员。"
    mc "新成立一个社团一定很难吧。"
    m 3b "确实这样。"
    m "没有多少人会愿意把全部精力投入到全新的事物中..."
    m "尤其是像文学这样，不能第一时间吸引到注意力的东西。"
    m "你必须加倍努力才能让别人相信，文学既有趣又有意义。"
    m "而这也让校园活动，比如学园祭，变得更加重要。"
    m 2k "我有自信我们能在我们毕业之前，将文学部发展起来！"
    m "对吧，Natsuki？"
    show monika at t22 zorder 2
    show natsuki 4q at t21 zorder 2
    n "emm..."
    n "...大概吧。"
    "Natsuki 勉勉强强同意了。"
    "这样几个完全不同的女生，却都对同样的事物感兴趣...."
    "Monika must have worked really hard just to find these two."
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot in the middle."
    show natsuki at thide zorder 1
    show monika at thide zorder 1
    hide natsuki
    hide monika
    show yuri 1a at t21 zorder 2
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I-I guess..."
    show monika 4a at f22 zorder 3
    m "Ehehe, don't let yourself get intimidated, Yuri's just trying to impress you."
    show monika at t22 zorder 2
    show yuri at hf21
    y 3n "Eh?! T-That's not..."
    "Insulted, Yuri looks away."
    y 4b "I meant that, you know..."
    show yuri at t21 zorder 2
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    show yuri at f21 zorder 3
    y 2u "I'm glad..."
    show yuri at t21 zorder 2
    "Yuri faintly smiles to herself in relief."
    show monika at thide zorder 1
    hide monika
    show yuri 1a at t32 zorder 2
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    mc "...Manga..."
    "I mutter quietly to myself, half-joking."
    show natsuki 1c at t41 zorder 2
    "Natsuki's head suddenly perks up."
    "It looks like she wants to say something, but she keeps quiet."
    show natsuki at thide zorder 1
    hide natsuki
    y 3u "N-Not much of a reader, I guess..."
    mc "...Well, that can change..."
    "What am I saying?"
    "I spoke without thinking after seeing Yuri's sad smile."
    mc "Anyway, what about you, Yuri?"
    y 1l "Well, let's see..."
    "Yuri traces the rim of her teacup with her finger."
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "Yuri goes on, clearly passionate about her reading."
    "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Ah, I read a horror book once..."
    "I desperately grasp something I can relate to at the minimal level."
    "At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1j at f33 zorder 3
    m "Ahaha. I'd expect that from you, Yuri."
    m 1a "It suits your personality."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 1a "Oh, is that so?"
    y "Really, if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show yuri at t32 zorder 2
    show natsuki 5q at f31 zorder 3
    n "Ugh, I hate horror..."
    show natsuki at t31 zorder 2
    show yuri at f32 zorder 3
    y 1f "Oh? Why's that?"
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    n 5q "Never mind."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    show monika at t33 zorder 2
    show natsuki 1o at f31 zorder 3
    n "W-What?"
    n "What gives you that idea?"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 3b "You left a piece of scrap paper behind last club meeting."
    m "It looked like you were working on a poem called--"
    show monika at t33 zorder 2
    show natsuki 1p at f31 zorder 3
    n "Don't say it out loud!!"
    n "And give that back!"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1j "Fine, fine~"
    show monika 1a at t33 zorder 2
    mc "Natsuki, you write your own poems?"
    show natsuki at f31 zorder 3
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    show natsuki at t31 zorder 2
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    show natsuki at f31 zorder 3
    n 5q "N-No!"
    "Natsuki averts her eyes."
    n "You wouldn't...like them..."
    show natsuki at t31 zorder 2
    mc "Ah...not a very confident writer yet?"
    show yuri at f32 zorder 3
    y 2f "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show yuri at t32 zorder 2
    show monika 2a at f33 zorder 3
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s32
    y 3o "..."
    mc "I guess it's the same for Yuri..."
    "We all sit in silence for a moment."
    show monika at f33 zorder 3
    m 5a "Hey, I just got an idea!"
    m "How about this?"
    show monika at t33 zorder 2
    show natsuki 2k at f31 zorder 3
    show yuri 3e at f32 zorder 3
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    show natsuki at t31 zorder 2
    show yuri at t32 zorder 2
    show monika at f33 zorder 3
    m 2b "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    show monika 2a at t33 zorder 2
    show natsuki at f31 zorder 3
    n 5q "U-Um..."
    show natsuki at t31 zorder 2
    show yuri 3v at f32 zorder 3
    y "..."
    show yuri at t32 zorder 2
    show monika 2m at f33 zorder 3
    m "Ah..."
    m "I mean, I thought it was a good idea..."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 2l "Well..."
    y "...I think you're right, Monika."
    y 2f "We should probably start finding activities for all of us to participate in together."
    y 2h "I did decide to take on the responsibility of Vice President, after all..."
    y "I need to do my best to nurture the club as well as its members."
    y 2a "Besides, now that we have a new member..."
    y "It seems like a good step for us to take."
    y "Do you agree as well, [player]?"
    show yuri at t32 zorder 2
    mc "Hold on...there's still one problem."
    show monika at f33 zorder 3
    m 1d "Eh? What's that?"
    "Now that we've reached the most important topic, I bluntly come forth with what's been on my mind the entire time."
    show monika at t33 zorder 2
    mc "I never said I would join this club!"
    mc "Monika may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "I lose my train of thought."
    "All three girls stare back at me with dejected eyes."
    show monika at s33
    m 1p "B-But..."
    show yuri at s32
    y 2v "I'm sorry, I thought..."
    show natsuki at s31
    n 5s "Hmph."
    mc "Eh...?"
    "The girls exchange glances before Monika turns back to me."
    show monika at f33 zorder 3
    m 1m "I...guess I need to tell you the truth, [player]."
    m "The thing is..."
    m 1p "...We don't have enough members yet to form an official club."
    m "We need four..."
    m "And I've been trying really, really hard to find new members."
    m "And if we don't find one more before the festival..."
    show monika at t33 zorder 2
    mc "..."
    "I...I'm defenseless against these girls."
    "How am I supposed to make a clear-headed decision when it's like this?"
    "I would feel terrible for letting everyone down in this situation..."
    "And besides, the club itself seems pretty relaxed..."
    "So, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show monika 1e at t33 zorder 2
    show yuri 3f at t32 zorder 2
    show natsuki 1k at t31 zorder 2
    "One by one, the girls' eyes light up."
    show monika at f33 zorder 3
    m "Oh my goodness, really?"
    m "Do you really mean that, [player]?"
    show monika at t33 zorder 2
    mc "Yeah..."
    mc "It could be fun, right?"
    show yuri at f32 zorder 3
    y 1m "You really did scare me for a moment..."
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5q "I mean, if you really just left after all this, I would be super pissed."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m "[player], I'm so happy..."
    m 1k "We can become an official club now!"
    m 1e "Thank you so much for this. You're really amazing."
    m "I'll do everything I can to give you a great time, okay?"
    show monika at t33 zorder 2
    mc "Ah...thanks, I guess."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show monika at t11 zorder 2
    hide yuri
    hide natsuki
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over at me once more."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    mc "Y-Yeah..."
    show monika at thide zorder 1
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills?"
    "I already feel the anxiety welling up inside me."
    "Meanwhile, the girls continue to chit-chat as Yuri cleans up the tea set."
    mc "I guess I'll be on my way, then..."
    show monika 5a at t11 zorder 2
    m "Okay!"
    m "I'll see you tomorrow, then."
    m "I can't wait!"

    scene bg residential_day
    with wipeleft_scene

    "With that, I depart the clubroom and make my way home."
    "The whole way, my mind wanders back and forth between the three girls:"
    show natsuki 4a at t31 zorder 2
    "Natsuki,"
    show yuri 1a at t32 zorder 2
    "Yuri,"
    show monika 1a at t33 zorder 2
    "and, of course, Monika."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        show screen notify("达成成就：HEPPY THXXXXOUGHTS")
        call expression "poem_special_1" 
    else:
        pass

    call poem

    jump ch21_main
    python:
        try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
        except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

    return