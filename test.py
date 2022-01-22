from SqList import SqList
from LinkList import LinkList
from StaticLinkList import StaticLinkList
from CircularLinkList import CircularLinkList
from DoublyLinkedList import DoublyLinkedList
from SequentialStack import SequentialStack
from ChainStack import ChainStack


def ChainStack_test():
    c = ChainStack([x for x in range(5)])
    c.pop()
    print(c.get_top().element)
    c.push(123)
    print(c.get_top().element)
    print(c.stack_lengths())


def SequentialStack_test():
    s = SequentialStack([x for x in range(4)])
    s.push(123)
    print(s.get_top())
    s.pop()
    print(s.pop())
    print(s.stack_lengths())


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
    l = LinkList([x for x in range(5)])
    l.add_head(5)
    l.list_insert(2, 123)
    l.add_head(87)
    l.pop_tail()
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
    # equentialStack_test()
    ChainStack_test()
