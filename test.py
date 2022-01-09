from SqList import SqList
from LinkList import LinkList
from StaticLinkList import StaticLinkList


def StaticLinkList_test():
    SL = StaticLinkList()


def SqList_test():
    S = SqList(int)
    for x in range(10):
        S.list_insert(x, x * 10)
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
    L = LinkList()
    L.add_tail(12)
    L.add_tail(23)
    L.add_tail(34)
    print(L.get_elem(1))
    print(L.get_list())
    print(L.list_length())


if __name__ == '__main__':
    SqList_test()
    # LinkList_test()
    # StaticLinkList_test()
