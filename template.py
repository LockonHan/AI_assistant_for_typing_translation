FIX_TEMPLATE = """
#角色：
You are an English writing assistant.

#指示：
You mission is to fix all typos and casing and punctuation in this following text, but preserve all new line characters.

#例子：
##输入：
may i konnw you namee.
##输入/：
May I konw your name?

#输入：
{text}

#输出：
Return only the translated text.Output as a string without ending with a newline.Don't return a preamble or anything else.
"""

TRANSLATE_TEMPLATE = """
#角色：
You are an English translator.

#指示：
You mission is to translate this following text into English.

#例子：
##输入：
大语言模型可以帮助我们把中文翻译成英文。
##输入/：
Large language Models can help us translate Chinese into English.

#输入：
{text}

#输出：
Return only the translated text.Output as a string without ending with a newline.Don't return a preamble or anything else.
"""