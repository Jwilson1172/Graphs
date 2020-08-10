"""
Simple graph implementation
"""
from util import Stack, Queue


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        return

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # could add a conditional branch here to do something
        # diffrent if the index already occurins in the dictionary
        self.vertices[vertex_id] = set()
        return

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if (v1 in self.vertices) and (v2 in self.vertices):
            self.vertices[v1].add(v2)
        else:
            raise IndexError(
                "%s not found in array".format(str(v1) + ", " + str(v2)))
        return

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()

        # Create a set to store the visited nodes
        visited = set()

        # Init: enqueue the starting node
        q.enqueue(starting_vertex)

        # While the queue isn't empty
        while q.size() > 0:
            # Dequeue the first item
            v = q.dequeue()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)

                # Do something with the node
                print(f"Visited {v}")

                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
        return

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Create a set to store the visited nodes
        visited = set()

        # Init: push the starting node
        s.push(starting_vertex)

        # While the stack isn't empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)

                # Do something with the node
                print(f"Visited {v}")

                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)
        return

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        # this method is a good solution for the social network problem
        # because the bfs keeps track of the path, it can be used to find the
        # solution quickly.
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()

            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                # IF SO, RETURN PATH
                if v == destination_vertex:
                    return path

                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                # COPY THE PATH
                # APPEND THE NEIGHOR TO THE BACK

                for next_vert in self.get_neighbors(v):
                    new_path = list(path)  # Copy the list
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        # If we got here, we didn't find it
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make stack and add the starting vertex to the stack
        paths = Stack()
        paths.push([starting_vertex])

        # make a set to store the vertex's that have already been visited
        vertex_visited = set()

        while paths.size() > 0:
            path = paths.pop()

            current_vertex = path[-1]

            if current_vertex not in vertex_visited:
                if current_vertex == destination_vertex:
                    return path

                else:
                    for i in self.vertices[current_vertex]:
                        paths.push(path + [i])

            vertex_visited.add(current_vertex)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # cond init the local variables
        if vertex_visited is None:
            vertex_visited = set()

        if paths is None:
            paths = []

        # append to the visited vertexs and path list
        vertex_visited.add(starting_vertex)
        paths = paths + [starting_vertex]

        # exit condition
        if starting_vertex == destination_vertex:
            return paths

        # for each neghbor for the starting vertex if it hasn't been visited
        # call the dfs using the neigbor as the starting vertex
        for i in self.get_neighbors(starting_vertex):
            if i not in vertex_visited:
                new_path = self.dfs_recursive(
                    starting_vertex=i,
                    destination_vertex=destination_vertex,
                    paths=paths,
                    vertex_visited=vertex_visited)

                if new_path:
                    return new_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
