import module1
module1.posORneg(-10)
module1.posORneg(10)
module1.posORneg(0)

#another way
check= module1.posORneg
check(10)

#to use a particular function from a module
from module1 import hey
hey("chandhu")
from module1 import posORneg
posORneg(0)