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


class Stack():
    '''Quick Stack class to assist with Graph class'''
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


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

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dft (self, starting_vertex):
        s = Stack()
        visited = set()
        path = []

        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop
            if v not in visited:
                path.append(v)
                print(path)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


def earliest_ancestor(ancestors, starting_node):
    # build graph
    g = Graph()
    
    for item in ancestors:
        if item[0] not in g.vertices:
            g.add_vertex(item[0])
        if item[1] not in g.vertices:
            g.add_vertex(item[1])
        g.add_edge(item[0], item[1])

    g.dft(starting_node)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))