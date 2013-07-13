#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import zenhan

PAREN = re.compile(ur'\(.*\)', re.UNICODE)
PAREN2 = re.compile(ur'\（.*\）', re.UNICODE)

SPECIAL_SYMBOLS = (
    re.compile(ur'\*', re.UNICODE),
    re.compile(ur'\u30fb', re.UNICODE),
    re.compile(ur'[\u2000-\u206F]', re.UNICODE),  # punctuation
    re.compile(ur'[\u2500-\u257f]', re.UNICODE),  # box drawing
    re.compile(ur'[\u25a0-\u25ff]', re.UNICODE),  # geometric shapes
    re.compile(ur'[\u2600-\u26ff]', re.UNICODE),  # miscellaneous symbols
    re.compile(ur'[\u3000-\u303f]', re.UNICODE),  # cjk symbols and punctuation
    re.compile(ur'[\uff00-\uffef]', re.UNICODE),  # halfwidth and fullwdith forms
)

def normalize(ingredient):
    ingredient = ingredient.strip()

    ingredient = PAREN.sub(lambda s: '', ingredient)
    ingredient = PAREN2.sub(lambda s: '', ingredient)

    ingredient = zenhan.h2z(ingredient, mode=4)

    for SPECIAL_SYMBOL in SPECIAL_SYMBOLS:
        ingredient = SPECIAL_SYMBOL.sub(lambda s: '', ingredient)

    return ingredient
