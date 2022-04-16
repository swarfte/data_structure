class Node(object):  # 創建一個節點
    def __init__(self, e: object = None, n=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = n  # 指針域


class ChainQueue(object):
    def __init__(self, l: list = None):
        super(ChainQueue, self).__init__()
        self.__len = 0
        self.__front = Node()
        self.__rear = self.__front
        self.list_convert(l)

    def list_convert(self, l: list) -> None:
        if l is not None:
            for x in l:
                self.enter_queue(x)

    def clear_queue(self) -> None:
        self.__len = 0
        self.__front = Node()
        self.__rear = self.__front

    def queue_empty(self) -> bool:
        return not bool(self.__len)

    def get_head(self) -> object:
        return self.__front.next.element

    def enter_queue(self, e: object) -> None:
        new = Node(e)
        self.__len += 1
        if self.__front == self.__rear:
            self.__front.next = new
        else:
            self.__rear.next = new
        self.__rear = new

    def delete_queue(self) -> object:
        self.__len -= 1
        temp = self.__front.next.element
        self.__front.next = self.__front.next.next
        return temp

    def queue_length(self) -> int:
        return self.__len

    def get_queue(self) -> list:
        t = []
        head = self.__front
        for x in range(self.__len):
            head = head.next
            t.append(head.element)
        return t
