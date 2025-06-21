class NegativeError(Exception):
    pass


def area(length,breadth):
    if length>=0 and breadth>=0:
        a=length*breadth
        return a
    else:
        raise NegativeError('-ve dimensions')
print(area(-5,3))