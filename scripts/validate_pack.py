#!/usr/bin/env python3
"""Validate VÉRTICE content pack metadata without executing any content."""
from pathlib import Path
import hashlib, json, sys
ROOT = Path(__file__).resolve().parents[1]
errors=[]
def load(rel):
    try: return json.loads((ROOT/rel).read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'{rel}: JSON inválido ou ausente ({e})'); return {}
blocks=load('data/blocks.json').get('blocks', [])
items=load('data/items.json').get('items', [])
biomes=load('data/biomes.json').get('biomes', [])
recipes=load('data/recipes.json').get('recipes', [])
registry=load('data/asset_registry.json').get('assets', [])
for label, values in [('block', blocks),('item',items),('biome',biomes)]:
    ids=[v.get('id') for v in values]
    if len(ids)!=len(set(ids)): errors.append(f'IDs duplicados em {label}')
    keys=[v.get('key') for v in values if v.get('key')]
    if len(keys)!=len(set(keys)): errors.append(f'Keys duplicadas em {label}')
for a in registry:
    p=ROOT/a.get('path','')
    if not p.is_file(): errors.append(f'Asset ausente: {a.get("path")}'); continue
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    if digest != a.get('sha256'): errors.append(f'SHA-256 divergente: {a.get("path")}')
for r in recipes:
    if not r.get('id') or not r.get('result'): errors.append(f'Receita sem id/result: {r}')
if not (ROOT/'assets/runtime/atlas.png').is_file(): errors.append('Atlas runtime ausente')
if errors:
    print('FALHA DE VALIDAÇÃO:')
    for e in errors: print(' -', e)
    sys.exit(1)
print('OK: pacote válido')
print(f'Blocos: {len(blocks)} | Itens: {len(items)} | Biomas: {len(biomes)} | Receitas: {len(recipes)} | Assets PNG: {len(registry)}')
