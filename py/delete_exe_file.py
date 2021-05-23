# 現ディレクトリの上の階層から始まり
# サブディレクトリ内も含めて任意の拡張子の
# ファイルを削除するスクリプト
import glob
import os
import re

files = [
    p for p in glob.glob('../**', recursive=True)
    if re.search(r'\.[exe|out]', p)
]

for v in files:
    if os.path.isfile(v):
        os.remove(v)
