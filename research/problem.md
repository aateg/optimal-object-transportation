# Problem Description

## Optimal Sequential Heavy Object Transportation with Magnetically-Reconfigurable Drones

The problem in simple lines is how to perform optimal transportation of objects via drone swarms. 

But the complexity increases when you consider actions that can be taken considering the whole journey of the drones, i.e., the sequence that the objects need to be transported, capacity of drones and velocity.

In order to include sequential optimality, the agents selection might consider the location of the next object as well.

Given a network of drones and objects to be transported:
1. What is the optimal order that the objects should be transported? (**TSP with in-between transportation**)

2. How to select k drones out of N drones in the network to transport each object? (**Travel-MultiSalesmen-Problem with in-between transportation**)
    - Considering that the drones can couple and decouple
    - Considering schedule of the drones and location of all drones, not only the ones available

3. How many drones are necessary to take one object? (Guess it's already solved)
    - Considering coupling of the drones

4. Which is the optimal path for the transportation?
    - SOLVED - the optimal path is straigth line
    - Sure? Only if the drones coupled achieved the maximum capacity

Problems 1 and 2 need to be handled together, because optimality needs to consider the whole network (drones, objects and destination locations)

Needs to minimize the cost of the whole tour.


### Variables of the problem
- Drones velocity 
    - Are they different of not? (I think should be equal because otherwise might have problems to fligh coupled)
- Drones velocity when coupled
    - Does it increase or decrease?
- Drones capacity
    - If each drone has different capacities
- Drone capacity when coupled
- Sequence of the objects to colect

## Things we are ignoring
- Collisions
- Navigation aroung obstacles

