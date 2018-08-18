import pandas as pa
import quandl
from sklearn import preprocessing

df = quandl.get('WIKI/GOOGL')
print(df.head())
df=df[]