class SqList(object):
    def __init__(self, DataType, L=None):  # 初始化操作,建立一個空的線性表
        super(SqList, self).__init__()
        self.__data_type = DataType  # 每個類型均為DataType(即單一類型)
        self.__list = []
        self.__list_len = 0
        self.init(L)

    def init(self, L):
        if L is not None:
            for x in L:
                self.add_tail(x)

    def list_empty(self):  # 若線性表為空,返回True,否則返回False
        if len(self.__list) == 0:
            return True
        else:
            return False

    def clear_list(self):  # ClearList 將線性表清空
        self.__list = []

    def get_elem(self, i):  # GetElem 返回線性表中的第i個位置元素值
        return self.__list[i]

    def locate_elem(self, e):  # LocateElem 在線性表中查找給定值e相等的元素,如果查找成功,返回該元素在表中序號表示成功,否則返回-1表示失敗
        for x in range(self.__list_len):
            if self.__list[x] == e:
                return x
        return -1

    def add_tail(self, e):  # 在線性表結尾插入元素e
        if isinstance(e, self.__data_type):
            self.__list.append(e)
            self.__list_len += 1
        else:
            raise TypeError

    def add_head(self, e):  # 在線性表開頭插入元素e
        if isinstance(e, self.__data_type):
            self.__list = [e] + self.__list
            self.__list_len += 1
        else:
            raise TypeError

    def pop_tail(self):  # 刪除並返回線性表中最後的元素
        self.__list_len -= 1
        temp = self.__list[self.__list_len]
        self.__list = self.__list[:self.__list_len]
        return temp

    def pop_head(self):  # 刪除並返回線性表中第一個元素
        self.__list_len -= 1
        temp = self.__list[0]
        self.__list = self.__list[1:]
        return temp

    def list_insert(self, i, e):  # ListInsert 在線性表中第i個位置插入元素e
        if isinstance(e, self.__data_type):
            self.__list = self.__list[:i] + [e] + self.__list[i:]
            self.__list_len += 1
        else:
            raise TypeError

    def list_delete(self, i):  # ListDelete 刪除並返回線性表中第i個位置元素
        temp = self.__list[i]
        self.__list = self.__list[:i] + self.__list[i + 1:]
        self.__list_len -= 1
        return temp

    def list_length(self):  # ListLength 返回線性表的元素個數
        return self.__list_len

    def get_list(self):  # GetList 返回整個線性表
        return self.__list

    def get_DataType(self):  # 返回線性表的數據類型
        return self.__data_type
