from sys import meta_path
import pandas as pd

#from pandas.core.indexing import maybe_convert_ix
#from gilfoyle import report

df = pd.read_excel(r"/Users/B9Z/OneDrive - Storebrand/Attachments/soknader.xlsx")

#dropping rows
df = df.drop(labels=[0,0], axis=0)
df = df.drop(labels=range(178,524), axis=0)
df = df.drop(labels=range(2,162), axis=0)  #162
#print(df)

#dropping columns
df = df.drop(df.columns[[0,2,6,7,8]], axis=1)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 1)

df.to_html(r"/Users/B9Z/OneDrive - Storebrand/Attachments/mineSoknader.html", index=False)