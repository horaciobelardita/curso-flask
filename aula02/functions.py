def say_hi(name: str, to_upper=False):
    name = name.upper() if to_upper else name
    print(f"Hello, {name}")


def fn_sum(*args) -> int:
    from functools import reduce

    return reduce(lambda prev, num: prev + num, args)


def header(fn):
    def wrapper(*args, **kwargs):
        print("### Welcome to our site ###")
        print()
        return fn(*args, **kwargs)

    return wrapper


def footer(fn):
    def wrapper(*args, **kwargs):
        print("### Copyright 2020 ###")
        print()
        return fn(*args, **kwargs)

    return wrapper


@header
@footer
def message(content: str):

    print(content)


say_hi("Alex")

say_hi(name="Carla")
say_hi("Mark", to_upper=True)
params = ("Carlos", False)
say_hi(*params)
print(fn_sum(1, 2, 3, 4))

# header = lambda: say_hi("Header")
# footer = lambda: say_hi("Footer")
# message(header, footer)

message("Contenido del sitio aqui")
