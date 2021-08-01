#!/usr/bin/env python3
"""
Knights of the Round Table - graph method.

by pulsar77


All solutions are generated as follows:
- Create a directed graph of the knights and allowed pairs.
- Create the adjacency dict.
- Arthur and Lancelot can already be seated.
- Find all possible paths recursively, by selecting unseated knights from
the adjencency list of the right-most seated knight; each of them in turn
becomes the new right-most seated knight, and the recursion continues.
- A solution is found if all knights are seated and the right-most seated
knight is allowed to sit next to the left_most seated knight.
"""
from collections import namedtuple


Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])


def adjacency_dict(graph):
    """
    Returns the adjancency list representation of the graph.
    """
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj


nodes = [
    'Arthur', 'Lancelot', 'Bedivere', 'Gawain', 'Gareth',
    'Perceval', 'Tristan', 'Galahad', 'Lionel', 'Kay'
]


edges = [
    ('Arthur', 'Lancelot'),
    ('Lancelot', 'Galahad'), ('Lancelot', 'Lionel'),
    ('Bedivere', 'Tristan'), ('Bedivere', 'Lionel'),
    ('Gawain', 'Gareth'), ('Gawain', 'Perceval'), ('Gawain', 'Kay'),
    ('Gareth', 'Gawain'), ('Gareth', 'Perceval'), ('Gareth', 'Tristan'),
    ('Gareth', 'Lionel'), ('Perceval', 'Gawain'), ('Perceval', 'Gareth'),
    ('Perceval', 'Galahad'), ('Perceval', 'Kay'),
    ('Tristan', 'Bedivere'), ('Tristan', 'Gareth'), ('Tristan', 'Galahad'),
    ('Tristan', 'Lionel'), ('Galahad', 'Tristan'), ('Lionel', 'Bedivere'),
    ('Lionel', 'Gareth'), ('Lionel', 'Tristan'), ('Lionel', 'Kay'),
    ('Kay', 'Arthur')
]


knights = Graph(nodes, edges, is_directed=True)
adj = adjacency_dict(knights)


def round_table_from_graph():
    arrangements = find_arrangements(adj, seated=['Arthur', 'Lancelot'])
    for n, arrangement in enumerate(arrangements, 1):
        print(f"{n}. {', '.join(arrangement)}")


def find_arrangements(adj, seated):
    first, last = seated[0], seated[-1]
    if (len(seated) == len(adj)) and (first in adj[last]):
        yield seated
        return
    unseated = (knight for knight in adj[last] if knight not in seated)
    for next_knight in unseated:
        yield from find_arrangements(adj, seated+[next_knight])


if __name__ == "__main__":
    round_table_from_graph()
