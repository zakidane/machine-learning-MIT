# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):
    visited = set()
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        connected_nodes = graph.get_connected_nodes(node)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for k in connected_nodes:
                new_path = list(path)
                new_path.append(k)
                queue.append(new_path)
# ## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    visited = set()
    stack = []
    stack.append([start])
    while stack:
        path = stack.pop()
        node = path[-1]
        connected_nodes = graph.get_connected_nodes(node)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for k in connected_nodes:
                new_path = list(path)
                new_path.append(k)
                stack.append(new_path)

## Now we're going to add some heuristics into the search.
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    queue = [[start]]
    while len(queue) > 0 and queue[0][-1] != goal:
        current_path = queue.pop(0)
        current_node = current_path[-1]
        connected = graph.get_connected_nodes(current_node)
        new_paths = {}
        for connected_node in connected:
            distance_to_goal = graph.get_heuristic(connected_node, goal)
            if connected_node not in current_path:
                add_to_dictlist(new_paths, distance_to_goal, current_path + [connected_node])
        paths_for_front = []
        for path_distance in sorted(new_paths):
            paths_for_front.extend(new_paths[path_distance])
        queue = paths_for_front + queue
        print queue
    if len(queue) > 0:
        return queue[0]
    else:
        return []
def add_to_dictlist(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]

#     visited = set()
#     stack = []
#     stack.append([start])
#     min_path = stack[0]
#     min_distance = graph.get_heuristic(start, goal)
#     min_index = 0
#     while stack:
#                 #this needs to be modified to find the shortest remaining distance
#         #can be done by first sorting by heuristic distances
#         #last one has shortest remaining distance
#         #order by using .get_heuristic[last node in popped][goal]??
#         for min_path in stack:
#             min_node = min_path[-1]
#             if graph.get_heuristic(min_node, goal) < min_distance:
#                 min_distance = graph.get_heuristic(node, goal)
#                 min_index = stack.index(min_path)
#
#
#         stack_length = len(stack)
#         if stack_length > min_index:
#             path = stack.pop(min_index)
#             print(path)
#             node = path[-1]
#         else:
#             break
#
#
#         connected_nodes = graph.get_connected_nodes(node)
#
#         if node == goal:
#             return path
#
#         if node not in visited:
#             visited.add(node)
#             for k in connected_nodes:
#                 new_path = list(path)
#                 new_path.append(k)
#                 stack.append(new_path)
#
#     return []
# ## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the
# ## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = '10'
WHAT_I_FOUND_INTERESTING = 'dfs'
WHAT_I_FOUND_BORING = 'debugging'
