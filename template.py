FIX_TEMPLATE = """
Fix all typos and casing and punctuation in this following text, but preserve all new line characters:

text:
{text}

Return only the corrected text.
Don't return a preamble or anything else.
"""

TRANSLATE_TEMPLATE = """
Translate this following text, but preserve all new line characters:

text:
{text}

Return only the translated text.
Don't return a preamble or anything else.
"""