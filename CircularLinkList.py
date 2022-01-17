class Node(object):  # 創建一個節點
    def __init__(self, e=None, n=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = n  # 指針域


class CircularLinkList(object):  # 創建一個單鏈表 #TODO 應加入頭指針 方便操作
    def __init__(self, L=None):
        super(CircularLinkList, self).__init__()
        self.__head = Node()  # 防止外部改變頭節點 (沒有設定頭指針)
        self.__len = 0  # 防止外部改變鏈表長度
        self.__end = Node()
        self.init(L)

    def init(self, L):  # 初始化把列表轉為換鏈表
        if L is not None:
            for x in L:
                self.add_tail(x)

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

    def locate_elem(self, e):  # 查找鏈表中是否含有給定值元素e查找成功返回True,否則返回False
        node = self.__head
        for x in range(self.__len):
            if node.element == e:
                return True
            node = node.next
        return False

    def pop_head(self):  # 刪除並返回鏈表開頭的節點
        temp = self.__head
        self.__len -= 1
        self.__head = self.__head.next
        return temp

    def pop_tail(self):  # 刪除並返回鏈表結尾的節點
        last_node = self.__head
        self.__len -= 1
        for x in range(self.__len - 1):  # 獲取要刪除的節點的前一個節點
            last_node = last_node.next
        temp = last_node.next.element
        last_node.next = None  # 把指向要刪除的節點的指針設為空
        return temp

    def list_delete(self, index):  # 刪除並返回鏈表第index個位置的後一個節點
        node = self.__head
        self.__len -= 1
        i = 0
        while node.next is not None and i < index < self.__len and index >= 0:  # 遍歷至指定的索引位置
            node = node.next
            i += 1
        temp = node.next
        node.next = node.next.next  # 把當前節點的指針指向下一個節點的指針(跳過下一個節點)
        return temp

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

    def add_head(self, data):  # 在鏈表開頭新增元素
        new_node = Node(data)
        self.__len += 1
        if self.__head is None:
            self.__head = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node

    def list_insert(self, index, data):  # 在鏈表中第index個位置後插入新的節點 TODO (預期: 插入i的位置 目前情況: 插在i的位置後 不能插在頭/尾節點)
        new_node = Node(data)
        node = self.__head
        self.__len += 1
        i = 0
        while node.next is not None and i < index < self.__len and index >= 0:
            node = node.next
            i += 1
        new_node.next = node.next
        node.next = new_node

    def list_head(self):  # 獲取鏈表頭節點
        return self.__head

    def list_length(self):  # 獲取鏈表的長度
        return self.__len

    def get_list(self):  # 以list的列式返回鏈表中全部元素
        data = []
        for x in range(1,self.list_length()+1):
            data.append(self.get_elem(x))  # 獲取當前節點的元素
        return data

    def get_node_list(self):  # 以list的列式返回鏈表中全部節點
        data = []
        for x in range(1,self.list_length()+1):
            temp = self.get_node(x)
            if temp is not None:
                data.append(temp)  # 獲取當前節點的元素
        return data
