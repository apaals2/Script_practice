# 설명: 절대경로로 `.log`로 끝나는 파일만 출력

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # find_log.py 파일 기준
#print(BASE_DIR)
log_dir = os.path.join(BASE_DIR, "../etc/log")          # 상대경로 -> 절대경로로 변환
#print(log_dir)
log_dir = os.path.abspath(log_dir)                      # 경로 정규화
#print(log_dir)
for file in os.listdir(log_dir):                        # log_dir안의 모든 파일/폴더 순회
    path = os.path.join(log_dir, file)                  # 전체 경로 조합
    #print(path)
    if os.path.isfile(path) and file.endswith(".log"):  # 파일인지 확인 + .log 확장자인지 확인
        print(file)                                     # # 조건을 만족하는 경우 파일 이름 출력