class CTChild(object):  # (孩子)節點結構
    def __init__(self, child: int, nxt: "CTChild" = None):
        super(CTChild, self).__init__()
        self.child = child  # 存放該節點在數組中的下標
        self.nxt = nxt  # 指向同一父母其他孩子的指針域


class CTNode(object):  # (表頭)節點結構
    def __init__(self, data: object = None, parent: int = -1, first_child: CTChild = None):
        super(CTNode, self).__init__()
        self.data = data  # 存放該節點的數據
        self.parent = parent
        self.first_child = first_child  # 指看第一個孩子的指針域


class CTree(object):
    def __init__(self):
        super(CTree, self).__init__()
        self.nodes = []
        self.r = None
        self.n = 0

    def clear_tree(self) -> None:
        self.nodes = []
        self.r = None
        self.n = 0

    def tree_empty(self) -> bool:
        return not bool(self.n)

    def tree_depth(self) -> int:
        # 此處應用DFS算法
        pass

    def root(self) -> CTNode:
        return self.r

    def value(self, cur: CTNode) -> object:
        return cur.data

    def parent(self, cur: CTNode) -> CTNode | None:
        if cur.parent != - 1:
            return self.nodes[self.nodes.index(cur.parent)]
        else:
            return None

    def left_child(self, cur: CTNode) -> CTNode | None:  # 該節點的第一個孩子
        if self.empty_child(cur):
            return None
        else:
            return cur.first_child

    def right_sibling(self, cur: CTNode) -> CTNode | None:
        temp = self.all_sibling(cur)
        if len(temp):
            return temp[0]
        else:
            return None

    def empty_child(self, cur: CTNode) -> bool:
        return True if cur.first_child is None else False

    def insert_child(self, cur: CTNode, c: CTNode) -> None:
        c.parent = self.nodes.index(cur)
        self.nodes.append(c)
        child = CTChild(self.nodes.index(c))
        if self.empty_child(cur):
            cur.first_child = child
        else:
            temp = cur.first_child
            while temp.nxt is not None:
                temp = temp.nxt
            temp.nxt = child

    # def refresh(self): # 刷新樹的狀態
    #     node_parents_index = [x.parent for x in self.nodes]
    #     for x in self.nodes:
    #         if not self.empty_child(x):
    #             child = x.first_child
    #             while child.nxt is not None:
    #                 pass


    def delete_child(self, cur: CTNode, i: int) -> None:  # 刪除該節回的第i個子節點(孩子)
        node = cur.first_child
        for x in range(i-1):
            node = node.nxt
        node_index   = node.child
        if node.nxt is not None:
            pass
        # if i == 0 and node.nxt is not None:
        #     cur.first_child = node.nxt
        # else:
        #     cur.first_child = None
        # if i > 0:
        #     if node.nxt is not None:
        #         node.nxt = node.nxt.nxt

    def all_child(self, cur: CTNode) -> list:
        children = []
        if not self.empty_child(cur):
            temp = cur.first_child
            while temp.nxt is not None:
                children.append(temp)
                temp = temp.nxt
        return children

    def all_sibling(self, cur: CTNode) -> list:
        children = []
        for x in self.nodes:
            if x.parent == cur.parent and x != cur:
                children.append(x)
        return children

    def set_root(self, cur: CTNode) -> None:
        self.r = cur
        self.n += 1
        cur.parent = -1
        self.nodes.append(cur)

    def insert(self, cur: CTNode, c: CTNode = None):
        if self.tree_empty():
            self.set_root(cur)
        else:
            self.insert_child(cur, c)
