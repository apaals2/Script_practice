# 설명: 모든 파일 리스트에서 숨김/일반 구분 후 크기순 출력
import os

def format_size(size):
    if size >= 1024**2:
        return f"{size / (1024**2):.2f}MB"
    elif size >=1024:
        return f"{size / 1024:.2f}KB"
    else:
        return f"{size}B"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(BASE_DIR, "../etc/log")

files = []

for file in os.listdir(file_dir):
    path = os.path.join(file_dir, file)
    if os.path.isfile(path):
        size = os.path.getsize(path)
        if size :
            is_hidden = file.startswith(".")
            files.append((file, size, is_hidden))


files.sort(key=lambda x: x[1])

for file,size,is_hidden in files:
    tag = "[숨김파일]" if is_hidden else "파일명:"
    readable_size = format_size(size)
    print(f"{tag}{file}, 크기:{readable_size} ")