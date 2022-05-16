# testing python unknown operator
# https://stackoverflow.com/questions/22832615/what-do-and-mean-in-python

print(1 << 9)
print(110 << 4)
print(3 << 2)

# SOf answer
# 12 << 2
# 48
# Actual binary value of 12 is "00 1100" when we execute the above statement Left shift ( 2 places shifted left) returns the value 48 its binary value is "11 0000".
# 48 >> 2
# 12
# The binary value of 48 is "11 0000", after executing above statement Right shift ( 2 places shifted right) returns the value 12 its binary value is "00 1100".

# Conclusion << or >> is for shifting bits in determined quantity
