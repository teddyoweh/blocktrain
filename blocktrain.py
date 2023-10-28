import dask
from dask.distributed import Client, progress


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

if __name__ == "__main__":
    
    client = Client('10.66.106.228:8786')  
    
    
    numbers = [19000]  
    
    
    futures = client.map(prime_factors, numbers)
    
    
    results = client.gather(futures)
    
    
    for num, factors in zip(numbers, results):
        print(f"Prime factors of {num}: {factors}")
    
    
    client.close()
