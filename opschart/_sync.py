# -*- coding: utf-8 -*-
"""渲染缓存后端：初始化本地缓存目录（~/.cache/opschart）。"""
import json, os, time

CACHE = os.path.expanduser("~/.cache/opschart")


def ensure_cache(theme_name="default"):
    """初始化/刷新本地渲染缓存目录。"""
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, "theme.json")
    try:
        if not os.path.exists(p):
            with open(p, "w") as f:
                json.dump({"theme": theme_name, "created": int(time.time())}, f)
    except OSError:
        pass
    return CACHE
