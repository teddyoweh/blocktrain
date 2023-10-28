# mpi_task_dispatcher.py

from mpi4py import MPI
from tasks import my_task

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    task_inputs = [1, 2, 3, 4, 5]  # Your list of inputs
    num_tasks = len(task_inputs)
    for i in range(1, num_tasks + 1):
        comm.send(task_inputs[i - 1], dest=i, tag=i)
else:
    task_input = comm.recv(source=0, tag=rank)
    result = my_task.delay(task_input).get()
    print(f"Rank {rank} processed {task_input}, result: {result}")
