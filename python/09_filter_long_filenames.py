# 설명: 파일명 길이가 20자 이상인 파일만 출력
# 키워드: len(file), if

import os

file_dir = os.path.dirname(os.path.abspath(__file__)) # 파일 기준 경로

# 순서 정렬
files = sorted(os.listdir(file_dir))

for file in files:  
    if len(file)>=20: # os.path.isfile(path) 생략
        print(file)