class PTNode(object):  # 節點結構
    def __init__(self, data: object = None, parent: int = -1):
        super(PTNode, self).__init__()
        self.data = data  # 存放該節點的數據
        self.parent = parent  # 指向其父母的下標


class PTree(object):  # 樹結構
    def __init__(self, l: list = None):
        super(PTree, self).__init__()
        self.nodes = []  # 存放節點
        self.r = None  # 根的位置
        self.n = 0  # 結點數

    def clear_tree(self) -> None:
        self.nodes = []
        self.r = None
        self.n = 0

    def create_tree(self, l: list) -> None:
        if l is not None:
            pass

    def tree_empty(self) -> bool:
        return not bool(len(self.nodes))

    def tree_depth(self) -> int:
        d = 0
        if not self.tree_empty():
            for x in self.nodes:
                if d < x.parent:
                    d = x.parent
            return d + 2
        return d

    def root(self) -> PTNode:
        return self.r

    def value(self, cur: PTNode) -> object:
        return cur.data

    def parent(self, cur: PTNode) -> PTNode | None:
        return self.nodes[cur.parent]

    def left_child(self, cur: PTNode) -> PTNode | None:
        # for x in self.nodes:
        #     if x.parent == self.nodes.index(cur):
        #         return x
        #
        # return None
        return self.all_child(cur)[0]

    def right_sibling(self, cur: PTNode) -> PTNode | None:
        # for x in self.nodes:
        #     if x.parent == cur.parent:
        #         return x
        # return None
        return self.all_sibling(cur)[0]

    def insert_child(self, cur: PTNode, c: PTNode) -> None:
        c.parent = self.nodes.index(cur)
        self.nodes.append(c)
        self.n += 1

    def delete_child(self, cur: PTNode, i: int) -> None:
        run = i
        temp = None
        for x in self.nodes:
            if i:
                if x.parent == self.nodes.index(cur):
                    temp = x
                    i -= 1
            else:
                self.nodes.pop(self.nodes.index(temp))

    def set_root(self, cur: PTNode) -> None:
        cur.parent = -1
        self.nodes.append(cur)
        self.r = cur
        self.n += 1

    def insert(self, cur: PTNode, c: PTNode = None):
        if self.tree_empty():
            self.set_root(cur)
        else:
            self.insert_child(cur, c)

    def all_child(self, cur: PTNode) -> list:
        temp = []
        for x in self.nodes:
            if x.parent == self.nodes.index(cur):
                temp.append(x)
        return temp

    def all_sibling(self, cur: PTNode) -> list:
        temp = []
        for x in self.nodes:
            if x.parent == cur.parent:
                temp.append(x)
        return temp
