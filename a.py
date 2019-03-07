print("a.py: At the top before imports")
from defaults import defaults
import b
print("a.py: Finished Imports.")
print("a.py: defaults: {}".format(defaults))

print("a.py: Calling b.py")
b.print_normal()
b.print_mod()
b.print_normal()

print("a.py: defaults: {}".format(defaults))
