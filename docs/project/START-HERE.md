# 接手须知（给下一个接班的 AI / 人）

最后一版更新：2026-11-04。**先读完这一页，再动任何文件。**

## 一分钟认识这个项目

《爱在西农 ・ Love in NWAFU》——以西北农林科技大学北校区为舞台的单机 galgame，Ren'Py 引擎，中文界面。当前只做了**动物医学院**一条线，其余学院是"未开放"入口。目标是先做出"能从头玩完的第一天"，再扩内容。

## 必读顺序（共 4 份，十分钟）

1. [current-scope.md](current-scope.md)——**剧情与设定以它为准**，别自己加设定。
2. [collaboration-proposal.md](collaboration-proposal.md)——三路分工与交接契约。
3. [build-status.md](build-status.md)——**当前版本能玩到哪、哪些测过、哪些没测**。
4. [handoff-log.md](handoff-log.md)——最近谁交了什么、状态如何。

读完再 `git log --oneline -10` 看一眼最近提交。

## 环境

| 项 | 路径 |
|---|---|
| Ren'Py 8.3.7 | `G:\renpy\renpy-8.3.7-sdk` |
| 引擎 Python（**必须用这个**） | `G:\renpy\renpy-8.3.7-sdk\lib\py3-windows-x86_64\python.exe` |
| 项目 | `E:\Love_in_nwafu` |
| 系统 Python（跑脚本用） | `F:\python\python.exe` |

`F:\python\python.exe` **不能**直接跑 `renpy.py`（缺 `future` 模块），只能跑辅助脚本。

## 三条命令

```powershell
# 1. 脚本检查（改完 .rpy 必跑）
& 'G:\renpy\renpy-8.3.7-sdk\lib\py3-windows-x86_64\python.exe' 'G:\renpy\renpy-8.3.7-sdk\renpy.py' 'E:\Love_in_nwafu' lint

# 2. 启动游戏
& 'G:\renpy\renpy-8.3.7-sdk\renpy.exe' 'E:\Love_in_nwafu'

# 3. 看有没有报错文件（有就说明崩过）
Test-Path 'E:\Love_in_nwafu\errors.txt'
```

## 仓库结构（谁的地盘）

| 路径 | 内容 | 谁能改 |
|---|---|---|
| `game/` | 运行用的 `.rpy`、图片、字体 | 程序 |
| `story/` `characters/` `world/` | 剧本、人设、校园资料 | 策划编剧 |
| `assets/` | 美术与音频**原稿** | 美术 |
| `docs/day01/` | 素材清单、来源记录 | 策划 |
| `docs/project/` | 范围、分工、版本状态、交接看板 | 各管各的 |
| `private/` | 私人照片与原始资料 | **不进 Git，别提交** |

## 现在的状态（关键）

- 能玩：标题菜单 → 预告 Demo → 序章（含志愿填报表单）→ 第一天前半（南门→报到→西西→动医楼→答题→宿舍）。
- **全部美术是占位色块，全部音频缺失。**
- 没测过的：存读档、改名输入框、地图菜单、题目提示/跳过分支。详见 build-status.md。

## ⚠️ 最大的坑：构建脚本不在仓库里

生成 `game/` 里那些文件的源头，目前在**仓库外的** `E:\deepseek\.nwafu-build\`：

- `build.py`——复制 GUI 模板、打补丁、生成占位图、跑 lint
- `script.rpy`、`content/{characters,day01,teaser,prologue,volunteer}.rpy`——**剧本源文件**

也就是说：**换一台机器 / 换一个人，这套东西就丢了**，只能改 `game/` 里的生成物。接手第一件事，建议把 `build.py` 和 `content/*.rpy` 移进仓库（例如 `tools/` 与 `src/`），并改掉里面的绝对路径。**这件事还没做。**

## 硬性约束（踩过坑的）

1. **文本里不要用「·」（U+00B7）**——字体 `SourceHanSansLite` 没这个字形，会变成方框。用「・」（U+30FB）。
2. **不要把 `game/` 当成剧本**——剧本在 `story/*.md`，`game/content/*.rpy` 是由它转出来的。改剧情先改 md。
3. **Git 只按具体文件路径 `git add`**，禁止 `git add .` 或整个目录（曾经把别人未提交的改动卷进提交）。
4. **提交、推送由程序这一路负责**；其他两路只写文件、在 `handoff-log.md` 记一行。
5. 说"做好了"之前必须有：lint 通过 + 启动无 `errors.txt` + **实际点过**。没点过的写"未验证"。

## 建议的接手动作

1. 读上面 4 份文档。
2. 跑一次 lint 和启动，确认环境能用。
3. 看 `handoff-log.md` 最新的三行，决定先接哪个。
4. 把 `build.py` 与 `content/*.rpy` 纳入仓库（见上文"最大的坑"）。
