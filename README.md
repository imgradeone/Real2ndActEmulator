# 全真二周目模拟器

DDLC 中文 Mod 模板 新 Demo

## 警告

**请注意！本 Mod 不适合儿童或心理承受能力较弱的人。**

由于本 Mod 包含原作的恐怖元素（甚至发挥到了极致），焦虑症、抑郁症患者，以及儿童，均不适合游玩此 Mod。

对于原作的恐怖内容，请访问 [这里](https://ddlc.moe/warning.html)。（英文，包含剧透）

如果继续游玩本 Mod，我们将视为你已经通关原游戏，并接受任何剧透内容。

与此同时，我们将认为您是 13 岁以上的玩家，心理健康，且同意接受恐怖内容。

**不要说我们没有警告过你。**

详情参阅 [WARNING.md](./WARNING.md)

## 下载 Mod

您可以在 [Releases 页面](https://github.com/imgradeone/Real2ndActEmulator/releases) 获取。

### 关于移植

您可以自行研究 Ren'Py，然后进行 Mod 的 Android / iOS 移植，但是 **请勿分享移植版的安装包，移植仅供自用**，作者也不提供移植版的维护。

## 中文字体

中文版 DDLC Mod 模板使用了一些免费商用的中文字体，在此致谢。**开始 Mod 开发前，请务必下载这些字体，否则将无法启动工程。安装方式见 [中文字体包安装](#中文字体包安装) 小节。**

如有需要，您也可以自行修改配置文件，以自定义字体，**但请自主承担版权风险**。

中文字体详情请查看 [这里](./game/mod_assets/font/README.md)

## 中文字体包安装

> 请注意：我们仍然建议您从各个字体的官网下载这些字体，即便它们都是免费商用字体。

您可以下载懒人专用字体包，下载完后将字体解压到 `game/mod_assets/font` 目录下即可。

当前版本字体包：v1.2

对应支持模板 v1.2 版本，不支持模板 v1.0 ~ v1.1

您可以从以下地方获取 Mod 模板的中文字体包（v1.2）：

### 中国大陆地区用户

[奶牛快传（链接会于 2020-10-01 过期）](https://imgradeone.cowtransfer.com/s/3852906fbdf246) | [蓝奏云](https://imgradeone.lanzous.com/iwq7wec3j7a) | [百度网盘 提取码 hi2j](https://pan.baidu.com/s/1WiO1qD8cI8U1YTEVeVrkuQ) | [城通网盘（仅供赞助用途，实际体验差）](http://ct.imgradeone.xyz/file/24390393-452015477)

### 其他地区用户

[MediaFire](http://www.mediafire.com/file/6juwd7h0venrg7f/font%25282%2529.zip/file) | [Google 云端硬盘](https://drive.google.com/file/d/1LClyzgxq-les-N5egLXm1aK7ULATDpex/view?usp=sharing) | GitHub (later)

## 打包 Mod

1. 打开 Ren'Py SDK，点击 “Build Distributions” / “生成分发版”。
1. 在 “Build Packages:” / “生成分发包：” 选项中勾选 “DDLC Compatible Mod”，然后开始构建。
1. 构建完成后，系统将自动打开文件管理器，展示打包后的 Mod。建议先自行安装 Mod 并测试后，再分发到各个平台。

## 特别感谢

- Team Salvato http://teamsalvato.com / https://ddlc.moe
- Monika After Story Team http://www.monikaafterstory.com
- 所有中文字体作者
- Sayo-nika Team
- Doki Doki Mod Manager Team
- 汉化版作者

本 Demo 参考了知名汉化版的翻译，在此感谢。[Steam 社区原帖](https://steamcommunity.com/sharedfiles/filedetails/?id=1176221672)

## 翻译指南

本 Mod 对原游戏剧本的汉化会有一些小区别，请查阅 [TRANSLATIONS.md](./TRANSLATIONS.md)。

同时，本 Mod 的中文剧本翻译参考了知名汉化版的翻译、腾讯翻译官的机器翻译。

## 开源许可

本模板采用 [Sayo-nika 的 GitHub Action](https://github.com/Sayo-nika/quickstart-actions) 进行远程 Mod 构建，并进行定制化，在此致谢。

本 Mod 模板需要使用 Ren'Py。Ren'Py 包含自由软件许可中的一些许可证，包括 GNU 宽通用公共许可证。  
Ren'Py 由一系列开源组件构成，它们的开源协议可以在 https://www.renpy.cn/doc/license.html （简体中文）或 https://www.renpy.org/doc/html/license.html （英文）查看。

本模板基于 Monika After Story 团队的 [DDLCModTemplate](https://github.com/Monika-After-Story/DDLCModTemplate)。

本模板属于粉丝作品，遵循 Team Salvato IP Guidelines。

## TODO

- [x] 成就后端
- [ ] 安全模式 / 究极安全模式
- [ ] 能力者称号

## 加入社区

[Telegram 频道](https://t.me/DDLCModCN)