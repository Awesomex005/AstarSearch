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
- f_cost: path cost so far + heuristic

### AstarSearch properties
- Explored: a set of explored nodes.
- Frontier: a ser of nodes which are adjacent to explored nodes but did not explore.

### AstarSearch algorithm
Explore a node with **lowest f_cost** in *Frontier*, add this node to *Explored*, add its adjacent nodes to *Frontier*.
Keep exploring nodes in *Frontier* until we found the goal node.
