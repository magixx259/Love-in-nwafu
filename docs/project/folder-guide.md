# 文件夹导航：什么放在哪里

项目根目录：`E:\Love_in_nwafu`。中文说明便于阅读，文件夹使用稳定英文名称，便于引擎和 MOD 引用。

## 总览

```text
Love_in_nwafu/
  characters/       人物卡、外观设定、个人故事线
  story/            主线场景、学院事件、支线和剧情草稿
  world/            校园地点、地图说明、学院及课程资料
  assets/           可分享的美术／音频原稿及制作文件
  game/             Ren’Py 运行所需脚本和最终导出素材
  mods/             MOD 规范与示例预留位置
  docs/             项目说明、素材清单、来源及工作记录
  private/          原始照片、私人经历、未确认许可的参考资料（不上传）
  dist/             打包后的游戏（不上传）
```

`game/` 和 `mods/` 目前是目录预留，并不代表已经实现游戏或 MOD 加载功能。

## 一个人物的资料放在哪里

每人使用同一个稳定编号关联设定和美术，改显示名字不需要改目录。

| 人物 | 人物设定目录 | 美术与建模目录 |
|---|---|---|
| 白行简（玩家可改名） | `characters/ch00_bai_xingjian/` | `assets/characters/ch00_bai_xingjian/` |
| 俞菲姐 | `characters/ch01_yufei/` | `assets/characters/ch01_yufei/` |
| 西西 | `characters/ch02_xixi/` | `assets/characters/ch02_xixi/` |
| 农农 | `characters/ch03_nongnong/` | `assets/characters/ch03_nongnong/` |

每个人物设定目录中：

- `profile.md`：身份、性格、说话习惯、愿望、弱点、人物关系和不希望出现的设定。
- `appearance.md`：发型、服装、配色、表情、姿态及需要的美术形式。
- `route.md`：个人故事主题、与男主的关系发展和关键事件；男主则记录共同成长线。

每个人物美术目录中：

- `concept/`：设计草图、服装设定和三视图；PSD、KRA 等可编辑原稿也放这里。
- `portraits/`：静态立绘及原稿。
- `expressions/`：表情差分和拆分图层。
- `cg/`：该角色的剧情插画；多人插画放 `assets/cg/`。
- `live2d/source/`：可编辑 Live2D 工程、分层原画；`live2d/exports/` 放导出的模型文件。
- `models3d/source/`：Blender 等建模工程；`models3d/textures/` 放贴图，`models3d/exports/` 放 GLB／FBX 等导出文件。

第一版先用姓名框或静态立绘。Live2D 和 3D 是可选预留，尚未选择制作方式或接入运行库，人物卡不要求为了填目录而做模型。

## 其他资料

| 内容 | 位置 | 例子 |
|---|---|---|
| 第一天主线 | `story/main/day01/` | 到校、报到、参观、休息的场景脚本 |
| 动医专属事件 | `story/colleges/veterinary/` | 动物参观、解剖学知识互动 |
| 机电专属事件 | `story/colleges/mechanical/` | 后续版本预留 |
| 公共校园支线 | `story/side_stories/` | 食堂、早八、乐跑 |
| 尚未决定采用的剧情 | `story/drafts/` | 制作方提出的备选对白；私人真实经历仍放 private |
| 校园地点与地图说明 | `world/locations/`、`world/maps/` | 地点名称、位置依据、年代和路线 |
| 学院、课程和题目依据 | `world/colleges/`、`world/courses/` | 动物结构题的知识点及来源 |
| 场景美术 | `assets/backgrounds/` | 校门、动医楼、第五餐厅、宿舍，按地点分文件夹 |
| 地图美术 | `assets/maps/` | 原创地图工作稿 |
| UI 和标识 | `assets/ui/` | 对话框、按钮、学院卡片 |
| 小游戏图 | `assets/minigames/` | 原创骨骼示意图、匹配题图片 |
| 音乐、音效、环境声、配音 | `assets/audio/bgm/`、`sfx/`、`ambience/`、`voice/` | 可分享的音频及编辑工程 |
| 字体和许可 | `assets/fonts/`、`assets/licenses/` | 字体文件、许可证和署名文本 |
| 正式游戏素材 | `game/images/`、`game/audio/`、`game/fonts/` | 经过选择、压缩并确认可发布的导出文件 |
| 游戏程序与剧情脚本 | `game/scripts/`、`game/content/` | 系统脚本与 `.rpy` 剧情；实际结构随实现调整 |
| 个人照片 | `private/photos/` | 本人生活照、角色肖像参考 |
| 网上找的参考 | `private/references/` | 官方照片、商业游戏参考、许可未明确的素材 |
| 私人经历与原始填写内容 | `private/notes/` | 尚未去除真实人名和宿舍信息的故事 |
| 对话中的待分类附件／笔记 | `private/inbox/` | 先接收，再整理；不要放账号密码等无关信息 |

已有 `private/photos/5号餐厅原图.jpg` 和 `private/references/day01/` 保留原位置；不用为了新目录重复搬运。

## 从参考到游戏的路径

原始资料进 `private/` → 去除私人细节后形成 `characters/`、`story/`、`world/` 中的设定 → 确认可分享的制作稿进 `assets/` → 选定且可发布的导出文件进 `game/`。

`assets/` 存制作稿，`game/` 只存运行需要的结果。修改美术时回到原稿，不手动维护两份互相冲突的设定。
