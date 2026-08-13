#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path


def load_registry(index_path: Path | None = None) -> dict:
    """Load the modular 37-factor registry and return one normalized object.

    The index contains metadata plus `factor_files`. Each entry may be a path
    string or an object with `path`, `group`, and `count` metadata. Group files
    contain `group`, `count` (or `factor_count`), and `factors`.
    """
    index_path = Path(index_path) if index_path else (Path(__file__).resolve().parent.parent / 'references/factor-registry.json')
    index = json.loads(index_path.read_text(encoding='utf-8'))
    factors = []
    loaded_groups = []
    for entry in index.get('factor_files', []):
        if isinstance(entry, str):
            rel = entry
            expected_group = None
            expected_count = None
        elif isinstance(entry, dict):
            rel = entry['path']
            expected_group = entry.get('group')
            expected_count = entry.get('count')
        else:
            raise ValueError(f'Invalid factor_files entry: {entry!r}')

        path = index_path.parent / rel
        doc = json.loads(path.read_text(encoding='utf-8'))
        group = doc.get('group')
        group_factors = doc.get('factors', [])
        declared_count = doc.get('count', doc.get('factor_count'))

        if expected_group is not None and group != expected_group:
            raise ValueError(f'Group mismatch in {path}: {group!r} != {expected_group!r}')
        if expected_count is not None and len(group_factors) != expected_count:
            raise ValueError(f'Index count mismatch in {path}: {len(group_factors)} != {expected_count}')
        if declared_count is not None and len(group_factors) != declared_count:
            raise ValueError(f'Group count mismatch in {path}: {len(group_factors)} != {declared_count}')

        factors.extend(group_factors)
        loaded_groups.append({'path': rel, 'group': group, 'count': len(group_factors)})

    normalized = dict(index)
    normalized['factors'] = factors
    normalized['loaded_groups'] = loaded_groups
    return normalized


if __name__ == '__main__':
    data = load_registry()
    print(json.dumps({
        'model_name': data.get('model_name'),
        'factor_count': len(data['factors']),
        'group_counts': data.get('group_counts'),
        'loaded_groups': data.get('loaded_groups'),
    }, ensure_ascii=False, indent=2))
