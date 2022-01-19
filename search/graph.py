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
        
        #if there is an end node but either the start or end node is not actually in the graph, return None
        if (end is not None) and (self.graph.has_node(start)==False or self.graph.has_node(end)==False):
            return None
        
        #if there is not an end node but the start node given is not actually in the graph, return None
        if ((end is None) and self.graph.has_node(start)==False):
            return None
        
        #if there is an end node but no path exists between the start and end node, return None
        if (end is not None) and (nx.has_path(self.graph, start, end) == False):
            return None
        
        #if there is no end node, return a list with order of traversal, which will be stored in Backtrack
        if ((end is None) and (self.graph.has_node(start)==True)):
            
            visited = [] #queue to store visited nodes
            queue = [] #general queue
            path = {} #dictionary for storing parent nodes

            queue.append(start) #add start node to the queue
            visited.append(start) #mark the start node as visited

            #while there are still nodes in the queue...
            while queue:
                cur_node = queue.pop(0) #dequeue the current node

                #for each unvisited neighbor of the current node...
                for nghbr in set(nx.neighbors(self.graph, cur_node)):
                    if nghbr not in visited:
                        queue.append(nghbr) #add current neighbor to the queue
                        visited.append(nghbr) #mark current neighbor as visited
                        path[nghbr] = cur_node #store the parent node of the neighbor in the dictionary
            return visited #visited gives the order of traversal
        
        
        #if there is an end node and a path exists between the start and end node, return shortest path
        if ((end is not None) and nx.has_path(self.graph, start, end)):
            
            visited = [] #queue to store visited nodes
            queue = [] #general queue
            shortest_path = []
            path = {} #dictionary for storing parent nodes
            
            queue.append(start) #add start node to the queue
            visited.append(start) #mark the start node as visited
            
            while queue:
                cur_node = queue.pop(0) #dequeue the current node
                
                if cur_node == end:
                    #the first entry of the shortest path queue will be the end node, the last entry will be start node
                    shortest_path.append(cur_node) #append the end node to the shortest_path queue
                    while (path.get(cur_node) is not None):
                        shortest_path.append(path[cur_node]) #traceback the shortest path by appending the parent nodes in order
                        cur_node = path[cur_node] #update cur_node variable to be the parent node
                    return shortest_path

                #for each unvisited neighbor of the current node...
                for nghbr in set(nx.neighbors(self.graph, cur_node)):
                    if nghbr not in visited:
                        queue.append(nghbr) #add current neighbor to the queue
                        visited.append(nghbr) #mark current neighbor as visited
                        path[nghbr] = cur_node #store the parent node of the neighbor in the dictionary


