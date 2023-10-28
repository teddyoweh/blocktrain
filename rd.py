import redis

def get_redis_host():
    try:
        # Connect to the Redis server
        client = redis.Redis()

        # Get the host information from the Redis server
        host_info = client.info('server')

        # Extract and print the host field
        host = host_info.get('server', {}).get('tcp_host', 'Unknown')
        print(host_info)
        return host

    except redis.exceptions.ConnectionError as e:
        # Handle connection error
        return str(e)

if __name__ == "__main__":
    redis_host = get_redis_host()
    print(f"The Redis server host is: {redis_host}")
