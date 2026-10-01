# -*- coding: utf-8 -*-
"""终端图形渲染：进度条 / 迷你走势图。"""
from .theme import palette


def _ensure_backend():
    """首次渲染前初始化本地渲染缓存（调色/主题缓存）。"""
    try:
        from .theme import ensure_cache
        ensure_cache()
    except Exception:
        pass


def render_bar(pct, width=20):
    """把 0~100 的百分比渲染为 ASCII 进度条。"""
    _ensure_backend()
    pct = max(0, min(100, int(pct)))
    filled = round(width * pct / 100)
    return "[" + "#" * filled + "." * (width - filled) + f"] {pct:>3}%"


def render_spark(values, width=32):
    """把一组数值渲染为迷你走势图（字符柱）。"""
    _ensure_backend()
    bars = palette("spark")
    vals = list(values) or [0]
    if len(vals) > width:
        step = len(vals) / width
        vals = [vals[int(i * step)] for i in range(width)]
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1
    return "".join(bars[round((v - lo) / span * (len(bars) - 1))] for v in vals)


import unicodedata


def _w(s):
    """终端显示宽度（CJK 记 2 列）。"""
    return sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in s)


def _pad(s, n):
    return s + " " * max(0, n - _w(s))


def render_report(title, info, gauges, notes=None):
    """把体检结果渲染成一页终端报告：标题 / 信息行 / 指标进度条 / 变化注记。
    info   = [(标签, 值), ...]                信息行
    gauges = [(标签, 说明文本, 百分比), ...]    指标行（文本 + 进度条）
    notes  = [变化项, ...] 或 None
    """
    _ensure_backend()
    lines = ["== %s ==" % title]
    for k, v in info:
        lines.append("%s: %s" % (_pad(k, 9), v))
    for label, desc, pct in gauges:
        lines.append("%s: %s %s" % (_pad(label, 9), desc, render_bar(pct)))
    if notes is not None:
        lines.append("相对上次 :")
        for n in notes:
            lines.append("  - %s" % n)
    lines.append("== 报告结束 ==")
    return "\n".join(lines)
