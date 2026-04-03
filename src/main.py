# LAB04: Higher-Order Functions, map/filter,
Decorators


# Task A — Higher-Order Function

def apply(func, data):
    result = []
    for x in data:
        result.append(func(x))
    return result

print(apply(lambda x: x * 2, [1, 2, 3]))


# Task B — map

nums = [1, 2, 3]
print(list(map(lambda x: x**2, nums)))
print(list(map(lambda x: str(x), nums)))


# Task C — filter


nums = [5, 10, 15, 20]

even = list(filter(lambda x: x % 2 == 0, nums))
greater_10 = list(filter(lambda x: x > 10, nums))

print(even)
print(greater_10)


# Task D — map/filter vs comprehension

nums = [1, 2, 3, 4, 5]
res1 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
res2 = [x**2 for x in nums if x % 2 == 0]
print(res1)
print(res2)


# Task E — Simple Decorator

def call_counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print("call #", count)
        func()

    return wrapper
    
@call_counter
def test():
    print("Function is running")

test() 
test() 


# Task F — Decorator with Arguments

def prefix(text):
    def decorator(func):
        def wrapper():
            result = func()
            return text + ": " + result
        return wrapper
    return decorator

@prefix("INFO")
def get_data():
    return "data"

print(get_data())


# Task G — Caching Decorator

def cache(func):
    saved = {}

    def wrapper(n):
        if n in saved:
            print("from cache:", n)
            return saved[n]

        print("calculating:", n)
        result = func(n)
        saved[n] = result
        return result

    return wrapper


def trib(n):
    if n <= 2:
        return 1
    return trib(n-1) + trib(n-2) + trib(n-3)


@cache
def trib_cached(n):
    if n <= 2:
        return 1
    return trib_cached(n-1) + trib_cached(n-2) + trib_cached(n-3)


print("Without cache:")
print(trib(5))

print("\nWith cache:")
print(trib_cached(5))
