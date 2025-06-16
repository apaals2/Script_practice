import os

# 1. os.listdir(path)
files = os.listdir(".")  # 현재 디렉토리
print(files)
# 출력: ['find_log.py', 'find_log2.py', 'test.py']
print("-----------------------------")

# os.path.isfile(path)
print(os.path.isfile("test.py"))     # True (파일이면)
print(os.path.isfile("python"))       # False (폴더면)
# 출력 : 
# True
# False
print("-----------------------------")

# str.endswith(suffix)
filename = "file_log.log"
print(filename.endswith(".log"))
print(filename.endswith((".log",".txt")))
print(filename.endswith(".py"))
# 출력:
# True
# True
# False
print("-----------------------------")

# os.path.join(path1, path2, ...)
folder = "logs"
filename = "logfile.log"
full_path = os.path.join(folder, filename)
print(full_path)
# 출력: logs/logfile.log
print("-----------------------------")

# 5. os.path.abspath(path)
relative_path = "../etc/log"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)
# 출력 예시: /Users/username/project/etc/log
print("-----------------------------")

# 6. __file__ : 현재 파일의 경로
print(__file__)
# 출력 예시: /Users/username/project/find_log.py
print("-----------------------------")

# 7. os.path.dirname(path)
script_path = os.path.abspath(__file__)
base_dir = os.path.dirname(script_path)
print(base_dir)
# 출력 예시: /Users/username/project
print("-----------------------------")