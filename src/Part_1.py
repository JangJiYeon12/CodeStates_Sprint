"""
Bare Minimum Requirements
해시테이블의 기본 개념을 알아봅시다

요구사항:
    name에 따라 num이 매칭될 수 있도록 코드를 구현하세요.

    코드에서 구현되야 할 주요기능과 코드는 아래와 같습니다.
    기능1) 아래 기능을 포함하는 클래스
    기능2) 키에 따른 값을 담아주는 함수
    기능3) name에 따라 특정값을 반환해주는 해시함수
    기능4) name에 따라 num이 매칭되도록 설정하는 함수
    기능5) name에 따라 매칭되는 num을 찾아주는 함수

    아래 예제코드를 통해 hash_table 클래스가 어떻게 동작하는지 확인해주세요
    
    예제 코드 
        ht = hash_table()

        ht.hash_put('Kim', 1234)
        ht.hash_put('Johne', 5678)
        ht.hash_put('Smith', 1526)
        ht.hash_put('Michael', 3748)

        print(ht.hash_search('Johne')) # 5678

    해시충돌을 방지하는 형태로 작성된 테스트코드를 통과하기 위해 주어진 아래 함수를 완성해주세요
    hint) hash_function 함수에서 반환되는 값을 활용하여 hash_put 함수와 hash_search 함수를 완성해야 합니다.
"""


# 기능1) 아래 전체 함수를 포함하는 클래스
class hash_table:
    # 기능2) 키에 따른 값을 담아주는 함수
    def __init__(self):
        self.table = pass
    

    # 기능3) name에 따라 특정값을 반환해주는 해시함수
    def hash_function(self, name):
        table_sum = 0
        pass


    # 기능4) name에 따라 num이 매칭되도록 설정하는 함수
    def hash_put(self, name, num):
        pass


    # 기능5) name에 따라 매칭되는 num을 찾아주는 함수
    def hash_search(self, name):
        pass 
