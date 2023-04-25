from mpi4py import MPI 
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

if rank == 0:
    data = np.arange(6.0)

else:
    data = None

data = comm.scatter(data, root=0)

print('Process {} has data:'.format(rank), data)
