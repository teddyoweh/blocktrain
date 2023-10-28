from mpi4py import MPI

def prime_factors(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1

    return factors

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        number = 1000
        print(f"Calculating prime factors of {number} using {size} processes")

    
    number = comm.bcast(number, root=0)

    
    chunk_size = number // size
    start = rank * chunk_size
    end = start + chunk_size if rank != size - 1 else number

    local_factors = prime_factors(number)[start:end]

    
    all_factors = comm.gather(local_factors, root=0)

    if rank == 0:
        
        combined_factors = []
        for factors in all_factors:
            combined_factors.extend(factors)
        
        print(f"Prime factors of {number}: {combined_factors}")

if __name__ == "__main__":
    main()
