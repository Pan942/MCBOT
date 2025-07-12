# Minecraft Bot v1.0
# 作者: apanzinc

# —————————————————配置列表——————————————————
# 镜像源列表
mirrors = [
    "https://mirrors.aliyun.com/pypi/simple/",
    "https://pypi.tuna.tsinghua.edu.cn/simple",
    ""
]

# 依赖库列表，程序需要的第三方库
required_packages = ['pyperclip', 'openai', 'pyautogui', 'pygame']

# 初始化
import importlib  # 用于动态导入模块
import subprocess  # 用于执行系统命令
import sys  # 用于获取 Python 解释器路径
import os  # 用于文件和目录操作

# 全局变量初始化
a = ""
x = ""
y = ""
z = ""
zhil = ""
mox = "mox.txt"  # ✅ 修复：指定模型名称保存的文件路径

# 配置文件名
diz_file = 'diz.txt'
api_key_file = 'AI.txt'

# 清屏并打印程序信息
print("\033c", end="")
print("𝕄𝕚𝕟𝕖𝕔𝕣𝕒𝕗𝕥𝔹𝕠𝕥 v1.0")
print("作者:apanzinc")
print("—————————————————————")
print("")
print("🔍正在检查必要的运行库")

# 检查依赖是否已经安装
DEPS_MARKER_FILE = ".deps_installed"

if not os.path.exists(DEPS_MARKER_FILE):
    all_installed = True  # 表示是否所有依赖都安装成功

    # 遍历依赖列表，检查是否已安装
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"\033[F\033[K❓缺少{package}库，正在尝试安装...")
            success = False
            # 尝试使用不同的镜像安装依赖
            for mirror in mirrors:
                try:
                    cmd = [sys.executable, "-m", "pip", "install", package]
                    if mirror:
                        cmd += ["-i", mirror]
                    subprocess.check_call(cmd)
                    print(f"✅ {package} 安装成功（使用镜像源：{mirror if mirror else '官方源'}）")
                    success = True
                    break
                except subprocess.CalledProcessError as e:
                    print(f"❌ 使用镜像源 {mirror if mirror else '官方源'} 安装 {package} 失败，正在尝试下一个镜像...")
                    continue
            if not success:
                all_installed = False
                break  # 安装失败，跳出循环

    if all_installed:
        # 所有依赖安装完成后创建标记文件，并提示用户重启程序
        with open(DEPS_MARKER_FILE, "w") as f:
            f.write("Dependencies installed.")
        print("\n" + "=" * 60)
        print("✅ 所有依赖库已成功安装！Python环境已恢复正常")
        print("⚠️ 重要提示：请重启程序以确保所有模块正确加载")
        print("=" * 60 + "\n")
        input("按任意键退出程序...")
    else:
        print("❌无法安装部分依赖，请检查网络或手动安装")

    sys.exit(0)
else:
    print("\033[F\033[K✅所有依赖已安装")

# 导入已安装的模块
from openai import OpenAI
import subprocess
import pyautogui
import pyperclip
import pygame
import time

pygame.mixer.init()

print("\033c", end="")
print("𝕄𝕚𝕟𝕖𝕔𝕣𝕒𝕗𝕥𝔹𝕠𝕥 v1.0")
print("作者:apanzinc")
print("—————————————————————")
print("")

# 设置 pyautogui 的按键间隔
pyautogui.PAUSE = 1

# 加载或创建 API 配置
yuorapiket = ""
diz = ""

# 在首次配置或加载配置时正确读取 mox.txt 内容
if os.path.exists(api_key_file):
    with open(api_key_file, 'r', encoding='utf-8') as f:
        yuorapiket = f.read()
    with open(diz_file, 'r', encoding='utf-8') as f:
        diz = f.read()
    with open(mox, 'r', encoding='utf-8') as f:
        mox_model = f.read().strip()  # ✅ 从 mox.txt 中读取模型名
else:
    print("欢迎！请先配置你的AI。")
    diz_input = input("请输入你的API的地址:")
    key_input = input("请输入你的API的密钥:")
    model_input = input("请输入你的模型名称:")  # 例如输入 gpt-4o

    with open(diz_file, 'w', encoding='utf-8') as f:
        f.write(diz_input)
    with open(api_key_file, 'w', encoding='utf-8') as f:
        f.write(key_input)
    with open(mox, 'w', encoding='utf-8') as f:
        f.write(model_input)

    # 加载写入的内容
    with open(diz_file, 'r', encoding='utf-8') as f:
        diz = f.read()
    with open(api_key_file, 'r', encoding='utf-8') as f:
        yuorapiket = f.read()
    with open(mox, 'r', encoding='utf-8') as f:
        mox_model = f.read().strip()

    print("加载中....")
    print(yuorapiket)
    print(diz)
    print(f"模型名称: {mox_model}")
    print(f"文件 {api_key_file} 已创建")

print("\033c", end="")
print("𝕄𝕚𝕟𝕖𝕔𝕣𝕒𝕗𝕥𝔹𝕠𝕥 v1.0")
print("作者:apanzinc")
print("—————————————————————")
print("")

# 用户输入模型和 Minecraft 版本
banb = input("当前我的世界客户端版本):")

print("\033c", end="")
print("𝕄𝕚𝕟𝕖𝕔𝕣𝕒𝕗𝔱𝔹𝕠𝕥 v1.0")
print("作者:apanzinc")
print("—————————————————————")
print("")
# 提示用户确保 Minecraft 已启动
print("操作前准备：")
print("1. 启动游戏客户端")
print("2. 进入目标游戏世界")
print("3. 确认当前玩家拥有OP权限（管理员权限）")

# 主循环，用户输入指令并执行
while True:
    print("\n【建筑指令输入】")
    a = input("请输入建造指令（例如：建造一个现代别墅/生成10只羊）：")
    print("\n【基准坐标设置】（以建筑左下角为基准点）")
    x = input("X 轴坐标（东西方向）：")
    y = input("Y 轴坐标（垂直高度）：")
    z = input("Z 轴坐标（南北方向）：")

    print(a)
    print(x)
    print(y)
    print(z)

    if input("是这个吗请输入y，如果不对请输入n:") == "y":
        zuob = f"x坐标为{x}, y坐标为{y}, z坐标为{z}"
        zhil = (
            f"你现在是一个Java版{banb}我的世界坐标位于0,0,0的玩家，现在有个人想要你在坐标{zuob}为左下角的位置{a}，请你把输出的指令通过以下格式发送给我：/指令1`/指令2`/指令3（以此类推），不要添加任何解释或其他文字，只输出指令。"
        )
        print("正在思考，可能需要很长时间.......................")

        # 创建 OpenAI 客户端并发送请求
        client = OpenAI(api_key=yuorapiket, base_url=diz)
        response = client.chat.completions.create(
        model=mox_model,  # ✅ 使用的是文件中的模型名，而不是文件名
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": zhil},
        ],
        stream=False
)

        # 解析并执行返回的指令
        youxshuc = response.choices[0].message.content
        instructions = youxshuc.split("`")
        for i, instr in enumerate(instructions, 1):
            pyautogui.press(keys="t", presses=1)
            text = instr
            pyautogui.write(message=text, interval=0)
            pyautogui.press(keys="return", presses=2)
            time.sleep(0.5)
            print(instr)

        # 播放完成提示音
        pygame.mixer.Sound("完成.mp3").play()
