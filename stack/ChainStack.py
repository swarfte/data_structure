class Node(object):  # 創建一個節點
    def __init__(self, e: object = None, n=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = n  # 指針域


class ChainStack(object):
    def __init__(self, l: list = None):
        super(ChainStack, self).__init__()
        self.__head = None
        self.__len = 0
        self.list_convert(l)

    def list_convert(self, l: list) -> None:
        if l is not None:
            for x in l:
                self.push(x)

    def clear_stack(self) -> None:
        self.__head = Node()
        self.__len = 0

    def stack_empty(self) -> bool:
        return not bool(self.__len)

    def stack_lengths(self) -> int:
        return self.__len

    def get_top(self) -> Node:
        return self.__head

    def push(self, e: object) -> None:
        self.__len += 1
        new_node = Node(e)
        new_node.next = self.__head
        self.__head = new_node

    def pop(self) -> object:
        self.__len -= 1
        throw = self.__head.element
        self.__head = self.__head.next
        return throw
