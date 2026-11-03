# 预告 Demo —— 约 1 分钟，从标题界面「预告 Demo」进入

label teaser:

    scene black with fade
    with Pause(0.4)
    centered "{size=34}有些故事，从一通电话开始。{/size}"
    with Pause(0.6)

    scene bg room with fade
    "那个夏天，我以为自己只是换了座城市。"
    with Pause(0.3)

    scene bg gate with fade
    "后来才知道，有些东西是从校门口开始算的。"
    with Pause(0.3)

    show xixi normal at right with dissolve
    xx "你也是动医的？那以后就是同学了。"
    with Pause(0.3)

    show nongnong normal at left with dissolve
    nn "……那边封了。"
    nn "我知道另一条路。跟不跟？"
    with Pause(0.3)

    hide xixi
    hide nongnong
    with dissolve

    scene black with fade
    phone "先看通知。"
    with Pause(0.5)

    centered "{size=52}爱在西农{/size}\n\n{size=26}LOVE IN NWAFU{/size}"
    with Pause(0.8)
    centered "{size=22}序章预告 ・ 未完待续{/size}"
    centered "{size=18}试玩版本 v0.1-demo{/size}"
    "（Demo 结束。感谢试玩。）"
    return
