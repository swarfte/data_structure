class SqList(object):
    def __init__(self, DataType: object, l: list = None):  # 初始化操作,建立一個空的線性表
        super(SqList, self).__init__()
        self.__data_type = DataType  # 每個類型均為DataType(即單一類型)
        self.__list = []
        self.__list_len = 0
        self.list_convert(l)

    def list_convert(self, l: list) -> None:
        if l is not None:
            for x in l:
                self.add_tail(x)

    def list_empty(self) -> bool:  # 若線性表為空,返回True,否則返回False
        return bool(self.__list_len)

    def clear_list(self) -> None:  # ClearList 將線性表清空
        self.__list = []

    def get_elem(self, index: int) -> object:  # GetElem 返回線性表中的第i個位置元素值
        return self.__list[index]

    def locate_elem(self, e: object) -> int:  # LocateElem 在線性表中查找給定值e相等的元素,如果查找成功,返回該元素在表中序號表示成功,否則返回-1表示失敗
        for x in range(self.__list_len):
            if self.__list[x] == e:
                return x
        return -1

    def add_tail(self, e: object) -> None:  # 在線性表結尾插入元素e
        if isinstance(e, self.__data_type):
            self.__list.append(e)
            self.__list_len += 1
        else:
            raise TypeError

    def add_head(self, e: object) -> None:  # 在線性表開頭插入元素e
        if isinstance(e, self.__data_type):
            self.__list = [e] + self.__list
            self.__list_len += 1
        else:
            raise TypeError

    def pop_tail(self) -> object:  # 刪除並返回線性表中最後的元素
        self.__list_len -= 1
        temp = self.__list[self.__list_len]
        self.__list = self.__list[:self.__list_len]
        return temp

    def pop_head(self) -> object:  # 刪除並返回線性表中第一個元素
        self.__list_len -= 1
        temp = self.__list[0]
        self.__list = self.__list[1:]
        return temp

    def list_insert(self, index: int, e: object) -> None:  # ListInsert 在線性表中第i個位置插入元素e
        if isinstance(e, self.__data_type):
            self.__list = self.__list[:index] + [e] + self.__list[index:]
            self.__list_len += 1
        else:
            raise TypeError

    def list_delete(self, index: int) -> object:  # ListDelete 刪除並返回線性表中第i個位置元素
        temp = self.__list[index]
        self.__list = self.__list[:index] + self.__list[index + 1:]
        self.__list_len -= 1
        return temp

    def list_length(self) -> int:  # ListLength 返回線性表的元素個數
        return self.__list_len

    def get_list(self) -> list:  # GetList 返回整個線性表
        return self.__list

    def get_DataType(self) -> object:  # 返回線性表的數據類型
        return self.__data_type
