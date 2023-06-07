"""
Part_4

JSON 데이터를 Mongo DB 에 저장한 뒤, SQLite 로 전달하기 (Github API -> ds-sa-nosql-issues)

Github API 를 이용해서 ds-sa-nosql-issues 레포지토리의 이슈 리스트를 받아옵니다.

1. 이슈 리스트를 MongoDB 에 저장합니다.
2. MongoDB 에 저장된 리스트를 SQLite 에 전달합니다.

위와 같은 데이터 파이프라인은 NoSQL 을 JSON 수집용으로 사용하고,
데이터 분석이 가능하도록 데이터웨어하우스를 구성하는 것과 같은 방식입니다. 

cf. 예를 들어, 데이터 엔지니어는 데이터 수집을 빠르게 진행하고자 NoSQL 로 데이터 수집을 진행한 뒤
데이터 모델링을 거쳐서 데이터 분석가가 분석이 가능하도록 데이터웨어하우스 혹은 데이터마트 형태로 데이터를 전달합니다.

스키마는 아래와 같이 구성합니다. (스키마에 지정되지 않는 컬럼은 제외하세요)
- [PR_List_RDB Schema](https://i.imgur.com/QnCdw5E.png)
- Primary key 로 있는 값은 입력할 때 중복되지 않아야 한다는 점 주의하세요


pytest 로만 통과할 수 없습니다. `python src/Part_4.py`로 MongoDB 에 데이터를 입력하세요
- 코드에 적혀있는 대로 콜렉션 이름은 변경하지 말아주세요!
"""

import os
import time
import copy
import sqlite3
import requests
from pymongo import MongoClient

prlist = ''
dont_touch= ''
response = requests.get("https://api.github.com/repos/codestates/ds-sa-nosql-issues/issues")
# 주의할 점 : github API 는 호출이 너무 많이 발생하면 자체적으로 제한을 걸 수 있습니다.
# 한번의 API 호출 후 1초 sleep 시간을 지정합니다.
time.sleep(1)

if response.status_code == 200:
    prlist = response.json()
    dont_touch = copy.deepcopy(prlist)

"""
MONGODB SETUP
"""

HOST = ''
USER = ''
PASSWORD = ''
DATABASE_NAME = ''
COLLECTION_NAME = 'PR_LIST'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"
DB_FILENAME = 'PR_LIST_RDB.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)


"""
위 코드는 힌트입니다. 자신에 맞는 HOST,USER, PASSWORD, DATABASE_NAME 을 입력하세요
! COLLECTION_NAME = 'PR_LIST'
! DB_FILENAME = 'PR_LIST_RDB.db'
아래 pass 를 지우고 코드를 작성하세요
"""

pass
