from mpi4py import MPI 
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

if rank == 0:
    data = np.arange(302.0)
    #sum(data)
    data = np.array_split(data, nprocs)


else:
    data = None

data = comm.scatter(data, root=0)

print('Process {} has data:'.format(rank), data)
#print(data[2])
partial_sum = 0.0 

for i in data:
    partial_sum += i

partial_sum = comm.gather(partial_sum, root=0)

#total_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)

if rank == 0:
    print("Gathered at head")
    print("Sum is {} from all data" .format(sum(partial_sum)))
    #print("Sum is {}" .format(total_sum))

