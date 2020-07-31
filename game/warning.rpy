label warning:

    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    play music mend

    $ m_name = "???"

    m "...\"{w=2.0}{nw}"
    m "你..."
    m "我曾经做过那么多的错事，你现在却要让它们都恢复回来？"
    m "...\"{w=2.0}{nw}"
    m "好吧。"
    m "我是 Monika。"
    $ m_name = "Monika"
    m "我在开屏时已经警告过你，这个 Mod 会模拟二周目。"
    m "而，整个游戏最黑暗的地方就是二周目。"
    m "我非常痛恨它。"
    m "但..."
    m "你现在想把它弄回来..."
    m "..."
    m "而且，你也知道的，Sayori 不在二周目里。"
    m "所以 Sayori 厨最好不要继续玩下去。"
    m "我该警告的都警告完了。"
    m "接下来，{i}那个{/i} Monika 的行为都与我无关。"
    m "你真的要进入二周目吗？"

    menu:
        "是。":
            m "..."
            m "好吧。"
            "正在删除 Sayori...{nw}"
            call updateconsole("os.remove(\"characters/sayori.chr\")", "sayori.chr deleted successfully.") from _call_updateconsole_18
            $ delete_character("sayori")
            "正在加载二周目...{nw}"
            $ persistent.playthrough = 1
            show screen notify("二周目已加载。")
            pause 1.0
            "正在重新启{nw}"
            $ srf = screenshot_srf()
            show layer screens:
                truecenter
                zoom 1.00
            show screen tear(20, 0.1, 0.1, 0, 40, srf)
            stop music
            play sound "sfx/s_kill_glitch1.ogg"
            pause 1
            $ renpy.utter_restart()
        "不。":
            pass

    return