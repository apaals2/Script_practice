# 설명: 특정 폴더에서 `.log`로 끝나는 파일만 출력
# 키워드: os.listdir(), os.path.isfile(), str.endswith()

import os

log_dir = "etc/log" # Script_practice/ 기준일때
#log_dir = "../etc/log" # Script_practice/python 기준일때

for file in os.listdir(log_dir):
    path = os.path.join(log_dir, file)
    if os.path.isfile(path) and file.endswith(".log"):
        print(file)
