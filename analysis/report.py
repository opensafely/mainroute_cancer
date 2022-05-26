import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("output/input_paired.csv")

data_symptom = data[["colorectal_symptom_1_date_symp_date", "colorectal_symptom_2_date_symp_date", "colorectal_symptom_3_date_symp_date", "colorectal_symptom_4_date_symp_date", "colorectal_symptom_5_date_symp_date", "colorectal_symptom_6_date_symp_date", "colorectal_symptom_7_date_symp_date", "colorectal_symptom_8_date_symp_date", "colorectal_symptom_9_date_symp_date", "colorectal_symptom_10_date_symp_date"]]
data_referral = data[["colorectal_symptom_1_date_ref_date", "colorectal_symptom_2_date_ref_date", "colorectal_symptom_3_date_ref_date", "colorectal_symptom_4_date_ref_date", "colorectal_symptom_5_date_ref_date", "colorectal_symptom_6_date_ref_date", "colorectal_symptom_7_date_ref_date", "colorectal_symptom_8_date_ref_date", "colorectal_symptom_9_date_ref_date", "colorectal_symptom_10_date_ref_date"]]

num_symptoms = data_symptom.count(axis=1)

plt.hist(num_symptoms.values.tolist(), bins=10)

plt.savefig('output/colorectal_cancer.jpg')

plt.clf()

data_symptom['colorectal_symptom_1_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_1_date_symp_date'])
data_symptom['colorectal_symptom_2_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_2_date_symp_date'])
data_symptom['colorectal_symptom_3_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_3_date_symp_date'])
data_symptom['colorectal_symptom_4_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_4_date_symp_date'])
data_symptom['colorectal_symptom_5_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_5_date_symp_date'])
data_symptom['colorectal_symptom_6_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_6_date_symp_date'])
data_symptom['colorectal_symptom_7_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_7_date_symp_date'])
data_symptom['colorectal_symptom_8_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_8_date_symp_date'])
data_symptom['colorectal_symptom_9_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_9_date_symp_date'])
data_symptom['colorectal_symptom_10_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_10_date_symp_date'])
data_month_year_1 = data_symptom['colorectal_symptom_1_date_symp_date'].dt.to_period('M')
data_month_year_2 = data_symptom['colorectal_symptom_2_date_symp_date'].dt.to_period('M')
data_month_year_3 = data_symptom['colorectal_symptom_3_date_symp_date'].dt.to_period('M')
data_month_year_4 = data_symptom['colorectal_symptom_4_date_symp_date'].dt.to_period('M')
data_month_year_5 = data_symptom['colorectal_symptom_5_date_symp_date'].dt.to_period('M')
data_month_year_6 = data_symptom['colorectal_symptom_6_date_symp_date'].dt.to_period('M')
data_month_year_7 = data_symptom['colorectal_symptom_7_date_symp_date'].dt.to_period('M')
data_month_year_8 = data_symptom['colorectal_symptom_8_date_symp_date'].dt.to_period('M')
data_month_year_9 = data_symptom['colorectal_symptom_9_date_symp_date'].dt.to_period('M')
data_month_year_10 = data_symptom['colorectal_symptom_10_date_symp_date'].dt.to_period('M')

data_month_year = pd.concat([data_month_year_1, data_month_year_2, data_month_year_3, data_month_year_4, data_month_year_5, data_month_year_6, data_month_year_7, data_month_year_8, data_month_year_9, data_month_year_10], axis=1)

counts = data_month_year.stack().value_counts()

counts = counts.sort_index()

ax = counts.plot.bar()

plt.savefig('output/colorectal_cancer_2.jpg')

plt.clf()

data_null = data.notnull()

def condition1(s):
    if s['colorectal_symptom_1_date_symp_date'] & s['colorectal_symptom_1_date_ref_date']:
        return 1
    else:
        return 0

def condition2(s):
    if s['colorectal_symptom_2_date_symp_date'] & s['colorectal_symptom_2_date_ref_date']:
        return 1
    else:
        return 0

def condition3(s):
    if s['colorectal_symptom_3_date_symp_date'] & s['colorectal_symptom_3_date_ref_date']:
        return 1
    else:
        return 0

def condition4(s):
    if s['colorectal_symptom_4_date_symp_date'] & s['colorectal_symptom_4_date_ref_date']:
        return 1
    else:
        return 0

def condition5(s):
    if s['colorectal_symptom_5_date_symp_date'] & s['colorectal_symptom_5_date_ref_date']:
        return 1
    else:
        return 0

def condition6(s):
    if s['colorectal_symptom_6_date_symp_date'] & s['colorectal_symptom_6_date_ref_date']:
        return 1
    else:
        return 0

def condition7(s):
    if s['colorectal_symptom_7_date_symp_date'] & s['colorectal_symptom_7_date_ref_date']:
        return 1
    else:
        return 0

def condition8(s):
    if s['colorectal_symptom_8_date_symp_date'] & s['colorectal_symptom_8_date_ref_date']:
        return 1
    else:
        return 0

def condition9(s):
    if s['colorectal_symptom_9_date_symp_date'] & s['colorectal_symptom_9_date_ref_date']:
        return 1
    else:
        return 0

def condition10(s):
    if s['colorectal_symptom_10_date_symp_date'] & s['colorectal_symptom_10_date_ref_date']:
        return 1
    else:
        return 0

data['colorectal_conversion_1'] = data_null.apply(condition1, axis=1)
data['colorectal_conversion_2'] = data_null.apply(condition2, axis=1)
data['colorectal_conversion_3'] = data_null.apply(condition3, axis=1)
data['colorectal_conversion_4'] = data_null.apply(condition4, axis=1)
data['colorectal_conversion_5'] = data_null.apply(condition5, axis=1)
data['colorectal_conversion_6'] = data_null.apply(condition6, axis=1)
data['colorectal_conversion_7'] = data_null.apply(condition7, axis=1)
data['colorectal_conversion_8'] = data_null.apply(condition8, axis=1)
data['colorectal_conversion_9'] = data_null.apply(condition9, axis=1)
data['colorectal_conversion_10'] = data_null.apply(condition10, axis=1)

data_1 = data[['colorectal_symptom_1_date_symp_date', 'colorectal_conversion_1']]
data_1 = data_1.rename(columns={"colorectal_symptom_1_date_symp_date":"symptom_date", "colorectal_conversion_1":"conversion"})
data_1['symptom_date'] = pd.to_datetime(data_1['symptom_date'])
data_1['symptom_date'] = data_1['symptom_date'].dt.to_period('M')

data_2 = data[['colorectal_symptom_2_date_symp_date', 'colorectal_conversion_2']]
data_2 = data_2.rename(columns={"colorectal_symptom_2_date_symp_date":"symptom_date", "colorectal_conversion_2":"conversion"})
data_2['symptom_date'] = pd.to_datetime(data_2['symptom_date'])
data_2['symptom_date'] = data_2['symptom_date'].dt.to_period('M')

data_3 = data[['colorectal_symptom_3_date_symp_date', 'colorectal_conversion_3']]
data_3 = data_3.rename(columns={"colorectal_symptom_3_date_symp_date":"symptom_date", "colorectal_conversion_3":"conversion"})
data_3['symptom_date'] = pd.to_datetime(data_3['symptom_date'])
data_3['symptom_date'] = data_3['symptom_date'].dt.to_period('M')

data_4 = data[['colorectal_symptom_4_date_symp_date', 'colorectal_conversion_4']]
data_4 = data_4.rename(columns={"colorectal_symptom_4_date_symp_date":"symptom_date", "colorectal_conversion_4":"conversion"})
data_4['symptom_date'] = pd.to_datetime(data_4['symptom_date'])
data_4['symptom_date'] = data_4['symptom_date'].dt.to_period('M')

data_5 = data[['colorectal_symptom_5_date_symp_date', 'colorectal_conversion_5']]
data_5 = data_5.rename(columns={"colorectal_symptom_5_date_symp_date":"symptom_date", "colorectal_conversion_5":"conversion"})
data_5['symptom_date'] = pd.to_datetime(data_5['symptom_date'])
data_5['symptom_date'] = data_5['symptom_date'].dt.to_period('M')

data_6 = data[['colorectal_symptom_6_date_symp_date', 'colorectal_conversion_6']]
data_6 = data_6.rename(columns={"colorectal_symptom_6_date_symp_date":"symptom_date", "colorectal_conversion_6":"conversion"})
data_6['symptom_date'] = pd.to_datetime(data_6['symptom_date'])
data_6['symptom_date'] = data_6['symptom_date'].dt.to_period('M')

data_7 = data[['colorectal_symptom_7_date_symp_date', 'colorectal_conversion_7']]
data_7 = data_7.rename(columns={"colorectal_symptom_7_date_symp_date":"symptom_date", "colorectal_conversion_7":"conversion"})
data_7['symptom_date'] = pd.to_datetime(data_7['symptom_date'])
data_7['symptom_date'] = data_7['symptom_date'].dt.to_period('M')

data_8 = data[['colorectal_symptom_8_date_symp_date', 'colorectal_conversion_8']]
data_8 = data_8.rename(columns={"colorectal_symptom_8_date_symp_date":"symptom_date", "colorectal_conversion_8":"conversion"})
data_8['symptom_date'] = pd.to_datetime(data_8['symptom_date'])
data_8['symptom_date'] = data_8['symptom_date'].dt.to_period('M')

data_9 = data[['colorectal_symptom_9_date_symp_date', 'colorectal_conversion_9']]
data_9 = data_9.rename(columns={"colorectal_symptom_9_date_symp_date":"symptom_date", "colorectal_conversion_9":"conversion"})
data_9['symptom_date'] = pd.to_datetime(data_9['symptom_date'])
data_9['symptom_date'] = data_9['symptom_date'].dt.to_period('M')

data_10 = data[['colorectal_symptom_10_date_symp_date', 'colorectal_conversion_10']]
data_10 = data_10.rename(columns={"colorectal_symptom_10_date_symp_date":"symptom_date", "colorectal_conversion_10":"conversion"})
data_10['symptom_date'] = pd.to_datetime(data_10['symptom_date'])
data_10['symptom_date'] = data_10['symptom_date'].dt.to_period('M')

data_symptom_conversion = pd.concat([data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10])

unique_dates = data_symptom_conversion['symptom_date'].unique()

unique_dates = sorted(unique_dates)

dict = {}

for item in unique_dates:
    df = data_symptom_conversion.loc[data_symptom_conversion['symptom_date'] == item]
    con = df['conversion'].mean()
    dict.update({item: con})

plt.bar(range(len(dict)), list(dict.values()), tick_label=list(dict.keys()))

plt.savefig('output/colorectal_cancer_3.jpg')
