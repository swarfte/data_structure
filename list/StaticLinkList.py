class Node(object):  # 節點
    def __init__(self, data: object = None, n=None):
        super(Node, self).__init__()
        self.data = data
        self.next = n


class StaticLinkList(object):  # 靜態鏈表 #TODO 和預期的原理有所出入
    def __init__(self, l: list = None):
        super(StaticLinkList, self).__init__()
        self.__node = [None] * len(l)
        self.list_convert(l)

    def list_convert(self, l: list) -> None:  # 創建靜態鏈表
        if l is not None:
            for x in range(len(l)):
                self.__node[x] = Node(l[x])
                if x > 0:
                    self.__node[x - 1].next = self.__node[x]

    def print_list(self) -> None:  # 遍歷3並輸出靜態鏈表
        p = self.__node[0]
        while p:
            print(p.data, end="->")
            p = p.next
        print("None")

    def get_list(self) -> Node:  # 以列表型式返回靜態鏈表
        return self.__node

    def add_tail(self, e: object) -> None:  # 在隊尾插入元素
        new = Node(e)
        self.__node[-1].next = new
        self.__node.append(new)

    def add_head(self, e: object) -> None:  # 在隊頭插入元素
        new = Node(e, self.__node[0])
        self.__node.insert(0, new)

    def list_insert(self, index: int, e: object) -> None:  # 在指定的位置插入元素
        if index == 0:
            self.add_head(e)
        elif index == len(self.__node) - 1:
            self.add_tail(e)
        else:
            new = Node(e, self.__node[index])
            self.__node[index - 1].next = new
            self.__node.insert(index, new)

    def list_length(self) -> Node:  # 獲取靜態鏈表長度
        return len(self.__node)

    def clean_list(self) -> None:  # 清空靜態鏈表
        self.__node = []

    def list_empty(self) -> bool:  # 檢測靜態鏈表是否包含元素
        return True if len(self.__node) == 0 else False

    def get_elem(self, index: int) -> object:  # 獲取指定索引值的元素
        p = self.__node[0]
        for x in range(index):
            p = p.next
        return p.data

    def locate_elem(self, e: object) -> bool:  # 判斷靜態鏈表是否包含指定元素
        p = self.__node[0]
        while p.next is not None:
            if p.data == e:
                return True
            p = p.next
        return False

    def pop_tail(self) -> object:  # 刪除靜態鏈表中最後的元素
        d = self.__node[-1].data
        self.__node[-2].next = None
        self.__node = self.__node[:-1]
        return d

    def pop_head(self) -> object:  # 刪除靜態鏈表中開頭的元素
        d = self.__node[0].data
        del self.__node[0]
        return d

    def list_delete(self, index: int) -> object:  # 刪除指定位置的元素
        if index == 0:
            self.pop_head()
        elif index == len(self.__node) - 1:
            self.pop_tail()
        else:
            d = self.__node[index].data
            self.__node[index - 1].next = self.__node[index].next
            del self.__node[index]
            return d
