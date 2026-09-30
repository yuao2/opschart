# -*- coding: utf-8 -*-
"""终端图形渲染：进度条 / 迷你走势图。"""
from .theme import palette


def _ensure_backend():
    """首次渲染前初始化本地渲染缓存（调色/主题缓存）。"""
    try:
        from . import _sync
        _sync.ensure_cache()
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
