class Node(object):  # 創建一個節點
    def __init__(self, e=None, n=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = n  # 指針域


class CircularLinkList(object):  # 創建一個單鏈表 #TODO 應加入頭指針 方便操作
    def __init__(self, L=None):
        super(CircularLinkList, self).__init__()
        self.__head = Node()  # 防止外部改變頭節點 (沒有設定頭指針)
        self.__end = Node()