#Page is unused but will be what would be encoding the user submitted recommended classes into a single decimal
import math, cmath
class1 = 1 #8 booleans from user submission ready to be encoded
class2 = 1
class3 = 0
class4 = 1
class5 = 0
class6 = 1
class7 = 1
class8 = 1

def encode(class1,class2,class3,class4,class5,class6,class7,class8):
   code = 0
   code = (2*code) + class1
   code = (2*code) + class2
   code = (2*code) + class3
   code = (2*code) + class4
   code = (2*code) + class5
   code = (2*code) + class6
   code = (2*code) + class7
   code = (2*code) + class8
   return code

UserClass = (encode(class1,class2,class3,class4,class5,class6,class7,class8)))


classcode = 100 #already encoded classes


def decode(code):
   binary = []
   for x in range(0, 8):
       binary.append(code%2)
       print(code%2)
       print(code)
       code=math.floor(code/2)
   binary.reverse()
   return binary

print(decode(classcode))

