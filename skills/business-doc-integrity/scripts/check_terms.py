#!/usr/bin/env python3
import re
import sys
from collections import Counter

text = sys.stdin.read() if not sys.argv[1:] else ' '.join(sys.argv[1:])
# crude extraction of repeated mixed Chinese/English capitalized-ish terms
patterns = re.findall(r'[A-Za-z][A-Za-z0-9_-]{2,}|[\u4e00-\u9fff]{2,8}', text)
counts = Counter(patterns)
for term, count in counts.most_common(40):
    if count >= 2:
        print(f'{term}\t{count}')
