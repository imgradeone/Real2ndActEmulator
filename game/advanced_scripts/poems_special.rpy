#This is a copy of poem_special.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#This script defines the special poems that might be shown to the player
#Only three of these are ever shown to the player, selected at random
image poem_special1 = "poem_special/poem_special1.png" #Happy Thoughts
image poem_special2 = "poem_special/poem_special2.png" #Can you hear me?
image poem_special3 = "poem_special/poem_special3.png" #Nothing is real
image poem_special4 = "poem_special/poem_special4.png" #Cutting memento
#Stare at the dot, after 10 seconds show "I love you"
image poem_special5:
    "poem_special/poem_special5a.png"
    10.0
    "poem_special/poem_special5b.png"
image poem_special6 = "poem_special/poem_special6.png" #A Joke
#Glitchy monika
image poem_special7a = "poem_special/poem_special7a.png"
image poem_special7b = "poem_special/poem_special7b.png"
image poem_special8 = "poem_special/poem_special8.png" #A Dream
image poem_special9 = "poem_special/poem_special9.png" #Things I like about Papa
image poem_special10 = "poem_special/poem_special10.png" #Go to therapy
image poem_special11 = "poem_special/poem_special11.png" #A Dream

#This is the ending poem, either Monika's goodbye or Dan's thank you
image poem_end = ConditionSwitch(
    "persistent.clearall == True", "poem_special/poem_end_clearall.png",
    "True", "poem_special/poem_end.png")

#Each of these define a label for showing a poem
label poem_special_1:
    show screen notify("达成成就：叮！您点的晴天娃娃！")
    $ quick_menu = False
    play sound page_turn
    show poem_special1 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return

#All the rest are the same
label poem_special_2:
    show screen notify("达成成就：CAN YOU HEAR ME?")
    $ quick_menu = False
    play sound page_turn
    show poem_special2 with Dissolve(1.0)
    $ pause()
    play sound "sfx/giggle.ogg" # 此时有人正在傻笑
    $ quick_menu = True
    return
label poem_special_3:
    show screen notify("达成成就：这是甚么东西？？？")
    $ quick_menu = False
    play sound page_turn
    show poem_special3 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_4:
    show screen notify("达成成就：今天 Yuri 自 wei 了吗（")
    $ quick_menu = False
    play sound page_turn
    show poem_special4 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_5:
    show screen notify("达成成就：盯着那个黑点，10 秒！！！")
    $ quick_menu = False
    play sound page_turn
    show poem_special5 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_6:
    show screen notify("达成成就：世界线错乱")
    $ quick_menu = False
    play sound page_turn
    show poem_special6 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_7:
    show screen notify("达成成就：借 尸 还 魂")
    $ quick_menu = False
    play sound page_turn
    show poem_special7a as ps with Dissolve(1.0)
    $ pause()
    show poem_special7b as ps
    pause 0.01
    $ quick_menu = True
    return
label poem_special_8:
    show screen notify("达成成就：都是桃子（？）")
    $ quick_menu = False
    play sound page_turn
    show poem_special8 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_9:
    show screen notify("达成成就：拒绝家暴，从我做起")
    $ quick_menu = False
    play sound page_turn
    show poem_special9 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_10:
    show screen notify("达成成就：adfhsdfkbsbdfaldfbjs")
    $ quick_menu = False
    play sound page_turn
    show poem_special10 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_11:
    show screen notify("达成成就：✝我要退赛✝")
    $ quick_menu = False
    play sound page_turn
    show poem_special11 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
