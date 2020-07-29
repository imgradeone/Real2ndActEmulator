label warning2:
    $ allow_skipping = False

    scene tos
    with Dissolve(1.0)
    pause 1.0

    "[config.name] 是 Doki Doki Literature Club 的粉丝向 Mod，与 Team Salvato 无关。"
    "本 Mod 还在开发中，因此可能会遇到汉化不完全和其他 bug。"
    "本 Mod 理应在通关原游戏后再进行游玩，因此本 Mod 包含大量剧透。"
    "要游玩本 Mod，需要原版 Doki Doki Literature Club 的文件。您可以在 {a=https://ddlc.moe}DDLC.moe{/a} 或者 Steam 免费获取。"
    "中文剧本内容基于 Steam 社区知名汉化版 DDLC 进行翻译并加以修改，在此致谢。"
    "您可以访问 {a=https://steamcommunity.com/sharedfiles/filedetails/?id=1176221672}这里{/a} 以下载汉化版 DDLC，支持汉化大佬。"
    pause 1.0
    "请注意！本 Mod 不适合儿童或心理承受能力较弱的人。"
    "由于本 Mod 包含原作的恐怖元素（甚至发挥到了极致），焦虑症、抑郁症患者，以及儿童，均不适合游玩此 Mod。"
    "同时受“清朗”行动的影响，请务必谨慎游玩。"
    "对于原作的恐怖内容，请访问 {a=https://ddlc.moe/warning.html}这里{/a}。（英文，包含剧透）"
    pause 1.0
    "如果继续游玩 [config.name] 将视为你已经通关原游戏。"#，并接受任何剧透内容。"
    "与此同时，我们将视你为 16 岁以上的玩家，心理健康，且同意接受恐怖内容。"
    scene tos2
    with Dissolve(1.5)
    "既然你已经同意过了，那么我们也就不再让您同意。"
    "但是，如果感到不适，请立即退出游戏。"
    "祝您玩得愉快！"
    $ allow_skipping = True

    return