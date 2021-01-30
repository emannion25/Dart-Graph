# Dart-Graph

``Dartgraph(edges, vertices)`` takes list of dart edges and list of dart vertices.
We use a tuple to list an edge: ``([ dart1, dart2 ], label)``
and use a tuple to list a vertex: ``([ dart1, dart2, dart3, ... ], label)``
so that ``edges`` is a list of tuples and ``vertices`` is also a list of tuples.

Our darts ``dart1,dart2,...`` are non-negative integers while ``label`` can be a number or a string. Also ``label`` can be empty but a comma must follow the list of darts
eg. ``([1,2,3], )`` is valid but ``([1,2,3] )`` is invalid.

Note that the **order of the darts** in  each vertex is important, we list the darts in the counter-clockwise direction. (It determines the embedding in an orientable surface)


## What is a *Dart Graph*?

Traditionally a graph *G* consists of a set of edges *E* and a set of vertices *V*
where edges describe the connection between vertices.
A *dart graph* is defined over a set of darts *D* ={1,2,3,...,n}.
We think of darts as half edges and a vertex is represented by the set of darts that
are connected to it.

| Normal | Dart |
|---|---|
|<img src="images/graph3normal.png" alt="Normal Notation" height="300px"/>| <img src="images/graph3dart.png" alt="Dart Notation" height="300"/>|
