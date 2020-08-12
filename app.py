# import package_example.utils
from package_example import utils  # package.module
import convertor  # module

utils.display("Sumit")
print(convertor.kgs_to_lbs(70))

# two ways to organise code
# module is collection of functions
# package is collection of modules

# ex: package called Number has Interger, Float as section and each of these
# will have modules which will be collection of related functions

# Number > Integer > utils.py
# Number > Float > utils.py
