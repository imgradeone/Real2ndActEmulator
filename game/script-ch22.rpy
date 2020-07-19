image yuri half = "images/yuri/1l.png"
image yuri_half2:
    "images/yuri/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    $ chapter = 2
    python:
        try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
    show screen notify("当前 ch22")
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "又是平常的一天，眨眼间已经到了社团活动的时间了。"
    "几天过去，我对文学部已经相当习惯了。"
    "我走进教室，迎来的又是那熟悉的一幕。"
    # 1/3 几率，Yuri 崩坏
    if renpy.random.randint(0,2) == 0:
        show screen notify("达成成就：苏 联 解 体")
        show yuri half at i11 zorder 2
        show yuri_half2 at i11 zorder 1
    else:
        show yuri 1s at t11 zorder 2
    y "[player]，欢迎回来..."
    hide yuri_half2
    mc "啊，你好，Yuri..."
    "我不太确定是因为我，还是因为 Yuri 的脸色..."
    "昨天的争吵的影响似乎依旧让氛围有些沉重。"
    y 2v "emmmmmm..."
    "Yuri 侧着头，视线在教室里徘徊。"
    "Natsuki 正在一边看漫画。"
    "令人惊讶的是，Monika 还没有到。"
    "突然，Yuri 抓着我的胳膊把我拉到了教室的角落。"
    show bg closet
    show yuri 2t at t11 zorder 2
    with wipeleft
    y "关于昨天的事..."
    y "我..."
    y 2v "我真的需要道歉。"
    y "以前从来没有发生过这样的事..."
    y 2t "而且...可能发生了什么了..."
    y "我昨天情绪上不是很好。"
    y 2w "请千万不要认为我们一直都是这样！"
    y "不光是我，Natsuki 也一样..."
    show yuri 2t
    mc "Yuri..."
    mc "你能反省与道歉，我就已经很开心了。"
    mc "还是别太计较这件事了。"
    mc "我才来这里几天，都能感觉到昨天的异常..."
    mc "也许我们昨天只是因为第一次分享诗，所以有点过分敏感了。"
    mc "不过无论如何..."
    mc "这件事并没有让我看轻你。"
    mc "我早就认为你不是个坏人了。"
    mc "更何况现在你在道歉，我就更明白，你不是故意那样做了。"
    y 3t "啊-啊..."
    y "[player]..."
    y 3u "别这么直白嘛..."
    y "会让我有点点开心的。"
    y 1s "你能这样理解我，真的非常感激..."
    y "你加入社团也是如此。"
    y "有你在身边，一切似乎都明亮了起来，而且--"
    y 1t "啊--"
    y 4c "抱歉，我在说些什么...？"
    y "我只是--"
    show natsuki 2c at f33 zorder 3
    n "嘿，你们看见 Monika 了吗？"
    show natsuki at t33 zorder 2
    show yuri 3n at h32
    y "啊--！"
    mc "没，没看到..."
    mc "我也在想她去哪了呢。"
    show natsuki at f33 zorder 3
    n 5g "wdnmd..."
    n 5c "Yuri,我猜你应该也没见到她吧？"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 4a "..."
    "Yuri 很显然被 Natsuki 那样冷静地跟她说话吓了一跳。"
    y "没-没看到..."
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 1u "天哪，这一点也不像她的风格。"
    n "我知道有点傻，但是我就是忍不住去担心她一下..."
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 2t "..."
    show yuri at t32 zorder 2
    show natsuki 1h at f33 zorder 3
    n "你这样看着我干嘛？"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y "emmmmm..."
    y "Natsuki，昨天的事..."
    y 3w "我-我只是想道歉！"
    y "我发誓我说的话都只是一时冲动！"
    y 3t "从现在起，我会更加尽力控制住自己的情绪的..."
    y "所以--"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 2c "Yuri，你在说什么？"
    n "你昨天做了什么？"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 3f "...诶？"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    $ style.say_dialogue = style.normal
    n 2a "噫..."
    $ style.say_dialogue = style.edited
    n "不管你在在意什么事情，我觉得肯定没什么大不了啦。"
    n "我根本不记得发生过什么。"
    n "所以你就是那种总是在意鸡毛蒜皮的事的那种人，对吧？"
    $ style.say_dialogue = style.normal
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 2o "..."
    y "但-但是..."
    if renpy.random.randint(0, 3) == 0:
        show screen notify("达成成就：MOPEMOPE")
        $ style.say_dialogue = style.edited
        if not persistent.alt_safe_mode:
            show yuri at t32 zorder 2
            show natsuki mouth as nm at i33 zorder 3
        show n_moving_mouth zorder 3:
            xoffset 400
        n 2a "啊wee改哈鞥嫦娥我刚不疤痕处哈维楚王嗡阿格王朔鸡e句NBA我是猪tix来试谱啊11宝宝呢囜您呢你娘比起重机究其本质你只是个浅水区的牛蛙"
        # n 2a "mibulls sailcloth blindsight lifeline anan rectipetality faultlessly offered scleromalacia neighed catholicate"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki at f33 zorder 3
    n 2j "如果这样能让你好受些的话，我也会接受你的道歉。"
    n "另外，我其实总是担心你在暗地里讨厌我或者别的什么，所以我能听到你这么坦诚，其实还挺开心的。"
    n 2z "诶嘿嘿。"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 3q "没-没有，怎么会...！"
    y "我不讨厌你的..."
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 2l "啊哈哈。"
    n "你是有点古怪，不过我也不讨厌你的。"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 3t "..."
    "Natsuki 转向了我。"
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 2a "你的可还在试用期哦。"
    show natsuki at t33 zorder 2
    mc "嘿...！"
    "突然，门被猛地拉开了。"
    show monika 1g at l41
    m "抱歉！非常抱歉！"
    mc "啊，你来了..."
    show monika at f41 zorder 3
    m "我真不是有意迟到的..."
    m "希望你们没有担心我之类的！"
    show monika at t41 zorder 2
    mc "Nope..."
    mc "好吧，其实 Natsuki 挺担心的。"
    show natsuki at f33 zorder 3
    n 1p "我-我可没有！"
    show natsuki at t33 zorder 2
    show monika at f41 zorder 3
    m 1k "啊哈哈。"
    show monika at t41 zorder 2
    show natsuki at f33 zorder 3
    n 1s "...话说回来，你为什么迟到了啊？"
    show natsuki at t33 zorder 2
    show monika at f41 zorder 3
    m 1e "啊..."
    m "嗯，前面是自习课。"
    m "说实话，我忘了时间..."
    m "啊哈哈..."
    show monika at t41 zorder 2
    show natsuki at f33 zorder 3
    n 2c "那也没道理啊。"
    n "你至少应该听到下课铃了吧。"
    show natsuki at t33 zorder 2
    show monika at f41 zorder 3
    m 1m "那一定是因为被我练钢琴的声音盖过去了..."
    show monika at t41 zorder 2
    show yuri at f32 zorder 3
    y 1e "钢琴...？"
    y "Monika，我之前还不知道你会弹钢琴啊。"
    show yuri at t32 zorder 2
    show monika at f41 zorder 3
    m 1l "啊，我还差得远呢。"
    m 1m "虽然有练了一段时间了，不过我的水平还不够好。"
    show monika at t41 zorder 2
    show yuri at f32 zorder 3
    y 1a "但是..."
    y "你肯定也已经付出相当多的努力。"
    y "所以，我依旧很佩服。"
    show yuri at t32 zorder 2
    show monika at f41 zorder 3
    m 5 "喔，谢谢你，Yuri～"
    show monika at t41 zorder 2
    show natsuki at f33 zorder 3
    n 2d "You should play something for us sometime!"
    show natsuki at t33 zorder 2
    show monika at f41 zorder 3
    m "Ahaha, that's..."
    "Monika looks at me."
    m 1a "Well, I am working on writing a song, but it's not quite done yet..."
    m "Maybe once I get a little bit better, I will."
    show monika at t41 zorder 2
    mc "That sounds cool."
    mc "I look forward to it."
    show monika at f41 zorder 3
    m 1b "Is that so?"
    m "In that case..."
    m "I won't let you down, [player]."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    show monika 5 at t11 zorder 2
    "Monika smiles sweetly."
    mc "Ah..."
    mc "I didn't mean any pressure or anything like that!"
    m 1a "Ahaha, don't worry."
    m "I was hoping that I could share it with you, anyway."
    m "I guess that's why I've been practicing so much recently."
    mc "I see..."
    "I'm not sure if Monika was referring to the whole club, or just me..."
    mc "In that case, best of luck."
    m 1j "Thanks~!"
    m 1a "So, I didn't miss anything, did I?"
    mc "Not...not really."
    show monika at thide zorder 1
    hide monika
    "I choose not to bring up anything that the three of us talked about."
    "Besides, Natsuki has already run off into the closet."
    show yuri 2q at t11 zorder 2
    y "[player]..."
    y "Um..."
    y "Since your compliments put me in a good mood..."
    y "I was wondering if you would like to spend some time together today."
    y 3o "I mean--in the club!"
    if poemwinner[0] == "natsuki":
        $ y_appeal = 1
        mc "Ah, I suppose so."
        mc "I don't think I could say no to you, after you gave that book to me."
        mc "Well, I guess I need to make sure Natsuki isn't waiting for me."
        mc "After we finished reading yesterday, she--"
        y 3r "S-She's fine!"
        y 3h "She's reading over there."
        y 3y6 "So it's okay, right?"
        mc "Ah--"
        mc "In that case, I don't see any problem..."
    else:
        $ y_appeal = 2
        mc "Yeah, definitely."
        mc "I planned on it anyway."
    show yuri at h11 zorder 2
    y 3y5 "Okay!"
    y "Can we start now?"
    y "Let's find a place to sit--"
    y 3n "A-Ah--"
    y "I'm being a little forceful, aren't I...?"
    y 4c "I'm sorry!"
    y "My heart...just won't stop pounding, for some reason..."
    mc "Don't worry about it."
    mc "If anything, it's nice to see you have so much energy."
    y 3q "Y-Yeah!"
    y "But..."
    y 3j "I need to try to calm down."
    y "I won't be able to focus on reading like this..."
    mc "Take your time."
    "Yuri takes a deep breath, then pulls a copy of the book out of her bag."
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "yuri"

    #Call exclusive scene
    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = "yuri_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene from _call_expression_11
    call poemresponse_start
    jump ch22_end

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("你解锁了一首特殊诗歌。\n是否查看？\n有概率获得成就哦！", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1]) from _call_expression_12
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        show screen notify("达成成就：死 者 视 角 打 游 戏")
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b at t32 zorder 2
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show image Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show image Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        show screen notify("达成成就：你鼠标里的 DNA（（（")
        $ mouse_modify_random = True
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}
    else:
        $ mouse_modify_random = False

    # 死 不 瞑 目 纱 师 弟（1/3）

    m "Okay, everyone!"
    m "We're all done reading each other's poems, right?"
    if mouse_modify_random:
        show screen notify("光标已重置。")
        $ mouse_modify_random = False

    $ config.mouse = None
    m "We have something we need to go over today, so if everyone could come sit at the front of the room..."
    show natsuki 3c at f31 zorder 3
    n "Is this about the festival?"
    show natsuki at t31 zorder 2
    show monika 1j at f32 zorder 3
    m "Well, sort of~"
    show monika 1a at t32 zorder 2
    show natsuki 1m at f31 zorder 3
    n "Ugh. Do we really have to do something for the festival?"
    n "It's not like we can put together anything good in just a few days."
    n "We'll just end up embarrassing ourselves instead of getting any new members."
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki at t31 zorder 2
    show yuri 2g at f33 zorder 3
    y "That's a concern of mine as well."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "I don't really do well with last-minute preparations..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1b "Don't worry so much!"
    m "We're going to keep it simple, okay?"
    m 2a "Look..."
    m 2m "I know everyone's been a little more...lively...ever since [player] joined and we've started with some club activities."
    m 2d "But this isn't the time for us to become complacent."
    m "We still only have four members..."
    m 2a "And the festival is our only real chance to find more, you know?"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5g "What's so great about getting new members, anyway?"
    n "We already have enough to be considered an official club."
    n "More members will just mean everything gets noisier and more difficult to manage."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1g "Natsuki..."
    m "I don't think you're looking at it the right way at all."
    m "Don't you want to share your passion with as many people as you can?"
    m 3e "To inspire them to find the same feelings that brought you here in the first place?"
    m "The Literature Club should be a place where people can express themselves like they can't do anywhere else."
    m "It should be a place so intimate that you never want to leave."
    m 2e "I know you feel that way, too."
    m 2b "I know we all do!"
    m "So that's why we should work hard and put something together for the festival...even if it's something small!"
    m "Right, [player]?"
    show monika 2a at t32 zorder 2
    mc "Ah..."
    show natsuki at f31 zorder 3
    n 42c "Oh, come on!"
    n "You can't take advantage of [player] to agree with you just because he doesn't know how to say no to anything."
    stop music fadeout 1
    n 1c "Look, Monika."
    n "Do you really think any of us here joined the club with other people in mind?"
    n "Yuri never even talked until [player] joined."
    n 2b "As for me, I just like it better here than I do at home."
    n "And [player] isn't even passionate about literature in the first place."
    n "And that's everyone."
    n 4w "Sorry, but you're really the only one who's so interested in finding new members."
    n "The rest of us are fine like this."
    n 4q "I know you're President and all, but you should really consider our opinions for once."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1g "..."
    "Monika is clearly taken aback by Natsuki's words."
    play music t9
    m 1m "That's...not true at all."
    m 2m "I'm sure Yuri and [player] want to get more members too..."
    m 2p "...Right?"
    show monika at t32 zorder 2
    show yuri at f33 zorder 3
    y 4b "..."
    show yuri at t33 zorder 2
    mc "..."
    "I don't know about Yuri, but I'm kind of indifferent."
    "If I showed as much enthusiasm as Monika wanted, then I would probably be lying."
    "Still, if it's up to me to rescue this situation..."
    mc "Um--"
    show monika at f32 zorder 3
    m 1i "No."
    m "Natsuki's right, isn't she?"
    m 1g "This club..."
    m "It's nothing more than a place for a few people to hang out."
    m 1r "Why did I think that everyone here saw it the same way as I did?"
    show monika at t32 zorder 2
    mc "But that doesn't mean that we're against getting new members or anything..."
    show monika at f32 zorder 3
    m 1i "[player], why did you even join this club?"
    m "What were you hoping to get out of it?"
    show monika at t32 zorder 2
    mc "Well--"
    "That's not really something I can be honest about, is it?"
    show monika at f32 zorder 3
    m 1p "In fact..."
    m "If I remember, you weren't even given a choice not to join."
    show monika at thide zorder 1
    hide monika
    "Monika sits down and stares at her desk."
    m "What's the point of all this, anyway?"
    m "What if starting this club was a mistake?"
    mc "..."
    show yuri at f33 zorder 3
    y 2g "Now you've done it, Natsuki..."
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 1p "What, me?"
    n 1s "I just spoke my mind..."
    n "Is it a crime to be honest?"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 2l "It's not about being honest."
    y "It's about word choice."
    y 2h "Besides, you have no right to speak for everyone else in the club like that..."
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 1e "You don't understand at all!"
    n 5s "I just..."
    n "I just want a place that feels nice to hang out with a few friends."
    n 5u "Is there a problem with the club being that for me?"
    n "There aren't...there aren't many other places like that for me..."
    n 5x "And now Monika wants to take it away from me!"
    show natsuki at t31 zorder 2
    mc "She's not taking anything away--"
    show natsuki at f31 zorder 3
    n 1g "No, [player]."
    n "It's not the same."
    n 1q "It won't be the same with the direction she wants to take it."
    n "If I wanted that, then I could have just joined any other stupid club."
    n 12d "But this one..."
    n "I mean..."
    n 12e "At least for a little bit of time..."
    n "Things were nice."
    "Natsuki starts packing up her things."
    n 12d "I'm going home."
    n "I feel like...I don't belong here right now."
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 3t "Natsuki..."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki ignores Yuri and walks right out of the classroom."
    show yuri at t11 zorder 2
    y 3v "..."
    y "This is bad..."
    y "I don't know what to do..."
    mc "Well..."
    mc "Do you have an opinion on the festival?"
    y 4b "I-I don't know..."
    $ style.say_dialogue = style.normal
    y "I'm kind of indifferent, I guess..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "谁在乎那个死玻璃心小鬼啊？"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "I mean, I like how nice and quiet the club is right now..."
    y "And I'm just...happy with you here..."
    y 2t "But still!"
    y "I'm the Vice President..."
    y "It's not right for me to ignore my responsibilities like that..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "她就算是自裁了，也不会有人会为她哭。"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    pause 0.5
    if not persistent.alt_safe_mode:
        play sound "sfx/stab.ogg"
        show blood_eye zorder 3:
            pos (710,380) zoom 2.5
        pause 0.75
        stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "I should do my best to consider everyone's perspective and make the decision that's right for the club."
    y 1t "But what about you, [player]?"
    y "What do you want to get out of this club?"
    "Yuri repeats the same question as Monika."
    "I decide giving an indirect answer is better than nothing."
    mc "...I think the most important thing is for everyone to get along..."
    mc "...And for the club to provide something that you can't get anywhere else."
    mc "I don't think it's about how many members, but rather the quality of each member."
    mc "That's what will end up making the Literature Club a special place."
    y 1u "I see..."
    y "I really agree with you."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "Each member contributes their own qualities in a special way."
    y "With each change in members, the identity of the club as a whole will change, too."
    y 1h "I don't think that's necessarily a bad thing."
    y "Stepping out of your comfort zone once in a while..."
    y 1a "So if you would like to help Monika with the festival, then I'm on your side as well."
    hide blood_eye2
    mc "Alright."
    mc "Well, maybe we can all talk to Natsuki tomorrow..."
    "Yuri nods."
    show monika 1g at f21 zorder 3
    show yuri at t22 zorder 2
    m "Hey, Yuri..."
    show monika at t21 zorder 2
    show yuri at f22 zorder 3
    y 1t "Eh?"
    show yuri at t22 zorder 2
    show monika at f21 zorder 3
    m 1p "Um, I know things were a little awkward yesterday..."
    m "But I feel like you deserve to know that I still think you're a wonderful vice president."
    m 1e "And also, a wonderful friend."
    show monika at t21 zorder 2
    show yuri at f22 zorder 3
    y 3s "M-Monika..."
    show yuri at t22 zorder 2
    show monika at f21 zorder 3
    m 2e "I want to do everything I can to make this the best club ever."
    m "Okay?"
    show monika at t21 zorder 2
    show yuri at f22 zorder 3
    y "...Me too."
    show yuri at t22 zorder 2
    show monika at f21 zorder 3
    m 1a "Yeah..."
    m "Let's all go home for today."
    m "We'll talk about the festival tomorrow."
    show monika at t21 zorder 2
    show yuri at f22 zorder 3
    y 1m "Okay."
    y "I look forward to it."
    y 1a "Shall we go, [player]?"
    show yuri at t22 zorder 2
    show monika at f21 zorder 3
    m 1d "Um--"
    m 1p "Please don't take this the wrong way, but..."
    m "I'm going to chat a little bit with [player] before we leave."
    m 1d "Just to see what he thinks of his time here and all that..."
    m "It's important to me, as President."
    show monika at t21 zorder 2
    show yuri at f22 zorder 3
    y 2v "..."
    "Yuri looks a little troubled, but she doesn't protest."
    y 2t "Okay."
    y 2s "I trust your judgment, Monika."
    y "In that case, I'll see the two of you tomorrow."
    show yuri at t22 zorder 2
    show monika at f21 zorder 3
    m 1j "See you tomorrow~"
    show yuri at thide zorder 1
    hide yuri
    "Monika waves as Yuri exits the classroom."
    
    show monika 2a at t11 zorder 2
    m "Phew..."
    m 2e "Things have been a bit hectic lately, haven't they?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], I just wanted to make sure you're enjoying your time at this club."
    m "I would really hate to see you unhappy."
    m 2m "I feel kind of like I'm responsible for that, as President..."
    stop music
    m 4e "And I really do care about you...you know?"
    m "I don't like seeing the other girls give you a hard time."
    m 4r "With how mean Natsuki is and everything..."
    m 4m "And Yuri being a little bit...you know."
    m 5a "Ahaha..."
    m "Sometimes it feels like you and I are the only real people here."
    m "You know what I mean?"
    m 1g "But it's weird, because in all the time you've been here, we've hardly gotten to spend any time together."
    m 1n "Ah...I mean..."
    m "I guess it's technically only been a couple days..."
    m 1l "Sorry, I didn't mean to say something weird!"
    m 1e "There are just some things I've been hoping to talk about with you..."
    m "Things I know only you could understand."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "所以这就是为什么--\"{space=5000}{w=0.75}{nw}"
    m 1g "等等，我还没说完啊！\"{space=5000}{w=0.5}{nw}"
    m "别！\"{space=5000}{w=0.5}{nw}"
    m "快停下！\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front

    call poem(False)

    jump ch23_main

    return
