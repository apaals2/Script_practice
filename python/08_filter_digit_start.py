# 설명: 파일명이 숫자로 시작하는 파일만 출력
# 키워드: file[0].isdigit()


import os

file_dir = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(file_dir):
    path = os.path.join(file_dir, file)
    if os.path.isfile(path) and file[0].isdigit(): # 파일의 첫 글자
        print(file)

print("----------------------------------------------")
# 알파벳/숫자순 정렬
file_dir2 = os.path.dirname(os.path.abspath(__file__))

files = sorted(os.listdir(file_dir2))

for file in files:
    path = os.path.join(file_dir2, file)
    print(file)

print("----------------------------------------------")

file_list = os.listdir("./") # 현재 폴더 기준(경로 이동 필수)
for file in file_list:
    path = os.path.join(".", file)
    if os.path.isfile(path) and file[0].isdigit():
        print(file)
print("----------------------------------------------")
for file in sorted(file_list):
    print(file)