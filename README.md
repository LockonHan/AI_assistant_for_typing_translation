# A self-hosted AI powered typing and translation assistant with the help of Ollama and LangChain

A script that can run in the background and listen to hotkeys, then uses a self-hosted Large Language Model to fix or translate the text.

It works on both Windows and macOS. It automatically detects which system it's running on.


## Get Started

### 1. Setup Ollama

Ollama Installation: https://github.com/ollama/ollama

Run `ollama run qwen:7b`

qwen:7b works well for this task, but feel free to try other models, too :)

### 2. Install dependencies
```
pip install pynput pyperclip langchain langchain_community python-dotenv pyautogui
```

### 3. Configure it
Configure .env to let it konw where and which LLM to communicate with
```
OLLAMA_ENDPOINT = "http://localhost:11434"
OLLAMA_MODEL = "qwen:7b"
```

### 4. Run it
Start the assistant:
```
python main.py
```

### 5. Hotkeys
Hotkeys you can then press:
```
- F8: Fixes the current selection
- F9: Fixes the current line (without having to select the text)
- F10: Fixes the current selection
- F11: translate the current line(without having to select the text)
- F12: translate the current selection
```


## Customize

Hotkeys, prompt, and Ollama config can be easily customized and extended in the code.

For example, here are some prompt templates you can try:

in template.py:

```

PROMPT_TEMPLATE_FIX_TEXT = Template(
    """Fix all typos and casing and punctuation in this text, but preserve all new line characters:

{text}

Return only the corrected text."""
)

PROMPT_TEMPLATE_GENERATE_TEXT = Template(
    """Generate a snarky paragraph with 3 sentences about the following topic:

{text}

Return only the corrected text."""
)

PROMPT_TEMPLATE_SUMMARIZE_TEXT = Template(
    """Summarize the following text in 3 sentences:

{text}

Return only the corrected text."""
)
```
