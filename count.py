import os, os.path
import pathlib

dir=r'H:\fruits'

subfolders = [ (f.path, f.name) for f in os.scandir(dir) if f.is_dir() ]
res = []
for subfolder in subfolders:
    res.append((subfolder[1], len(os.listdir(subfolder[0]))))

total = 0
for r in res:
    print(f'{r[0]}: {r[1]} samples')
    total=total+r[1]
print(f'Total sample size: {total}')