from mpi4py import MPI
import time
def prime_factors(n):
    factors = []
    # Handle the case of even numbers first
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd divisors starting from 3 up to the square root of n
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2  # Skip even divisors

    # If n is a prime number greater than 2, add it to factors
    if n > 2:
        factors.append(n)

    return factors


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        number = 353435435359340#345394804848484894784982498449824984
        print(f"Calculating prime factors of {number} using {size} processes")

    number = comm.bcast(number, root=0)

    chunk_size = number // size
    start = rank * chunk_size
    end = start + chunk_size if rank != size - 1 else number

    # Timing: start measuring time
    start_time = time.time()

    local_factors = prime_factors(number)[start:end]

    all_factors = comm.gather(local_factors, root=0)

    if rank == 0:
        # Stop measuring time
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time for factorization: {elapsed_time} seconds")

        combined_factors = []
        for factors in all_factors:
            combined_factors.extend(factors)

        print(f"Prime factors of {number}: {combined_factors}")

if __name__ == "__main__":
    main()
 