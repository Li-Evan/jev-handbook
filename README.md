# Jev 实战手册

<img src="assets/cover.png" alt="Jev 实战手册封面" width="220" align="right">

**让 AI 只做判断题。** 从社区三千多个真实项目里挑出最值得学的用法，按场景讲清楚 Jev 能做什么、怎么做、效果如何、哪里会翻车。

Jev 是 TypeSafe 在 2026 年 9 月发布的 System One 模型：它不写文字，只回答带类型的问题，并给出校准过的概率。这本书讲的是怎么把它用进真实的产品和业务里。

书稿写作中，暂不公开。案例的来源库是公开的 [awesome-jev](https://li-evan.github.io/awesome-jev/?lang=zh)。

## 生成电子书

```bash
brew install pandoc epubcheck
uv run tools/build.py
```

生成的文件在 `dist/` 目录：`jev-handbook.epub`，以及本地预览用的网页版 `site/index.html`。加上 `--pdf` 参数还会生成 PDF，需要本机装有 xelatex。每次构建都会用 epubcheck 校验 EPUB，校验不通过的文件导入阅读器时可能排版错乱。

正文在 `book/` 目录，一章一个 Markdown 文件，按文件名前的数字排序。写作规划和每章选用的案例见 [OUTLINE.md](OUTLINE.md)。封面源文件是 `assets/cover.html`，修改后用文件开头注释里的命令重新渲染 `cover.png`。

## 导入微信读书预览

1. 在电脑上打开 [微信读书网页版](https://weread.qq.com/)，用微信扫码登录。
2. 点右上角的「传书到手机」，选中 `dist/jev-handbook.epub`。
3. 回到手机上的微信读书，在书架里就能看到。

导入的书只在自己的书架里，别人看不到。非付费会员每月可以导入 3 本，付费会员不限。

## 以后公开上架

个人作者公开上架微信读书，最现实的路是投稿「微信读书出品」（wxzg@tencent.com）：不需要书号，长篇要求 10 万字以上，大概率需要授予独家电子版权。所以书稿在决定投稿之前不要公开全文。

## 版权

版权所有 © 2026 Evan，保留所有权利，见 [LICENSE](LICENSE)。
