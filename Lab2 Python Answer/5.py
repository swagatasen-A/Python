#5. Compute a)sin of 60 degree b)cos of pi c)sin(0.8660254037844386) d)tan of 90 degree 
import math
sin_60 = math.sin(math.radians(60))
cos_pi = math.cos(math.pi)
sin_value = math.sin(0.8660254037844386)
try:
    tan_90 = math.tan(math.radians(90))
except ValueError as e:
    tan_90 = str(e)

print(f"sin(60 degrees) = {sin_60}")
print(f"cos(pi) = {cos_pi}")
print(f"sin(0.8660254037844386) = {sin_value}")
print(f"tan(90 degrees) = {tan_90}")
