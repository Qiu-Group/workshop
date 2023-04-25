from mpi4py import MPI 
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

if rank == 0:
    data = np.arange(32.0)
    #sum(data)
    data = np.array_split(data, nprocs)


else:
    data = None

data = comm.scatter(data, root=0)

print('Process {} has data:'.format(rank), data)
