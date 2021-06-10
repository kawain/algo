# 現ディレクトリ以下の
# サブディレクトリ内も含めて
# 任意の拡張子のファイルを
# 削除するスクリプト
import glob
import os
import re

files = [
    p for p in glob.glob('./**', recursive=True)
    if re.search(r'\.(exe|out)$', p)
]

for v in files:
    if os.path.isfile(v):
        os.remove(v)
