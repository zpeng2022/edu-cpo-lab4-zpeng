registration = {}


class Multiple(object):
    # Create a function
    def __init__(self, name):
        self.name = name
        self.typemap = {}

    # Make the object itself callable
    def __call__(self, *args, **kwargs):
        function = self.check_key_type(args, kwargs)
        return function(*args, **kwargs)

    def check_key_type(self, args, kwargs):
        type_list = list(self.typemap.keys())
        input_list = [arg for arg in args]
        for value in kwargs.values():
            input_list.append(value)
        for a_type in type_list:
            if len(a_type) == len(input_list):
                flag = 1
                for i in range(len(a_type)):
                    if isinstance(input_list[i], a_type[i]) is False:
                        flag = 0
                if flag == 1:
                    return self.typemap.get(a_type)
        raise TypeError("no match")

    # Add a new function to the type diagram
    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("multiple same registration")
        self.typemap[types] = function


def multiple(*types):
    def register(function):
        # add
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        result = registration.get(name)
        if result is None:
            result = registration[name] = Multiple(name)
        result.register(types, function)
        # add
        result.__lastreg__ = function
        return result

    return register
