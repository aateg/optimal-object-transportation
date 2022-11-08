# Unstructured Notes

Since the problem is sequential, we need to optimize the whole tour through the objects, but the way the drones goes to the object needs to consider the whole tour, and also might take different solutions considering the distance between destination of first object, and location of the second, plus the distance between the location of the second object and its destination.

Cost function should consider destination of the first object and location of the second.

## Strategy discussion

Another strategy might be to couple on-the-fly at an object. The advantage is that the problem is no longer potentially infinite, because you cannot couple and decouple repeatedly. It may even be possible to write it down formally as an optimization program, e.g. put three copies of an object that needs three drones, then the time to transport this object will be given as the time until all three drones arrive plus transportation time.

- Assign another object to an agent immediately after it is done with one object.

# Ideas

## TSP with in-between transportation 

Possible description for the novel 
- Salesman needs to visit each city but after each city he needs to takes the money he gained to some other destination  
- Salesman needs to see his wife after each city, for each city the salesman is, the wife is in a random location (known a priori for the salesman).  

The problem is similar to the original TSP, the difference is that the origin changes according to the city the salesman goes.This problem implies that selecting one city defines the location of the next origin (which is not the same)

### Questions
- How to model this as a linear programming approach?
- How to extend this to Multi salesmen?

