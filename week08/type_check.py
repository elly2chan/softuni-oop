def type_check(data_type):
    def decorator(function):
        def wrapper(value):
            if not isinstance(value, data_type):
                return 'Bad Type'
            return function(value)
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))