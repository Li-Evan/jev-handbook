# Jev 实战手册

<img src="assets/cover.png" alt="Jev 实战手册封面" width="220" align="right">

**让 AI 只做判断题。** 从社区三千多个真实项目里挑出最值得学的用法，按场景讲清楚 Jev 能做什么、怎么做、效果如何、哪里会翻车。

Jev 是 TypeSafe 在 2026 年 9 月发布的 System One 模型：它不写文字，只回答带类型的问题，并给出校准过的概率。这本书讲的是怎么把它用进真实的产品和业务里。

书稿正在开源写作中，每次更新会自动生成新的电子书。

- 在线阅读：<https://li-evan.github.io/jev-handbook/>
- 下载 EPUB：<https://li-evan.github.io/jev-handbook/jev-handbook.epub>
- 全部案例的来源库：[awesome-jev](https://li-evan.github.io/awesome-jev/?lang=zh)

## 导入微信读书

1. 在电脑上下载 EPUB 文件。
2. 打开 [微信读书网页版](https://weread.qq.com/)，用微信扫码登录，点右上角的「传书到手机」，选中下载的 EPUB。
3. 回到手机上的微信读书，在书架里就能看到这本书。

导入的书只在你自己的书架里，别人看不到。按微信读书目前的规则，非付费会员每月可以导入 3 本，付费会员不限。

## 目录

第一部分 认识 Jev：Jev 是什么、三种问法、半小时跑通第一个请求。

第二部分 按场景看用法：金融与交易、编程 agent、浏览器与电脑操控、Agent 编排与路由、搜索与 RAG、安全与审核、数据与评测、客服与销售、电商营销与内容、实时交互、个人效率与更多行业。

第三部分 用好 Jev：设计模式、它不擅长什么、开源复刻与替代。

各章的写作进度和选用案例见 [OUTLINE.md](OUTLINE.md)。

## 自己生成电子书

```bash
brew install pandoc epubcheck
uv run tools/build.py
```

生成的文件在 `dist/` 目录：`jev-handbook.epub` 和在线阅读版 `site/index.html`。加上 `--pdf` 参数还会生成 PDF，需要本机装有 xelatex。

正文在 `book/` 目录，一章一个 Markdown 文件，按文件名前的数字排序。

## 参与

发现事实错误、链接失效，或者想推荐一个值得写进书里的案例，欢迎提 issue。

## 说明

本书由社区作者编写，与 TypeSafe 官方无关。Jev 的价格、限额和能力以 [官方文档](https://docs.typesafe.ai) 为准。

书稿以 [CC BY-NC-SA 4.0](LICENSE) 许可发布：可以自由转载和改编，但需要署名、不能用于商业用途，改编后的作品也要用同样的许可发布。
