class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

# --- 코드 실행부 ---

# LinkedList 객체를 생성하고 head 노드를 설정합니다.
linked_list = LinkedList(5)

# 초기 head 노드의 데이터를 출력합니다.
print(linked_list.head.data)

# 연결 리스트에 12와 8을 추가합니다.
linked_list.append(12)
linked_list.append(8)

# 연결 리스트의 모든 데이터를 출력합니다.
linked_list.print_all()