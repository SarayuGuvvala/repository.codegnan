'''
Data Analysis
------------
--> is the process of inspecting,cleaning, transforming , modeling data to discovers useful insights , support decision making .

types-
1.Descriptive Analysis
----------------------
--> summarizing data

2.Diagnostic Analysis
---------------------
--> is the process of examining data to understand why something happened. it helps identify the root cause of a problem or
situation by analyzing patterns,relationships,and trends in the data

3. Prescriptive Analysis
------------------------
--> Suggesting actions based on the data (Marketing)


Why?

NumPy
-----
--> Numerical python (Numpy) for computing
Numpy is a python library used for numerical and mathematical operations.
it provides support for arrays,matrices,and many mathematical functions

Creating NumPy Arrays
---------------------






'''
import numpy as np
arr_1 = np.array([1,2,3,4,5])
print(arr_1)

import numpy as np
arr_1 = np.array([1,2,3,4,5],[6,7,8,9,10])
print(arr_1)

'''
arange
-----
'''
import numpy as np
arr_1 = np.arange(1,20,2)
print(arr_1)
'''
Reshape
-------
'''
import numpy as np
arr_1 = np.array([[1,2,3,4],[5,6,7,8]])
reshape = arr_1.reshape(4,2)
print(reshape)
'''
Shallow copy & Deep copy
------------------------
'''
import numpy as np
arr_1 = np.array([10,20,30])
arr_view = arr_1.view()
arr_view[0] = 40 
print(arr_view)
print(arr_1)





'''
Pandas
------
-->pandas is a powerful Python library
'''
import pandas as pd
price = pd.Series([65,90,45,20],index=["apple","banana","curd","dal"]
print(price)
