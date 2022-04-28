from list.SqList import SqList
from list.LinkList import LinkList
from list.StaticLinkList import StaticLinkList
from list.CircularLinkList import CircularLinkList
from list.DoublyLinkedList import DoublyLinkedList
from stack.SequentialStack import SequentialStack
from stack.ChainStack import ChainStack
from stack.SequentialStack import Postfix
from pyqueue.SqQueue import SqQueue
from pyqueue.ChainQueue import ChainQueue
from tree.ParentalNotation import PTree, PTNode
from tree.LinkBinaryTree import LinkBinaryTree, BinaryTreeNode
from graph.MatrixGraph import MatrixGraph

def MatrixGraph_test():
    pass


def LinkBinaryTree_test():
    # tree = LinkBinaryTree((BinaryTreeNode(x) for x in
    #                        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
    #                         "s", "t", "u", "v", "w", "x", "y", "z"]))
    tree = LinkBinaryTree((BinaryTreeNode(x) for x in range(1, 123)))
    root = tree.root
    print(len(tree))
    print(tree)
    tree - BinaryTreeNode(3)
    print(len(tree))
    print(tree)
    # print(root.right.left.right.left.data)  # 1 ->3-> 6-> 13-> 26(z)
    # print(tree[10].data)
    # tree[10].data = 55
    # print(tree[10].data)
    #
    # print(tree[10].left.data)
    # tree[10].left = tree[11].right
    # print(tree[10].left.data)
    # print(len(tree))
    # del tree[3]
    # print(len(tree))
    # # print([x.data for x in tree.preorder_traverse()])
    # print([x.data for x in tree.inorder_traverse()])
    # print([x.data for x in tree.postorder_traverse()])
    # print([x.data for x in tree.bfs_traverse()])
    # print(tree.height)
    # print(tree.find_node_path(14))
    # for x in tree:
    #     print(x.data)
    # print(len(tree))

    pass


def PTree_test():
    p = PTree()
    p.insert(PTNode("A"))
    root = p.root()
    # print(p.root().data)
    p.insert(root, PTNode("B"))
    p.insert(root, PTNode("C"))
    root_child = p.all_child(root)
    p.insert(root_child[0], PTNode("D"))
    p.insert(root_child[1], PTNode("E"))
    p.insert(root_child[1], PTNode("F"))
    b_child = p.left_child(root_child[0])
    p.insert(b_child, PTNode("G"))
    p.insert(b_child, PTNode("H"))
    p.insert(b_child, PTNode("I"))
    p.delete_child(b_child, 1)  # 刪去了中間的"H"節點
    for x in p.all_child(b_child):
        print(x.data)
    print(p.tree_depth())


def ChainQueue_test():
    c = ChainQueue([x for x in range(10)])
    print(c.get_head())
    print(c.get_queue())
    print(c.delete_queue())
    print(c.delete_queue())
    print(c.get_queue())
    print(c.queue_length())


def SqQueue_test():
    s = SqQueue([x for x in range(5)])
    print(s.queue_length())
    print(s)
    print(s.delete_queue())
    print(s)


def postfix_expression_test():
    infix = "9+(3-1)*3+10/2"  # 進階的四則運算也OK
    # infix = "3*(5+4)" # 簡單括號運算OK
    # infix = "3*5+40/8*5" # 沒括號四則運算OK
    # infix = "2*3/6" # 同級運算OK
    print(infix)
    c = Postfix(infix)
    print(c.get_postfix())
    print(c.calc())


def ChainStack_test():
    c = ChainStack([x for x in range(5)])
    c.pop()
    print(c.get_top().element)
    c.push(123)
    print(c.get_top().element)
    print(c.stack_lengths())
    while c.stack_empty():
        print(c.pop())


def SequentialStack_test():
    s = SequentialStack([x for x in range(4)])
    # s.push(123)
    # print(s.get_top())
    # s.pop()
    # print(s.pop())
    # print(s.stack_lengths())
    while s.stack_empty():
        print(s.pop())


def DoublyLinkedList_test():
    d = DoublyLinkedList([x for x in range(1, 6, 2)])
    print(d.get_list())
    print(d.get_elem(2))
    print(d.locate_elem(5))
    d.pop_head()
    d.pop_tail()
    d.add_tail(12)
    d.add_head(19)
    d.list_insert(0, 159)
    d.list_insert(d.list_length(), 888)
    d.list_insert(d.list_length() // 2, 555)
    d.list_delete(1)
    print(d.get_list())
    print(d.get_node(2).prior.prior.prior.prior.prior.element)


def CircularLinkList_test():
    c = CircularLinkList([x for x in range(5)])
    print(c.list_empty())
    print(c.add_head(12))
    print(c.list_empty())
    c.pop_head()
    c.pop_tail()
    t = c.get_node_list()
    print(t[3].next.next.next.element)
    c.list_insert(2, 123)
    c.list_delete(1)
    print(c.get_list())
    print(c.locate_elem(3))


def StaticLinkList_test():
    a = ["ab0", "cc", "ee"]
    s = StaticLinkList(a)
    s.add_tail("rra")
    s.add_head("qwe")
    s.add_head("ppp")
    s.list_insert(2, "test")
    s.print_list()
    print(s.get_elem(2))
    print(s.locate_elem("test"))
    print(s.pop_tail())
    s.pop_head()
    s.list_delete(1)
    s.print_list()


def SqList_test():
    # S = SqList(int)
    # for x in range(10):
    #     S.list_insert(x, x * 10)
    S = SqList(int, [x for x in range(5)])
    S.list_insert(5, 123)
    print(S.get_list())
    print(S.list_length())
    print(S.get_list())
    print(S.locate_elem(123))
    print(S.list_empty())
    print(S.pop_head())
    S.add_head(456)
    print(S.get_list())


def LinkList_test():
    l = LinkList([x for x in range(100, 0, -1)])
    print(l.get_list())


# def my_gen(n):
#     index = 0
#     while index < n:
#         yield index
#         index += 1


if __name__ == '__main__':
    # SqList_test()
    # LinkList_test()
    # StaticLinkList_test()
    # CircularLinkList_test()
    # DoublyLinkedList_test()
    # SequentialStack_test()
    # ChainStack_test()
    # postfix_expression_test()
    # SqQueue_test()
    # ChainQueue_test()
    # PTree_test()
    LinkBinaryTree_test()
