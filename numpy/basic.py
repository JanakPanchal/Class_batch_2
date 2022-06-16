import numpy as np
from numpy import random
import pandas as pd
arr = random.randint(1000)
print(arr)

arr1 = np.array([1,10,20,3,15,20, 10, 22, 50,24])
print(arr1[2])
arr2 = np.array([10,30.40,50,20,40])
arr3 = np.concatenate((arr1,arr2))
print(arr3)
arr4 = arr3

#romdom
random.shuffle(arr4)
print(arr4)
random.permutation(arr3)
print(arr3)


#noraml
#loc = means
#scale = SD
#size

y = random.normal(loc = 40 , scale= 100 , size=(3,5) )
print(y)

#Binomial
a = random.binomial(n = 10 , p = 0.5 , size = 10)
print(a)

#Poisson
z = random.poisson(lam= 3 , size=10)
print(z.copy())

