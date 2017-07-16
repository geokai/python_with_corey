import sys
sys.path.append('/home/pi/bin/05.python_with_corey/my-modules')

from screen_clear import clear

clear()

# various ways to import modules:
#import my_module
#import my_module as mm
from my_module import find_index, test

print(sys.executable)
print(sys.version)
print()
print(sys.path)
print()


print()

courses = ['History', 'Math', 'Physics', 'ComSci']

#index = my_module.find_index(courses, 'Math')
#index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Lit')
#index = fi(courses, 'Math')
print(index)
print(test)
print()

