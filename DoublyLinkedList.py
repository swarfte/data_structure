class Node(object):  # 創建一個節點
    def __init__(self, e=None, n=None, p=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = n  # 後驅指針域
        self.prior = p  # 前驅指針域
