

class AdjacencyMatrix(object):
    def __init__(self, vexes: list = None):
        super().__init__()
        self.vexes = []
        self.arcs = []
        self.maximum = 2147483647
        self.minimum = 0
        self.create_graph(vexes)

    def __str__(self):
        sentence = ""
        for arc in self.arcs:
            sentence += str(arc)
            sentence += "\n"
        return sentence

    def create_graph(self, vexes: list) -> None:
        if vexes:
            for v in vexes:
                self.insert_vex(v)

    def insert_vex(self, vex: str) -> None:
        for arc in self.arcs:
            arc.append(self.maximum)
        arc = []
        for _ in self.vexes:
            arc.append(self.maximum)
        self.vexes.append(vex)
        arc.append(self.minimum)
        self.arcs.append(arc)

    def destroy_graph(self) -> None:
        self.vexes = []
        self.arcs = []

    def locate_vex(self, vex: str) -> int:
        return self.vexes.index(vex)

    def get_vex(self, index: int) -> str:
        return self.vexes[index]

    def put_vex(self, old_vex: str, new_vex: str) -> None:
        self.vexes[self.locate_vex(old_vex)] = new_vex

    def first_AdjVex(self, vex: str) -> str:
        relationship = self.arcs[self.locate_vex(vex)]
        for index in range(len(relationship)):
            if self.minimum < relationship[index] < self.maximum:
                return self.vexes[index]

    def next_AdjVex(self, tail_vex: str, in_vex: str) -> str | None:
        relationship = self.arcs[self.locate_vex(tail_vex)]
        for index in range(len(relationship)):
            if self.minimum < relationship[index] < self.maximum:
                if self.vexes[index] != in_vex:
                    return self.vexes[index]
        return None

    def delete_vex(self, vex: str) -> None:
        index = self.locate_vex(vex)
        for arc in self.arcs:
            arc.pop(index)
        self.arcs.pop(index)
        self.vexes.pop(index)

    def insert_arc(self, tail_vex: str, in_vex: str, weight: int) -> None:
        self.arcs[self.locate_vex(tail_vex)][self.locate_vex(in_vex)] = weight

    def delete_arc(self, tail_vex: str, in_vex: str) -> None:
        self.arcs[self.locate_vex(tail_vex)][self.locate_vex(in_vex)] = 0

    def dfs_traverse(self, vex: str) -> list:
        # for the first vex
        check = [False for _ in self.vexes]
        traverse = []
        stack = []
        temp = []
        i = self.locate_vex(vex)
        for j in range(len(self.vexes)):
            if self.minimum < self.arcs[i][j] < self.maximum:
                temp.append(self.vexes[j])
        stack.extend(temp[::-1])
        check[i] = True
        traverse.append(vex)

        # for the state vex
        while stack:
            current_vex = stack.pop()
            i = self.locate_vex(current_vex)
            if not check[i]:
                temp = []
                for j in range(len(self.vexes)):
                    if self.minimum < self.arcs[i][j] < self.maximum:
                        temp.append(self.vexes[j])
                stack.extend(temp[::-1])
                check[i] = True
                traverse.append(current_vex)
        return traverse

    def bfs_traverse(self, vex: str) -> list:
        # for the first vex
        check = [False for _ in self.vexes]
        traverse = []
        queue = []
        i = self.locate_vex(vex)
        for j in range(len(self.vexes)):
            if self.minimum < self.arcs[i][j] < self.maximum:
                queue.append(self.vexes[j])
        check[self.locate_vex(vex)] = True
        traverse.append(vex)

        # for the queue vex
        while queue:
            current_vex = queue.pop(0)
            i = self.locate_vex(current_vex)
            if not check[i]:
                check[i] = True
                for j in range(len(self.vexes)):
                    if self.minimum < self.arcs[i][j] < self.maximum:
                        queue.append(self.vexes[j])
                traverse.append(current_vex)
        return traverse

    def small_tree(self,vex:str) -> list:

        pass
