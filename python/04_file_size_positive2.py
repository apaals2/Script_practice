# 설명: 파일 크기 단위로 출력
# 키워드: os.path.getsize(), if

import os


def format_size(size):
    if size >= 1024**2:
        return f"{size / (1024**2):.2f}MB"
    elif size >=1024:
        return f"{size / 1024:.2f}KB"
    else:
        return f"{size}B"
    
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "../etc/log")

file_info_list = []

# 반환되는 순서대로 출력
for file in os.listdir(file_path):
    path = os.path.join(file_path, file)

    # 단위로 출력
    if os.path.isfile(path) and os.path.getsize(path):
        size = os.path.getsize(path)
        readable_size = format_size(size)
        print(f"파일명: {file}, 크기: {readable_size}")