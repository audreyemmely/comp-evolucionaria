import pandas as pd 
import numpy as np

column_names = ['c1', 'c2', 'c3', 'c4', 'c5']
row_names = ['A', 'B', 'C', 'D', 'E']

matrix = np.reshape((1, 1, 0, 0, 0,
                     0, 0, 1, 0, 1,
                     1, 1, 0, 0, 1,
                     0, 1, 1, 1, 0,
                     1, 1, 0, 0, 1), (5, 5))

data = pd.DataFrame(matrix, columns = column_names, index = row_names)

# print(data) 
#só p conferir que tá nomeado corretamente