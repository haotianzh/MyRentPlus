import popgen
import numpy as np 
from popgen import utils
st = '((1,2), (3,4));'


configs = {'sequence_length': 500, 
           'population_size': 10,
           'rate': 1e-3,
           'recombination_rate': 1e-3}


simulator = popgen.Simulator(configs)
data = next(simulator(10, 1))
haplotype = data.haplotype.matrix
# print(np.arange(data.haplotype.nsites))
for row in haplotype:
    print(row)
# print(haplotype.shape)

bkpts = list(data.ts.breakpoints())
positions = data.haplotype.positions
start = 0
blocks = []
for i in range(data.haplotype.nsites):
    while (bkpts[start] <= positions[i]):
        start += 1
    blocks.append(start-1)

for i, row in enumerate(data.genealogies()):
    print(row, data.haplotype.positions[i], blocks[i])

print(bkpts)
print(data.haplotype.positions)
print(f'recomb: {len(list(data.ts.breakpoints()))}, mutation: {data.haplotype.nsites}')