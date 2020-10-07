class Queue():
    '''Quick queue class to assist with Graph class'''
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop()
        else:
            return None
    
    def size(self):
        return len(self.queue)


class Graph():
    '''Graph class made for earliest_ancestors function'''
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent Vertex")


def earliest_ancestor(ancestors, starting_node):
    # build graph
    g = Graph()
    
    for item in ancestors:
        if item[0] not in g.vertices:
            g.add_vertex(item[0])
        if item[1] not in g.vertices:
            g.add_vertex(item[1])
        g.add_edge(item[1], item[0])

    q = Queue()

    max_path_length = 1
    eldest_ancestor = -1

    q.enqueue([starting_node])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if len(path) > max_path_length:
            max_path_length = len(path)
            eldest_ancestor = v
        elif len(path) >= max_path_length and v < eldest_ancestor:
            max_path_length = len(path)
            eldest_ancestor = v

        for neighbor in g.vertices[v]:
            new_path = path + [neighbor]
            q.enqueue(new_path)

    return eldest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))