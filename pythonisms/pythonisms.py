# Exploring functionality specific to Python

# iterators/generators examples

# basic iterator class with limit (help from G4G):
class Print:
    def __init__(self, limit):
        self.limit = limit
        
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        count = self.x
        
        if count <= self.limit:
            self.x = count + 1
            return count
        else:
            raise StopIteration

# basic iterator printing odds up to a limit

# custom dunders
    def __affirm__(self):
        return f'You entered {self.limit} as the limit'
    
    def __type__(self):
        input_type = isinstance(self.limit,int)
        if input_type:
            return f'You entered the integer {self.limit}'
        else:
            return f'Ack, we can\'t do {self.limit} iterations'


class Printcount:
    def __init__(self, limit):
        self.limit = limit
        
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        count = self.x
        
        if count <= self.limit:
            self.x = count + 2
            return count
        else:
            raise StopIteration
        
# generator example

def repeated(thing):
    yield thing
    yield thing
    
def info_twice():
    for x in repeated('yellow'):
        print(x)

# decorators examples 

def python_dec(func):
    def wrapper(*args):
        a = 'pi'
        add_on = func(*args)
        b = 'a pie'        
        return f"{a}{add_on}{b}"
    return wrapper

@python_dec
def printzees():
    return 'zzzzzz'


@python_dec
def notzees(string):
    return f" {string} "

# Note the decorators in testing...I've been using these most of the course





# "Anything that catches your eye"

# *args and *kwargs -- useful for writing functions with generic parameters when
# arguments are unknown--works brilliantly with multiple passed-in arguments of 
# different types and using built-in .join():

def generic_arguments(*args):
    for item in args:
        return " ".join(args)
    
    
