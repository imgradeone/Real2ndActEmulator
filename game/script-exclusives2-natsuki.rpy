init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight

            for i in range(self.numRects):
                self.add(self.displayable)
           
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
            
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    n "呃...!"
    "I hear Natsuki utter an exasperated sigh from within the closet."
    "看起来她正在烦恼着什么。"
    "I approach her, in case she needs a hand."
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r at t11 zorder 2
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    mc "你在这里找什么吗？"
    $ style.say_dialogue = style.edited
    n 4x "monika我丢雷楼某mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm" # 爆粗口的 Natsuki 是屑（
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Monika 讨厌鬼..." # 放心，历史记录被我们改了
    n "从来都不把我的东西放回去！"
    n "如果有人老是把你的东西乱放，那整理起来又有什么意义啊？wdnmd！"
    "Natsuki 把书架上的漫画重新插进套装盒中。"
    mc "漫画..."
    n 2c "我记得你也看漫画，对吧？"
    mc "啊--"
    mc "...偶尔吧..."
    "漫画这种东西，在不知道对方的态度前，你不能直接承认自己非常喜欢它。"
    mc "...你怎么知道？"
    n 2k "我之前听你提起过。"
    n "更何况，你脸上就像是这么写着的。"
    "这是想表达什么意思...？"
    mc "这-这样啊..."
    "在其中一个书架的一边，有一本漫画被放在了一堆各种各样的书之中。"
    "我有点好奇，把它从把书堆里抽了出来。"
    n 1b "原来它在{i}这里{/i}！"
    "Natsuki 从我手里抢过了那本漫画。"
    "她转过身，把那本漫画按照册号重新插回漫画盒中。"
    n 4d "啊哈，舒服多了！"
    n "Seeing a box set with one book missing is probably the most irritating sight in the world."
    mc "I know that feel..."
    "I get a closer look at the box set she's admiring."
    mc "Parfait Girls...？"
    "我从没听说过这个系列。"
    "要么它不是我喜欢的类型，要么就是个屑作。"
    n 5g "如果你还要品头论足的话，你可以透过门上的玻璃朝外面说。"
    "她指着教室的门。"
    mc "喂-喂，我可没有要评头论足...！"
    mc "我还什么都没说呢。"
    n 5c "你的语调已经表现出来了。"
    $ style.say_dialogue = style.normal
    n "但我要先告诉你一件事，[player]。"
    n 4l "这句话也适用于整个文学部：{nw}"
    $ _history_list[-1].what = "这句话也适用于整个文学部：不要光凭封面评判一本书！" # 我们必须假装 bug 没有发生过 
    $ style.say_dialogue = style.edited
    n "不要光凭封fffffffffffmmmmmmmmm 就jjjjjjjjj 判ppp{space=20}书{space=40}s{space=120}s{space=160}s{space=200}s"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "实际上--"
    "Natsuki 从盒子里抽出 Parfait Girls（帕菲女孩）的第一册。"
    n "我来告诉你为什么！"
    "她把漫画塞进我的手里。"
    mc "Ah..."
    "我看着封面。"
    "上面画着四个盛装美少女摆出漫画女主角的姿势。"
    "这个...\"萌\"得出血了。"
    n 4b "别傻站着啊！"
    mc "呜啊--"
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki 抓着我的手臂把我拖出了储藏间。"
    "然后她靠墙坐下了，就坐在窗沿底下。"
    "她拍了拍身边的地面，示意我坐在那里。"
    show bg club_day
    show natsuki 2a at t11 zorder 2
    with wipeleft
    mc "Wouldn't chairs be more comfortable...?"
    "I take my seat."
    n 2k "Chairs wouldn't work."
    n "We can't read at the same time like that."
    mc "Eh? Why's that?"
    mc "Ah...I guess it's easier to be close together like this..."
    n 2o "--!"
    n 5r "D-Don't just say that!"
    n "You'll make me feel weird about it!"
    "Natsuki crosses her arms and scootches an inch away from me."
    mc "Sorry..."
    show natsuki 5g
    "I didn't exactly expect to be sitting this close to her, either..."
    "Not that I can say it's a particularly bad thing."
    "I open the book."
    "It's only a few seconds before Natsuki once again inches closer, reclaiming the additional space while she hopes I won't notice."
    "I can feel her peering over my shoulder, much more eager to begin reading than I am."
    n 1k "Wow, how long has it been since I read the beginning...?"
    mc "Hm?"
    mc "You don't go back and flip through the older volumes every now and then?"
    n 2k "Not really."
    n "Maybe sometimes after I've already finished the series."
    n 2c "Hey, are you paying attention?"
    mc "Uh..."
    "I am, but nothing's really happened yet, so I can talk at the same time."
    "It looks like it's about a bunch of friends in high school."
    "Typical slice-of-life affair."
    "I kind of grew out of these, since it's rare for the writing to be entertaining enough to make up for the lack of plot."
    $ persistent.clear[0] = True
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...Are you sure this isn't boring for you?"
    n "It's not!"
    mc "Even though you're just watching me read?"
    n "Well...!"
    n "I'm...fine with that."
    mc "If you say so..."
    mc "...I guess it's fun sharing something you like with someone else."
    mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    mc "You know what I mean?"
    n "...?"
    mc "Hm?"
    mc "You don't?"
    show n_cg1_exp2 at cgfade
    n "Um..."
    n "That's not..."
    n "Well, I wouldn't really know."
    mc "...What do you mean?"
    mc "你不和自己的朋友一起看漫画吗？"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Could you not rub it in?"
    n "Jeez..."
    mc "Ah... Sorry..."
    n "Hmph."
    n "说得好像我有可以一起看漫画的朋友一样..."
    n "他们都觉得漫画是给小屁孩看的。"
    n "每当我提起漫画，他们就像是在说..."
    n "'诶？你还没长大吗？'"
    n "真是让我想要揍爆她们的脸..."
    mc "Urgh, I know those kinds of people..."
    mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are also into it..."
    mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    mc "But it's probably harder for someone like you..."
    hide n_cg1_exp3
    n "Hm."
    n "Yeah, that's pretty accurate."
    "{i}...等下，哪个部分？？{/i}"
    $ style.say_dialogue = style.normal
    n "我是说，我甚至都没法把漫画放在自己房间里..."

    $ style.say_dialogue = style.edited
    n "我爸看到这东西，绝逼把我连翔都 TM 打出来。"
    # n "My dad would beat the shit out of me if he found this."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "不晓得我爸看到后会是什么感受。"
    n "至少放在部室里挺安全的。"
    show n_cg1_exp3 at cgfade
    n "除了 Monika 这个 baka..."
    n "可恶！我难道就赢不了吗？"
    mc "Well, it paid off in the end, didn't it?"
    mc "I mean, here I am, reading it."
    n "Well, it's not like that solves any of my problems."
    mc "Maybe..."
    mc "But at least you're enjoying yourself, right?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...So？"
    mc "Ahaha."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "嘶~你够了！"
    n "你到底还读不读了？"
    mc "Yeah, yeah..."
    "我又翻了一页。"
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "时间过去了。"
    hide n_cg1_exp3
    show n_cg1_exp4 at cgfade behind black
    "Natsuki 出奇地安静。"
    "我悄悄瞥了她一眼。"
    hide black with dissolve_cg
    "她似乎快要睡着了。"
    mc "嘿，Natsuki..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "嗯-哦...？"
    "突然之间，夏树倒向了我。"
    play sound fall
    $ style.say_dialogue = style.normal
    mc "诶-诶--"
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base
    # 噔 噔 咚

    show screen notify("达成成就：低 级 马 赛 克")
    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r at t11 zorder 2
    m "哦，天啊..."
    m 1d "Natsuki，R U OK？"
    show monika at t21 zorder 2
    show natsuki 12b at f22 zorder 3
    n "..."
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m 1a "来，把这个吃了..."
    show monika at t21 zorder 2
    "Monika 从她的包里拿出了类似能量棒一样的东西。"
    show screen notify("饿了就吃士力架（（（")
    "She throws it in Natsuki's direction."
    "Natsuki's eyes suddenly light up again."
    "She snatches the bar from the floor and immediately tears off the wrapper."
    show natsuki at f22 zorder 3
    n 1s "I told you not to give mmph..."
    show natsuki at t22 zorder 2
    "She doesn't even finish her sentence before stuffing it into her mouth."
    show natsuki at thide zorder 1
    hide natsuki
    show monika 3b at t11 zorder 2
    m "Don't worry, [player]."
    m "She's fine."
    m "It just happens every now and then."
    m 1a "That's why I always keep a snack in my bag for her."
    m 5a "Anyway...!"
    m "Why don't we all share poems now?"

    return
