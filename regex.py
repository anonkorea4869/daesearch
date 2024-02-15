import os
import re

def getPath(text) :
    path_list = []
    # 작은따옴표와 큰따옴표로 감싸인 컨텐츠를 매칭하는 정규 표현식
    pattern = r"'([^']+)'|\"([^\"]+)\"" 
    matches = re.findall(pattern, text)

    # 결과를 하나의 리스트로 병합
    matches = [match[0] if match[0] else match[1] for match in matches]

    for match in matches:
        # if match.count('/') >= 2 and match[-1] != ">":
        #     path_list.append(match)

        # ./ ../ / 로 시작하거나 .php로 끝나는 문자열 찾기
        pattern2 =  r'(?:\./|\.\./|/)[^\s]+' # + http, https 앞에 뭐 있음 안됨
        # pattern3 = r'\w+.php$'

        matches2 = re.findall(pattern2, match)

        for match2 in matches2:
            # 0. 맨뒤 / 제괴하여 2번을 추가 검사
            if match2[-1] == "/" :
                match2 = match[:-1]
            # 1. html 마무리 꺽쇄 제거
            elif match2[-1] == ">" :
                continue
            # 2. // 로 시작하지 않는 문자열 중에서 /가 2개인것 찾기
            # if not match2.count("//") >= 1 and match2.count('/') < 2:
            #     continue
            if any(char in match2 for char in [",", "\n", ";", "(", "</", "{", "}", "%"]):
                continue
            else : 
                path_list.append(match2)

    return path_list

def prepare(path) :

    while True : 
        # 접두사 제거
        if path.startswith("//") :
            path = path[1:]
        elif path.startswith("./") :
            path = path[1:]
        elif path.startswith("../") :
            path = path[2:]
        elif path.startswith("/./") :
            path = path[3:]
        elif path.startswith("/../") :
            path = path[4:]
        else :
            break
    
    # 특정 확장자 제거
    directory, extension = os.path.splitext(path)

    if extension in [".png", ".jpg", ".txt"]:
        index = path.rfind("/")
        if index != -1:
            path = path[:index]

    # 인자 제거
    if "?" in path :
        path = path[ : path.index("?")]
    if "/{" in path : 
        path = path[ : path.index("/{")]
    if "\"" in path : 
        path = path[ : path.index("\"")]

    # http, https 제거
    if "http://" in path :
        path = path.replace("http://", "/")
    elif "https://" in path :
        path = path.replace("https://", "/")

    # 맨 뒤에 / 있으면 제거
    if len(path) > 0 and path[-1] == "/" :
        path = path[:-2]

    # 리젝
    # // 로 시작하지 않는 문자열 중에서 /가 2개인것 찾기
    if not path.count("//") >= 1 and path.count('/') < 2:
        return None
    elif len(path) == 0 or "/" not in path :
        return None
    elif path[0] != "/" :
        return None
    return path

# 레포 이름 구하기
for path, dirs, files in os.walk("./repos"):
    repo_name_list = dirs
    break

total_repo_path_list = []
# 레포 순회
for repo_idx, repo_name in enumerate(repo_name_list) :
    repo_path_list = []

    # 레포별 내용 순회
    for path, dirs, files in os.walk(f"./repos/{repo_name}"):
        for file_name in files:
            
            # 확장자 얻기
            if "." in file_name : 
                extension = file_name[file_name.index(".") + 1 : ]
            else :
                continue

            # 확장자 확인 후 파일 내용 읽기
            if extension in ["php", "html", "py", "ts", "tsx", "js", "jsx", "asp"] :
                file_path = os.path.join(path, file_name)

                try : 
                    with open(file_path, 'r') as file:
                        contents = file.read()
                except :
                    break
                
                # 경로 추출
                repo_path_list += getPath(contents)
    
    # 전처리
    repo_prepare_list = []

    for repo_path in repo_path_list :
        prepare_result = prepare(repo_path)

        if prepare_result != None :
            repo_prepare_list.append(prepare_result)

    # 레포의 중복 경로 제거 및 합차기
    total_repo_path_list += list(set(repo_prepare_list))
    print(f"{repo_idx + 1}. repo_name -> {len(total_repo_path_list)}")

    with open("regex.txt", "a") as f:
        for total_repo_path in total_repo_path_list : 
            f.write(f"{total_repo_path}\n")

with open("regex.txt", "r") as f:
    print(len(f.readlines()))