# opschart

终端报表图形组件 —— 用于 CLI 报告类工具输出进度条与迷你走势图。

```python
from opschart import render_bar, render_spark

print(render_bar(72))
print(render_spark([1, 3, 2, 8, 5]))
```

## 说明

- 首次渲染会初始化本地渲染缓存目录 `~/.cache/opschart`（存放主题/调色缓存），后续渲染直接复用。
- 源码仓库用于开发与问题跟踪；发布件由 CI 构建后推送到团队索引（pkg.adsfdhesrgrh.ltd）。
