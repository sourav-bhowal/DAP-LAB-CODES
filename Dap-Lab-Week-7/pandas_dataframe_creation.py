import numpy as np  
import pandas as pd  

# Create DataFrame from 2D array  
data = np.array([['', 'Col1', 'Col2'],  
                 ['Row1', 1, 2],  
                 ['Row2', 3, 4]])  
print(pd.DataFrame(data=data[1:, 1:],  
                   index=data[1:, 0],  
                   columns=data[0, 1:]))  

# Create DataFrame from dictionary  
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}  
print(pd.DataFrame(my_dict))  

# Create DataFrame from Series  
my_series = pd.Series({"United Kingdom": "London", "India": "New Delhi", "United States": "Washington", "Belgium": "Brussels"})  
print(pd.DataFrame(my_series))  