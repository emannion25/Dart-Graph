# Dart-Graph

``Dartgraph(edges, vertices)`` takes list of dart edges and list of dart vertices.
We use a tuple to list an edge: ``([ dart1, dart2 ], label)``
and use a tuple to list a vertex: ``([ dart1, dart2, dart3, ... ], label)``
so that ``edges`` is a list of tuples and ``vertices`` is also a list of tuples.

Our darts ``dart1,dart2,...`` are non-negative integers while ``label`` can be a number or a string. Also ``label`` can be empty but a comma must follow the list of darts
eg. ``([1,2,3], )`` is valid but ``([1,2,3] )`` is invalid.

Note that the **order of the darts** in  each vertex is important! We list the darts in the counter-clockwise direction (It determines the embedding in an orientable surface).


## What is a *Dart Graph*?

Traditionally a graph *G* consists of a set of edges *E* and a set of vertices *V*
where edges describe the connection between vertices.
A *dart graph* is defined over a set of darts *D* = {1,2,3,...,n}.
We think of darts as half edges and a vertex is represented by the set of darts that
are connected to it.

| Normal | Dart |
|---|---|
|<img src="images/graph3normal.png" alt="Normal Notation" height="300px"/>| <img src="images/graph3dart.png" alt="Dart Notation" height="300"/>|

The image on the left is the standard representation of a graph *G=(V,E)*.
We have vertex set *V*={*v1,v2,v3*} and edge set *E*={*e1,e2,e3*}.

The image on the right shows the same graph *G* but using dart notation.
This graph is defined over the set of darts *D* = {1, 2, 3, 4, 5, 6}.
Here the edge *e1* becomes the pair {1, 2}, *e2* is the pair {3, 4} and *e3* is the pair {5, 6}.
The vertex *v1* becomes the set {1, 6}, *v2* = {2, 3} and *v3* = {4, 5}. 
Here we have edge set *E* ={{1, 2}, {3, 4}, {5, 6}} and vertex set *V* = {{1, 6}, {2, 3}, {4, 5}}

## Example
The following piece of code is used to create the dart graph object for graph *G* above.
```python

from DartClass import Dartgraph
edges = [ ( [ 1 , 2 ] , ’ e1 ’ ) ,
          ( [ 3 , 4 ] , ’ e2 ’ ) ,
          ( [ 5 , 6 ] , ’ e3 ’ ) ]
vertices = [ ( [ 1 , 6 ] , ’ v1 ’ ) ,
             ( [ 2 , 3 ] , ’ v2 ’ ) ,
             ( [ 4 , 5 ] , ’ v3 ’ ) ]
G = Dartgraph( edges, vertices )
```



