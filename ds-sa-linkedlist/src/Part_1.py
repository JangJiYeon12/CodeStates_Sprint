"""
Bare Minimum Requirements

요구사항
    큐, 스택을 구현해주세요.
    각 메소드에 작성되어있는 문제를 확인하여 코드를 작성해주세요.

    단 collections 라이브러리는 사용하지 마세요.
    메소드 이름은 변경하지 마세요.
    메소드의 매개변수를 추가하거나 삭제하지 마세요.
"""
class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,item):
        new_node = LinkedListNode(item)
        if self.rear is None:       #큐가 비어있다면,
            self.front = new_node   #front와 rear 다 new_node를 가르킨다.
            self.rear = new_node
        else:
            self.rear.next = new_node  #rear.next에 새로운 값을 넣고,
            self.rear = new_node 

        return new_node.data


    def dequeue(self):
        if self.front is not None:
            # front값을 old front에 삽입
            old_front = self.front
            # old front 다음 값을 front값에 삽입
            self.front = old_front.next
            return old_front.data

        else:
            # rear를 None으로 지정한다.
            self.rear = None
            return None


    def return_queue(self):
        ls = []
        node = self.front
        
        while node:
            ls.append(node.data)
            node = node.next
        
        return ls


class Stack():
    def __init__(self):
        self.top = None


    def push(self, item):
        new_node = LinkedListNode(item)
        new_node.next = self.top            #새 노드를 현재 최상단 노드에 링크
        self.top = new_node                 #이제 최상단은 새 노드를 가르키게 함
        return new_node.data


    def pop(self):
        if self.top is not None:
            popped_node = self.top          #삭제할 최상단의 노드를 지정
            self.top = popped_node.next     #그 노드의 한단계 아래(next)를 탑으로 지정
            return popped_node.data
        else:
            return None


    def return_stack(self):
        """
        #. 문제 8.
        Stack내부에 있는 값을 반환하는 메소드를 구현해주세요.

        input: 
            input은 없습니다.
        output: 
            Stack내부에 있는 값을 리스트 형태로 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        ls = []
        node = self.top
        while node:
            ls.append(node.data)
            node = node.next
        
        return [i for i in reversed(ls)]

    
