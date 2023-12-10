try:
    raise ValueError
except ValueError:
    print("ValueError occurred")
    raise TypeError
except TypeError:
    print("TypeError occurred")
