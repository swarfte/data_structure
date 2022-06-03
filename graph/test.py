import AdjacencyMatrix

if __name__ == '__main__':
    def add_arc(matrix, arc_relation):
        for arc in arc_relation:
            matrix.insert_arc(*arc)


    vexes = ["v" + str(x) for x in range(9)]
    arc_relation = [
        ["v0", "v1", 10],
        ["v0", "v5", 11],
        ["v1", "v0", 10],
        ["v1", "v2", 18],
        ["v1", "v6", 16],
        ["v1", "v8", 12],
        ["v2", "v1", 18],
        ["v2", "v3", 22],
        ["v2", "v8", 8],
        ["v3", "v2", 22],
        ["v3", "v4", 20],
        ["v3", "v6", 24],
        ["v3", "v7", 16],
        ["v3", "v8", 21],
        ["v4", "v3", 20],
        ["v4", "v5", 26],
        ["v4", "v7", 7],
        ["v5", "v0", 11],
        ["v5", "v4", 26],
        ["v5", "v6", 17],
        ["v6", "v1", 16],
        ["v6", "v3", 24],
        ["v6", "v5", 17],
        ["v6", "v7", 19],
        ["v7", "v3", 16],
        ["v7", "v4", 7],
        ["v7", "v6", 19],
        ["v8", "v1", 12],
        ["v8", "v2", 8],
        ["v8", "v3", 21]

    ]
    matrix = AdjacencyMatrix.AdjacencyMatrix(vexes)
    add_arc(matrix, arc_relation)
    print(matrix)
    print(matrix.dfs_traverse("v2"))
    print(matrix.bfs_traverse("v2"))

    # print(matrix.first_AdjVex("v2"))
    # print(matrix.next_AdjVex("v2", "v1"))
    # matrix.delete_vex("v7")
    # print(matrix.dfs_traverse("v4"))
