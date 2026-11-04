# -*- coding: utf-8 -*-
"""生成可下载的单文件版 cometrec.html：把 renders/ 里的渲染图内联成 base64。
three.js 与字体仍从 CDN 加载，打开时需要联网。用法：python3 build.py"""
import base64, os, re
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'index.html'), encoding='utf-8').read()
def inline(m):
    data = open(os.path.join(here, m.group(1)), 'rb').read()
    return 'src="data:image/jpeg;base64,' + base64.b64encode(data).decode() + '"'
s = re.sub(r'src="(renders/[^"]+\.jpg)"', inline, s)
# 莫奈原画（JS 与色块 CSS 里都引用）
monet = 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(here, 'assets/monet.jpg'), 'rb').read()).decode()
s = s.replace('<script src="assets/monet.js"></script>', '<script>window.MONET_SRC = ' + repr(monet) + ';</script>')
s = s.replace('assets/monet.jpg', monet)
chip = 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(here, 'assets/monet-chip.jpg'), 'rb').read()).decode()
s = s.replace('assets/monet-chip.jpg', chip)
# 单文件版里不再显示“下载”按钮
s = s.replace('<a class="pill" id="dlBtn" href="cometrec.html" download>下载离线版 HTML</a>', '')
open(os.path.join(here, 'cometrec.html'), 'w', encoding='utf-8').write(s)
print('cometrec.html', round(len(s) / 1024), 'KB')
