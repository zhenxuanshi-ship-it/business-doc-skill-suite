#!/usr/bin/env python3
import re
import sys
from pathlib import Path

DOC_TYPE_MAP = {
    'feasibility-report': 'feasibility-report',
    'project-proposal': 'project-proposal',
    'prd': 'prd',
    'architecture-design': 'architecture-design',
    'implementation-plan': 'implementation-plan',
    'executive-summary': 'executive-summary',
}

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'[^a-z0-9\-\u4e00-\u9fff]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text or 'document'

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: make_filename.py <doc-type> <topic>')
        sys.exit(1)
    doc_type = DOC_TYPE_MAP.get(sys.argv[1], sys.argv[1])
    topic = slugify(' '.join(sys.argv[2:]))
    print(f'{doc_type}-{topic}.md')
