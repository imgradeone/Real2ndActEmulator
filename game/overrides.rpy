## This file is for overriding specific declarations from DDLC
## Use this if you want to change a few variables, but don't want
## to replace entire script files that are otherwise fine.

## Normal overrides
## These overrides happen after any of the normal init blocks in scripts
## Use these to chagne variables on screens, effects, etc
init 10 python:
    achievement.register("卡 姿 兰 大 眼 睛")
    achievement.register("苏 联 解 体")
    achievement.register("MOPEMOPE")
    achievement.register("死 者 视 角 打 游 戏")
    achievement.register("你鼠标里的 DNA")
    achievement.register("死 不 瞑 目 沙 师 弟")
    achievement.register("但是我拒绝！")
    achievement.register("低 级 马 赛 克")
    achievement.register("眉 飞 色 舞")
    achievement.register("七 龙 珠")
    achievement.register("Touch")
    achievement.register("O w O")
    achievement.register("看到啥都乱点，小学生啊（")
    achievement.register("在？为什么迫害 PurpleShep？？？")
    achievement.register("被叫爸爸的感觉怎么样（")
    achievement.register("今日你迫害 Sayori 了吗（")
    achievement.register("我 TM 炸开！（物理）")
    achievement.register("陪我玩！！！！")
    achievement.register("叮！您点的晴天娃娃！")
    achievement.register("CAN YOU HEAR ME?")
    achievement.register("这是甚么东西？？？")
    achievement.register("今天 Yuri 自 wei 了吗（")
    achievement.register("盯着那个黑点，10 秒！！！")
    achievement.register("世界线错乱")
    achievement.register("借 尸 还 魂")
    achievement.register("都是桃子（？）")
    achievement.register("拒绝家暴，从我做起")
    achievement.register("adfhsdfkbsbdfaldfbjs")
    achievement.register("我要退赛")
    achievement.register("下次一定")
    achievement.register("一键忽略")

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
