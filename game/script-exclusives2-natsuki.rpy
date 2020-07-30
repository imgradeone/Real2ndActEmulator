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
    n "呃...！"
    "我听见 Natsuki 在储藏间那里发出了一声窝火的声音。"
    "看起来她正在烦恼着什么。"
    "我走过去，看看能不能帮上她。"
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
    n "世界上最令人愤怒的事情，大概就是看着一整套漫画缺了一本。"
    mc "我懂..."
    "我凑近看了眼她赞赏着的这套漫画。"
    mc "Parfait Girls（帕菲女孩）...？"
    "我从没听说过这个系列。"
    "要么它不是我喜欢的类型，要么就是个屑作。"
    n 5g "如果你还要评头论足的话，this way，please。"
    "她指着教室的门。"
    mc "喂-喂，我可没有要评头论足...！"
    mc "我还什么都没说呢。"
    n 5c "可你的语调已经表现出来了。"
    $ style.say_dialogue = style.normal
    n "但我得先告诉你一件事，[player]。"
    n 4l "这句话也适用于整个文学部：{nw}"
    $ _history_list[-1].what = "这句话也适用于整个文学部：不要光凭封面就评判一本书！" # 我们必须假装 bug 没有发生过 
    $ style.say_dialogue = style.edited
    n "不要光凭封fffffffffffmmmmmmmmm 就jjjjjjjjj 判ppp{space=20}书{space=40}s{space=120}s{space=160}s{space=200}u"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "实际上--"
    "Natsuki 从盒子里抽出 Parfait Girls 的第一册。"
    n "告诉你为什么吧！"
    "她把漫画塞进我的手里。"
    mc "啊..."
    "我看着封面。"
    "上面画着四个盛装美少女摆出漫画女主角的姿势。"
    "这个...“萌”得出血了。"
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
    mc "椅子它不香吗...？"
    "我坐了下来。"
    n 2k "椅子不行。"
    n "那样就没法让我们两个一起读了。"
    mc "诶？为什么？"
    mc "啊...我知道了，两个人像这样更容易凑近一点..."
    n 2o "--！"
    n 5r "别-别说得那么直接啦！"
    n "说得很奇怪诶！"
    "Natsuki 交叉着双臂，挪远了一些。"
    mc "抱歉..."
    show natsuki 5g
    "我也没想到会和她坐得这么近..."
    "虽然这样也不坏啦。"
    "我打开了漫画。"
    "不一会儿，Natsuki 又悄悄地挪了回来，好像在希望我没有发现她的动作。"
    "我感觉到从身边透来的视线，其实 Natsuki 比我还想看这本漫画。"
    n 1k "哇，我上次读这个开头是啥时候来着...？"
    mc "嗯？"
    mc "你不会时不时地回头翻一翻前面几册么？"
    n 2k "一般不会。"
    n "可能等到整个系列读完的时候，我会回去看一下。"
    n 2c "喂，你有在认真看漫画么？"
    mc "呃..."
    "我正在看，但是没什么特别的桥段，所以我可以一边看一边聊天。"
    "这部漫画似乎就是关于一群高中女生聚在一起。"
    "烂尾的日常剧情。"
    "我感觉自己有些厌倦日常系的作品了，因为这种类型通常缺乏剧情的展开，很难让人产生兴趣。"
    $ persistent.clear[0] = True
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "你这样坐着不无聊吗？"
    n "并没有！"
    mc "即便你只是在这看着我读？"
    n "好吧...！"
    n "我...觉得还行。"
    mc "既然你这样说的话..."
    mc "...可能把自己喜欢的作品推荐给别人，也蛮有趣的。"
    mc "我自己也会因为朋友在读我喜欢的漫画而高兴。"
    mc "你懂吧？"
    n "...？"
    mc "嗯？"
    mc "你不明白？"
    show n_cg1_exp2 at cgfade
    n "emm..."
    n "没有..."
    n "嗯，我不是很懂。"
    mc "...什么？"
    mc "你不和自己的朋友一起看漫画吗？"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "能别说得那么直接吗？"
    n "口意..."
    mc "啊...对不起..."
    n "哼唧。"
    n "说得好像我有可以一起看漫画的朋友一样..."
    n "他们都觉得漫画是给小屁孩看的。"
    n "每当我提起漫画，他们就像是在说..."
    n "'诶？你还是小孩子吗？'"
    n "真是想把她们锤爆的感觉..."
    mc "呃，我知道有这种人的..."
    mc "说真的，能找到一个不对你评头论足的朋友已经够难了，更何况对方还要同样喜欢漫画..."
    mc "我已经差不多是个渣渣了，所以我觉得自己会被慢慢吸引到同类里。"
    mc "但对你这样的人来说可能会难一点..."
    hide n_cg1_exp3
    n "口亨。"
    n "好吧，你说得还挺对的。"
    "{i}...等下，哪个部分啊？？{/i}"
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
    mc "嗯，但最后，付出也有回报了，不是吗？"
    mc "我是说，至少还有我，能够读着这本漫画。"
    n "好吧，可是这又没解决我的问题。"
    mc "大概吧..."
    mc "但至少你也乐在其中，不是吗？"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...SO？"
    mc "啊哈哈。"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "嘶~你够了！"
    n "你到底还读不读了？"
    mc "好吧，好吧..."
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
    "突然，Natsuki 倒向了我。"
    play sound fall
    $ style.say_dialogue = style.normal
    mc "诶-诶--"
    show n_cg1_exp5
    hide n_cg1_exp5
    if persistent.alt_safe_mode:
        show n_cg1b_alt
    else:
        show n_cg1b
    hide n_cg1_base
    # 噔 噔 咚

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    $ achievement.grant("低 级 马 赛 克")
    show screen notify("达成成就：低 级 马 赛 克")
    if not persistent.disable_awful_music:
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
    "她把这个东西丢给了 Natsuki。"
    "Natsuki 的眼睛又一下子有神起来。"
    "她猛地一把抓起地上的能量棒，扯掉了外包装。"
    show natsuki at f22 zorder 3
    n 1s "我跟你说过不要让我吃-唔..."
    show natsuki at t22 zorder 2
    "她连话都没说完，就把那东西塞到了嘴里。"
    show natsuki at thide zorder 1
    hide natsuki
    show monika 3b at t11 zorder 2
    m "别担心，[player]。"
    m "她没事的。"
    m "只是个突发事件罢了。"
    m 1a "所以我在包里都会给她准备一些零食。"
    m 5a "话说回来...！"
    m "是时候分享诗了！"

    return
