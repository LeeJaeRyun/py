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

# 연결 리스트에서는 배열처럼 인덱스를 이용해 한 번에 특정 노드에 접근할 수 없습니다
    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1
        return cur

linked_list = LinkedList(5)
linked_list.append(12)

print(linked_list.get_node(0).data)
