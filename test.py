from SqList import SqList
from LinkList import LinkList
from StaticLinkList import StaticLinkList


def StaticLinkList_test():
    # SL = StaticLinkList()
    pass

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
    L.add_tail(12) # 0
    L.add_tail(24) # 1
    L.add_head(789) # 2
    L.list_insert(100,123)
    L.add_tail(45)
    L.add_tail(77)
    # print(L.pop_tail())
    print(L.get_elem(1))
    print(L.list_last().element)
    print(L.get_list())
    L.clear_list()
    print(L.get_list())
    # print(L.get_node_list())
    print(L.list_length())


if __name__ == '__main__':
    #SqList_test()
    LinkList_test()
    # StaticLinkList_test()
