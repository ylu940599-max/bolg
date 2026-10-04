---
title: "安装 Hexo 框架"
date: 2026-10-03 17:49:04
tags:
  - 未分类
categories:
---

  `Hexo` 是一个基于 `Node.js` 的框架，所以使用这个框架的条件就是要有 `Node.js` ，与此同时为了方便框架的安装与生成，还需要安装一个从 GitHub 上拉源码的工具 `Git`，所以一共需要这么几个工具：

> - **[Node.js](https://nodejs.org/en/download)**：一个 JavaScript 引擎，Hexo 框架的基础
> - **[Git](https://git-scm.com/)**：GitHub 配套工具
> - **[VSCode](https://code.visualstudio.com/docs/setup/windows)**：方便对博客源码进行编辑

# 安装 Hexo 框架

首先，需要更换 `Node.js` 的包管理器 `npm` 是国内源

 ```bash
 npm config set registry https://registry.npmmirror.com
 ```

安装 Hexo 的前提是已经完成了 Node.js 框架的安装，现在打开 [Hexo](https://hexo.io/) 官网

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E5%AE%89%E8%A3%85-Hexo-%E6%A1%86%E6%9E%B6-1.png)

复制里面的命令进行安装

```bash
npm install hexo-cli -g
```

终端中显示如下界面即安装完成

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E5%AE%89%E8%A3%85-Hexo-%E6%A1%86%E6%9E%B6-2.png)

# 生成 Hexo 初始博客

在生成之前确保你的 `Git` 工具已经完成安装，执行以下命令开始创建你的博客文件夹：

**格式：**

```bash
hexo init <你的博客文件夹名称>
```

**示例：**

```bash
hexo init blog
```

主要执行过程是从 Hexo 官方源码仓库将博客模板 clone 下来并且生成你的博客，生成完成是这样的界面

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E7%94%9F%E6%88%90-Hexo-%E5%88%9D%E5%A7%8B%E5%8D%9A%E5%AE%A2-1.png)

现在已经可以在你的资源管理器中看到这个博客目录了

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E7%94%9F%E6%88%90-Hexo-%E5%88%9D%E5%A7%8B%E5%8D%9A%E5%AE%A2-2.png)

# 选择并安装你喜欢的主题

打开 **[Hexo 主题页面](https://hexo.io/themes/)** ，选择自己喜欢的主题

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E4%BD%A0%E5%96%9C%E6%AC%A2%E7%9A%84%E4%B8%BB%E9%A2%98-1.png)

我这里因为是做演示的关系，所以我就随便选择一个 **[主题](https://github.com/EvanNotFound/hexo-theme-redefine)**

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E4%BD%A0%E5%96%9C%E6%AC%A2%E7%9A%84%E4%B8%BB%E9%A2%98-2.png)

# 安装主题

打开会是一个项目仓库

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E4%BD%A0%E5%96%9C%E6%AC%A2%E7%9A%84%E4%B8%BB%E9%A2%98-3.png)

去项目说明书中找到这个主题的安装方式

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%80%89%E6%8B%A9%E5%B9%B6%E5%AE%89%E8%A3%85%E4%BD%A0%E5%96%9C%E6%AC%A2%E7%9A%84%E4%B8%BB%E9%A2%98-4.png)

里面写了两种安装方式，分别是使用 `npm` 管理器进行安装，和自行下载源码修改两种方式，我就选择 `npm` 包管理器安装

**进入目录：**

```bash
cd blog
```

**安装：**

```bash
npm install hexo-theme-redefine@latest
```

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E5%AE%89%E8%A3%85%E4%B8%BB%E9%A2%98-1.png)

**更改配置文件：**

使用 vi 编辑器打开 `_config.yml` 文件

```bash
vi _config.yml
```

找到主题相关配置

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E5%AE%89%E8%A3%85%E4%B8%BB%E9%A2%98-2.png)

改成这样

```bash
theme: redefine
```

**启动查看效果：**

生成：

```bash
hexo g
```

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E5%AE%89%E8%A3%85%E4%B8%BB%E9%A2%98-3.png)

预览：

```bash
hexo s
```

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E5%AE%89%E8%A3%85%E4%B8%BB%E9%A2%98-4.png)

# 配置个人博客

文章的 front formatter

作者名称

博客标题

友链链接

这些都可以去 GitHub 作者的 README 上去找，这些配置就不过多赘述了……

# 部署

首先先新建你自己博客的仓库

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2-1.png)

上传到 GitHub，首先需要初始化你的仓库

```bash
git init
```

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2-2.png)

设置你的远程仓库地址

```bash
git remote add origin https://github.com/xxx/xxx.git
```

设置分支名称

```bash
git branch -M main
```

设置提交用户名称和邮箱，都按照你的 GitHub 中信息填写

```bash
git config --global user.name "xxxx"
git config --global user.email "xxxx@ivoinkwell.xyz"
```

现在可以去 VSCode 看看

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2-3.png)

这个时候会出现一个仓库，下方全部是更改，添加的文件，根据下图填写后进行提交即可

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2-4.png)

确保仓库里面有你的博客内容

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2-5.png)

# 部署到 Cloudflare 全球 CDN 节点

打开你的 Cloudflare 控制面板，找到 Workers 和Pages

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2%E5%88%B0-Cloudflare-%E5%85%A8%E7%90%83-CDN-%E8%8A%82%E7%82%B9-1.png)

点击创建

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2%E5%88%B0-Cloudflare-%E5%85%A8%E7%90%83-CDN-%E8%8A%82%E7%82%B9-2.png)

按照图中选择，创建 Pages

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2%E5%88%B0-Cloudflare-%E5%85%A8%E7%90%83-CDN-%E8%8A%82%E7%82%B9-3.png)

选择这个，连接你的 GitHub 账号

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2%E5%88%B0-Cloudflare-%E5%85%A8%E7%90%83-CDN-%E8%8A%82%E7%82%B9-4.png)

选择你的博客仓库

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2%E5%88%B0-Cloudflare-%E5%85%A8%E7%90%83-CDN-%E8%8A%82%E7%82%B9-5.png)

构建命令输入：`npm install -g hexo; hexo clean; hexo generate`

输出目录选择：`public`

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2%E5%88%B0-Cloudflare-%E5%85%A8%E7%90%83-CDN-%E8%8A%82%E7%82%B9-6.png)

保存构建之后连接你的域名，绑定后界面就和我的一样了

![](https://cdn.jsdelivr.net/gh/ivoinkwell/share-img@main/%E4%BD%BF%E7%94%A8%20Hexo%20%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E4%BD%BF%E7%94%A8-Hexo-%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-%E9%83%A8%E7%BD%B2%E5%88%B0-Cloudflare-%E5%85%A8%E7%90%83-CDN-%E8%8A%82%E7%82%B9-7.png)

之后正常访问网页即可