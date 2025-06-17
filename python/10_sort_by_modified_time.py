# 설명: 최근 수정 시간 기준으로 파일을 정렬해서 출력
# 키워드: os.path.getmtime(), sorted()

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(base_dir, "../etc/log")

files = []

for file in os.listdir(file_dir):
    path = os.path.join(file_dir, file)
    if os.path.isfile(path): # 현재 경로에 파일이 있다면
        modified_time = os.path.getmtime(path)
        files.append((file, modified_time))

files.sort(key=lambda x: x[1]) #오름차순

for file, mtime in files:
    print(f"파일명: {file}, 최근 수정 시간: {mtime}")