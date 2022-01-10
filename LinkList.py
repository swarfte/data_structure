class Node(object):  # 創建一個節點
    def __init__(self, e=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = None  # 指針域


class LinkList(object):  # 創建一個單鏈表
    def __init__(self):
        super(LinkList, self).__init__()
        self.__head = None  # 防止外部改變頭節點
        self.__len = 0  # 防止外部改變鏈表長度
        self.__last = None  # 防止外部改變尾節點

    def get_elem(self, index):  # 獲取單鏈表中第i個數據元素的值
        node = self.__head
        i = 0
        if node is not None:
            while node.next is not None and i < index:
                node = node.next  # 移動到下一個節點
                i += 1
            return node.element

    def get_node(self, index):  # 獲取鏈表中第i個節點
        node = self.__head
        i = 0
        if node is not None:
            while node.next is not None and i < index:
                node = node.next  # 移動到下一個節點
                i += 1
            return node

    def list_empty(self):  # 判斷鏈表是否為空
        if self.__head is not None:
            return True
        else:
            return False

    def clear_list(self):  # 把鏈表清空
        self.__head = None
        self.__len = 0
        self.__last = None

    def pop_tail(self):  # 在鏈表結尾刪除元素
        pass

    #     node = None
    #     self.__len -= 1
    #     for x in range(self.__len):  # 遍歷至倒數第二個節點
    #         node = self.__head.next
    #     self.__last = node
    #     temp = self.__last.next.element
    #     self.__last.next = None
    #     return temp

    def add_tail(self, data):  # 在鏈表結尾新增元素
        new_node = Node(data)  # 創建一個節點
        self.__len += 1
        if self.__head is None:  # 如果是鏈表第一個節點則設為頭節點
            self.__head = new_node
            self.__last = self.__head
        else:  # 已經設置了頭節點的情況下
            self.__last.next = new_node  # 先把目前最後節點的指針指向新節點
            self.__last = new_node  # 把新節點設置為最後節點

            # last_node = self.__head  # 獲取頭節點 且不改動頭節點
            # while last_node.next is not None:  # 直至找到最後的節點
            #     last_node = last_node.next  # 移動到下一個節點
            # last_node.next = new_node  # 把最後節點的指針域中的指針指向新節點

    def add_head(self, data):  # 在鏈表開頭新增元素
        new_node = Node(data)
        self.__len += 1
        if self.__head is None:
            self.__head = new_node
            self.__last = self.__head
        else:
            new_node.next = self.__head
            self.__head = new_node

    def list_insert(self, index, data):  # 在鏈表中第index位置插入元素data
        new_node = Node(data)
        node = self.__head
        self.__len += 1
        i = 0
        if node is not None:
            while node.next is not None and i < index :
                node = node.next
                i += 1
        if index >= self.__len:
            raise ValueError
        if node == self.__head:
            self.add_head(data)
        elif node == self.__last :
            self.add_tail(data)
        else:
            new_node.next = node.next
            node.next = new_node

    def list_head(self):  # 獲取鏈表頭節點
        return self.__head

    def list_last(self):  # 獲取鏈表尾節點
        return self.__last

    def list_length(self):  # 獲取鏈表的長度
        return self.__len

    def get_list(self):  # 以list的列式返回鏈表中全部元素
        data = []
        for x in range(self.list_length()):
            data.append(self.get_elem(x))  # 獲取當前節點的元素
        return data

    def get_node_list(self):  # 以list的列式返回鏈表中全部節點
        data = []
        for x in range(self.list_length()):
            temp = self.get_node(x)
            if temp is not None:
                data.append(temp)  # 獲取當前節點的元素
        return data
