# Complex-Network
## Simulate computer virus propagation on scale-free network using Python
Because I'm still learning about markdown syntax, some formulars will update later.

## Abstract
This is a model to simulate the spread of computer virus over a scale-free network. It is based on SIR model for epidemics, then change from the constant infected probability to different values according to the new definition. Here, the new definition is related to the node's attributions (OS system and its' state) and its' neighbors’ attributions.

## Problem Formulation
In a typical epidemic propagation model, the states of all computers are classified into: 
S (Susceptible) - healthy state (can be infected by others). 
I (Infected) - infected state (can infect others). 
R (Recovered) - recovered state (cannot be infected by others again). 
There are three different common models for epidemic propagation due to the different combinations of these two states, SI model, SIS model, and SIR model. 

### SIR Model 
Once the node is recurred, it cannot be infected by others again. By qualitative analysis, one can find the following: 
S0>𝛿/𝜆: virus will spread out for some time, but eventually die out. 
S0≤ 𝛿/𝜆: virus will die out quickly. 

Once the computer can detect this kind of virus, it won't be infected again. Therefore, SIR Model is more suitable for this situation. However, SIR Model assume the same probability for each node. To be more practical, I consider networks as BA Scale-Free Networks, and set different probability for each node according to its computer system and its neighbors.  

## model description
I neglect both the nature of computer viruses and the details of their infection, and simply assume that, at any time, every computer in the world is in one of three possible states: susceptible, infected, and recovered. For simplicity, we assume that the lifetime of a virus or disease is much shorter than the lifetime of computers, therefore, birth and death of nodes are not taken into consideration in the following study. To be more practical, I chose BA Scale-Free Networks as the simulation networks. 

Assume that each node has two attribution: 
1) OS system. Different systems show different level of immunity to the virus. 
2) State. Every computer is in one of three possible states: susceptible, infected, and recovered. Once the state is recovered, it won't change any more. 
We set coefficients for these two attributions as ﻿system_infected_coef and ﻿state_infected_coef, respectively. Here, if the state is recovered, set state_infected_coef=0; if the state is susceptible, state_infected_coef=0.5; if the state is infected, state_infected_coef=1. 

If we randomly pick a node, there are three cases: 
1) The node is in state "recover" 
    If the node is in state "recover", then no change will happen in networks. 
2) The node is in state "susceptible" 
    If the node is in state " susceptible ", we define the probability that node i will be infected as v. 

Assume the neighbor of node i is B[i].  
Due to contacts with possible infected node j, we define the probability that node i is uninfected in condition of node j (j∈B(i)): (formular)
Then the probability of node i is uninfected in condition of node i's neighbor， with considering : 
(formula)

## Simulation
Formulas would be updated later.

## Analysis

This project was designed to simulate the propagation of virus over a scale-free network. Here, we use Python 3.7 and "networkx" module to do it. It could be carried out in the following steps: 
1) Generate a typical scale-free network with N nodes;  
2) Set each node's system attribution and infected some nodes randomly; 
3) According to the specific virus, determine the value of system_infected_coef for each system and the probability of recovery, 𝛾.  
4) Randomly pick a node, there are three cases:  
    a) state_infected_coef=0 
        It means the state of this node is "recover", no change will happen. 
    b) state_infected_coef=0.5 
        It means the state of this node is "susceptive", calculate the infected probability of this node, v. Compare the random number  
        with v, to determine whether this node will be infected. 
    c) state_infected_coef=1 
        It means the state of this node is "susceptive", calculate the infected probability of this node, v. Compare the random number 
        with v, to determine whether this node will be infected. repeat step iv iteration_number (e.g. 1000) times. show the number of             computers in different states. 

## Analysis 
Figure would update later.
