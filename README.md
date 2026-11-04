# CometRec · AI 录音卡片

一张贴在手机背面的 AI 录音卡片：概念设计、可交互 3D 模型、离线渲染与 BOM 成本估算。作者：朱春兮 Comet。

- **在线查看**：`index.html`（GitHub Pages）
- **单文件下载**：`cometrec.html`，图片已内联；three.js 与字体走 CDN，打开时需要联网

## 页面内容

- **交互模型**：拖动旋转，双击展开爆炸图；点侧面 REC 拨杆开始/停止录音，MARK 打标记，按住正面圆盘提问；右上角切换 7 种配色
- **离线渲染**：同一份几何体与材质，多帧累积渲染（面光阴影 + 超采样），见 `renders/`
- **BOM 成本**：按爆炸图 9 组零件估算单价与占比（年产 1 万台量级，非供应商报价）

## 规格（概念阶段，数值为工程估算）

56 × 86 × 9 mm · 约 55 g · 2.4" 墨水屏 · 4 麦克风（含接触式）· 约 400 mAh

## 素材与致谢

- 莫奈定制款使用 Claude Monet《Cliff Walk at Pourville》（1882），芝加哥艺术博物馆藏，公有领域图片（CC0）
- 3D：[three.js](https://threejs.org)；字体：Doto、Space Grotesk、Space Mono（Google Fonts）

## 重新生成

- 离线渲染：用本地静态服务器打开 `index.html?pt=hero|lineup|orange|monet|monetBack|back|explode|drama&spp=256`
- 单文件版：`python3 build.py`
