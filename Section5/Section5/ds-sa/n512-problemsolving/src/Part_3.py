"""
Advanced Requirements
반복문과 조건문을 활용한 문제를 해결은 계속됩니다.

요구사항:
    1부터 입력받은 숫자까지 모든 숫자에 대해 소수가 몇 개 있는지 반환하세요.
    입력받은 숫자는 1 이상입니다.
    0이하의 경우 ValueError를 발생시켜 주세요.
"""

def part3(N):
    if N < 1:
        raise ValueError

    result = []
    
    for i in range(2, N+1):
        a = 0
        for j in range(2, i):
            if i%j==0:
                break;
            else:
                a += 1
        if a == i-2:
            result.append(i)

    return len(result)
