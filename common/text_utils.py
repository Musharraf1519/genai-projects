# common/text_utils.py
# Small utilities for text normalization, tokenization, etc.

import re

def normalize_whitespace(s: str) -> str:
    return re.sub(r'\s+', ' ', s).strip()
