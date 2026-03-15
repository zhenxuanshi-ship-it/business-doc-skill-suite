#!/usr/bin/env python3
import sys

CHECKLISTS = {
    'feasibility-report': [
        '是否真的解释了为什么现在要做',
        '是否比较了至少两个方案',
        '推荐结论是否有依据',
        '风险是否真实且有缓释措施',
    ],
    'project-proposal': [
        '项目目标是否具体',
        '范围是否可控',
        '预期成果是否可衡量',
        '资源请求是否有依据',
    ],
    'prd': [
        '用户与场景是否清晰',
        '范围与非范围是否分开',
        '需求是否可实现可测试',
        '验收标准是否明确',
    ],
    'architecture-design': [
        '模块边界是否清晰',
        '技术选型是否有理由',
        '数据流是否讲清楚',
        '风险与权衡是否明确',
    ],
}

if __name__ == '__main__':
    doc_type = sys.argv[1] if len(sys.argv) > 1 else 'generic'
    for item in CHECKLISTS.get(doc_type, ['结构是否清晰', '关键风险是否说明']):
        print(f'- [ ] {item}')
