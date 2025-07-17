import importlib
import subprocess
import sys
import os
mirrors = [
    "https://mirrors.aliyun.com/pypi/simple/",
    "https://pypi.tuna.tsinghua.edu.cn/simple", 
    "",
]
# 依赖列表
required_packages = ['pyperclip', 'openai', 'pyautogui', 'pygame']
DEPS_MARKER_FILE = ".deps_installed"

#——————————————————————————————

print("\033c", end="")
print("MCBot v2.5.0")
print("作者：寄鑲鷡，开发帮助：apanzinc，和热爱mc的大家，本程序允许自由分发改版")
print("——————————————————————") 
print(" ") 
print("🔍让我康康你的python的库发育得正不正常啊") 


# 如果标记文件存在，说明已经安装过依赖，跳过安装步骤
if not os.path.exists(DEPS_MARKER_FILE):

    all_installed = True  # 新增标志位，表示是否所有依赖都安装成功
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"{package} 没有库？开装！...")
            success = False
            for mirror in mirrors:
                try:
                    cmd = [sys.executable, "-m", "pip", "install", package]
                    if mirror:
                        cmd += ["-i", mirror]
                    subprocess.check_call(cmd)
                    print(f"✅ {package} 安装那可太成功了（使用镜像源：{mirror if mirror else '官方源'}）")
                    success = True
                    break
                except subprocess.CalledProcessError as e:
                    print(f"❌ 使用镜像源 {mirror if mirror else '官方源'} 安装 {package} 失败，正在尝试下一个镜像...")
                    continue
            if not success:
                all_installed = False
                break  # 安装失败，跳出循环

    if all_installed:
        # 所有依赖处理完毕后提示重启，并创建标记文件
        with open(DEPS_MARKER_FILE, "w") as f:
            f.write("Dependencies installed.")
        print("\n***********************************************************")
        print("所有库已安装完成！你的py的库现在正常了，为了确保模块正常加载，请重新启动程序。")
        print("***********************************************************\n")
        input("按任意键退出并重启程序...")
    else:
        print("无法安装部分依赖，请手动安装，还有你的网线！")

    sys.exit(0)
else:
    print("\033[F\033[K✅所有依赖已安装")



import pyperclip
import re
import pygame
pygame.mixer.init()
import os
import subprocess
import time
from openai import OpenAI
import pyautogui


pygame.mixer.Sound("完成.mp3").play()
diz = 'diz.txt'
AI = 'AI.txt'
pyautogui.PAUSE = 0.5
a = "石头小屋"
x = 11
y = 64
z = 11
zhil = "你现在是一个我的世界坐标位于0，0，0的玩家，现在有个人想要你在坐标11，55，66为左下角的位置生成一个石头小屋，请你把输出的指令通过以下格式发送给我：指令1，指令2，指令3 。以此类推。不能增加任何的解释以及其他文字只能存在指令"
print("欢迎使用MC指令BOT")
print("你可以用自然语言让它完成一些指令，但完成得怎么样取决于它的想象")
print("本程序通过操控键盘完成指令输入，请在完成输入建筑名称和坐标后，返回游戏并切换英语输入法，在生成过程中请勿使用键盘和鼠标滚轮")
if os.path.exists(AI):
    # 文件存在则读取内容
    with open(AI, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(diz, 'r', encoding='utf-8') as f:
        cooo = f.read()
    print("配置已存在，加载中：")
    yuorapiket = content
    diz = cooo
    print(content)
else:
    # 文件不存在则创建并写入初始内容
    print("你已经完成了安装库的前提条件了，现在需要你输入你的api地址和密钥")
    with open(AI, 'w', encoding='utf-8') as f:
        f.write(input("请输入你的API的密钥:"))
    with open(diz, 'w', encoding='utf-8') as f:
        f.write(input("请输入你的API的地址:"))
    with open(AI, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(diz, 'r', encoding='utf-8') as f:
        cooo = f.read()
    print("配置已存在，加载中：")
    yuorapiket = content
    diz = cooo
    print(content)  
    print(cooo)  
    print(f"文件 {AI} 已创建")
mox= (input("请选择模型(请输入比如deepseek-chat或deepseek-reasoner,提示：模型越小速度越快质量越差，模型越大反之)："))
banb = (input("当前我的世界客户端版本)："))
yxms = (input("玩家游戏模式)："))
gly = (input("是否有管理员权限(必须输入‘有’或者‘没有’)："))
rzwj = (input("请输入我的世界客户端日志文件latest.log,windows的我的世界日志文件路径示例为.minecraft\logs\latest.log："))
print("现在请确保我的世界JAVA版客户端已启动，并进入游戏再加入服务器，其他服务器玩家可以通过游戏聊天框输入：吉祥物+要求的任务。来让ai工作")
while True:
    log_path =f"{rzwj}"# 替换为实际路径
    d = "asd" # 初始化变量a
    with open(log_path, "r", encoding="ANSI", errors="ignore") as file:
        file.seek(0, 2)  # 跳到文件末尾
        while True:
            line = file.readline()
            if line:
                # 使用正则匹配玩家消息（格式：[时间] [线程] [INFO]: <玩家名> 消息）
                match = re.search(r'<(\w+)> (.+)$', line)
                if match:
                    player_name = match.group(1)
                    message = match.group(2)
                    d = message  # 保存到变量a
                    print(f"检测到消息: {d}")  # 可选：打印消息
            time.sleep(0.1)  # 避免CPU占用过高 
            if (d.find("吉祥物")!=-1):
                a = d
                d = "读取完了"
                print(a)
                
                zhil = (
                    f"你现在是一个Java版{banb}我的世界的玩家名叫吉祥物，游戏模式为{yxms}，游戏模式不可以更改，你{gly}管理员权限，现在你需要完成{a}，"
                    "请你把输出的指令通过以下格式发送给我：指令1`指令2`指令3 。每个指令前都要加/，以此类推。并且你的客户端安装了baritone模组，你可以使用baritone的指令，但使用baritone指令时baritone指令前要加#，当没有管理员权限时你不能使用原版指令，"
                    "不要添加任何解释或其他文字，只输出指令,在开始输入指令前你需要向其他玩家说话，说话不需要输入/say指令，你需要按照这个格式:这是你要说的话`指令1`指令2`指令3。如果两条指令之间需要时间等待，可以输出不带/和#的纯数字，单位为秒，比如等待10秒，就输出10,等待一分钟就输出60"
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
