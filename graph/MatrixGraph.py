class MatrixGraph(object):
    def __init__(self, vertex: dict = None, relationship: dict = None):
        # example -> vertexes = {"a" :1,"b":2,"c":3}, relationship = {"a" : ["a","c"],"b":["c"],"c":["a"]}
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

    def __str__(self):
        return "".join([str(x) + "\n" for x in self.matrix])

    def __getitem__(self, vertex: str):  # 獲取指定頂點的值
        return self.get_vex(vertex)

    def __setitem__(self, vertex: str, value):  # 對指定頂點賦值
        self.put_vex(vertex, value)

    def __delitem__(self, vertex: str):  # 刪除指定頂點
        self.delete_vex(vertex)

    def __add__(self, vertex: dict):
        self.insert_vex(*vertex.items())

    def create_graph(self, vertex: dict, relationship: dict):  # 創建矩陣圖
        # example -> vertexes = {"a" :1,"b":2,"c":3}, relationship = {"a" : ["a","c"],"b":["c"],"c":["a"]}
        if vertex and relationship:
            self.relationship = relationship  # 頂點之間的關係(弧)
            self.vertex_number = len(vertex)  # 頂點數量
            self.vertexes = vertex  # 頂點的值
            for x in self.vertexes.keys():
                row = []
                for y in self.vertexes.keys():
                    if y in self.relationship[x]:  # 頂點x為出弧,頂點y為入弧
                        row.append(1)
                    else:
                        row.append(0)
                self.matrix.append(row)

    def destroy_graph(self):  # 刪除矩陣圖
        self.relationship = {}
        self.vertex_number = 0
        self.vertexes = {}
        self.matrix = []

    def locate_vex(self, vertex: str):  # 找到該頂點在圖中的位置
        return list(self.vertexes.keys()).index(vertex)

    def get_vex(self, vertex: str):  # 返回該頂點的值
        return self.vertexes[vertex]

    def put_vex(self, vertex: str, value):  # 對頂點賦值
        self.vertexes[vertex] = vertex

    def first_AdjVex(self, vertex: str):  # 返回頂點的第一個鄰近節點
        # example -> vertex = "a", self.vertexes= {"a" = ["b","c"],"b" = ["b"],"c" = ["a"]}, return "b"
        relationship = self.relationship[vertex]
        if relationship:
            return relationship[0]
        else:
            return None

    def insert_vex(self, vertex: str, value):  # 插入頂點
        self.matrix.append([0 for x in self.vertexes.keys()])  # 填充為0表示和其他頂點沒關係
        self.vertexes[vertex] = value
        self.relationship[vertex] = set()
        for vex in self.matrix:  # 補充當前頂點和新頂點的關係
            vex.append(0)
        self.vertex_number += 1

    def delete_vex(self, vertex: str):  # 刪除頂點
        location = list(self.vertexes.keys()).index(vertex)
        del self.vertexes[vertex]  # 刪除頂點和相關的值
        del self.relationship[vertex]  # 刪除頂點的弧
        for vex in self.relationship.keys():  # 刪除頂點的關係
            if vertex in self.relationship[vex]:  # 檢測其他頂點是否和被刪除的頂點有關係
                self.relationship[vex].remove(vertex)
        self.matrix.pop(location)  # 刪除頂點所佔的行
        for vex in self.matrix:
            vex.pop(location)  # 刪除頂點所佔的列
        self.vertex_number -= 1

    def insert_arc(self, out_vertex: str, in_vertex: str):  # 在圖中插入弧
        if in_vertex not in self.relationship[out_vertex]:
            order = list(self.vertexes.keys())
            out_location = order.index(out_vertex)
            in_location = order.index(in_vertex)
            self.relationship[out_vertex].add(in_vertex)
            self.matrix[out_location][in_location] = 1

    def delete_arc(self, out_vertex: str, in_vertex: str):  # 在圖中刪除弧
        order = list(self.vertexes.keys())
        out_location = order.index(out_vertex)
        in_location = order.index(in_vertex)
        self.relationship[out_vertex].remove(in_vertex)
        self.matrix[out_location][in_location] = 0

    def dfs_traverse(self, vertex: str):
        pass

    def bfs_traverse(self, vertex: str):
        pass
