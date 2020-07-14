from graph.graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # ancestors is a list of tuples
    # give the graph in that form transverse it to find the root element
    # so becuase it is a list of tuple then the graph is going to be directed
    G = Graph()
    return ancestors


if __name__ == '__main__':
    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8),
                      (8, 9), (11, 8), (10, 1)]
    for i in range(10):
        earliest_ancestor(test_ancestors, i)
