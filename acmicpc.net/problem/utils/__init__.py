def check_time_limit(solution, limit: int):
    from time import time

    def wrapper(*args, **kwargs):
        start = time()
        result = solution(*args, **kwargs)
        assert time() - start <= limit
        return result
    return wrapper
