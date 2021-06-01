class Graph:
    def __init__(self):
        self.num_nodes = 0
        self.adj_list = {}
    
    def insert_node(self, data):
        if data not in self.adj_list:
            self.adj_list[data] = []
            self.num_nodes += 1
            return
    
    def insert_edge(self, v1, v2):
        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return
        return "Edge already exists"
    
    def show_conn(self):
        for node in self.adj_list:
            print(f'{node} -->> {" ".join(map(str, self.adj_list[node]))}')


my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_edge(1,2)
my_graph.insert_edge(1,3)
my_graph.insert_edge(2,3)
my_graph.show_conn()

"""
1 -->> 2 3
2 -->> 1 3
3 -->> 1 2
"""

print(my_graph.adj_list)
#{1: [2, 3], 2: [1, 3], 3: [1, 2]}

print(my_graph.num_nodes)
#3