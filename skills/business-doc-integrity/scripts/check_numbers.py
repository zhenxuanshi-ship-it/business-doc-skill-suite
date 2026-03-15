#!/usr/bin/env python3
import re
import sys
from collections import Counter

text = sys.stdin.read() if not sys.argv[1:] else ' '.join(sys.argv[1:])
nums = re.findall(r'\d+(?:\.\d+)?(?:万|亿|%|个月|天|人|台|套|个)?', text)
counts = Counter(nums)
for item, count in counts.most_common():
    if count >= 1:
        print(f'{item}\t{count}')
