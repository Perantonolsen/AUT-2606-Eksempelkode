from ctypes import *
so_file = "/home/pi/test_files/c_function.so"
function = CDLL(so_file)

print(function.square(0.5))
