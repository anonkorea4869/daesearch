import requests
import math
import time
import json

def getHref(json_text):
    # JSON 문자열을 파싱하여 딕셔너리로 변환
    json_data = json.loads(json_text)

    # "hl_name" 값을 저장할 리스트 생성
    repositories = []

    # "results" 배열의 각 요소에서 "hl_name" 필드의 값을 추출하여 리스트에 추가
    for result in json_data['payload']['results']:
        repositories.append(result['hl_name'].replace("<em>", "").replace("</em>", ""))

    return repositories

crawling_count = 500

repositories = []

for page in range(1, math.ceil(crawling_count/10) + 1) :
    # print((math.ceil(crawling_count/10) - page))
    url = f"https://github.com/search?q=website&type=repositories&p={page}"
    print(url)
    time.sleep(20)
    session = requests.session()
    response = session.get(url)
    if response.status_code == 404 :
        break

    json_text = response.text

    for repository in getHref(json_text) :
        repositories.append(repository)
if len(repositories) < crawling_count :
    count = len(repositories)
else :
    count = crawling_count

with open("git.sh", "w") as f:
    for i in range(0, count) : 
        f.write(f"git clone https://github.com/{repositories[i]}.git {repositories[i]}\n")

print("FOUND %d/%d"%(count, crawling_count))

