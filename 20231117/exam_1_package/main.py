from test import test


try:
    print(test.Test.string)
except ImportError:
    print("error occured!")
