class PTNode(object):
    def __init__(self, data=None, parent=-1):
        super(PTNode, self).__init__()
        self.data = data
        self.parent = parent


class PTree(object):
    def __init__(self, l: list = None):
        super(PTree, self).__init__()
        pass

    def clear_tree(self) -> None:
        pass

    def tree_empty(self) -> bool:
        pass

    def tree_depth(self) -> int:
        pass

    def value(self, cur: PTNode) -> object:
        pass

    def parent(self, cur: PTNode) -> PTNode | None:
        pass

    def left_child(self, cur: PTNode) -> PTNode | None:
        pass

    def right_sibling(self, cur: PTNode) -> PTNode | None:
        pass

    def insert_child(self, i: int, c: "CTree") -> None:
        pass

    def delete_child(self, cur: PTNode, i: int) -> None:
        pass
