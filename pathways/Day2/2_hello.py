from mpi4py import MPI 

comm = MPI.COMM_WORLD   # comm is the MPI object we will use
size = comm.Get_size()
rank = comm.Get_rank()

print ("Hello world from core", str(rank), "of", str(size))