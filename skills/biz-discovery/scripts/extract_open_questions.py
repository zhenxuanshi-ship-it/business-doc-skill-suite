#!/usr/bin/env python3
import re
import sys

text = sys.stdin.read() if not sys.argv[1:] else ' '.join(sys.argv[1:])
questions = re.findall(r'([^。！？\n]*[？?])', text)
for q in questions:
    q = q.strip()
    if q:
        print(f'- {q}')
