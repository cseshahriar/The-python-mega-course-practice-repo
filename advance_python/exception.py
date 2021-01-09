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


def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is to high')


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
