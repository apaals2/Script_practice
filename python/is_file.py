# 설명: 리스트에 주어진 파일명들 중 존재하는 것만 출력
# 키워드: os.path.isfile(), for, if

import os

filename = ["find_log.py", "test.py", "find_log.log", "find_log2.log", "none.py"]

# 상대경로기준
for file in filename:
    if os.path.isfile(file):
        print(file)

# 절대경로기준(기준 디렉토리 설정 : ../etc/log 기준으로 절대경로 구성)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(BASE_DIR, "../etc/log")
#file_dir = os.path.abspath(file_dir)

#for file in os.listdir(file_dir): # listdir은 폴더(디렉토리)경로여야함. filename은 문자열 목록(List[str])
for file in filename:
    path = os.path.join(file_dir, file)
    #if os.path.isfile(path) and file.endswith(filename): # endswith는 문자열, 튜플만 받음 리스트 안받음
    if os.path.isfile(path):
        print(file)