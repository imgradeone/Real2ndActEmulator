## This file is for overriding specific declarations from DDLC
## Use this if you want to change a few variables, but don't want
## to replace entire script files that are otherwise fine.

## Normal overrides
## These overrides happen after any of the normal init blocks in scripts
## Use these to chagne variables on screens, effects, etc
init 10 python:
    register_achievement_all("卡 姿 兰 大 眼 睛", "KAMONI_BIG_EYES", "见到 Monika 崩坏的大眼睛")
    register_achievement_all("苏 联 解 体", "YURI_YURI_ICE_CREAM", "见到变成两半的 Yuri") # 尝试翻译旺旺碎碎冰失败
    register_achievement_all("MOPEMOPE", "MOUTHY_NATSUKI", "见到 Natsuki 的真实嘴")
    register_achievement_all("死 者 视 角 打 游 戏", "DEAD_SAYORI_GAMEPLAY", "见到游戏画面”昏厥“效果")
    register_achievement_all("你鼠标里的 DNA", "SAYORI_CURSOR_NORMAL_GAMEPLAY", "在普通游戏流程中获得 Sayori 的指针")
    register_achievement_all("死 不 瞑 目 沙 师 弟", "SHAMEFUL_HANG", "看到”死亡“ Sayori 的 noface 形态")
    register_achievement_all("但是我拒绝！", "JUST_MONIKA", "在第 3 章选你的真实意见时没选 Monika")
    register_achievement_all("低 级 马 赛 克", "I_AM_HUNGRY", "看到 Natsuki 饥饿时的”鬼“样子")
    register_achievement_all("眉 飞 色 舞", "ONE_EYE", "看到眼睛错位的 Yuri")
    register_achievement_all("七 龙 珠", "URI_DRAGONBALL", "看到 Yuri 让你马上读 Portrait of Markov 时的样子")
    register_achievement_all("Touch", "YURI_CHEST_TOUCH", "看到 Yuri 把你的手放在她胸前后的紧张样子")
    register_achievement_all("O w O", "YURI_ODD_EYES", "看到 Yuri 奇怪的眼睛")
    register_achievement_all("看到啥都乱点，小学生啊（", "POEMGAME_GLITCH", "把 Poemgame GUI 弄得一团糟")
    register_achievement_all("在？为什么迫害 PurpleShep？？？", "YURI_STICKER", "看到 Poemgame 里 Yuri 崩坏的贴图")
    register_achievement_all("被叫爸爸的感觉怎么样（", "PLAYED_BAA", "在 Poemgame 里听到 baa.ogg")
    register_achievement_all("今日你迫害 Sayori 了吗（", "POEMGAME_SAYORI_EYES", "看到使 Sayori 厨震怒的 Poemgame 彩蛋")
    register_achievement_all("我 TM 炸开！（物理）", "NEAT_EYEXPLOSION", "看到 Natsuki 眼球炸开")
    register_achievement_all("陪我玩！！！！", "PLAY_WITH_ME", "被 Natsuki 缺乏玩耍的鬼魂吓死")
    register_achievement_all("叮！您点的晴天娃娃！", "HAPPY_THOUGHTS", "特殊诗 1")
    register_achievement_all("CAN YOU HEAR ME?", "HEAR_ME", "特殊诗 2")
    register_achievement_all("这是甚么东西？？？", "WHAT_THE_HELL", "特殊诗 3"))
    register_achievement_all("今天 Yuri 自 wei 了吗（", "SELF_PLEASURE", "特殊诗 4"))
    register_achievement_all("盯着那个黑点，10 秒！！！", "DOT_LOVELETTER", "特殊诗 5"))
    register_achievement_all("世界线错乱", "THE_SCRIPT_DERAIL", "特殊诗 6")
    register_achievement_all("借 尸 还 魂", "GO_BACK", "特殊诗 7")
    register_achievement_all("都是桃子（？）", "PEACHES_FULL_SITE", "特殊诗 8")
    register_achievement_all("拒绝家暴，从我做起", "NATSUKI_PAPA", "特殊诗 9")
    register_achievement_all("adfhsdfkbsbdfaldfbjs", "FRICKING_GIBBERISH", "特殊诗 10")
    register_achievement_all("我要退赛", "IWR_QUIT", "特殊诗 11")
    register_achievement_all("下次一定", "ONE_PRESS_DOUBLEHIT", "听到 Yuri 要 Natsuki 钻到售货机底下去捡硬币")
    register_achievement_all("一键忽略", "IGNORING_NATSUKI", "听到 Yuri 说 Natsuki 习惯被")
    register_achievement_all("蓝屏钙 V2", "MONIOS_BSOD", "使你的电脑被 Monika 吓得蓝屏")
    pass

## Late overrides
## These overrides happen aftre prety much everything else in startup.
## Use these to change displayables and other late definitions in renpy.
init 501 python:
    pass

## Early overrides
## These overrides happen befoer the normal init blcosk in scripts
## Use these in the rare event taht you need to overwrite some variable
## before it's called in another init blcok
## You probably wont use this
init -10 python:
    pass

## Super early overrides
## These get called before any of the init blocks are read, before the
## persistent data is read. Basically right after RenPy loads itself but
## before the game / mod is loaded.
## You almost never will need this
python early:
    pass
