#!/usr/bin/env python3
import sys

text = (' '.join(sys.argv[1:])).lower()

mapping = [
    ('scope', ['范围', 'scope', '边界']),
    ('logic', ['逻辑', '依据', '支撑', 'logic']),
    ('clarity', ['不清楚', '模糊', 'clarity', '明确']),
    ('inconsistency', ['不一致', '冲突', '矛盾', 'inconsistent']),
    ('risk gap', ['风险', 'mitigation', '缓释']),
    ('technical gap', ['技术', '架构', '接口', '性能']),
    ('delivery gap', ['里程碑', '排期', '交付', '资源']),
]

for label, keys in mapping:
    if any(k in text for k in keys):
        print(label)
        raise SystemExit(0)
print('general')
