"""
Bare Minimum Requirements
그래프의 연결에 대해 소스코드와 함께 이해합니다.

요구사항:
    그래프야말로 가장 실생활과 가까운 자료구조입니다.
    그래프에서 발생할 수 있는 상황은 다양하고 추상화정도도 복잡합니다.
    인접리스트를 확인하면서 지정된 시작노드와 끝노드에 따라 경로를 찾아야 합니다.
    입력값에 따라 출력값이 나올 수 있도록 코드를 작성해봅니다.
    
    hint) Part_1 과제에서는 시작노드에서 끝노드로 이동할 수 있는 최단경로를 구하는 문제가 아니라, 
    시작노드에서 시작하여 끝노드까지 이동하면서 순차적으로 탐색한 모든 노드를 출력하는 것이 목적입니다.

    입력값:
        connection_info = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']
        }
        
        search_route(connection_info, 'B', 'D')
    출력값:
        ['B', 'C', 'D']
"""

def search_route(connection_info, start_node, end_node, route=[]):
    route = route + [start_node]
    if start_node == end_node:
        ### 소스코드 작성 ###
    if not connection_info.__contains__(start_node):
        ### 소스코드 작성 ###
    for node in connection_info[start_node]:
        ### 소스코드 작성 ###
