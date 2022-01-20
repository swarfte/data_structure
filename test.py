from SqList import SqList
from LinkList import LinkList
from StaticLinkList import StaticLinkList
from CircularLinkList import CircularLinkList
from DoublyLinkedList import DoublyLinkedList


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
    c.list_insert(2,123)
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
    L = LinkList([1, 2, 3, 4, 5])
    # L = LinkList()
    L.pop_tail()
    L.add_tail(12)
    L.pop_head()
    L.add_head(123)
    L.list_insert(0, 234)
    print(L.list_delete(2).element)
    print(L.locate_elem(234))
    print(L.get_list())
    print(L.list_length())


# def my_gen(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1


if __name__ == '__main__':
    # SqList_test()
    # LinkList_test()
    # StaticLinkList_test()
    CircularLinkList_test()
    # DoublyLinkedList_test()
