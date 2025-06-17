# 설명: 크기가 0보다 큰 파일만 출력
# 키워드: os.path.getsize(), if

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "../etc/log")

# 반환되는 순서대로 출력
for file in os.listdir(file_path):
    path = os.path.join(file_path, file)
    #if os.path.isfile(path) and os.path.getsize(path): # 파일인지 확인하고 크기가 있다면
    # 일반 파일 (숨김X, 크기 > 0)
    if not file.startswith(".") and os.path.isfile(path) and os.path.getsize(path):
        print(f"파일명: {file}, 크기: {os.path.getsize(path)}")
      
    # 숨김 파일 (크기 > 0)
    if file.startswith(".") and os.path.isfile(path) and os.path.getsize(path):
        print(f"[숨김파일]파일명: {file}, 크기: {os.path.getsize(path)}")

# 숨김 + 크기 순/ 일반 + 크기 순 출력
normal_files = []
hidden_files = []

for file in os.listdir(file_path):
    path = os.path.join(file_path, file)
    if os.path.isfile(path) and os.path.getsize(path):
        size = os.path.getsize(path)
        if file.startswith("."):
            hidden_files.append((file,size))
        else:
            normal_files.append((file,size))

normal_files.sort(key=lambda x: x[1], reverse=True)
hidden_files.sort(key=lambda x: x[1], reverse=True)

for file, size in hidden_files:
    print(f"[숨김파일]파일명: {file}, 크기: {size}")

for file, size in normal_files:
    print(f"파일명: {file}, 크기: {size}")


# 숨김/일반 구분 후 크기 순 출력

files = []
for file in os.listdir(file_path):
    path = os.path.join(file_path, file)
    if os.path.isfile(path) and os.path.getsize(path):
        size = os.path.getsize(path)
        files.append((file, size))

files.sort(key=lambda x: x[1], reverse=False)
for file, size in files:
    if file.startswith("."):
        print(f"[숨김파일]파일명: {file}, 크기: {size}")
    else:
        print(f"파일명: {file}, 크기: {size}")
