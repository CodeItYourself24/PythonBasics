
#           <<<<<<<< BASIC INTRO OF DATA STRUCTURES IN PANDAS >>>>>>>>>>

import pandas as pd

# SERIES >>

l = [10,20,30,40,50]
print(pd.Series(l))     # pass the list as a parameter

'''
gives the o/p as:

0    10
1    20
2    30
3    40
4    50
dtype: int64
'''

# we can also change/add the index as below

print(pd.Series(l,index=[1,2,3,4,5]))
'''
gives o//p as:

1    10
2    20
3    30
4    40
5    50
dtype: int64
'''

# DATAFRAME >>

d = {'Name':['Sandeep','Tarun','Shiva'],'Age':[29,29,30]}
print(pd.DataFrame(d,index=[1,2,3]))  # passing the dic as a parameter
'''
gives o/p as below:

      Name  Age
1  Sandeep   29
2    Tarun   29
3    Shiva   30
'''

