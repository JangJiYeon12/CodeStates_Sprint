"""
Part 4
클라우드 데이터베이스에 'passenger' 라는 테이블을 생성하고 titanic.csv 에 있는 데이터를 'passenger' 테이블로 옮깁니다.

1. passenger 테이블의 필드를 알맞게 추가합니다 (필드명은 자유입니다).
아래에는 각 필드에 해당하는 데이터 타입입니다.
- Id : INT (0부터 시작하고, 테이블의 한 행마다 주어진 INT형 숫자이며 csv에는 없습니다)
- Survived: INT
- Pclass: INT
- Name: VARCHAR(128)
- Sex: VARCHAR(12)
- Age: FLOAT
- Siblings/Spouses Aboard: INT
- Parents/Children Aboard: INT
- Fare: FLOAT

2. psycopg2.connect 를 이용해 connection 변수가 데이터베이스와 연결할 수 있도록 다음 변수들에 알맞은 정보를 담습니다:
- host: 데이터베이스 호스트 주소를 입력합니다.
- user: 데이터베이스 유저 정보를 입력합니다.
- password: 데이터베이스 비밀번호를 입력합니다.
- database: 데이터베이스 이름을 입력합니다.

3. passenger 테이블에 titanic.csv 에 있는 데이터를 옮깁니다.

"""

# import psycopg2

# host = '호스트 주소를 입력해주세요'
# user = '유저 이름을 입력해주세요'
# password = '비밀번호를 입력해주세요'
# database = '데이터베이스 이름을 입력해주세요'

# connection = psycopg2.connect(
#     host=host,
#     user=user,
#     password=password,
#     database=database
# )

# 나머지 코드는 titanic.csv 의 데이터를 passenger 테이블로 전달할 수 있도록 자유롭게 작성해주시기 바랍니다.
