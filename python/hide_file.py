# 설명: 파일명 앞에 .이 붙은 숨김 파일만 출력
# 키워드: str.startswith(), if, os

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #현재파일경로기준
file_dir = os.path.join(BASE_DIR, "../etc/")
file_dir = os.path.abspath(file_dir)

for file in os.listdir(file_dir):
    path = os.path.join(file_dir, file)
    #if file.startswith(file): # 항상 True 조건임(자기 자신으로 시작하는지 묻고있음) 
    if file.startswith("."): # .으로 시작하는 파일 출력
        print(file)

# os.walk()를 사용한 전체 경로 순회 + 숨김 파일 탐색
for root, dirs, files in os.walk("/"): # 루트부터 시작 (Linux/Mac 기준)
    for file in files:
        if file.startswith("."):
            full_path = os.path.join(root, file)
            print(full_path)