# AstarSearch
An implementation of A* Search in Python3.

##### The MAP here is in the following format.
- The MAP.intersections are represented as a dictionary.
  - keys are node_id/intersections_id
  - values are the node/intersections coordinate.
- The MAP.roads property is a list where roads[**i**] contains a list of the nodes/intersections that node/intersection **i** connects to.

## Key conponents and base concepts
### Node properties
- state
  - ID: node_id/intersections_id
  - coordinates:
  - heuristic: estimated/sortest distance to the goal node
- parent: record this node was expand from which node, will be use to generate final path.
- f_cost: the path cost (real disrance) so far + heuristic

### AstarSearch properties
- Explored: a set of explored nodes.
- Frontier: a ser of nodes which are adjacent to explored nodes but did not explore.

### AstarSearch algorithm
- Explore a node with **lowest f_cost** in *Frontier*, 
  - add this node to *Explored*, 
  - calculate its adjacent nodes' f_cost 
  - and add these adjacent nodes to *Frontier* (if a node instance has already existed in *Frontier*, According to f_cost, leave the better one.).
- Keep exploring nodes in *Frontier* until we found the goal node.
