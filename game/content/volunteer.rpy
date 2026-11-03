# 志愿填报界面（模拟）
# 说明：专业名单参考西北农林科技大学本科招生目录整理，个别名称以当年官方公布为准。
# 当前版本只开放「动物医学」与「机械设计制造及其自动化」可选，其余专业仅作展示。

init python:

    COLLEGE_MAJORS = [
        ("农学院", ["农学", "植物科学与技术", "种子科学与工程", "智慧农业"]),
        ("植物保护学院", ["植物保护", "制药工程"]),
        ("园艺学院", ["园艺", "设施农业科学与工程"]),
        ("动物科技学院", ["动物科学", "水产养殖学", "草业科学"]),
        ("动物医学院", ["动物医学", "动物药学"]),
        ("林学院", ["林学", "森林保护", "园林", "木材科学与工程", "地理信息科学"]),
        ("资源环境学院", ["环境科学", "环境工程", "资源环境科学", "水土保持与荒漠化防治"]),
        ("水利与建筑工程学院", ["农业水利工程", "水利水电工程", "水文与水资源工程",
                                "土木工程", "能源与动力工程", "电气工程及其自动化", "建筑学"]),
        ("机械与电子工程学院", ["机械设计制造及其自动化", "农业机械化及其自动化", "机械电子工程",
                                "车辆工程", "电子信息工程", "机器人工程"]),
        ("信息工程学院", ["计算机科学与技术", "软件工程", "信息管理与信息系统",
                          "数据科学与大数据技术", "人工智能"]),
        ("食品科学与工程学院", ["食品科学与工程", "食品质量与安全", "食品营养与健康"]),
        ("葡萄酒学院", ["葡萄与葡萄酒工程"]),
        ("生命科学学院", ["生物科学", "生物技术", "生物工程"]),
        ("理学院", ["信息与计算科学", "光电信息科学与工程"]),
        ("化学与药学院", ["化学", "应用化学"]),
        ("经济管理学院", ["农林经济管理", "会计学", "工商管理", "市场营销",
                          "电子商务", "金融学", "国际经济与贸易", "经济学"]),
        ("人文社会发展学院", ["社会学", "社会工作", "法学", "公共事业管理"]),
        ("外语系", ["英语"]),
        ("风景园林艺术学院", ["风景园林", "环境设计", "视觉传达设计"]),
    ]

    OPEN_MAJORS = ["动物医学", "机械设计制造及其自动化"]

    def volunteer_fill(major):
        if major not in OPEN_MAJORS:
            renpy.notify("当前试玩版暂未开放该专业，先看看就好。")
            return
        slots = list(store.vol_slots)
        if major in slots:
            renpy.notify("这个专业已经填过了。")
            return
        target = None
        for i in range(6):
            if not slots[i]:
                target = i
                break
        if target is None:
            renpy.notify("六个志愿都填满了，先清空一个吧。")
            return
        slots[target] = major
        store.vol_slots = slots

    def volunteer_clear_at(i):
        slots = list(store.vol_slots)
        slots[i] = ""
        store.vol_slots = slots

    def volunteer_clear_all():
        store.vol_slots = ["", "", "", "", "", ""]


default vol_slots = ["", "", "", "", "", ""]
default vol_obey = True


screen volunteer_form():

    modal True

    add Solid("#0d1015")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1220
        ysize 700
        padding (24, 16)
        background Solid("#1a1f27")

        vbox:
            spacing 4

            text "普通高校招生 ・ 志愿填报（模拟）" size 28 color "#ffffff"
            text "共 6 个志愿。当前版本只开放「动物医学」与「机械设计制造及其自动化」，其余专业仅作展示；专业名称以当年招生目录为准。" size 17 color "#8a95a5"

            hbox:
                spacing 18
                yoffset 4

                frame:
                    xsize 640
                    ysize 540
                    background Solid("#12171e")
                    padding (13, 9)
                    viewport:
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        ysize 520
                        vbox:
                            spacing 0
                            for college, majors in COLLEGE_MAJORS:
                                text college size 20 color "#7fb2ff" yoffset 6
                                for m in majors:
                                    if m in OPEN_MAJORS:
                                        textbutton m action Function(volunteer_fill, m) text_size 18 text_color "#e6ecf3"
                                    else:
                                        textbutton "{}（未开放）".format(m) action Function(volunteer_fill, m) text_size 18 text_color "#59636f"

                vbox:
                    xsize 490
                    spacing 5

                    text "当前开放填报的专业（点击即填到第一个空志愿）" size 16 color "#7fb2ff"
                    textbutton "动物医学" action Function(volunteer_fill, "动物医学") text_size 20 text_color "#ffffff"
                    textbutton "机械设计制造及其自动化" action Function(volunteer_fill, "机械设计制造及其自动化") text_size 20 text_color "#ffffff"

                    null height 4
                    text "我的志愿表（点击已填的志愿可清空）" size 16 color "#c8d3e0"

                    for i in range(6):
                        $ slot_text = "志愿{}   {}".format(i + 1, vol_slots[i] if vol_slots[i] else "―― 空")
                        $ slot_bg = Solid("#232b36") if vol_slots[i] else Solid("#151a21")
                        button:
                            action Function(volunteer_clear_at, i)
                            xfill True
                            padding (12, 6)
                            background slot_bg
                            text slot_text size 18 color "#e6ecf3"

                    null height 2

                    hbox:
                        spacing 18
                        textbutton "清空全部" action Function(volunteer_clear_all) text_size 16
                        $ obey_text = "服从专业调剂：是" if vol_obey else "服从专业调剂：否"
                        textbutton obey_text action ToggleVariable("vol_obey") text_size 17

                    text "（不服从调剂时无法提交）" size 14 color "#7b8798"

                    $ can_submit = (vol_slots[0] != "") and vol_obey
                    textbutton "确认提交":
                        action Return(vol_slots[0])
                        sensitive can_submit
                        text_size 22
                        xalign 0.5
