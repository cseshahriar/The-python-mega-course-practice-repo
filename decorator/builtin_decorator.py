"""
কাস্টম ডেকোরেটর নিয়ে বেশ আলোচনা হয়েছে। এবার আমরা পাইথনের শক্তিশালী তিনটি 
বিল্ট-ইন ডেকোরেটর সম্পর্কে জানব।
"""

# classmethod ==============================================================


class MyClass:
    """Simple Class to define something"""

    def __init__(self):
        pass

    def square(self, x):
        return x**2

    @classmethod
    def cube(self, x):
        """
        ক্লাসমেথড ডেকোরেটর ব্যবহার করা হয় তখন ওই ফাংশন অবজেক্ট তৈরি না করেও 
        কল করা যায়।
        ক্লাসমেথড ডেকোরেটরের ক্ষেত্রে প্রথম আর্গুমেন্ট হবে ক্লাস বা ক্লাস ইনস্ট্যান্স।
        """
        return x**3


if __name__ == "__main__":

    obj = MyClass()
    # call by obj
    print(obj.square(3))
    print(obj.cube(3))

    # call by class
    print(MyClass.cube(3))
    # print(MyClass.square(3))  # problem is here


# staticmethod ============================================================
# ক্লাস ইনস্ট্যান্স বা self
class MyStaticClass:
    """Simple Class to define something"""

    def __init__(self):
        pass

    def square(self, x):
        return x**2

    @staticmethod
    def cube(x):  # self ?
        return x**3


if __name__ == "__main__":
    staticObj = MyClass()

    print(staticObj.square(3))
    print(staticObj.cube(3))

    print(MyStaticClass.cube(3))
    # print(MyStaticClass.square(3))


# প্রোপার্টি - @property =========================================================
"""
প্রোপার্টি ডেকোরটের ব্যবহার করে আমরা full_name() মেথডকে রিড-অনলি অ্যাট্রিবিউটে পরিণত করেছি। তাই সাধারণভাবে ডট চিহ্ন (.) দিয়ে full_name-কে অ্যাক্সেস করতে পারছি।
 আর রিড-অনলি হওয়ায় এই অ্যাট্রিবিউটে নতুন কিছু দেওয়া যাচ্ছে না। 
"""


class MyAnotherAnotherClass:
    """Simple Class to define something"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


if __name__ == "__main__":
    obj3 = MyAnotherAnotherClass('Maksudur', 'Rahman')
    print(obj3.full_name)
    # obj3.full_name = 'New Name' # read only
