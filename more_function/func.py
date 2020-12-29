""" function """
def area(a, b=6): # params, 6 is default params
    return a * b

print(area(4, 5)) # non keyword args
print(area(a=5, b=5)) # keyword args

""" args not limit """
def mean(*args): # * for non keyword args
    return sum(args) / len(args)

print(mean(1,2,3,4,5))

def mean2(**kwargs): # ** for keyword args 
    return kwargs # return to dict

print(mean2(a=1, b=2, c=3))