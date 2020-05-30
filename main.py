import numpy as np
import pandas as pd
from random import randint
n = 10000 # set the variable responsible for the number of rows and columns
df = pd.DataFrame (np.random.randint (0,2, size = (n, n)), columns = range (n)) # create a frame with a random number
nullnumber = randint (0, n) # Generate a value for the column that we fill with zeros
df [nullnumber] = 0 # Fill one column with zero values ​​for certainty
df.iloc [nullnumber: nullnumber + 1] = 0 # For certainty, fill one line with zero values
df = df.loc [:, (df! = 0) .any (axis = 0)] # Find all the columns with zero values ​​by the columns and delete them
df ['summ'] = df.sum (axis = 1) # Count the sum over all columns in a new column
df = df.loc [df.loc [:, 'summ']> 0] [:]
#We save only those columns where the sum> 0, those are non-zero values.
del df ['summ'] # Delete the extra column
collections = df.drop_duplicates (keep = 'first'). reset_index (drop = True) # create a frame where each line has a unique collection of films.
