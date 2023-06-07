
import os
import sqlite3
# DB_FILENAME, DB_FILEPATH 변경하지 마세요
DB_FILENAME = "twitter_db.sqlite3"
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)



def get_cursor(DB_FILEPATH):
    """
    get_cursor 함수는 데이터베이스와 연결된 커서 객체를 리턴합니다.

    리턴 :
     - connection 인스턴스 : 데이터베이스와 연결된 connection 인스턴스를 리턴합니다.
     - cursor 인스턴스 : 데이터베이스에 sql 쿼리문을 보낼 수 있는 cursor 인스턴스를 러턴합니다.
    """
    pass

def add_user(username, connection, cursor):
    """
    add_user 함수는 username 을 기반으로 user 를 새로 추가하고 해당 user 객체를 리턴합니다.
    - username 을 가지고 있는 유저가 기존에 존재한다면 유저를 추가하지 않습니다.
    - id 는 자동으로 생성되어도, 여러분이 생성하셔도 상관없습니다.
    - 해당 함수가 끝나면 데이터베이스에 데이터가 입력되어 있어야합니다.

    파라미터:
        - username: 추가할 유저 이름을 담은 문자열(str) 입니다.
        - connection 인스턴스 : 데이터베이스와 연결된 connection 인스턴스 입니다.
        - cursor 인스턴스 : 데이터베이스에 sql 쿼리문을 보낼 수 있는 cursor 인스턴스 입니다.
    """
    pass

def add_tweet(username, tweet_text, connection, cursor):
    """
    add_tweet 함수는 tweet_text 와 username 이 주어지면 해당 유저와 연결된
    새로운 트윗을 추가합니다.
    - username 에 해당하는 유저가 user 테이블에 없다면, user 테이블에 username 에 해당하는 user를 추가해야합니다.

    파라미터:
        - username: 추가할 유저 이름을 담은 문자열(str) 입니다.
        - tweet_text: 추가할 트윗을 담은 문자열(str) 입니다.
        - connection 인스턴스 : 데이터베이스와 연결된 connection 인스턴스 입니다.
        - cursor 인스턴스 : 데이터베이스에 sql 쿼리문을 보낼 수 있는 cursor 인스턴스 입니다.
    """
    pass
    


def delete_user(user_id, connection, cursor):
    """
    delete_user 함수는 user_id 가 주어지면 데이터베이스에서 해당 user 를 삭제합니다.
    - user 와 연관된 연관된 tweet 테이블의 tweet 들도 같이 삭제해야 합니다.

    파라미터:
        - user_id: 데이터베이스에서 삭제할 트윗 레코드 고유번호(int) 입니다.
        - connection 인스턴스 : 데이터베이스와 연결된 connection 인스턴스 입니다.
        - cursor 인스턴스 : 데이터베이스에 sql 쿼리문을 보낼 수 있는 cursor 인스턴스 입니다.
    """
    pass


