class SqList:
    def __init__(self, DataType):  # 初始化操作,建立一個空的線性表
        super(SqList, self).__init__()
        self.data_type = DataType  # 每個類型均為DataType(即單一類型)
        self.list = []
        self.list_len = 0

    def list_empty(self):  # 若線性表為空,返回True,否則返回False
        if len(self.list) == 0:
            return True
        else:
            return False

    def clear_list(self):  # ClearList 將線性表清空
        self.list = []

    def get_elem(self, i):  # GetElem 返回線性表中的第i個位置元素值
        return self.list[i]

    def locate_elem(self, e):  # LocateElem 在線性表中查找給定值e相等的元素,如果查找成功,返回該元素在表中序號表示成功,否則返回-1表示失敗
        for x in range(self.list_len):
            if self.list[x] == e:
                return x
        return -1

    def list_insert(self, i, e):  # ListInsert 在線性表中第i個位置插入元素e
        if isinstance(e, self.data_type):
            self.list = self.list[:i] + [e] + self.list[i:]
            self.list_len += 1
        else:
            raise TypeError

    def list_delete(self, i):  # ListDelete 刪除線性表中第i個位置元素,
        temp = self.list[i]
        self.list = self.list[:i] + self.list[i + 1:]
        self.list_len -= 1
        return temp

    def list_length(self):  # ListLength 返回線性表的元素個數
        return self.list_len

    def get_list(self):  # GetList 返回整個線性表
        return self.list
