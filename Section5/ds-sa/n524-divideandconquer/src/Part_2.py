"""
Bare Minimum Requirements
정렬을 구현하며 분할정복에 익숙해집니다.

요구사항:
    정렬은 대부분의 상황에서 활용되는 대표적인 개념입니다.
    분할정복 알고리즘을 한 번 상기하면서 정렬이라는 목적을 달성해봅니다.

    분할정복 알고리즘 개념을 적용하여 머지소트(합병정렬)를 작성해주세요.
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


def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        # 9. 각 반복 동안 두 리스트의 모든 위치에 있는 요소를 비교합니다.
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    # 11. 남아있는 리스트 요소에서 현재 i, j 값을 기준으로 각각 리스트의 마지막지점 인덱스까지 값을 넣고 결과값을 반환합니다.
    output.extend(left[i:])
    output.extend(right[j:])

    return output


@counter # 삭제하거나 변경하지 마세요!
def merge_sort(li):
    list_length = len(li)

    if list_length == 1:
        return li

    mid_point = list_length // 2  # //연산자는 몫을 구한다

    left_partition = merge_sort(li[:mid_point])
    right_partition = merge_sort(li[mid_point:])

    return merge(left_partition, right_partition)
