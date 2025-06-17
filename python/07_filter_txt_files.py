# 설명: .txt 확장자를 가진 파일만 출력
# 키워드: str.endswith()

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(base_dir, "../etc") # 현재 폴더에서 "../etc" 경로 기준

for file in os.listdir(file_dir):
    path = os.path.join(file_dir, file)
    if os.path.isfile(path) and file.endswith(".txt"):
        print(file)


# 루트 경로 기준
for root, dirs, files in os.walk("/"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root,file)) # 전체 경로와 같이 출력