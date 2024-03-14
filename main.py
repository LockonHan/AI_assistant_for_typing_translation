import sys
from pynput import keyboard
from AIAssistantBotForWin import AIAssistantBotForWin
from AIAssistantBotForMac import AIAssistantBotForMac

def get_os():
    if "darwin" in sys.platform:
        return "mac"
    elif "win" in sys.platform:
        return "win"
    else:
        return "unknown"


if __name__ == "__main__":

    if get_os() == 'win':
        bot = AIAssistantBotForWin()
    elif get_os() == 'mac':
        bot = AIAssistantBotForMac()
    else:
        print("This application currently does not support your operating system. Please stay tuned for updates.")
    "I love you so much."

    # 创建键盘监听器
    with keyboard.Listener(on_press=bot.handle_key_press) as listener:
        # 监听键盘事件，直到按下 esc 键退出
        listener.join()

    # 结束监听器
    listener.stop()
