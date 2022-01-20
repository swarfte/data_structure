class Node(object):  # 創建一個節點
    def __init__(self, e=None, n=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = n  # 指針域


class LinkList(object):  # 創建一個單鏈表
    def __init__(self, l=None):
        super(LinkList, self).__init__()
        self.__head = None  # 頭指針
        self.__len = None  # 鏈表長度
        self.clear_list()
        self.list_change(l)  # 可選的

    def clear_list(self):
        self.__head = Node()
        self.__len = 0

    def list_change(self, l):
        if l is not None:
            for x in l:
                self.add_tail(x)

    def list_length(self):
        return self.__len

    def locate_elem(self, e):
        p = self.__head.next
        for x in range(self.__len):
            if p.element == e:
                return True
            p = p.next
        return False

    def list_empty(self):
        return bool(self.__len)

    def add_head(self, e):
        new_node = Node(e)
        p = self.__head
        new_node.next = p.next
        p.next = new_node
        self.__len += 1

    def add_tail(self, e):
        new_node = Node(e)
        p = self.__head
        for x in range(self.__len):
            p = p.next
        p.next = new_node
        self.__len += 1


    def pop_head(self):
        self.__len -= 1
        p = self.__head
        n = self.__head.next
        p.next = p.next.next
        return n.element

    def pop_tail(self):
        self.__len -= 1
        p = self.__head
        for x in range(self.__len):
            p = p.next
        n = p
        p.next = None
        return n.element


    def list_insert(self, index, e):
        new_node = Node(e)
        p = self.__head
        for x in range(index):
            p = p.next
        new_node.next = p.next
        p.next = new_node
        self.__len += 1

    def list_delete(self, index):
        self.__len -= 1
        p = self.__head
        for x in range(index):
            p = p.next
        n = p
        p.next = p.next.next
        return n.element

    def get_elem(self, index):
        p = self.__head.next
        for x in range(index):
            p = p.next
        return p.element

    def get_node(self, index):
        p = self.__head.next
        for x in range(index):
            p = p.next
        return p

    def get_list(self):
        l = []
        for x in range(self.__len):
            l.append(self.get_elem(x))
        return l

    def get_node_list(self):
        l = []
        for x in range(self.__len):
            l.append(self.get_node(x))
        return l
