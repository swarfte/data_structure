class CTNode(object):  # 孩子結構
    def __init__(self, child: int = -1, nxt: "CTNode" = None):
        super(CTNode, self).__init__()
        self.child = child  # 存放該節點在數組中的下標
        self.nxt = nxt  # 指向同一父母其他孩子


class CTBox(object):  # 表頭結構
    def __init__(self, data: object = None, first_child: "CTNode" = None):
        super(CTBox, self).__init__()
        self.data = data  # 存放該節點的數據
        self.first_child = first_child  # 指看第一個孩子


class CTree(object):
    def __init__(self, l: list = None):
        super(CTree, self).__init__()
        pass

    def clear_tree(self) -> None:
        pass

    def create_tree(self, l: list) -> None:
        pass

    def tree_empty(self) -> bool:
        pass

    def tree_depth(self) -> int:
        pass

    def value(self, cur: CTNode) -> object:
        pass

    def parent(self, cur: CTNode) -> CTNode | None:
        pass

    def left_child(self, cur: CTNode) -> CTNode | None:
        pass

    def right_sibling(self, cur: CTNode) -> CTNode | None:
        pass

    def insert_child(self, i: int, c: "CTree") -> None:
        pass

    def delete_child(self, cur: CTNode, i: int) -> None:
        pass
