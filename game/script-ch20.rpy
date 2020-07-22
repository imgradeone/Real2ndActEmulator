label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    show screen notify("存档已删除。您现在已经进入真正的二周目。")
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    show screen notify("二周目...是停不下来的！！！")
    jump ch20_main2

label ch20_main2:
    "今天，一如既往，是个平常的上学日。"
    "早上可以说是最糟糕的，去学校的路上总会被周围的一大波现充包围着。"
    "与此同时，我却总是一个人。"
    "我经常告诉自己，差不多是时候该找一个女朋友之类的了..."
    "但我确实没什么动力去加入什么社团。"
    "可以把空余时间花在游戏和动画上，我其实已经相当满足了。"
    "学校总是会有动画部的，但是那里怎么可能会有女孩啊..."
    
    scene bg class_day
    with wipeleft_scene

    "在学校的日子和往常一样枯燥，不知不觉就结束了。"
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
        show screen notify("达成成就：卡 姿 兰 大 眼 睛")
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "我回来啦～！"
    m "而且我还带来了一位客人！"
    show yuri 2t at t33 zorder 2
    # if not config.skipping:
    #     show screen invert(0.15, 0.3)
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
    "Yuri，看起来更加成熟，但却有点害羞，似乎不太跟得上类似 Natsuki 这样的人的节奏。"
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
    "Monika 为了找这两个成员，一定花了不少功夫。"
    "Yuri 带着一套茶具回到了桌子。"
    "她小心地在每个人面前放了一个茶杯，之后在桌子中间放了一个茶壶。"
    show natsuki at thide zorder 1
    show monika at thide zorder 1
    hide natsuki
    hide monika
    show yuri 1a at t21 zorder 2
    mc "你在这个教室里放了一整套茶具吗？"
    y "别担心，老师已经同意了。"
    y "而且，读书的时候配上一杯暖茶，不是很好嘛？"
    mc "啊...大-大概吧..."
    show monika 4a at f22 zorder 3
    m "诶嘿嘿，别被吓到了，Yuri 只是想给你留个好印象。"
    show monika at t22 zorder 2
    show yuri at hf21
    y 3n "诶？！不-不是的..."
    "Yuri 红着脸，看向一边。"
    y 4b "我的意思是，那个..."
    show yuri at t21 zorder 2
    mc "我相信你。"
    mc "嗯，虽然阅读和品茶并不是我的消遣活动，但至少我也喜欢喝茶。"
    show yuri at f21 zorder 3
    y 2u "那就好..."
    show yuri at t21 zorder 2
    "Yuri 微微一笑。"
    show monika at thide zorder 1
    hide monika
    show yuri 1a at t32 zorder 2
    y "所以，[player]，你平时都有读些什么呢？"
    mc "这个...啊..."
    "考虑到我过去几年匮乏的阅读量，我真的不知道该如何回答。"
    mc "...漫画..."
    "我半开玩笑地小声嘀咕着。"
    show natsuki 1c at t41 zorder 2
    "Natsuki 的头突然扬了起来。"
    "她似乎想说些什么，不过最后还是选择了沉默。"
    show natsuki at thide zorder 1
    hide natsuki
    y 3u "不-不算是一个阅读爱好者呢，我猜..."
    mc "...嗯，这也是可以改变的.."
    "我在说什么？"
    "我一看见 Yuri 难过的微笑，就想都没想地说了出来。"
    mc "话说回来，Yuri，你喜欢读些什么呢？"
    y 1l "嗯，让我想想..."
    "Yuri 的指尖描划着茶杯边缘。"
    y 1a "我最喜欢的是那种构建了深邃复杂世界的幻想小说。"
    y "它们背后的创造力和匠心水平，真的是让我大开眼界。"
    y 1f "并且在那种陌生的世界观下，能叙述好一个故事的能力也很令人钦佩。"
    "Yuri 继续说着，很明显对她的阅读抱有热烈的情感。"
    "从我走进社团以来，她似乎一直很害羞和沉默，但从她亮起来的眼神可以看出，比起现实的人际关系，她更喜欢在书中寻找自己的恬静。"
    y 2m "但我也喜欢很多其他的类型。"
    y "有深入的心理元素的故事也能让我沉浸其中。"
    y 2a "作者利用你在想象力上的缺乏，将你完全丢入到循环中，不觉得这样很神奇吗？"
    y "不过，最近我倒是读了不少恐怖小说呢..."
    mc "啊，我以前也读过一本..."
    "我好不容易抓住了一点我至少曾涉及过的东西。"
    "不然再这样下去，Yuri 就要像是在和一块石头说话了。"
    show monika 1j at f33 zorder 3
    m "啊哈哈，确实很像你呢，Yuri。"
    m 1a "这很符合你的性格。"
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 1a "哦，真的吗？"
    y "真的，如果这个故事可以让我引起思考，或者将我带到了另一个世界，那么我真的会手不释卷。"
    y "超现实主义的恐怖小说会改变你看待世界的方式，哪怕只有一小会。"
    show yuri at t32 zorder 2
    show natsuki 5q at f31 zorder 3
    n "唔，我讨厌恐怖..."
    show natsuki at t31 zorder 2
    show yuri at f32 zorder 3
    y 1f "哦？为什么？"
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5c "好吧，我只是..."
    "Natsuki 短暂地瞥了我一眼。"
    n 5q "没什么。"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1a "这就对了，你平常更喜欢写可爱的东西，Natsuki，不是吗？"
    show monika at t33 zorder 2
    show natsuki 1o at f31 zorder 3
    n "什-什么？"
    n "你从哪里冒出来的这种想法？"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 3b "上次社团会议结束后，你掉了一张便签纸在教室里。"
    m "好像你正在写一首诗，叫做--"
    show monika at t33 zorder 2
    show natsuki 1p at f31 zorder 3
    n "你吼辣么大声干什么！！"
    n "把纸条还给我！"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1j "好吧，好吧～"
    show monika 1a at t33 zorder 2
    mc "Natsuki，你会自己写诗？"
    show natsuki at f31 zorder 3
    n 1c "诶？对，偶尔。"
    n "你问这个干嘛？"
    show natsuki at t31 zorder 2
    mc "我觉得这很了不起啊。"
    mc "为什么不偶尔给大家看一下呢？"
    show natsuki at f31 zorder 3
    n 5q "不-不行！"
    "Natsuki 的眼神游移着。"
    n "你们不会...喜欢的..."
    show natsuki at t31 zorder 2
    mc "啊...对自己的水平还不够自信吗？"
    show yuri at f32 zorder 3
    y 2f "我理解 Natsuki 的感受。"
    y "分享那种水平的文字需要的可不仅仅是自信。"
    y 2k "最真挚的文字是写给自己的。"
    y "所以分享的前提是，作者必须要愿意向读者敞开心扉，暴露出自己的弱点，甚至抵达心灵的最深处。"
    show yuri at t32 zorder 2
    show monika 2a at f33 zorder 3
    m "所以 Yuri，你也有写作的经验吗？"
    m "如果你愿意分享一下你的作品，没准在榜样作用下，Natsuki 也会愿意分享的。"
    show yuri at s32
    y 3o "..."
    mc "似乎 Yuri 也是这样想的..."
    "气氛短时间陷入了沉默。"
    show monika at f33 zorder 3
    m 5a "嘿，我突然有个主意！"
    m "这样如何？"
    show monika at t33 zorder 2
    show natsuki 2k at f31 zorder 3
    show yuri 3e at f32 zorder 3
    ny "...？"
    "Natsuki 和 Yuri 迷惑地望着 Monika。"
    show natsuki at t31 zorder 2
    show yuri at t32 zorder 2
    show monika at f33 zorder 3
    m 2b "我们每个人回家写一首自己的诗吧！"
    m "下次活动的时候，我们就可以彼此分享了。"
    m "这样的话，大家就扯平了！"
    show monika 2a at t33 zorder 2
    show natsuki at f31 zorder 3
    n 5q "唔-唔..."
    show natsuki at t31 zorder 2
    show yuri 3v at f32 zorder 3
    y "..."
    show yuri at t32 zorder 2
    show monika 2m at f33 zorder 3
    m "啊..."
    m "我是说，我觉得这是个好主意..."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 2l "那个..."
    y "...Monika，你说得对。"
    y 2f "我们或许应该开始找一些可以让全员参与的活动了。"
    y 2h "毕竟作为副部长，我也要负起责任来..."
    y "我也要尽力培养社团和社团的成员。"
    y 2a "况且，既然我们有了一个新成员..."
    y "迈出这一步似乎也不错。"
    y "你也同意吗，[player]?"
    show yuri at t32 zorder 2
    mc "等一下...还有一个问题。"
    show monika at f33 zorder 3
    m 1d "诶？还有什么问题？"
    "既然已经提到了最重要的话题，我终于能够坦率地说出我一直以来的想法。"
    show monika at t33 zorder 2
    mc "我从来都没说过我要入部！"
    mc "虽然 Monika 说服了我来看看，但我从没下过任何决定。"
    mc "我还有别的一些社团要看看，并且...唔..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "我的思路断掉了。"
    "三个女生都用失落的眼神看着我。"
    show monika at s33
    m 1p "但-但是..."
    show yuri at s32
    y 2v "抱歉，我以为..."
    show natsuki at s31
    n 5s "哼唧。"
    mc "诶...？"
    "女孩们相互交换了一下眼神，之后 Monika 转向了我。"
    show monika at f33 zorder 3
    m 1m "我...我猜我需要告诉你真相，[player]."
    m "事实上..."
    m 1p "...我们甚至还没有达到组建一个正式社团的最低人数要求。"
    m "我们至少需要四个人..."
    m "而且我已经非常、非常尽力地去寻找新成员了。"
    m "而如果我们没能在学园祭之前再找到一个的话..."
    show monika at t33 zorder 2
    mc "..."
    "我...我对可爱的女孩子超没辙的。"
    "这种情况下我怎么做一个头脑清醒的决定啊？"
    "在这种情况下，我还让她们失望的话，我会感到很难受的..."
    "更何况，这个社团本身看上去还挺轻松的..."
    "所以，如果只要写写诗，我就能每天和这些可爱的女生待在一起..."
    mc "...好吧。"
    mc "好吧，那我决定了。"
    mc "我要加入文学部。"
    show monika 1e at t33 zorder 2
    show yuri 3f at t32 zorder 2
    show natsuki 1k at t31 zorder 2
    "女生们的眼神一个接一个地亮了起来。"
    show monika at f33 zorder 3
    m "我的天啊，真的吗？"
    m "你真的确定吗，[player]?"
    show monika at t33 zorder 2
    mc "是的..."
    mc "应该会挺有意思的，对吧？"
    show yuri at f32 zorder 3
    y 1m "你有一瞬间真的吓到我了..."
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5q "如果你真的就这么走了，我真的会超生气的。"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m "[player], 我非常高兴..."
    m 1k "我们终于可以成为正式社团了！"
    m 1e "真的非常感谢你。你很了不起。"
    m "我会尽一切努力让你在这里的时间变得有意义的，可以吗？"
    show monika at t33 zorder 2
    mc "啊...谢谢你。"
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show monika at t11 zorder 2
    hide yuri
    hide natsuki
    m 3b "好了，各位！"
    m "我想, 今天的社团活动到这里就正式结束了。"
    m "各位要记得每个人今晚的任务:"
    m "每个人写一首明天带过来的诗，这样我们就可以分享了！"
    "Monika 再一次看向了我。"
    m 1a "[player]，期待你的表现哦。"
    show monika 5 at hop
    m "诶嘿嘿～"
    mc "好-好的..."
    show monika at thide zorder 1
    hide monika
    "我真的能用我那平庸的写作水平打动校园明星 Monika 么?"
    "焦虑已经在我的心中开始翻涌了。"
    "与此同时，女孩们也在继续着她们的闲聊，Yuri 还在一边清理她的茶具。"
    mc "那我就回家了..."
    show monika 5a at t11 zorder 2
    m "好的！"
    m "那么我们明天见。"
    m "我都等不及了！"

    scene bg residential_day
    with wipeleft_scene

    "就这样，我从部室离开了，踏上了回家的路。"
    "一路上，我的思绪都在三位女孩间游转："
    show natsuki 4a at t31 zorder 2
    "Natsuki，"
    show yuri 1a at t32 zorder 2
    "Yuri，"
    show monika 1a at t33 zorder 2
    "当然，还有 Monika。"
    "每天在放学后去文学部，我会一直非常开心的吧？"
    "说不定我还有机会能和三个女生中的一个...变得更亲密..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "好的！"
    "我只要充分利用条件就行了，好运总有一天会来的。"
    "看来我要从今晚的写诗开始了..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("你解锁了一首特殊诗歌。\n是否查看？\n有概率获得成就哦！", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0])
    else:
        pass

    call poem
    python:
        try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
        except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

    jump ch21_main

    return