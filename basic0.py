#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:50:51 2019

@author: pumpkin
"""

# Reference
# https://networkx.github.io/documentation/stable/_downloads/networkx_reference.pdf

import random
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


'''
G = nx.Graph()
# DiGraph, MultiGraph, MultiDiGraph()
g_data = [(1,2,6),(1,3,1),(1,4,5)]
G.add_weight_edges_from(g_data)


G.add_edge(1, 2)
G.add_edge(2, 3, weight=0.9)
plt.subplot(122)
nx.draw(G, node_color = 'r', edge_color = 'b' )
'''

'''
ER = nx.random_graphs.erdos_renyi_graph(20, 0.2)
pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels=False, egdg_color='b', alpha=0.3, node_size=30)
plt.show()
'''

node_count = 100
itera_count = 100
gamma = 0.3 # gamma, recover rate, a constant
BA = nx.random_graphs.barabasi_albert_graph(node_count, 2)
pos = nx.spring_layout(BA)
# 01) draw the network topology
# nx.draw(BA, pos, with_labels=False, node_size=30,edge_color='b', alpha=0.3)
# plt.savefig("fig1.png")

degree =nx.degree_histogram(BA)
x = range(len(degree))
y = [z / float(sum(degree)) for z in degree]
# 02) draw the historgram of node distribution
# plt.loglog(x, y, color="blue", linewidth = 2)
# plt.savefig("fig2.png")
# print all network nodes degree
# print(BA.degree())
# print the number of different degree nodes
# print(nx.degree_histogram(BA))

# add distributions of nodes
# attr1: different OS systems have different coefficients to be infected
system_infected_coef = [0.6, 0.3, 0.2]
# attr2: state influce infected coefficient
# state0 - recover, state1 - healthy, state2 - infected 
# e.g. state0, recovered, and it will never be infected again
# e.g. state1, health, and coefficient is 0.5 to be infected
# e.g. state2, has been infected
state_infected_coef = [0, 0.5, 1]

# set color for nodes
# it's related to the nodes state
node_color=['black', 'blue', 'red']

# assume that the originl network has some infected nodes
# while no recovered nodes
nodes_color_list = []
for i in range(node_count):
    # attr1 - system coefficience
    attr1 = random.randint(0,2)
    # attr2 - state coefficience
    # tips: init don't have nodes recovered
    attr2 = random.randint(1,2)
    BA.add_node(i, sys_coef = system_infected_coef[attr1], 
                state_coef = state_infected_coef[attr2])
    # print(BA.node[i]['sys_coef'], BA.node[i]['state_coef'])
    nodes_color_list = np.append(nodes_color_list, node_color[attr2])
# 03) draw nodes with different color
# plt.savefig("fig3.png")
# nx.draw(BA, pos, with_labels=False, node_color = nodes_color_list,
#         node_size=30,edge_color='b', alpha=0.3)


# do itera_count times
# pick one node each time
# print(BA.node)

for i in range(itera_count):
    # randomly pick one node
    node_id = random.randint(0, node_count-1)
    # print("node_id%s"%node_id)
    # print("coef%s"%BA.node[node_id]['state_coef'])
    # print(BA.node[node_id]['state_coef'])
    # if the state of node[node_id] is recover, no change
    if BA.node[node_id]['state_coef'] == state_infected_coef[0]:
        # print("state 0")
        continue
    # if the state of node[node_id] is healthy
    # calculate the infected rate, beta
    # different nodes has different infected rate
    elif BA.node[node_id]['state_coef'] == state_infected_coef[1]:
        # calculate the threshold of infected rate 
        beta_ba = 1
        beta_ba_max = 1
        for nodej_id in BA[node_id]:
            beta_ba = beta_ba * (1-BA.node[nodej_id]['sys_coef'])*(1-math.ceil(BA.node[nodej_id]['state_coef']-0.5))
            beta_ba_max = beta_ba_max * (1-system_infected_coef[2]) * (1-math.ceil(state_infected_coef[0]-0.5))
        beta_ba = beta_ba * (1 - BA.node[node_id]['sys_coef'])
        beta_ba_max = beta_ba_max * (1-system_infected_coef[2])
        beta = 1 - beta_ba * 1.0/beta_ba_max
        # print(beta)
        # generate the random number, and compare
        # if the number is in range(0, beta), then infected
        # because the probability to be infected is beta
        # otherwise, still healthy
        rand_infec = random.uniform(0, 1)
        if rand_infec <= beta:
            BA.node[node_id]['state_coef'] = state_infected_coef[2]
            nodes_color_list[node_id] = node_color[2]
     # if the state of node[node_id] is infected
     # judge whether the node will be recovered by gamma
    else:
        # generate a random number
        rand_rec = random.uniform(0, 1)
        if rand_rec <= gamma:
            BA.node[node_id]['state_coef'] = state_infected_coef[0]
            nodes_color_list[node_id] = node_color[0]
        
# 04) draw the new network
# plt.savefig("fig3.png")
nx.draw(BA, pos, with_labels=False, node_color = nodes_color_list,
        node_size=30,edge_color='y', alpha=0.3)
# beta means infected probability when connect with infected computers
 
    

plt.show()