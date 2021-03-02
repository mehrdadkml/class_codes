class Graph: 
    def __init__(self):
        self.adj_matrix = {}  # {"node" : [connected nodes]}

    def add_node(self, node):
        if node in self.adj_matrix.keys():
            raise ValueError(f"{node} node exist")
        self.adj_matrix[node] = []

    def add_vertice(self, node_a, node_b):
        if not node_a in self.adj_matrix.keys():
            self.adj_matrix[node_a] = []
        if not node_b in self.adj_matrix.keys():
            self.adj_matrix[node_b] = []

        if (node_a in self.adj_matrix[node_b]) or (node_b in self.adj_matrix[node_a]):
            raise ValueError(f"{node_a} and{node_b} are connected")
            
        self.adj_matrix[node_a].append(node_b)
        self.adj_matrix[node_b].append(node_a)
    
    def deg_node(self, node):
        try:
            return len(self.adj_matrix[node])
        except Exception as e:
            raise e


    def find_path(self, start_node, end_node, path=[]):
        path = path + [start_node]


        if start_node == end_node:
            return path
        
        for node in self.adj_matrix[start_node]:  
            if node not in path:              
                temp_path = self.find_path(node, end_node, path)

                if temp_path:
                    return temp_path
        

    def find_all_path(self):
        pass


    def is_connected(self):
        pass

    def shortest_path(self, node_a, node_b):   #DFS
        pass

    
    def __str__(self):
        return str(self.adj_matrix)
            
    def rename_node(self, old_name, new_name):
        if not old_name in self.adj_matrix:
            raise ValueError(f"{old_name} la mojud")
        
        if new_name in self.adj_matrix:
            raise ValueError(f"{new_name} hast mojud")

        for node in self.adj_matrix[old_name]:
            self.adj_matrix[node].remove(old_name)
            self.adj_matrix[node].append(new_name)

        self.adj_matrix[new_name]= self.adj_matrix.pop(old_name)


class DirectedGraph(Graph):
    def add_vertice(self, node_a, node_b):
        if not node_a in self.adj_matrix.keys():
            self.adj_matrix[node_a] = []
        if not node_b in self.adj_matrix.keys():
            self.adj_matrix[node_b] = []

        if node_a in self.adj_matrix[node_b]:
            raise ValueError(f"{node_a} connected to {node_b}")

        self.adj_matrix[node_a].append(node_b)





g = Graph()

g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")


g.add_vertice("a", "b")
g.add_vertice("a", "e")
g.add_vertice("c", "b")
g.add_vertice("c", "e")
g.add_vertice("c", "m")
g.add_vertice("n", "m")
g.add_vertice("n", "f")
g.add_vertice("v", "z")


print(g.deg_node("b"))
print(g)


# g.rename_node("a", "halghe_talai")


print(g.find_path("a", "z"))