#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian → Hexo 博客同步脚本
用法：
  python sync_obsidian.py          # 同步所有新文章
  python sync_obsidian.py --watch  # 持续监听，文件变化自动同步
"""

import os
import re
import sys
import shutil
import hashlib
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

# ============ 配置区 ============
OBSIDIAN_VAULT = r"C:\Users\lhrtxm\Desktop\Obsidian库"
BLOG_ROOT = r"D:\blog"
POSTS_DIR = os.path.join(BLOG_ROOT, "source", "_posts")
IMAGES_DIR = os.path.join(BLOG_ROOT, "source", "images")
SYNC_RECORD = os.path.join(BLOG_ROOT, ".obsidian-sync.json")  # 同步记录
# ================================


def ensure_dirs():
    """确保目标目录存在"""
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)


def load_sync_record():
    """加载同步记录（记录已同步文件的 hash）"""
    if os.path.exists(SYNC_RECORD):
        try:
            with open(SYNC_RECORD, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_sync_record(record):
    """保存同步记录"""
    with open(SYNC_RECORD, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)


def file_hash(filepath):
    """计算文件内容的 MD5"""
    h = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None


def slugify(filename):
    """把文件名转成适合 URL 的 slug（保留中文，处理空格）"""
    name = Path(filename).stem
    # 空格 → 连字符
    name = re.sub(r"\s+", "-", name)
    # 去掉不安全字符但保留中文
    name = re.sub(r"[<>:\"/\\|?*]", "", name)
    return name


def extract_title(filepath):
    """从文件名或内容提取标题"""
    title = Path(filepath).stem
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # 尝试从第一个 # 标题提取
        m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if m:
            title = m.group(1).strip()
    except Exception:
        pass
    return title


def generate_front_matter(title, tags=None, categories=None):
    """生成 Hexo Front-matter"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fm = "---\n"
    fm += f'title: "{title}"\n'
    fm += f"date: {now}\n"
    fm += "tags:\n"
    if tags:
        for t in tags:
            fm += f"  - {t}\n"
    else:
        fm += "  - 未分类\n"
    fm += "categories:\n"
    if categories:
        for c in categories:
            fm += f"  - {c}\n"
    fm += "---\n\n"
    return fm


def has_front_matter(content):
    """检查是否已有 Front-matter"""
    return content.strip().startswith("---")


def convert_obsidian_links(content, vault_path):
    """
    转换 Obsidian 特殊语法：
    1. ![[图片名.jpg]] → ![](/images/图片名.jpg)
    2. ![[图片名.jpg|宽度]] → ![](/images/图片名.jpg)
    3. [[笔记名]] → [笔记名](/posts/笔记名/)
    4. [[笔记名|显示名]] → [显示名](/posts/笔记名/)
    """
    # 处理嵌入图片 ![[xxx.png]] 或 ![[xxx.png|300]]
    def replace_embed(match):
        inner = match.group(1)
        if "|" in inner:
            parts = inner.split("|", 1)
            img_name = parts[0].strip()
        else:
            img_name = inner.strip()
        # 检查是否是图片
        if re.search(r"\.(png|jpg|jpeg|gif|svg|webp|bmp)$", img_name, re.IGNORECASE):
            return f"![](/images/{img_name})"
        return match.group(0)  # 非图片嵌入，保持原样

    content = re.sub(r"!\[\[([^\]]+)\]\]", replace_embed, content)

    # 处理内部链接 [[笔记名]] 或 [[笔记名|显示名]]
    def replace_link(match):
        inner = match.group(1)
        if "|" in inner:
            parts = inner.split("|", 1)
            note_name = parts[0].strip()
            display = parts[1].strip()
        else:
            note_name = inner.strip()
            display = note_name
        slug = slugify(note_name + ".md")
        return f"[{display}](/posts/{slug}/)"

    content = re.sub(r"(?<!\!)\[\[([^\]]+)\]\]", replace_link, content)

    return content


def copy_referenced_images(filepath, vault_path):
    """
    找到文章中 ![[xxx.jpg]] 引用的本地图片，
    从 Vault 中找到并复制到博客的 images 目录
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return

    # 匹配 ![[xxx.png]] 或 ![[xxx.png|宽度]]
    pattern = r"!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]"
    matches = re.findall(pattern, content)

    for img_name in matches:
        img_name = img_name.strip()
        if not re.search(r"\.(png|jpg|jpeg|gif|svg|webp|bmp)$", img_name, re.IGNORECASE):
            continue

        # 在 Vault 中搜索该图片
        for root, dirs, files in os.walk(vault_path):
            # 跳过 .obsidian 目录
            if ".obsidian" in root:
                continue
            if img_name in files:
                src = os.path.join(root, img_name)
                dst = os.path.join(IMAGES_DIR, img_name)
                if not os.path.exists(dst) or file_hash(src) != file_hash(dst):
                    try:
                        shutil.copy2(src, dst)
                        print(f"  [图片] 复制: {img_name}")
                    except Exception as e:
                        print(f"  [图片] 复制失败 {img_name}: {e}")
                break


def guess_categories(filepath, vault_path):
    """根据 Vault 中的子目录结构猜测分类"""
    rel = os.path.relpath(filepath, vault_path)
    parts = Path(rel).parts
    # 去掉文件名，取目录层级作为分类
    cats = [p for p in parts[:-1] if p and not p.startswith(".")]
    if not cats:
        return None
    return cats


def sync_file(filepath, vault_path, record):
    """同步单个 Markdown 文件"""
    h = file_hash(filepath)
    if not h:
        return False

    rel_path = os.path.relpath(filepath, vault_path)
    key = rel_path

    # 检查是否已同步且未变化
    if key in record and record[key].get("hash") == h:
        return False  # 未变化

    print(f"\n{'='*50}")
    print(f"同步: {rel_path}")

    # 读取内容
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"  读取失败: {e}")
        return False

    # 转换 Obsidian 语法
    content = convert_obsidian_links(content, vault_path)

    # 复制本地引用的图片
    copy_referenced_images(filepath, vault_path)

    # 生成 slug 文件名
    slug = slugify(rel_path)
    target_file = os.path.join(POSTS_DIR, slug + ".md")

    # 补 Front-matter（如果没有）
    if not has_front_matter(content):
        title = extract_title(filepath)
        categories = guess_categories(filepath, vault_path)
        fm = generate_front_matter(title, categories=categories)
        content = fm + content
    else:
        # 已有 front-matter，检查 tags/categories 是否完整
        if "tags:" not in content:
            content = re.sub(r"^---\n", "---\ntags:\n  - 未分类\n", content, count=1)

    # 写入目标文件
    try:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [完成] → {target_file}")
    except Exception as e:
        print(f"  写入失败: {e}")
        return False

    # 更新记录
    record[key] = {
        "hash": h,
        "target": target_file,
        "synced_at": datetime.now().isoformat(),
    }
    return True


def find_md_files(vault_path):
    """查找 Vault 中所有 .md 文件（排除 .obsidian 目录）"""
    md_files = []
    for root, dirs, files in os.walk(vault_path):
        # 排除 .obsidian 目录
        if ".obsidian" in dirs:
            dirs.remove(".obsidian")
        # 排除模板目录
        if "模板" in dirs:
            dirs.remove("模板")

        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(root, f))
    return md_files


def run_sync():
    """执行一次全量同步"""
    ensure_dirs()
    record = load_sync_record()
    md_files = find_md_files(OBSIDIAN_VAULT)

    if not md_files:
        print("未找到 Markdown 文件")
        return 0

    print(f"找到 {len(md_files)} 个 Markdown 文件")

    synced = 0
    for filepath in md_files:
        if sync_file(filepath, OBSIDIAN_VAULT, record):
            synced += 1

    save_sync_record(record)
    print(f"\n{'='*50}")
    print(f"同步完成: {synced} 个文件已更新")

    if synced > 0:
        print("\n提示: 运行以下命令预览博客:")
        print("  cd D:/blog && npx hexo server")

    return synced


def watch_sync(interval=5):
    """持续监听 Vault 变化，检测到变化自动同步"""
    print(f"开始监听 Obsidian Vault: {OBSIDIAN_VAULT}")
    print(f"检查间隔: {interval} 秒")
    print("按 Ctrl+C 停止\n")

    ensure_dirs()
    record = load_sync_record()

    while True:
        try:
            md_files = find_md_files(OBSIDIAN_VAULT)
            changed = False

            for filepath in md_files:
                if sync_file(filepath, OBSIDIAN_VAULT, record):
                    changed = True

            if changed:
                save_sync_record(record)

            time.sleep(interval)
        except KeyboardInterrupt:
            print("\n停止监听")
            save_sync_record(record)
            break


def main():
    parser = argparse.ArgumentParser(description="Obsidian → Hexo 博客同步工具")
    parser.add_argument("--watch", action="store_true", help="持续监听模式")
    parser.add_argument("--clean", action="store_true", help="清除同步记录")
    args = parser.parse_args()

    if args.clean:
        if os.path.exists(SYNC_RECORD):
            os.remove(SYNC_RECORD)
            print("已清除同步记录")
        return

    if args.watch:
        watch_sync()
    else:
        run_sync()


if __name__ == "__main__":
    main()
