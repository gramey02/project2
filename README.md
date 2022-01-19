[![BuildStatus](https://github.com/gramey02/Project2/workflows/Project2/badge.svg?event=push)]

# Breadth-first Search Algorithm Description
* Algorithm traverses nodes in a given graph structure, one layer at a time
* If a start and end node are given to the algorithm, it returns the shortest path between them (if a path exists)
* If no path exists between the start and end node, or if the start or end node is not in the given graph, then None is returned
* If no end node is supplied, the algorithm traverses all of the nodes in the graph
* The algorithm works with queue structures to store current and visited nodes, and it also uses a dictionary structure to store the parent nodes of each visited node. Backtracking through this dictionary gives the shortest path between nodes.
