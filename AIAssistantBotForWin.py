import time
import pyperclip
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from pynput import keyboard
from pynput.keyboard import Key, Controller
from dotenv import dotenv_values
import pyautogui
from template import FIX_TEMPLATE, TRANSLATE_TEMPLATE


class AIAssistantBotForWin:
    def __init__(self):
        self.env = dotenv_values('.env')
        self.prompt_fix = PromptTemplate.from_template(FIX_TEMPLATE)
        self.prompt_translate = PromptTemplate.from_template(TRANSLATE_TEMPLATE)
        self.ollama_endpoint = self.env.get("OLLAMA_ENDPOINT", "http://localhost:11434")
        self.ollama_model = self.env.get("OLLAMA_MODEL", "qwen:7b")
        self.model = Ollama(base_url=self.ollama_endpoint, model=self.ollama_model)
        self.parser = StrOutputParser()
        self.fix_text_chain = {"text": RunnablePassthrough()} | self.prompt_fix | self.model | self.parser
        self.translate_text_chain = {"text": RunnablePassthrough()} | self.prompt_translate | self.model | self.parser
        self.controller = Controller()
        print(f"AI Assistant For Win is ready!\n"
              f"Ollama run {self.ollama_model}\nOllama endpoint: {self.ollama_endpoint}\n"
              f"F8 to quit\nF9 to fix current line\nF10 to fix selection\n"
              f"F11 to translate current line\nF12 to translate selection\n")

    def fix_text(self, text):
        return self.fix_text_chain.invoke(text)

    def translate_text(self, text):
        return self.translate_text_chain.invoke(text)

    def fix_selection(self):
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.3)
        text = pyperclip.paste()
        if not text:
            print("No text in clipboard")
            return
        fixed_text = self.fix_text(text)
        if not fixed_text:
            return
        pyperclip.copy(fixed_text)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyperclip.copy('')

    def translate_selection(self):
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.3)
        text = pyperclip.paste()
        if not text:
            print("No text in clipboard")
            return
        fixed_text = self.translate_text(text)
        if not fixed_text:
            return
        pyperclip.copy(fixed_text)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyperclip.copy('')

    def fix_current_line(self):
        self.controller.press(Key.shift)
        self.controller.press(Key.home)

        self.controller.release(Key.shift)
        self.controller.release(Key.home)
        self.fix_selection()

    def translate_current_line(self):
        self.controller.press(Key.shift)
        self.controller.press(Key.home)

        self.controller.release(Key.shift)
        self.controller.release(Key.home)
        self.translate_selection()

    def handle_key_press(self, key):
        try:
            if key == keyboard.Key.f9:
                self.fix_current_line()
            elif key == keyboard.Key.f10:
                self.fix_selection()
            elif key == keyboard.Key.f11:
                self.translate_current_line()
            elif key == keyboard.Key.f12:
                self.translate_selection()
            elif key == keyboard.Key.f8:
                return False
        except AttributeError:
            pass
        return True


if __name__ == "__main__":
    # for test the basic function
    bot = AIAssistantBotForWin()
    pre_text = "Pythoon iss soo ccool"
    print(bot.fix_text(pre_text))
    pre_text = "今天天气很不错"
    print(bot.translate_text(pre_text))
