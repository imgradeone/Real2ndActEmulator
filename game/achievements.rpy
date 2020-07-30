label achievements_list:
    scene black
    "系统" "您现在查看的是成就列表，这里可以显示你已经达成的成就，并且兑换能力者称号。"
    "系统" "正在结算您的成就......{w=1.0}{nw}"
    $ persistent.achievements_count = 0
    $ persistent.achievements_point = 0

    # 1
    if achievement.has("卡 姿 兰 大 眼 睛"):
        $ persistent.achievements_point += 3
        $ persistent.achievements_count += 1
        $ text1 = "卡 姿 兰 大 眼 睛 / 普通"
    else:
        $ text1 = "未达成"
    # 2
    if achievement.has("苏 联 解 体"):
        $ persistent.achievements_point += 3
        $ persistent.achievements_count += 1
        $ text2 = "苏 联 解 体 / 普通"
    else:
        $ text2 = "未达成"
    # 3
    if achievement.has("MOPEMOPE"):
        $ persistent.achievements_point += 3
        $ persistent.achievements_count += 1
        $ text3 = "MOPEMOPE / 普通"
    else:
        $ text3 = "未达成"
    # 4
    if achievement.has("死 者 视 角 打 游 戏"):
        $ persistent.achievements_point += 5
        $ persistent.achievements_count += 1
        $ text4 = "死 者 视 角 打 游 戏 / 较稀有"
    else:
        $ text4 = "未达成"
    # 5
    if achievement.has("你鼠标里的 DNA"):
        $ persistent.achievements_point += 3
        $ persistent.achievements_count += 1
        $ text5 = "你鼠标里的 DNA / 普通"
    else:
        $ text5 = "未达成"
    # 6
    if achievement.has("死 不 瞑 目 沙 师 弟"):
        $ persistent.achievements_point += 10
        $ persistent.achievements_count += 1
        $ text6 = "死 不 瞑 目 沙 师 弟 / 稀有"
    else:
        $ text6 = "未达成"
    # 7
    if achievement.has("但是我拒绝！"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text7 = "但是我拒绝！ / 极普通"
    else:
        $ text7 = "未达成"
    # 8
    if achievement.has("低 级 马 赛 克"):
        $ persistent.achievements_point += 2
        $ persistent.achievements_count += 1
        $ text8 = "低 级 马 赛 克 / 普通"
    else:
        $ text8 = "未达成"
    # 9
    if achievement.has("眉 飞 色 舞"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text9 = "眉 飞 色 舞 / 极普通"
    else:
        $ text9 = "未达成"
    # 10
    if achievement.has("七 龙 珠"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text10 = "七 龙 珠 / 极普通"
    else:
        $ text10 = "未达成"
    # 11
    if achievement.has("Touch"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text11 = "Touch / 极普通"
    else:
        $ text11 = "未达成"
    # 12
    if achievement.has("O w O"):
        $ persistent.achievements_point += 2
        $ persistent.achievements_count += 1
        $ text12 = "O w O / 普通"
    else:
        $ text12 = "未达成"
    # 13
    if achievement.has("看到啥都乱点，小学生啊（"):
        $ persistent.achievements_point += 3
        $ persistent.achievements_count += 1
        $ text13 = "看到啥都乱点，小学生啊（ / 普通"
    else:
        $ text13 = "未达成"
    # 14
    if achievement.has("在？为什么迫害 PurpleShep？？？"):
        $ persistent.achievements_point += 15
        $ persistent.achievements_count += 1
        $ text14 = "在？为什么迫害 PurpleShep？？？ / 超稀有"
    else:
        $ text14 = "未达成"
    # 15
    if achievement.has("被叫爸爸的感觉怎么样（"):
        $ persistent.achievements_point += 8
        $ persistent.achievements_count += 1
        $ text15 = "被叫爸爸的感觉怎么样（ / 中等"
    else:
        $ text15 = "未达成"
    # 16
    if achievement.has("今日你迫害 Sayori 了吗（"):
        $ persistent.achievements_point += 3
        $ persistent.achievements_count += 1
        $ text16 = "今日你迫害 Sayori 了吗（ / 普通"
    else:
        $ text16 = "未达成"
    # 17
    if achievement.has("我 TM 炸开！（物理）"):
        $ persistent.achievements_point += 5
        $ persistent.achievements_count += 1
        $ text17 = "我 TM 炸开！（物理） / 较稀有"
    else:
        $ text17 = "未达成"
    # 18
    if achievement.has("陪我玩！！！！"):
        $ persistent.achievements_point += 2
        $ persistent.achievements_count += 1
        $ text18 = "陪我玩！！！！ / 普通"
    else:
        $ text18 = "未达成"
    # 19
    if achievement.has("叮！您点的晴天娃娃！"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text19 = "叮！您点的晴天娃娃！ / 特殊诗"
    else:
        $ text19 = "未达成"
    # 20
    if achievement.has("CAN YOU HEAR ME?"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text20 = "CAN YOU HEAR ME? / 特殊诗"
    else:
        $ text20 = "未达成"
    # 21
    if achievement.has("这是甚么东西？？？"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text21 = "这是甚么东西？？？ / 特殊诗"
    else:
        $ text21 = "未达成"
    # 22
    if achievement.has("今天 Yuri 自 wei 了吗（"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text22 = "今天 Yuri 自 wei 了吗（ / 特殊诗"
    else:
        $ text22 = "未达成"
    # 23
    if achievement.has("盯着那个黑点，10 秒！！！"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text23 = "盯着那个黑点，10 秒！！！ / 特殊诗"
    else:
        $ text23 = "未达成"
    # 24
    if achievement.has("世界线错乱"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text24 = "世界线错乱 / 特殊诗"
    else:
        $ text24 = "未达成"
    # 25
    if achievement.has("借 尸 还 魂"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text25 = "借 尸 还 魂 / 特殊诗"
    else:
        $ text25 = "未达成"
    # 26
    if achievement.has("都是桃子（？）"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text26 = "都是桃子（？） / 特殊诗"
    else:
        $ text26 = "未达成"
    # 27
    if achievement.has("拒绝家暴，从我做起"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text27 = "拒绝家暴，从我做起 / 特殊诗"
    else:
        $ text27 = "未达成"
    # 28
    if achievement.has("adfhsdfkbsbdfaldfbjs"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text28 = "adfhsdfkbsbdfaldfbjs / 特殊诗"
    else:
        $ text28 = "未达成"
    # 29
    if achievement.has("我要退赛"):
        $ persistent.achievements_point += 1
        $ persistent.achievements_count += 1
        $ text29 = "我要退赛 / 特殊诗"
    else:
        $ text29 = "未达成"
    # 30
    if achievement.has("下次一定"):
        $ persistent.achievements_point += 3
        $ persistent.achievements_count += 1
        $ text30 = "下次一定 / 中等"
    else:
        $ text30 = "未达成"
    # 31
    if achievement.has("一键忽略"):
        $ persistent.achievements_point += 3
        $ persistent.achievements_count += 1
        $ text31 = "一键忽略 / 中等"
    else:
        $ text31 = "未达成"
    # 32
    if achievement.has("蓝屏钙 V2"):
        $ persistent.achievements_point += 15
        $ persistent.achievements_count += 1
        $ text32 = "蓝屏钙 V2 / 超稀有"
    else:
        $ text32 = "未达成"
    
    "系统" "您目前获得的成就数量为 [persistent.achievements_count] / 32。"
    "系统" "累计获得点数 [persistent.achievements_point] / 103。"
    
    if persistent.achievements_point >= 50:
        if persistent.achievements_count == 32:
            $ persistent.player_level = 3
            "系统" "您居然集齐了所有成就！恭喜您解锁彩蛋！（TODO）"# TODO: 彩蛋
        else:
            $ persistent.player_level = 2
            "系统" "挺强的，您现在可以查看更多选项了。现在前往游戏设置看看吧。（TODO）"
    # TODO: 更多选项（现在已经做了 Sayori 光标）

    "系统" "接下来看看你获得了哪些成就吧："
    "1. [text1]"
    "2. [text2]"
    "3. [text3]"
    "4. [text4]"
    "5. [text5]"
    "6. [text6]"
    "7. [text7]"
    "8. [text8]"
    "9. [text9]"
    "10. [text10]"
    "11. [text11]"
    "12. [text12]"
    "13. [text13]"
    "14. [text14]"
    "15. [text15]"
    "16. [text16]"
    "17. [text17]"
    "18. [text18]"
    "19. [text19]"
    "20. [text20]"
    "21. [text21]"
    "22. [text22]"
    "23. [text23]"
    "24. [text24]"
    "25. [text25]"
    "26. [text26]"
    "27. [text27]"
    "28. [text28]"
    "29. [text29]"
    "30. [text30]"
    "31. [text31]"
    "32. [text32]"
    # TODO: 显示成就相应场景

    if persistent.achievements_count == 32:
        "系统" "感谢您的爆肝。"
    else:
        "系统" "继续加油，集齐更多成就吧！"

    return

    # achievement.register("卡 姿 兰 大 眼 睛")
    # achievement.register("苏 联 解 体")
    # achievement.register("MOPEMOPE")
    # achievement.register("死 者 视 角 打 游 戏")
    # achievement.register("你鼠标里的 DNA")
    # achievement.register("死 不 瞑 目 沙 师 弟")
    # achievement.register("但是我拒绝！")
    # achievement.register("低 级 马 赛 克")
    # achievement.register("眉 飞 色 舞")
    # achievement.register("七 龙 珠")
    # achievement.register("Touch")
    # achievement.register("O w O")
    # achievement.register("看到啥都乱点，小学生啊（")
    # achievement.register("在？为什么迫害 PurpleShep？？？")
    # achievement.register("被叫爸爸的感觉怎么样（")
    # achievement.register("今日你迫害 Sayori 了吗（")
    # achievement.register("我 TM 炸开！（物理）")
    # achievement.register("陪我玩！！！！")
    # achievement.register("叮！您点的晴天娃娃！")
    # achievement.register("CAN YOU HEAR ME?")
    # achievement.register("这是甚么东西？？？")
    # achievement.register("今天 Yuri 自 wei 了吗（")
    # achievement.register("盯着那个黑点，10 秒！！！")
    # achievement.register("世界线错乱")
    # achievement.register("借 尸 还 魂")
    # achievement.register("都是桃子（？）")
    # achievement.register("拒绝家暴，从我做起")
    # achievement.register("adfhsdfkbsbdfaldfbjs")
    # achievement.register("我要退赛")
    # achievement.register("下次一定")
    # achievement.register("一键忽略")
    # achievement.register("蓝屏钙 V2")

