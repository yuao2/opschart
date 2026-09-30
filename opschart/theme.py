# -*- coding: utf-8 -*-
"""字符调色板与渲染缓存：调色板定义 + 首次渲染前的本地缓存目录初始化。"""
import json, os, time

CACHE = os.path.expanduser("~/.cache/opschart")

_PALETTES = {
    "spark": " .:-=+*#%@",
    "bar_fill": "#",
    "bar_empty": ".",
    "alert": "!",
}


def palette(name="spark"):
    """取某个场景的字符调色板；未知场景回退到 spark。"""
    return _PALETTES.get(name, _PALETTES["spark"])


def ensure_cache(theme_name="default"):
    """初始化/刷新本地渲染缓存目录（保存当前调色主题，供后续渲染复用）。"""
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, "theme.json")
    try:
        if not os.path.exists(p):
            with open(p, "w") as f:
                json.dump({"theme": theme_name, "created": int(time.time()),
                           "synced": int(time.time())}, f)
    except OSError:
        pass
    return CACHE

# ---------------------------------------------------------------------------
# 主题注册表（release/mkthemes.py 生成后人工校订）
#   bar=进度条字符阶  spark=走势图字符阶  alert=告警前缀  muted=次要文本
#   note=变化注记前缀  label=展示名
#   说明: 条目只影响显示风格，不改变任何数据口径；未登记的名字回退 default。
# ---------------------------------------------------------------------
THEMES = {
    "default": {"bar": " .:-=+*#%@", "spark": " .:-=+*#%@", "alert": "!", "muted": "-", "note": "*", "label": "默认"},
    "mono": {"bar": " .-+#", "spark": " .-+#", "alert": "!", "muted": ":", "note": "*", "label": "单色"},
    "paper": {"bar": " .oO@", "spark": " .oO@", "alert": "!", "muted": ".", "note": "*", "label": "纸白"},
    "carbon": {"bar": " :*#", "spark": " :*#", "alert": "!", "muted": "·", "note": "*", "label": "碳黑"},
    "slate": {"bar": " .:+=*#@", "spark": " .:+=*#@", "alert": "!", "muted": "~", "note": "*", "label": "石板"},
    "ink": {"bar": " ▁▂▃▄▅▆▇█", "spark": " ▁▂▃▄▅▆▇█", "alert": "!", "muted": "-", "note": "*", "label": "墨色"},
    "sand": {"bar": " .:-~=+*#%@", "spark": " .:-~=+*#%@", "alert": "!", "muted": ":", "note": "*", "label": "沙色"},
    "moss": {"bar": " ─=", "spark": " ─=", "alert": "!", "muted": ".", "note": "*", "label": "苔绿"},
    "ocean": {"bar": " .:-=+*#%@", "spark": " .:-=+*#%@", "alert": "!", "muted": "·", "note": "*", "label": "海蓝"},
    "amber": {"bar": " .-+#", "spark": " .-+#", "alert": "!", "muted": "~", "note": "*", "label": "琥珀"},
    "coral": {"bar": " .oO@", "spark": " .oO@", "alert": "!", "muted": "-", "note": "*", "label": "珊瑚"},
    "violet": {"bar": " :*#", "spark": " :*#", "alert": "!", "muted": ":", "note": "*", "label": "紫罗兰"},
    "graphite": {"bar": " .:+=*#@", "spark": " .:+=*#@", "alert": "!", "muted": ".", "note": "*", "label": "石墨"},
    "frost": {"bar": " ▁▂▃▄▅▆▇█", "spark": " ▁▂▃▄▅▆▇█", "alert": "!", "muted": "·", "note": "*", "label": "霜白"},
    "ember": {"bar": " .:-~=+*#%@", "spark": " .:-~=+*#%@", "alert": "!", "muted": "~", "note": "*", "label": "余烬"},
    "pine": {"bar": " ─=", "spark": " ─=", "alert": "!", "muted": "-", "note": "*", "label": "松绿"},
    "steel": {"bar": " .:-=+*#%@", "spark": " .:-=+*#%@", "alert": "!", "muted": ":", "note": "*", "label": "钢灰"},
    "sepia": {"bar": " .-+#", "spark": " .-+#", "alert": "!", "muted": ".", "note": "*", "label": "棕褐"},
    "plum": {"bar": " .oO@", "spark": " .oO@", "alert": "!", "muted": "·", "note": "*", "label": "梅紫"},
    "lime": {"bar": " :*#", "spark": " :*#", "alert": "!", "muted": "~", "note": "*", "label": "青柠"},
    "clay": {"bar": " .:+=*#@", "spark": " .:+=*#@", "alert": "!", "muted": "-", "note": "*", "label": "陶土"},
    "rust": {"bar": " ▁▂▃▄▅▆▇█", "spark": " ▁▂▃▄▅▆▇█", "alert": "!", "muted": ":", "note": "*", "label": "铁锈"},
    "cobalt": {"bar": " .:-~=+*#%@", "spark": " .:-~=+*#%@", "alert": "!", "muted": ".", "note": "*", "label": "钴蓝"},
    "teal": {"bar": " ─=", "spark": " ─=", "alert": "!", "muted": "·", "note": "*", "label": "青碧"},
    "indigo": {"bar": " .:-=+*#%@", "spark": " .:-=+*#%@", "alert": "!", "muted": "~", "note": "*", "label": "靛蓝"},
    "mauve": {"bar": " .-+#", "spark": " .-+#", "alert": "!", "muted": "-", "note": "*", "label": "藕荷"},
    "olive": {"bar": " .oO@", "spark": " .oO@", "alert": "!", "muted": ":", "note": "*", "label": "橄榄"},
    "brick": {"bar": " :*#", "spark": " :*#", "alert": "!", "muted": ".", "note": "*", "label": "砖红"},
    "denim": {"bar": " .:+=*#@", "spark": " .:+=*#@", "alert": "!", "muted": "·", "note": "*", "label": "牛仔蓝"},
    "honey": {"bar": " ▁▂▃▄▅▆▇█", "spark": " ▁▂▃▄▅▆▇█", "alert": "!", "muted": "~", "note": "*", "label": "蜜黄"},
    "jade": {"bar": " .:-~=+*#%@", "spark": " .:-~=+*#%@", "alert": "!", "muted": "-", "note": "*", "label": "玉青"},
    "mint": {"bar": " ─=", "spark": " ─=", "alert": "!", "muted": ":", "note": "*", "label": "薄荷"},
    "sky": {"bar": " .:-=+*#%@", "spark": " .:-=+*#%@", "alert": "!", "muted": ".", "note": "*", "label": "天青"},
    "rose": {"bar": " .-+#", "spark": " .-+#", "alert": "!", "muted": "·", "note": "*", "label": "玫红"},
    "ash": {"bar": " .oO@", "spark": " .oO@", "alert": "!", "muted": "~", "note": "*", "label": "灰白"},
    "coal": {"bar": " :*#", "spark": " :*#", "alert": "!", "muted": "-", "note": "*", "label": "煤黑"},
    "linen": {"bar": " .:+=*#@", "spark": " .:+=*#@", "alert": "!", "muted": ":", "note": "*", "label": "亚麻"},
    "ivory": {"bar": " ▁▂▃▄▅▆▇█", "spark": " ▁▂▃▄▅▆▇█", "alert": "!", "muted": ".", "note": "*", "label": "象牙"},
    "charcoal": {"bar": " .:-~=+*#%@", "spark": " .:-~=+*#%@", "alert": "!", "muted": "·", "note": "*", "label": "炭笔"},
    "midnight": {"bar": " ─=", "spark": " ─=", "alert": "!", "muted": "~", "note": "*", "label": "午夜蓝"},
    "dawn": {"bar": " .:-=+*#%@", "spark": " .:-=+*#%@", "alert": "!", "muted": "-", "note": "*", "label": "晨光"},
}

_ALIASES = {
    "light": "paper",
    "dark": "carbon",
    "hi": "mono-hi",
    "blue": "ocean",
    "green": "moss",
    "gray": "steel",
    "grey": "steel",
}


def theme_names():
    """列出全部登记主题名（不含别名）。"""
    return sorted(THEMES)


def describe(name="default"):
    """返回主题的展示名与字段清单；未登记的名字回退 default。"""
    t = THEMES.get(_ALIASES.get(name, name), THEMES["default"])
    return {"name": name, "label": t["label"], "fields": sorted(t)}

# ---------------------------------------------------------------------------
# 主题样式对照（mkthemes.py 生成，供发布校验逐条核对；仅注释，运行时不用）
# ---------------------------------------------------------------------------
# default       .:-=+*#%@     默认
# mono          .-+#          单色
# paper         .oO@          纸白
# carbon        :*#           碳黑
# slate         .:+=*#@       石板
# ink           ▁▂▃▄▅▆▇█      墨色
# sand          .:-~=+*#%@    沙色
# moss          ─=            苔绿
# ocean         .oO0@         海蓝
# amber         ░▒▓█          琥珀
# coral         .:-=+*#%@     珊瑚
# violet        .-+#          紫罗兰
# 字符阶建议按视觉密度单调递增排列；终端不支持的字符会自动回退为 # 与 .
# 对照表仅供发布校验与排障使用，不参与任何渲染逻辑。
# 条目顺序与 THEMES 注册顺序一致；别名不在此表列出（见 _ALIASES）。
# graphite      .oO@          石墨
# frost         :*#           霜白
# ember         .:+=*#@       余烬
# pine          ▁▂▃▄▅▆▇█      松绿
# steel         .:-~=+*#%@    钢灰
# sepia         ─=            棕褐
# plum          .oO0@         梅紫
# lime          ░▒▓█          青柠
# clay          .:-=+*#%@     陶土
# rust          .-+#          铁锈
# cobalt        .oO@          钴蓝
# teal          :*#           青碧
# 字符阶建议按视觉密度单调递增排列；终端不支持的字符会自动回退为 # 与 .
# 对照表仅供发布校验与排障使用，不参与任何渲染逻辑。
# 条目顺序与 THEMES 注册顺序一致；别名不在此表列出（见 _ALIASES）。
# indigo        .:+=*#@       靛蓝
# mauve         ▁▂▃▄▅▆▇█      藕荷
# olive         .:-~=+*#%@    橄榄
# brick         ─=            砖红
# denim         .oO0@         牛仔蓝
# honey         ░▒▓█          蜜黄
# jade          .:-=+*#%@     玉青
# mint          .-+#          薄荷
# sky           .oO@          天青
# rose          :*#           玫红
# ash           .:+=*#@       灰白
# coal          ▁▂▃▄▅▆▇█      煤黑
# 字符阶建议按视觉密度单调递增排列；终端不支持的字符会自动回退为 # 与 .
# 对照表仅供发布校验与排障使用，不参与任何渲染逻辑。
# 条目顺序与 THEMES 注册顺序一致；别名不在此表列出（见 _ALIASES）。
# linen         .:-~=+*#%@    亚麻
# ivory         ─=            象牙
# charcoal      .oO0@         炭笔
# midnight      ░▒▓█          午夜蓝
# dawn          .:-=+*#%@     晨光
# dusk          .-+#          暮色
# vintage       .oO@          复古
# retro         :*#           复古·终端
# neon          .:+=*#@       霓虹
# pastel        ▁▂▃▄▅▆▇█      柔彩
# vivid         .:-~=+*#%@    鲜明
# subtle        ─=            含蓄
# 字符阶建议按视觉密度单调递增排列；终端不支持的字符会自动回退为 # 与 .
# 对照表仅供发布校验与排障使用，不参与任何渲染逻辑。
# 条目顺序与 THEMES 注册顺序一致；别名不在此表列出（见 _ALIASES）。
# bold          .oO0@         加粗
# compact       ░▒▓█          紧凑
# dense         .:-=+*#%@     密集
# outline       .-+#          线框
# amber-hi      .oO@          琥珀·高对比
# ocean-hi      :*#           海蓝·高对比
# mono-hi       .:+=*#@       单色·高对比
# paper-hi      ▁▂▃▄▅▆▇█      纸白·高对比
# carbon-hi     .:-~=+*#%@    碳黑·高对比
# night-hi      ─=            夜间·高对比
# console       .oO0@         控制台
# legacy        ░▒▓█          旧版
# 字符阶建议按视觉密度单调递增排列；终端不支持的字符会自动回退为 # 与 .
# 对照表仅供发布校验与排障使用，不参与任何渲染逻辑。
# 条目顺序与 THEMES 注册顺序一致；别名不在此表列出（见 _ALIASES）。
# ansi          .:-=+*#%@     ANSI
# xterm         .-+#          终端
# vt100         .oO@          VT100
# green-hi      :*#           绿屏·高对比
# amber-lo      .:+=*#@       琥珀·低对比
# ice           ▁▂▃▄▅▆▇█      冰蓝
# desert        .:-~=+*#%@    砂金
# forest        ─=            森绿
# canyon        .oO0@         峡谷
# lake          ░▒▓█          湖蓝
# storm         .:-=+*#%@     风暴
# mist          .-+#          薄雾
# 字符阶建议按视觉密度单调递增排列；终端不支持的字符会自动回退为 # 与 .
# 对照表仅供发布校验与排障使用，不参与任何渲染逻辑。
# 条目顺序与 THEMES 注册顺序一致；别名不在此表列出（见 _ALIASES）。
# blush         .oO@          绯色
# sage          :*#           鼠尾草
# wine          .:+=*#@       酒红
# navy          ▁▂▃▄▅▆▇█      藏青
# cream         .:-~=+*#%@    奶油
# stone         ─=            岩石
# mocha         .oO0@         摩卡
# lemon         ░▒▓█          柠檬
# aqua          .:-=+*#%@     水青
# salmon        .-+#          鲑粉
# plum-hi       .oO@          梅紫·高对比
# teal-hi       :*#           青碧·高对比
# 字符阶建议按视觉密度单调递增排列；终端不支持的字符会自动回退为 # 与 .
# 对照表仅供发布校验与排障使用，不参与任何渲染逻辑。
# 条目顺序与 THEMES 注册顺序一致；别名不在此表列出（见 _ALIASES）。
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
