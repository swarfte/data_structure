from re import L
import re
from tkinter.messagebox import NO


class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return  f"data = {self.data} \n {self.data} -> left_node = {self.left} \n {self.data} -> right_node = {self.right}"


class AdjacencyMatrix(object):
    def __init__(self, vexes: list = None):
        super().__init__()
        self.vexes = []
        self.arcs = []
        self.maximum = 2147483647
        self.minimum = 0
        self.create_graph(vexes)

    def __str__(self):
        return "".join([str(arc) + "\n" for arc in self.arcs])

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
        out_vex = self.locate_vex(vex)
        for in_vex in range(len(self.vexes)):
            if self.minimum < self.arcs[out_vex][in_vex] < self.maximum:
                temp.append(self.vexes[in_vex])
        stack.extend(temp[::-1])
        check[out_vex] = True
        traverse.append(vex)

        # for the state vex
        while stack:
            current_vex = stack.pop()
            out_vex = self.locate_vex(current_vex)
            if not check[out_vex]:
                temp = []
                for in_vex in range(len(self.vexes)):
                    if self.minimum < self.arcs[out_vex][in_vex] < self.maximum:
                        temp.append(self.vexes[in_vex])
                stack.extend(temp[::-1])
                check[out_vex] = True
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

    def find_all_arcs(self, vex: str) -> list:
        arcs = []
        index = self.locate_vex(vex)
        for i in range(len(self.vexes)):
            relationship = []
            if self.minimum < self.arcs[index][i] < self.maximum:
                relationship.append(index)
                relationship.append(i)
                relationship.append(self.arcs[index][i])
                arcs.append(relationship)
        return arcs

    def vex_minimum(self, vex: str) -> list:
        minimum = [0, 0, self.maximum]
        out_vex = self.locate_vex(vex)
        for in_vex in range(len(self.arcs)):
            if self.minimum < self.arcs[out_vex][in_vex] < self.maximum:
                if self.arcs[out_vex][in_vex] < minimum[2]:
                    minimum = [out_vex, in_vex, self.arcs[out_vex][in_vex]]
        return minimum

    def arc_minimum(self, arcs: list) -> list:
        minimum = [0, 0, self.maximum]
        for arc in arcs:
            if arc[2] < minimum[2]:
                minimum = arc
        return minimum
    
    def extend_node_order(self, old_list: list, new_list: list) ->list:
        arcs = old_list
        for new_arc in new_list:
            check = True
            for old_arc in old_list:
                if old_arc[0] == new_arc[0] and old_arc[1] == new_arc[1]:
                    check = False
                    break
            if check:
                arcs.append(new_arc)
        return arcs
    
    def prim_tree(self,vex: str) -> BinaryTreeNode:
        head_node = BinaryTreeNode(vex)
        current_node = head_node
        node_order = [BinaryTreeNode() for _ in self.vexes]
        arc_list = []
        for run_time in range(len(self.vexes)):
            node_order[self.locate_vex(current_node.data)] = current_node
            arc_list = self.extend_node_order(arc_list,self.find_all_arcs(current_node.data))
        
            while True:
                minimum_arc = self.arc_minimum(arc_list)
                if minimum_arc in arc_list:
                    arc_list.remove(minimum_arc)
                else:
                    break
                if node_order[minimum_arc[1]].data is None or arc_list is None:
                    break
                    
            if node_order[minimum_arc[1]].data is None:
                next_node = BinaryTreeNode(self.vexes[minimum_arc[1]])
                if current_node.left is None:
                    current_node.left = next_node
                else:
                    current_node.right = next_node
                current_node = next_node
        return head_node
            

