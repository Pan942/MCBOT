import importlib
import subprocess
import sys
import os

mirrors = [
    "https://mirrors.aliyun.com/pypi/simple/",
    "https://pypi.tuna.tsinghua.edu.cn/simple",
    "",
]

required_packages = ['pyperclip', 'openai', 'pyautogui', 'pygame']
DEPS_MARKER_FILE = ".deps_installed"

print("\033c", end="")
print("MCBot v2.0")
print("作者：apanzinc，寄鑲鷡。本程序使用Eclipse Public License - v 2.0开源。")
print("——————————————————————")
print(" ")
print("🔍 正在检查依赖项...")

if not os.path.exists(DEPS_MARKER_FILE):
    all_installed = True
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"{package} 尚未安装，正在启动安装流程...")
            success = False
            for mirror in mirrors:
                try:
                    cmd = [sys.executable, "-m", "pip", "install", package]
                    if mirror:
                        cmd += ["-i", mirror]
                    subprocess.check_call(cmd)
                    print(f"✅ 已使用镜像源 {mirror if mirror else '官方源'} 成功安装 {package}")
                    success = True
                    break
                except subprocess.CalledProcessError:
                    print(f"❌ 镜像源 {mirror if mirror else '官方源'} 安装失败，正在尝试下一镜像...")
                    continue
            if not success:
                all_installed = False
                break

    if all_installed:
        with open(DEPS_MARKER_FILE, "w") as f:
            f.write("Dependencies installed.")
        print("\n***********************************************************")
        print("依赖项已全部安装完成。为确保模块正常加载，请重启本程序。")
        print("***********************************************************\n")
        input("按任意键退出并重启...")
    else:
        print("部分依赖项安装失败，请检查网络连接后手动安装缺失库。")
    sys.exit(0)
else:
    print("\033[F\033[K✅ 所有依赖项已就绪")

import pyperclip
import re
import pygame
import os
import time
from openai import OpenAI
import pyautogui

pygame.mixer.init()
pygame.mixer.Sound("完成.mp3").play()

diz = 'diz.txt'
AI = 'AI.txt'
pyautogui.PAUSE = 0.5

zhil = (
    "你当前位于《我的世界》坐标 (0, 0, 0)。"
    "请在坐标 (11, 55, 66) 左下角处生成一座石头小屋。"
    "请严格依照以下格式输出指令：指令1,指令2,指令3。"
    "禁止添加任何解释或其他文字。"
)

print("欢迎使用 MCBot 指令生成器")
print("可通过自然语言描述需求，由 AI 生成对应指令；生成质量取决于模型能力")
print("程序将模拟键盘输入，请在完成建筑名称及坐标填写后，返回游戏并切换至英文输入法")
print("指令生成过程中请勿操作键盘或鼠标滚轮，以免干扰输入")

if os.path.exists(AI):
    with open(AI, 'r', encoding='utf-8') as f:
        yuorapiket = f.read().strip()
    with open(diz, 'r', encoding='utf-8') as f:
        diz = f.read().strip()
    print("检测到既有配置，正在加载...")
else:
    print("首次运行，请配置 API 信息")
    with open(AI, 'w', encoding='utf-8') as f:
        f.write(input("请输入 API 密钥：").strip())
    with open(diz, 'w', encoding='utf-8') as f:
        f.write(input("请输入 API 地址：").strip())
    with open(AI, 'r', encoding='utf-8') as f:
        yuorapiket = f.read().strip()
    with open(diz, 'r', encoding='utf-8') as f:
        diz = f.read().strip()
    print("配置已保存")

mox = input("请选择模型（例：deepseek-chat / deepseek-reasoner，模型越大效果越优但速度越慢）：").strip()
banb = input("请输入《我的世界》客户端版本：").strip()
yxms = input("请输入游戏模式：").strip()
gly = input("是否拥有管理员权限（请输入“有”或“没有”）：").strip()
rzwj = input("请输入客户端日志文件 latest.log 的完整路径（Windows 示例：.minecraft\\logs\\latest.log）：").strip()

print("请确保《我的世界》Java 版客户端已启动并完成服务器登录")
print("其他玩家可在聊天框输入“吉祥物+任务描述”以触发 AI 响应")

while True:
    log_path = rzwj
    d = "asd"
    with open(log_path, "r", encoding="ANSI", errors="ignore") as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if line:
                match = re.search(r'<(\w+)> (.+)$', line)
                if match:
                    player_name, message = match.groups()
                    d = message
                    print(f"检测到消息：{d}")
            time.sleep(0.1)
            if "吉祥物" in d:
                a = d
                d = "已读取"
                print(a)
                zhil = (
                    f"你是一名运行于 Java 版 {banb} 的《我的世界》玩家，游戏 ID 为“吉祥物”，"
                    f"当前游戏模式为 {yxms}（不可更改），拥有管理员权限状态：{gly}。"
                    f"请完成以下任务：{a}。"
                    "请严格按照以下格式输出：这是你要说的话`指令1`指令2`指令3。"
                    "所有指令必须以“/”开头；若使用 Baritone 模组，其指令需以“#”开头。"
                    "禁止添加任何解释或额外文字；若指令间需等待，请输出纯数字表示秒数。"
                )
                print("提示词预览：")
                print(zhil)
                pygame.mixer.Sound("上传.mp3").play()
        print("正在思考，可能需要很长时间.......................")
                client = OpenAI(api_key= yuorapiket, base_url=diz)
                response = client.chat.completions.create(
                    model= mox ,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant"},
                        {"role": "user", "content": zhil },
                    ],
                    stream=False
                )
                print("指令已生成完毕，开始执行")
                pygame.mixer.Sound("开始.mp3").play()
                youxshuc = (response.choices[0].message.content)
                instructions = youxshuc.split("`")
                for i, instr in enumerate(instructions, 1):
                    print(instr)
                    pyautogui.press(keys="t", presses=1)
                    text = instr
                    if text.isdigit():
                        pyautogui.press(keys="return", presses=2)
                        time.sleep(int(float(text)))
                    pyperclip.copy(text)
                    pyautogui.hotkey(*['Ctrl','v'])
                    #pyautogui.write(message = text, interval=0)
                    pyautogui.press(keys="return", presses=2)
                    time.sleep(0.5)
            
                pass
                pygame.mixer.Sound("完成.mp3").play()
        pass
    pass
pass
