
import math, cmath


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


classcode = 100 #already encoded classes


def decode(code):
   binary = []
   for x in range(0, 8):
       binary.append(code%2)
       code=math.floor(code/2)
   binary.reverse()
   return binary



