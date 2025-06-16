## 1. `os.listdir(path)`

**설명:**

- 지정한 경로(`path`)의 **피일 및 디렉토리 목록을 리스트로 반환**

## 2. `os.path.isfile(path)`

**설명:**

- 해당 경로가 **파일인지 여부를 True/False로 반환**

## 3. `str.endswith(suffix)`

**설명:**

- 문자열이 **특정 접미사(예: `.log,`, `.txt`)로 끝나는지 확인**

## 4. `os.path.join(path1, path2, ...)`

**설명:**

- 여러 경로 문자열을 운영체제에 맞게 결합
- 직접 "폴더/파일"처럼 연결하는 것보다 안전하고 가독성이 높음

## 5. `os.path.abspath(__file__)`

**설명:**

- 전달된 경로(path)를 절대경로로 변환
- 예: "../etc/log" → /Users/username/project/etc/log

## 6. `__file__`

**설명:**

- 현재 실행 중인 파이썬 파일의 경로 문자열
- 예: /Users/username/project/find_log.py

## 7. `os.path.dirname(path)`

**설명:**

- 파일 경로에서 디렉토리 경로만 분리하여 반환
- 예: /a/b/c/find_log.py → /a/b/c
