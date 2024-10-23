def my_function(*args, **kwargs):
    return len([x for x in args if x in kwargs.values()])

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
