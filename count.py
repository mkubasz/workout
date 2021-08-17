from typing import Dict
from re import sub
from collections import Counter


def count_words(sentence: str) -> Dict[str, int]:
    omitted_chars = '[¿?!,]'
    return Counter(sub(omitted_chars, '', sentence).lower().split(" "))
