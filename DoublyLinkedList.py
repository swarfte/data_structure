class Node(object):  # 創建一個節點
    def __init__(self, e=None, n=None, p=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = n  # 後驅指針域
        self.prior = p  # 前驅指針域


class DoublyLinkedList(object):
    def __init__(self, l=None):
        super(DoublyLinkedList, self, ).__init__()
        self.__head = None  # 頭指針
        self.__end = None  # 尾指針
        self.__len = None  # 鏈長
        self.clean_list()  # 初始化
        self.list_change(l)  # 預生成雙向鏈 (可選)

    def list_change(self, l):
        if l is not None:
            for x in l:
                self.add_tail(x)

    def list_empty(self):
        if self.__head.next == self.__end \
                and self.__end.prior == self.__head:
            return False
        else:
            return True

    def list_length(self):
        return self.__len

    def get_node(self, index):
        p = self.__head.next
        for x in range(index):
            p = p.next
        return p

    def locate_elem(self, e):
        p = self.__head.next
        for x in range(self.__len):
            if p.element == e:
                return True
            p = p.next
        return False

    def get_elem(self, index):
        p = self.__head.next
        for x in range(index):
            p = p.next
        return p.element

    def clean_list(self):  # 初始化雙向鏈表
        self.__head = Node()
        self.__end = Node()
        self.__len = 0
        self.__head.prior = self.__end
        self.__head.next = self.__end
        self.__end.prior = self.__head
        self.__end.next = self.__head

    # def first_node(self,node):# 針對第一個節點的
    #     self.__head.next = node
    #     node.prior = self.__head
    #     node.next = self.__end
    #     self.__end.prior = node

    def add_head(self, e):
        self.__len += 1
        new_node = Node(e)
        new_node.next = self.__head.next
        new_node.prior = self.__head
        self.__head.next.prior = new_node
        self.__head.next = new_node

    def add_tail(self, e):
        self.__len += 1
        new_node = Node(e)
        new_node.prior = self.__end.prior
        new_node.next = self.__end
        self.__end.prior.next = new_node
        self.__end.prior = new_node

    def pop_head(self):
        self.__len -= 1
        self.__head.next.next.prior = self.__head
        self.__head.next = self.__head.next.next

    def pop_tail(self):
        self.__len -= 1
        self.__end.prior.prior.next = self.__end
        self.__end.prior = self.__end.prior.prior

    def list_insert(self, index, e):
        self.__len += 1
        new_node = Node(e)
        p = self.__head.next
        for x in range(index):
            p = p.next
        # 中途插入新節點
        new_node.next = p
        new_node.prior = p.prior
        p.prior.next = new_node
        p.prior = new_node

    def list_delete(self, index):
        self.__len -= 1
        p = self.__head.next
        for x in range(index):
            p = p.next
        p.next.prior = p.prior
        p.prior.next = p.next

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
