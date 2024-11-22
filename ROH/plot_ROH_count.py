import pandas as pd
import numpy as np
from plotnine import *

df=pd.read_csv('all_pops.roh', sep='\t', header = 0)

# Convert 'ROH' to numeric, setting errors='coerce' will replace non-numeric values with NaN
df['ROH'] = pd.to_numeric(df['ROH'], errors='coerce')

##add range column short=<200Kb; medium=200-400Kb; long=>400Kb
df['range'] = df['ROH'].apply(lambda value: 'short' if value < 200 else ('long' if value > 400 else 'medium'))
print(df)

# Remove rows where the first column starts with 'FID'
df = df[~df.iloc[:, 0].astype(str).str.startswith('FID')]

##Print new df
df.to_csv("all_pops.roh_classes", header=True, index=False, sep='\t', mode='w')

##count how many ROH per ind per range
df2 = df.groupby(['Species','Ind','range']).size().reset_index(name='counts')
print(df2)

##Print new df
df2.to_csv("all_pops.roh_classes.count", header=True, index=False, sep='\t', mode='w')

##plot average of count of ROH per ind per pop - DODGE
(
ggplot(df2)
+ geom_bar(aes('Species', 'counts', fill='range'), position='dodge', stat='summary', fun_y=np.mean)
+ theme_minimal()
)

##plot average of count of ROH per ind per pop - STACK
(
ggplot(df2)
+ geom_bar(aes('Species', 'counts', fill='range'), position='stack', stat='summary', fun_y=np.mean)
+ theme_minimal()
)

##sum ROH per ind per range
df3 = df.groupby(['Species','Ind','range'])['ROH'].agg('sum').reset_index()
print(df3)

##Print new df
df3.to_csv("all_pops.roh_classes.sum", header=True, index=False, sep='\t', mode='w')

##plot average of lenght per range of ROH per ind per pop
(
ggplot(df3)
+ geom_bar(aes('Species', 'ROH', fill='range'), position='dodge', stat='summary', fun_y=np.mean)
+ theme_minimal()
)
