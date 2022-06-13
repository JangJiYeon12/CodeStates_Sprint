"""
Bare Minimum Requirements
정렬을 구현하며 분할정복에 익숙해집니다.

요구사항:
    정렬은 대부분의 상황에서 활용되는 대표적인 개념입니다.
    분할정복 알고리즘을 한 번 상기하면서 정렬이라는 목적을 달성해봅니다.

    분할정복 알고리즘 개념을 적용하여 퀵소트를 작성해주세요.
    파이썬에서 제공되는 sort와 같은 내장함수를 사용하면 안됩니다.
    분할정복을 활용하여 구현하시길 바랍니다.
    
    각 문제 코드 위에 작성된 '@counter'는 변경하지 마세요.
"""

class counter:
    """
    해당 코드를 수정하지 마세요! 
    """
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)


@counter    # 삭제하거나 변경하지 마세요!
def quick_sort(li):
    ARRAY_LENGTH = len(li)
    
    if( ARRAY_LENGTH <= 1):
        return li
    else:
        PIVOT = li[0]
        GREATER = [ element for element in li[1:] if element > PIVOT ]
        LESSER = [ element for element in li[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
