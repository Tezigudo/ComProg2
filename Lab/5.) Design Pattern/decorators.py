def tracer(func):
    """decorator that print evey time that finction was call"""
    count = 0  # number of times the function was called

    def print_func(*args, **kwargs):
        """print function name and arguments"""
        nonlocal count  # nonlocal variable
        # print the function name and arguments if any,
        # with indentation based on the call depth
        kw_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        if len(args) == 1:
            print('  ' * count + f"{func.__name__}(", *args, ') ', kw_str, sep='')
        else:
            print('  ' * count + f"{func.__name__}{args} {kw_str}")
        count += 1  # increment the call depth
        result = func(*args, **kwargs)  # call the function
        print('  ' * (count-1), result, sep='')  # print the result
        count -= 1  # decrement the call depth
        return result
    return print_func
