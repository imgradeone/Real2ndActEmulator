label gameconsole:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    play music t10

    menu:
        "继续刷二周目":
            jump ch20_main
        "安全模式设置（开发中）":
            call safe_mode_settings

    jump gameconsole
return

label safe_mode_settings:
    "安全模式可以控制彩蛋的显示，避免您受到惊吓。"
    "默认情况下，仅已经获得成就的彩蛋会被安全模式屏蔽。"
    "如果您无法忍受任何彩蛋，请启用究极安全模式。"
    "目前该功能暂时无效。"

    menu:
        "不启用安全模式":
            $ persistent.safe_mode = 0
        "启用安全模式":
            $ persistent.safe_mode = 1
        "启用究极安全模式":
            $ persistent.safe_mode = 2

return
