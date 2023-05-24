from rp_param import Param
import numpy as np 
import popgen


class Sample(popgen.Haplotype):
    def __init__(self, ts=None, positions=None, matrix=None, ancestral_state=0):
        super().__init__(ts, positions, matrix, ancestral_state)
        self.mutation, self.singleton, self.informative = self._summary()
        haplotypes = []
        for i in range(self.nsamples):
            haplotypes.append(np.argwhere(self.matrix[i]==1).reshape(-1))
        self.haplotypes = haplotypes


    def _summary(self):
        summ = np.sum(self.matrix, axis=0)
        singleton = (summ==1) & (summ==self.nsamples-1)
        mutation = (summ!=0) & (summ!=self.nsamples)
        informative = mutation & ~singleton
        return mutation, singleton, informative

    def get_site(self, i):
        return self.matrix[:, i]

    def get_haplotype(self, i):
        return self.haplotypes[i]
    
    
    def calculate_pairwise_distance(self, i, j):
        first = self.get_haplotype(i)
        second = self.get_haplotype(j)
        left = 0
        right = 0
        left_mutation = 0
        right_mutation = 0
        index = 0

        current = 0 
        if first 
        
        # build for the first 

                


        


# class Node(popgen.Node):
#     def __init__(self, identifier=None, name=None, branch=None):
#         super().__init__(identifier, name, branch)


# class Clade():
#     def __init__(self, iterable=None) -> None:
#         if iterable is None:
#             self.nodes = []
#         else:
#             self.nodes = frozenset(iterable)

#     def add_node(self, node):
#         self.nodes.append(node)


# class Tree():
#     def __init__(self) -> None:
#         pass


