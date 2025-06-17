# 설명: 크기가 0보다 큰 파일만 출력 + 크기 기준으로 정렬
# 키워드: os.path.getsize(), if
# 설명: 디렉토리 내 파일을 크기 기준으로 오름차순 정렬 출력
# 키워드: sorted(), os.path.getsize(), lambda

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "../etc/log")

file_info_list = []

# 반환되는 순서대로 출력
for file in os.listdir(file_path):
    path = os.path.join(file_path, file)

    # 모든 파일을 크기 기준으로 정렬
    if os.path.isfile(path):
        size = os.path.getsize(path)
        file_info_list.append((file,size))

file_info_list.sort(key=lambda x:x[1], reverse=True) # False 내림차순

for file, size in file_info_list:
    print(f"파일명: {file}, 크기: {size}")