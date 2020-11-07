
import matplotlib.pyplot as plt
import numpy as np
'''
Set the values in the variable x
The function arange helps to generate an array with the 
following parameters arange(start,end,increment)
'''
x = np.arange(-100,100,1)
'''
Now set the formula in the variable y
'''
y = x**2
'''
Then add the pair (x,y) to the plot
'''
plt.plot(x,y)
'''
Finally show the graph
'''
plt.show()