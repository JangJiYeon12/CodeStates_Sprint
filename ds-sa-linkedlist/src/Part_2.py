"""
Bare Minimum Requirements
연결리스트의 개념은 변수의 인덱스에 직접접근하는 배열개념과는 다릅니다.
참조의 개념을 활용하여 변수에 접근하는 방법을 익혀봅니다.

요구사항:
    주어진 문제는 연결리스트지만 독립적으로 개념이 운용되는 것은 아닙니다.

    연결리스트를 구현해주세요.
    각 메소드에 작성되어있는 문제를 확인하여 코드를 작성해주세요.

    단 collections 라이브러리는 사용하지 마세요.
    메소드 이름은 변경하지 마세요.
    메소드의 매개변수를 추가하거나 삭제하지 마세요.
"""

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next


class linked_list:
    def __init__(self, value):
        self.head = Node(value)


    def add_node(self, value):
        if self.head ==None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)


    def del_node(self,value):
        if self.head == None:
            return None
        elif self.head.value == value:
            temp = self.head
            self.head = self.head.next
            return temp.value
        else:
            node = self.head
            while node.next:
                if node.next.value == value:
                    temp = node.next
                    node.next = node.next.next
                    return temp.value
                else : 
                    node = node.next


    def ord_desc(self):
        ls = []
        node = self.head
        while node:
            ls.append(node.value)
            node = node.next
        
        return ls


    def search_node(self,value):
        node = self.head
        while node:
            if node.value == value:
                return node
            else:
                node = node.next
        return None

