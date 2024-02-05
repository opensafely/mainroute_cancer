import pandas as pd
import numpy as np

df = pd.read_csv("output/measures/measures_demo_imd.csv")

df = df.drop(df[df['imd'] == 'unknown'].index)
df = df.drop(df[df['measure'] == 'ca_6_rate'].index)

b = (df['denominator'] % 5)
df['followup_round'] = df['denominator']  + np.where(b>=3,5-b,-b)

def follow_up_years(row):
    return (row['followup_round'] / 365)

df["follow_up_years_round"]=df.apply(follow_up_years, axis=1)

s = (df['numerator'] % 5)
df['events_round'] = df['numerator']  + np.where(s>=3,5-s,-s)

df = df.drop('numerator', axis=1)
df = df.drop('denominator', axis=1)
df = df.drop('ratio', axis=1)
df = df.drop('followup_round', axis=1)

df.to_csv("output/measures/measures_demo_imd_symptoms.csv")