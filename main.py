"""
When a Python interpreter reads a Python file, it first sets a few special 
variables. Then it executes the code from the file.
One of those variables is called __name__.
If you follow this article step-by-step and read its code snippets, 
you will learn how to use if __name__ == "__main__", and why it's so important.

"""
print("File one __name__ is set to: {}" .format(__name__))


def calculate_area(base, height):
    return 1/2 * (base * height)


if __name__ == "__main__":  # main is entry point
    a = calculate_area(10, 20)
    print(a)
