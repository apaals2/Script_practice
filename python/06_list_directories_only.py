# 설명: 현재 폴더 내에서 디렉토리만 필터링하여 출력
# 키워드: os.path.isdir() 

import os

base_dir = os.path.abspath("./") #현재 폴더 기준

for item in os.listdir(base_dir):
    path = os.path.join(base_dir, item)
    if os.path.isdir(path):
        print(f"[디렉토리] {item}")
