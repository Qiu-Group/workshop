from mpi4py import MPI 

comm = MPI.COMM_WORLD   # comm is the MPI object we will use
my_rank = comm.Get_rank()  # rank of processor 
p = comm.Get_size()       # how many processors  (this is after -n in your "mpirun -n 6 " command)

if my_rank != 0:    # rank = 0 is for the head processor 
    message = "Hello from "+str(my_rank)
    comm.send(message, dest=0)
else:
    for procid in range(1,p):
        message = comm.recv(source=procid)
        print("process  0 receives  message  from process", procid, ":", message)
