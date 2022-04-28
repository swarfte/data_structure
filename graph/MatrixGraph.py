class MatrixGraph(object):
    def __init__(self, vertex: dict = None, relationship: dict = None):
        super(MatrixGraph, self).__init__()
        self.relationship = {}  # 頂點之間的關係(弧)
        self.vertex_number = 0  # 頂點數量
        self.vertexes = {}  # 頂點的值
        self.matrix = []  # 鄰接矩陣圖
        self.create_graph(vertex, relationship)

    def __bool__(self):  # 判斷矩陣圖是否存在
        return bool(self.vertex_number)

    def __len__(self):  # 返回頂點的數量
        return self.vertex_number

    def __getitem__(self, vertex: str):  # 獲取指定頂點的值
        return self.get_vex(vertex)

    def __setitem__(self, vertex: str, value):  # 對指定頂點賦值
        self.put_vex(vertex, value)

    def __delitem__(self, vertex: str):  # 刪除指定頂點
        pass

    def create_graph(self, vertex: dict, relationship: dict):  # 創建矩陣圖
        # example -> vertexes = {"a" :1,"b":2,"c":3}, relationship = {"a" : ["a","c"],"b":["c"],"c":["a"]}
        if vertex and relationship:
            self.relationship = relationship  # 頂點之間的關係(弧)
            self.vertex_number = len(vertex)  # 頂點數量
            self.vertexes = vertex  # 頂點的值
            for x in self.vertexes.keys():
                row = []
                for y in self.vertexes.keys():
                    if y in self.relationship[x]:  # 頂點間存在弧
                        row.append(1)
                    else:
                        row.append(0)
                self.matrix.append(row)

    def check_vertex(self, vertex: str):  # 檢查頂點是否在圖中
        if vertex in self.vertexes:
            return True
        else:
            return False

    def destroy_graph(self):  # 刪除矩陣圖
        self.relationship = {}
        self.vertex_number = 0
        self.vertexes = {}
        self.matrix = []

    def locate_vex(self, vertex: str):  # 找到該頂點在圖中的位置
        if self.check_vertex(vertex):
            return list(self.vertexes.keys()).index(vertex)

    def get_vex(self, vertex: str):  # 返回該頂點的值
        if self.check_vertex(vertex):
            return self.vertexes[vertex]

    def put_vex(self, vertex: str, value):  # 對頂點賦值
        if self.check_vertex(vertex):
            pass

    def first_AdjVex(self, vertex: str):  # 返回頂點的第一個鄰近節點
        # example -> vertex = "a", self.vertexes= {"a" = ["b","c"],"b" = ["b"],"c" = ["a"]}
        if self.check_vertex(vertex):
            return self.relationship[vertex][0]
