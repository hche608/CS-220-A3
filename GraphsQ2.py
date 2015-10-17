#!/usr/bin/env python2
# A3 for COMPSCI220 2015
# Created by Hao CHEN
# UPI: 8476927

import sys
import networkx as nx

def longest_path(G):
    subDAGList = nx.topological_sort(G)  
    count = 0
            
    for i in range(subDAGList.index(0),len(nx.topological_sort(G))-1):
        if nx.topological_sort(G)[i]>nx.topological_sort(G)[i+1]:
            count-=1
        count+=1    
    return count+1

def subDAG(G):
    for dag in nx.weakly_connected_component_subgraphs(G):
        if dag.has_node(0):
            print(longest_path(dag))
            break

def main(input):
    G = nx.DiGraph()
    counter = 0
    number_of_nodes = 0
    lines = input.split('\n')   
    for line in lines:
        if counter == number_of_nodes:
            counter = 0
            try:
                number_of_nodes = int(line)
                if number_of_nodes == 0:
                    subDAG(G)
                    break
            except ValueError:
                break
            if G.number_of_nodes() > 0:
                subDAG(G)
                G.clear()
                G.add_nodes_from(range(0,number_of_nodes))                              
        else:
            nodes = line.split(' ')
            for n in nodes:
                if n != '':
                    G.add_edge(counter, int(n))
            counter+=1
        
            
if __name__ == '__main__':
    main(sys.stdin.read())
