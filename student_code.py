
def N2N_DISTANCE(coordinates_a, coordinates_b):
    return ((coordinates_a[0] - coordinates_b[0])**2 + (coordinates_a[1] - coordinates_b[1])**2 ) ** 0.5
    

class Frontier(object):
    def __init__(self):
        self.nodes = set() # elment intersection_num
        self.prio_queue = []

    def has(self, node_id):
        if node_id in self.nodes:
            return True
        else:
            return False
    
    def add(self, node):
        self.nodes.add(node.state["ID"])
        self.prio_queue.append(node)
        self.prio_queue.sort()
    
    def pop(self):
        if len(self.prio_queue):
            node = self.prio_queue.pop(0)
            self.nodes.remove(node.state["ID"])
            return node
        else:
            return None
        
    def size(self):
        return len(self.nodes)
        
        
class Explored(object):
    def __init__(self):
        self.nodes = set() # elment intersection_num
        
    def add(self, node):
        self.nodes.add(node.state["ID"])
        
    def has(self, node_id):
        if node_id in self.nodes:
            return True
        else:
            return False
        
        
class AStarSearch(object):
    def __init__(self, M, start, goal):
        self.nodes = {}
        self.frontier = Frontier()
        self.explored = Explored()
        self.M = M
        self.start = start
        self.goal = goal
        self.new_n_add2frontier(self.start, None) # add start point
        
    def new_n_add2frontier(self, node_id, parent):
        if self.explored.has(node_id):
            return
        
        node = Node(node_id, self.M.roads[node_id], self.M.intersections[node_id], parent, self.M.intersections[self.goal])
        if self.frontier.has(node_id):
            # if a node already exist in frontier. According to f_cost, leave the better one. 
            pre_node = self.nodes[node_id]
            if node < pre_node:
                pre_node.parent = node.parent
                pre_node.f_cost = node.f_cost
                del node
                self.frontier.prio_queue.sort()
        else:
            self.nodes.setdefault(node_id, node)
            self.frontier.add(node)
    
    def search(self):
        while True:
            if not self.frontier.size():
                return None
            node = self.frontier.pop()
            self.explored.add(node)
            if self.goal == node.state["ID"]:
                return node.get_path()
            for a in node.actions:
                self.new_n_add2frontier(a, node)
                
    
class Node(object):
    def __init__(self, intersection_num, adjacent_intersections, coordinates, parent, goal_coordinates):
        self.state = {"ID":intersection_num, "coordinates": coordinates, "heuristic": 0}
        self.actions = adjacent_intersections
        self.parent = parent
        self.state["heuristic"] = N2N_DISTANCE(coordinates, goal_coordinates)
        # f = g + h 
        # g: path cost so far
        # h: estimated distance to the goal
        if(parent):
            dst2parent = N2N_DISTANCE(self.state["coordinates"], parent.state["coordinates"])
            self.f_cost = parent.f_cost - parent.state["heuristic"] + dst2parent + self.state["heuristic"]
        else:
            self.f_cost = self.state["heuristic"]
        
    def printf(self):
        print(self.state)
        print("actions: ", self.actions)
        if(self.parent):
            print("parent: ", self.parent.state["ID"])
        else:
            print("parent: ", self.parent)
        print("f_cost: ", self.f_cost)
        
    def get_path(self):
        path = []
        node = self
        path.insert(0, node.state["ID"])
        while node.parent:
            node = node.parent
            path.insert(0, node.state["ID"])

        return path
        
    def __eq__(self, other):
        return not self.f_cost < other.f_cost and not other.f_cost < self.f_cost
    
    def __ne__(self, other):
        return self.f_cost < other.f_cost or other.f_cost < self.f_cost
    
    def __gt__(self, other):
        return other.f_cost < self.f_cost
    
    def __ge__(self, other):
        return not self.f_cost < other.f_cost
    
    def __le__(self, other):
        return not other.f_cost < self.f_cost


def shortest_path(M,start,goal):
    print("shortest path called")
    astar = AStarSearch(M,start,goal)
    path = astar.search()
    return path