# Note that Sage is required for full implementation.
# Sage works identical to Python with some additional 'Maths' features.

class Dartgraph():    
    def __init__(self,edges,vertices):
        from sage.rings.integer import Integer
        #Create list of edge darts and labels
        dartlist=[]
        edgelabels=[]
        for edge in edges:
            #Check edge is tuple
            if isinstance(edge,tuple)==False:
                raise TypeError('The edge %s is not a tuple!'%edge)
            #If there is no label given, use None
            if len(edge)==1:
                edge+=(None,)
            edgelabels+=[edge[1]]
            #Check only 2 darts in each edge
            if len(edge[0])!=2:
                raise ValueError('The edge %s must have 2 darts!'%edge[0])
            for dart in edge[0]:
                dartlist+=[dart]
        D={}
        for dart in dartlist:
            #Check darts are non negative integers
            if isinstance(dart,Integer)==False or dart<0:
                raise ValueError('In Edges:,%s is NOT a non-negative integer!'%dart)
            D[dart]=1
        #Check unique darts in edges
        if len(D)!=len(dartlist):
            raise ValueError('Edge Darts are NOT unique!')
        #Create list of vertex darts, degrees and labels
        degreelist=[]
        dartlistV=[]
        vertexlabels=[]
        for vertex in vertices:
            #Check vertex is tuple
            if isinstance(vertex,tuple)==False:
                raise TypeError('%s is not a tuple!'%vertex)
            #If there is no label given, use None
            if len(vertex)==1:
                vertex+=(None,)
            degree=len(vertex[0])
            degreelist+=[degree]
            vertexlabels+=[vertex[1]]
            for dart in vertex[0]:
                dartlistV+=[dart]
        D={}
        for dart in dartlistV:
            #Check darts are non negative integers
            if isinstance(dart,Integer)==False or dart<0:
                raise ValueError('In Vertices:, %s is NOT a non-negative integer!'%dart)
            D[dart]=1
        #Check unique darts in vertices
        if len(D)!=len(dartlistV):
            raise ValueError('Vertex Darts are NOT unique!')
        #Check both dart lists are the same
        dartlist.sort()
        dartlistV.sort()
        if dartlist!=dartlistV:
            raise ValueError('Edge darts are different to Vertex darts!')

        self.Edges=edges
        self.Vertices=vertices
        self.Darts=dartlist
        self.Degree_Sequence=degreelist
        self.Edge_Labels=edgelabels
        self.Vertex_Labels=vertexlabels

    def Sage_Vertices(self,label=False):
        #Create list of vertices in the standard form v1,v2,...
        sagevertexlist=[]
        vertices=self.Vertices
        for vertex in vertices:
            if label:
                ind=vertices.index(vertex)
                #If there is no label given, use None
                if len(vertex)==1:
                    vertex+=(None,)
                sagevertexlist+=[(ind,vertex[1])] #Labels
            else:
                sagevertexlist+=[vertices.index(vertex)] #No Labels
        return sagevertexlist
    
    def Sage_Edges(self,label=False):    
        #Create list of edges that can be used by standard sage graph function,
        #with an edge between v1 and v2 denoted (v1,v2)
        sageedgelist=[]
        for edge in self.Edges:
            sageedge=()
            for dart in edge[0]:
                vertnumb=0
                for vertex in self.Vertices:
                    if dart in vertex[0]:
                        if label:
                            if len(vertex)==1:
                                raise ValueError('All vertices must have a label!')
                            sageedge+=(vertex[1],) #Labels included
                        else:
                            sageedge+=(vertnumb,) #No Labels
                    vertnumb+=1
            if label:
                #If there is no label given, use None
                if len(edge)==1:
                    edge+=(None,)
                sageedgelist+=[sageedge+(str(edge[1]),)] #Labels included
            else:
                sageedgelist+=[sageedge] #No Labels
        return sageedgelist

    def Sage_Graph(self,label=False):
        # This creates a standard sage graph object.
        # If label=True then all vertices MUST have a label.
        from sage.graphs.graph import Graph
        edges=self.Sage_Edges(label)
        sagegraph=Graph(edges,loops=True,multiedges=True)
        return sagegraph

    # Graph corresponds to Rotation System (Sigma,Alpha)
    def Alpha(self):
        from sage.combinat.permutation import Permutation
        P=[]
        for edge in self.Edges:
            P.append(tuple(edge[0]))    
        alpha_perm=Permutation(P)
        return alpha_perm

    def Sigma(self):
        from sage.combinat.permutation import Permutation
        P=[]
        for vertex in self.Vertices:
            P.append(tuple(vertex[0]))
        sigma_perm=Permutation(P)
        return sigma_perm

    def Tau(self):
        alpha_perm=self.Alpha()
        sigma_perm=self.Sigma()
        tau_perm=sigma_perm.left_action_product(alpha_perm)
        return tau_perm

    def Alpha_group(self):
        from sage.groups.perm_gps.permgroup import PermutationGroup
        a=self.Alpha().cycle_tuples()
        A=PermutationGroup(gens=a)
        return A

    def Sigma_group(self):
        from sage.groups.perm_gps.permgroup import PermutationGroup
        s=self.Sigma().cycle_tuples()
        S=PermutationGroup(gens=s)
        return S

    def Tau_group(self):
        from sage.groups.perm_gps.permgroup import PermutationGroup
        t=self.Tau().cycle_tuples()
        T=PermutationGroup(gens=t)
        return T

    def Faces(self):
        #Returns list of faces.
        #Each face is a list of darts on its boundary.
        T=self.Tau_group()
        faces=T.orbits()
        return faces
        
    def Connected_components(self):
        from sage.groups.perm_gps.permgroup import PermutationGroup
        a=self.Alpha().cycle_tuples()
        s=self.Sigma().cycle_tuples()
        P=PermutationGroup(gens=a+s)
        ccs=P.orbits()
        return ccs

    def Is_connected(self):
        if len(self.Connected_components())==1:
            return True
        else:
            return False

    def Euler(self):
        v=len(self.Vertices)
        e=len(self.Edges)
        f=len(self.Faces())
        chi=v-e+f
        return chi
    
    def Genus(self):
        chi=self.Euler()
        g=1-chi/2
        return g
