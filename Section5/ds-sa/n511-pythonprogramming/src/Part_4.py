"""
Advanced Requirements

내장함수를 다양하게 활용할 줄 알아야 합니다.

요구사항:
    다양한 내장함수를 활용해봅니다.
    소문자는 대문자로, 대문자는 소문자로 변경해주세요.

    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    *예시 1* 
        입력값:
            'c t A'
        출력값:
            'a C T'
    
    *예시 2* 
        입력값:
            'z X y W v U t S'
        출력값:
            's u w x T V Y Z'
"""

def part4(s):
    ls = set(s.split(' '))
    ls = sorted(ls)

    result = []

    for i in ls:
        if i.isupper():
            result.append(i.lower())
        else:
            result.append(i.upper())

    #result = list(map(lambda i : i.lower() if i.isupper() else i.upper(), ls)) #람다로도 만들어봐따

    result = ' '.join(result)

    return result
