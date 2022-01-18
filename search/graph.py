import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        
        #breadth first traversal
        
        #if no end node, return a list with order of traversal, which will be stored in Backtrack
        if end==None:
            visited = [] #queue to store visited nodes
            queue = [] #general queue
            Backtrack = [] #queue for storing parent nodes

            queue.append(start) #add start node to the queue
            vistited.append(start) #mark the start node as visited

            #while there are still nodes in the queue...
            while queue:
                cur_node = queue.pop(0) #dequeue the current node

                #for each unvisited neighbor of the current node
                for nghbr in all_neighbors(self.graph, cur_node):
                    if nghbr not in visited:
                        queue.append(nghbr) #add current neighbor to the queue
                        visited.append(nghbr) #mark current neighbor as visited
                        Backtrack.append(cur_node) #store the current node as a parent
            return Backtrack
        
        #if there is an end node, then return the shortest path
        if (end !=None and has_path(self, start, end)):
            visited = [] #queue to store visited nodes
            queue = [] #general queue
            Backtrack = [] #queue for storing parent nodes

            queue.append(start) #add start node to the queue
            vistited.append(start) #mark the start node as visited

            #while there are still nodes in the queue...
            while queue:
                cur_node = queue.pop(0) #dequeue the current node

                #for each unvisited neighbor of the current node
                for nghbr in all_neighbors(self.graph, cur_node):
                    if nghbr not in visited:
                        queue.append(nghbr) #add current neighbor to the queue
                        visited.append(nghbr) #mark current neighbor as visited
                        Backtrack.append(cur_node) #store the current node as a parent
                        
        else:
            return None
        




