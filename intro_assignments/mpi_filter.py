from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# ADJUST THE FILTER FUNCTION HERE
def predicate(item):
    if item % 2 == 0:
        return True
    else:
        return False

if rank == 0:
    # ADJUST THE DATA HERE
    data = [random.randint(0,10) for _ in range(100)] 
    grouped_data = [[] for _ in range(size)]
    for i, datum in enumerate(data):
        grouped_data[i % size].append(datum)
else:
    data = []
    grouped_data = []

#Scatter
grouped_data = comm.scatter(grouped_data, root=0)
print "rank", rank, "recieved", data
grouped_data = filter(predicate, grouped_data)

#Gather
grouped_data = comm.gather(grouped_data, root=0)

comm.Barrier()

if rank == 0:
    print [item for sublist in grouped_data for item in sublist]