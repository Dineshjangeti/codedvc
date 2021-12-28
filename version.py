import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\mine\dvc_mine\data\data.csv")

Un = ['skin','has_diabetes','num_preg']

for i in Un:
    if i in df:
        del df[i]

diabetes_map = {True:1, False:0}
df['diabetes'] = df['diabetes'].map(diabetes_map)
print(df)
df.to_csv('Target.csv')
