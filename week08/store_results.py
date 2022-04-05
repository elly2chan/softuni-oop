def store_results(function):
    def wrapper(*args):
        func_result = function(*args)
        with open('./results.txt', 'a') as file:
            file.write(f"Function '{function.__name__}' was called. Result: {func_result}\n")
        return wrapper

@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)