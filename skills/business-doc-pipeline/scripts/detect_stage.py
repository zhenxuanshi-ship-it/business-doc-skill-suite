#!/usr/bin/env python3
import re
import sys

text = ' '.join(sys.argv[1:]).lower()

rules = [
    ('finalize', [r'定稿', r'最终版', r'final version', r'finalize']),
    ('revise', [r'修改', r'修订', r'评审意见', r'comments', r'revise']),
    ('review', [r'review', r'评审', r'审一下', r'critique', r'challenge']),
    ('blueprint', [r'大纲', r'结构', r'outline', r'structure']),
    ('draft', [r'写', r'生成', r'draft', r'write']),
]

for stage, patterns in rules:
    for p in patterns:
        if re.search(p, text):
            print(stage)
            raise SystemExit(0)

print('discovery')
