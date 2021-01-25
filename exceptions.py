""" exception handling"""
x = input("Enter number1: ")
y = input("Enter number2: ")

try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print('Zero division error ', e)
    z = None
except Exception as e:
    """ get exception type """
    print("Exception type is: ", type(e).__name__)
    z = None

print("div: ", z)
