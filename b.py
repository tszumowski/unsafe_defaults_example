print("b.py: At the top before imports")
from defaults import defaults
print("b.py: Finished Imports.")

def print_normal():
    print("b.py: print_normal(): {}".format(defaults))


def print_mod():
    print("b.py: print_mod(): {}".format(defaults))
    defaults["foo"] = "override!"
    print("b.py: print_mod(): {}".format(defaults))
