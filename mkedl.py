#!/usr/bin/env python3
"""
mkedl
使い方:
    python mkedl <入力ファイル> 
"""

import sys
import json
import csv
import os
import re
from yt_dlp import YoutubeDL
from yt_dlp.extractor.abematv import AbemaTVTitleIE

# コマンドライン引数のチェック
if len(sys.argv) < 2:
    print("使用方法: python mkedl <入力ファイル>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = os.path.splitext(input_path)[0] + '.edl'

if os.path.exists(output_path):
    sys.exit(1)

pattern = r"\[(.*)\]"

abema = AbemaTVTitleIE
m = re.search(pattern, input_path)
video_id = ''
if m:
    video_id = m.group(1)
else:
    print("abemaのvideo_idが見つかりません")
    sys.exit(1)
    
# 1. JSONの読み込み
Ydl = YoutubeDL()
Abema = Ydl.get_info_extractor("AbemaTVTitle")
api_response = Abema._call_api(
    f'v1/video/programs/{video_id}',video_id)
 
data = api_response['playbackMarkers']

# リスト形式に統一
records = data if isinstance(data, list) else [data]

def flatten(d, prefix=''):
    items = []
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else str(k)
        if isinstance(v, dict):
            items.extend(flatten(v).items())
        else:
            items.append((key, v))
    return dict(items)
 
records = [flatten(r) if isinstance(r, dict) else {'value': r} for r in records]
 
# 2. edlへ書き出し 
with open(output_path, mode='w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for obj in records:
        if 'endTimeMs' in obj:
            s = float(obj.get('startTimeMs', 0)) / 1000
            e = float(obj['endTimeMs']) / 1000
            writer.writerow([str(s),str(e),'3'])

print(f"変換完了: {input_path} -> {output_path} ({len(records)}件)")


