from SqList import SqList
from LinkList import LinkList
from StaticLinkList import StaticLinkList
from CircularLinkList import CircularLinkList
from DoublyLinkedList import DoublyLinkedList
from SequentialStack import SequentialStack
from ChainStack import ChainStack
from SequentialStack import Postfix


# from ChainStack import Postfix


def postfix_expression_test():
    infix = "9+(3-1)*3+10/2"  # 進階的四則運算也OK
    # infix = "3*(5+4)" # 簡單括號運算OK
    # infix = "3*5+40/8*5-7/9*5" # 沒括號四則運算OK
    # infix = "2*3/6" # 同級運算OK
    print(infix)
    p = Postfix(infix)
    print(p.get_postfix())


def ChainStack_test():
    c = ChainStack([x for x in range(5)])
    # c.pop()
    # print(c.get_top().element)
    # c.push(123)
    # print(c.get_top().element)
    # print(c.stack_lengths())
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
#     i = 0
#     while i < n:
#         yield i
#         i += 1


if __name__ == '__main__':
    # SqList_test()
    # LinkList_test()
    # StaticLinkList_test()
    # CircularLinkList_test()
    # DoublyLinkedList_test()
    # SequentialStack_test()
    # ChainStack_test()
    postfix_expression_test()
