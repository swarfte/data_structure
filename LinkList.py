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
        self.__last = None

    def get_elem(self, index):  # 獲取單鏈表中第i個數據元素的值
        node = self.__head
        i = 1  # 之所以用素引1開始查找 是因為返回值時會查找下一個節點
        while node.next is not None and i < index:
            node = node.next  # 移動到下一個節點
            i += 1
        return node.next.element

    def list_empty(self):  # 判斷鏈表是否為空
        if self.__head is not None:
            return True
        else:
            return False

    def clear_list(self):  # 把鏈表清空
        self.__head = None

    def pop_tail(self):  # 在鏈表結尾刪除元素
        self.__len -= 1

    def add_tail(self, data):  # 在鏈表結尾新增元素
        new_node = Node(data)  # 創建一個節點
        self.__len += 1
        if self.__head is None:  # 如果是鏈表第一個節點則設為頭節點
            self.__head = new_node
        else:  # 已經設置了頭節點的情況下
            last_node = self.__head  # 獲取頭節點 且不改動頭節點
            while last_node.next is not None:  # 直至找到最後的節點
                last_node = last_node.next  # 移動到下一個節點
            last_node.next = new_node  # 把最後節點的指針域中的指針指向新節點

    def list_head(self):  # 獲取鏈表頭節點
        return self.__head

    def list_length(self):  # 獲取鏈表的長度
        return self.__len

    def get_list(self):  # 以list的列式返回鏈表中全部元素
        data = []
        for x in range(self.list_length()):
            data.append(self.get_elem(x))  # 獲取當前節點的元素
        return data
