# Exploring functionality specific to Python

# iterators/generators

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

# basic iterator printing ods up to a limit
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

# decorators


# dunders


# "Anything that catches your eye"

# *args and *kwargs -- useful for writing functions with generic parameters when
# arguments are unknown--works brilliantly with multiple passed-in arguments of 
# different types and using built-in .join():

def generic_arguments(*args):
    for item in args:
        return " ".join(args)
    
    
