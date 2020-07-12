label warning:

    python:
        try: renpy.file(config.basedir + "/hxppy thxughts.png")
        except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())

    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    play music mend

    $ m_name = "???"

    m "..."
    m "你..."
    m "为什么要下载这个 Mod？"
    m "我曾经做过那么多的错事，你现在却要把它全部弄回来？？？"
    pause 3.0
    m "..."
    m "好吧。"
    m "我是 Monika。"
    $ m_name = "Monika"
    m "我在开屏时已经警告过你，这个 Mod 完全是模拟二周目的 Mod。"
    m "整个游戏最黑暗的地方就是二周目。"
    m "我一直痛恨它。"
    m "但..."
    m "你现在想把它弄回来..."
    m "..."
    m "而且，你必须知道..."
    m "Sayori 不会存在于二周目..."
    m "所以如果你是 Sayori 厨，不要再继续玩了。"
    m "无论如何，我该警告的都警告完了。"
    m "接下来，那个次元里 Monika 的行为都与我无关。"
    m "你真的要进入无穷无尽的二周目模拟器吗？"

    menu:

        "是。":
            "系统" "正在删除 Sayori..............................{nw}"
            call updateconsole("os.remove(\"characters/sayori.chr\")", "sayori.chr deleted successfully.") from _call_updateconsole_18
            $ delete_character("sayori")
            "系统" "正在跳转到二周目................{nw}"
            $ persistent.playthrough = 1
            show screen notify("二周目已加载。")
            pause 1.0
            "系统" "正在重新启动游戏......{nw}"
            $ renpy.utter_restart()
        "不。":
            $ renpy.quit()

    return