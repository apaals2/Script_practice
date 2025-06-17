# 설명: 모든 경로에서 디렉토리만 필터링하여 출력
# 키워드: os.path.isdir() 

import os

base_dir = os.path.abspath("/") # 루트 기준

for item in os.listdir(base_dir):
    path = os.path.join(base_dir, item)
    if os.path.isdir(path):
        print(f"[디렉토리] {item}")
