#!/usr/bin/env python2
# A3 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import sys
import networkx as nx


def dag_longest_path(G, weight='weight', default_weight=1):
    """Returns the longest path in a DAG
    If G has edges with 'weight' attribute the edge data are used as weight values.

    Parameters
    ----------
    G : NetworkX DiGraph
        Graph

    weight : string (default 'weight')
        Edge data key to use for weight

    default_weight : integer (default 1)
        The weight of edges that do not have a weight attribute

    Returns
    -------
    path : list
        Longest path

    Raises
    ------
    NetworkXNotImplemented
        If G is not directed

    See also
    --------
    dag_longest_path_length
    """
    dist = {} # stores {v : (length, u)}
    for v in nx.topological_sort(G):
        us = [(dist[u][0] + data.get(weight, default_weight), u)
            for u, data in G.pred[v].items()]
        # Use the best predecessor if there is one and its distance is non-negative, otherwise terminate.
        maxu = max(us) if us else (0, v)
        dist[v] = maxu if maxu[0] >= 0 else (0, v)
    u = None
    v = max(dist, key=dist.get)
    path = []
    while u != v:
        path.append(v)
        u = v
        v = dist[v][1]
    path.reverse()
    return path

def longest(G):
    #print(G.nodes())
    pathlist = dag_longest_path(G)
    try:
        print(len(pathlist) - pathlist.index(0))
    except ValueError:
        for dag in nx.weakly_connected_component_subgraphs(G):
            if dag.has_node(0):
                longest(dag)
                break
       
    
    # pathlist = dag_longest_path(G)
    # if not 0 in pathlist:
    #     for dag in nx.weakly_connected_component_subgraphs(G):
    #         if dag.has_node(0):
    #             pathlist = dag_longest_path(dag)
    #             break
    #
    # for i in range(0,len(pathlist)):
    #     if pathlist[i] == 0:
    #         print(len(pathlist)-i)
    #         break
    # #print(len(pathlist) - pathlist.index(0))

               
def main(input):
    G = nx.DiGraph()
    counter = 0
    number_of_nodes = 0
    lines = input.split('\n')  
    for line in lines:
        if counter == number_of_nodes:
            number_of_nodes = int(line)
            if G.number_of_nodes() > 0:
                longest(G)
                G.clear()
            if number_of_nodes == 0:
                break    
            G.add_nodes_from(range(0,number_of_nodes))
            counter = 0                          
        else:
            nodes = line.split(' ')
            for n in nodes:
                if n != '':
                    G.add_edge(counter, int(n))
            counter+=1
        
            
if __name__ == '__main__':
    main(sys.stdin.read())
