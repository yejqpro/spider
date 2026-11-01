# 引入pandas
import numpy as np
import pandas as pd
# 读取全部数据
df=pd.read_csv("./Cloudtheory.csv",names=['title','date','context'],skipinitialspace=True)
df['context'] = df['context'].str.replace(' ', '')
df['context'] = df['context'].str.replace('\n', '')
df['context'] = df['context'].str.replace('\r', '')
print(df)
df['context'] = df['context'].replace('', np.nan)
null=df.isnull()
df.fillna("null", inplace = True)
df.to_csv('./Cloudtheory_new.txt',header=0,index=False)