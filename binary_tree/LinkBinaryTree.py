class BinaryTreeNode(object):  # 二叉樹節點
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class LinkBinaryTree(object):  # 鏈表二叉樹
    def __init__(self, array=None):
        self.root = None  # 根節點
        self.height = 0  # 樹的高度
        self.members = 0  # 樹的節點數量
        if array:
            for x in array:
                self.__add__(x)

    def __bool__(self) -> bool:  # 判斷是否為空節點
        return bool(self.root)

    def __len__(self) -> int:  # 二叉樹數量
        return self.members

    def __getitem__(self, index: int) -> BinaryTreeNode:  # 獲取指定節點
        return self.find_node(index)

    def __setitem__(self, index: int) -> None:  # 設定節點
        pass

    def __iter__(self) -> BinaryTreeNode:  # 按高度依次生成元素(bfs)
        if self.__bool__():
            yield from self.bfs_traverse()

    def __delitem__(self, index: int) -> None:  # 刪除指定位置節點
        pass

    def __add__(self, node: BinaryTreeNode) -> None:  # 順序插入節點
        self.order_insert(node)

    def __sub__(self, node: BinaryTreeNode) -> None:  # 刪除指定的節點
        pass

    def check_index(self, index: int) -> bool:  # 檢測索引值是否合理
        return True if index < self.members else False

    def find_node(self, index: int) -> BinaryTreeNode:  # 返回指定素引值的節點
        t = self.root
        for x in self.find_node_path(index)[1:]:  # length = log 2 (index)
            t = t.left if x % 2 == 0 else t.right
        return t

    def find_node_path(self, index: int) -> list:  # 輸出找到素引值所需的路徑
        index += 1
        node = []
        while index > 1:
            node.append(index)
            index //= 2
        return [1] + node[::-1]

    def preorder_traverse(self) -> list:  # 前序遍歷 (dfs遍歷)
        data, stack = [], [self.root]
        while stack:
            nodes = stack.pop()  # 優先行左節點 再到右節點
            data.append(nodes)
            if nodes.right:
                stack.append(nodes.right)
            if nodes.left:
                stack.append(nodes.left)
        yield from data

    def inorder_traverse(self) -> list:  # 中序遍歷
        data, stack = [], []
        nodes = self.root
        while True:
            if nodes:  # 如果左/右節點存在的話
                stack.append(nodes)  # 記錄前進路徑
                nodes = nodes.left
            elif stack:  # 節點為空,則回到上一個節點並放入列表
                nodes = stack.pop()  # 回到上一個節點
                data.append(nodes)
                nodes = nodes.right  # 搜查右節點的路徑
            else:  # 沒有退路時則中止
                break
        yield from data

    def postorder_traverse(self) -> list:  # 後序遍歷
        data, stack = [], [self.root]
        while stack:
            nodes = stack.pop()  # 優先行右節點 然後再行左節點
            data.append(nodes)
            if nodes.left:
                stack.append(nodes.left)
            if nodes.right:
                stack.append(nodes.right)
        yield from data[::-1]  # 由於遍歷的方法是由上至下 由右至左,所以要翻轉為由下至上 由左至右

    def bfs_traverse(self) -> list:  # 層序遍歷 (BFS遍歷)
        data, queue = [], [self.root]
        while queue:
            nodes = queue.pop(0)
            data.append(nodes)
            if nodes.left:
                queue.append(nodes.left)
            if nodes.right:
                queue.append(nodes.right)
        yield from data

    def addition_node(self) -> None:  # 當新增節點時改變樹的狀態
        self.members += 1
        t = self.members
        h = 0  # 根節點為0
        while t > 1:
            t //= 2
            h += 1
        self.height = h

    def order_insert(self, node: BinaryTreeNode) -> None:  # 順序插入法
        self.addition_node()
        if self.root is None:
            self.root = node
        else:  # BFS算法
            queue = [self.root]
            while queue:
                nodes = queue.pop(0)
                if nodes.left is None:
                    nodes.left = node
                    break
                elif nodes.right is None:
                    nodes.right = node
                    break
                else:
                    queue.append(nodes.left)
                    queue.append(nodes.right)
