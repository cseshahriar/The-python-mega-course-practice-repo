""" exception """
try:
    a = 5 / 0
    b = a + '10'

except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everuthing is fine')
finally:
    print("cleaning up...")


""" custom exception """


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is to high')
    if x < 5:
        raise ValueTooSmallError('Value is to small', x)


try:
    test_value(4)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
