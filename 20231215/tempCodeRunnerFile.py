try:
    print("Grade is " + 0)
    raise Exception("Not Possible")
except:
    print("Wrong")
    try:
        raise
    except:
        print("Isn't it?")
finally:
    print("I'm 4.5")
