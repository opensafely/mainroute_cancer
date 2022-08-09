import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("output/input_basereferral.csv")

data_referral = data[["colorectal_symptom_1_date_ref_date", "colorectal_symptom_2_date_ref_date", "colorectal_symptom_3_date_ref_date", "colorectal_symptom_4_date_ref_date", "colorectal_symptom_5_date_ref_date", "colorectal_symptom_6_date_ref_date"]]
data_diagnosis = data[["colorectal_symptom_1_date_diag_date", "colorectal_symptom_2_date_diag_date", "colorectal_symptom_3_date_diag_date", "colorectal_symptom_4_date_diag_date", "colorectal_symptom_5_date_diag_date", "colorectal_symptom_6_date_diag_date"]]

num_referral = data_referral.count(axis=1)

plt.hist(num_referral.values.tolist(), bins=6)

plt.savefig('output/colorectal_cancer_7.jpg')

plt.clf()

data_referral['colorectal_symptom_1_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_1_date_ref_date'])
data_referral['colorectal_symptom_2_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_2_date_ref_date'])
data_referral['colorectal_symptom_3_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_3_date_ref_date'])
data_referral['colorectal_symptom_4_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_4_date_ref_date'])
data_referral['colorectal_symptom_5_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_5_date_ref_date'])
data_referral['colorectal_symptom_6_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_6_date_ref_date'])
data_month_year_1 = data_referral['colorectal_symptom_1_date_ref_date'].dt.to_period('M')
data_month_year_2 = data_referral['colorectal_symptom_2_date_ref_date'].dt.to_period('M')
data_month_year_3 = data_referral['colorectal_symptom_3_date_ref_date'].dt.to_period('M')
data_month_year_4 = data_referral['colorectal_symptom_4_date_ref_date'].dt.to_period('M')
data_month_year_5 = data_referral['colorectal_symptom_5_date_ref_date'].dt.to_period('M')
data_month_year_6 = data_referral['colorectal_symptom_6_date_ref_date'].dt.to_period('M')

data_month_year = pd.concat([data_month_year_1, data_month_year_2, data_month_year_3, data_month_year_4, data_month_year_5, data_month_year_6], axis=1)

counts = data_month_year.stack().value_counts()

counts = counts.sort_index()

ax = counts.plot.bar()

plt.savefig('output/colorectal_cancer_8.jpg')

plt.clf()

data_null = data.notnull()

def condition1(s):
    if s['colorectal_symptom_1_date_ref_date'] & s['colorectal_symptom_1_date_diag_date']:
        return 1
    else:
        return 0

def condition2(s):
    if s['colorectal_symptom_2_date_ref_date'] & s['colorectal_symptom_2_date_diag_date']:
        return 1
    else:
        return 0

def condition3(s):
    if s['colorectal_symptom_3_date_ref_date'] & s['colorectal_symptom_3_date_diag_date']:
        return 1
    else:
        return 0

def condition4(s):
    if s['colorectal_symptom_4_date_ref_date'] & s['colorectal_symptom_4_date_diag_date']:
        return 1
    else:
        return 0

def condition5(s):
    if s['colorectal_symptom_5_date_ref_date'] & s['colorectal_symptom_5_date_diag_date']:
        return 1
    else:
        return 0

def condition6(s):
    if s['colorectal_symptom_6_date_ref_date'] & s['colorectal_symptom_6_date_diag_date']:
        return 1
    else:
        return 0

data['colorectal_conversion_1'] = data_null.apply(condition1, axis=1)
data['colorectal_conversion_2'] = data_null.apply(condition2, axis=1)
data['colorectal_conversion_3'] = data_null.apply(condition3, axis=1)
data['colorectal_conversion_4'] = data_null.apply(condition4, axis=1)
data['colorectal_conversion_5'] = data_null.apply(condition5, axis=1)
data['colorectal_conversion_6'] = data_null.apply(condition6, axis=1)

data_1 = data[['colorectal_symptom_1_date_ref_date', 'colorectal_conversion_1']]
data_1 = data_1.rename(columns={"colorectal_symptom_1_date_ref_date":"referral_date", "colorectal_conversion_1":"conversion"})
data_1['referral_date'] = pd.to_datetime(data_1['referral_date'])
data_1['referral_date'] = data_1['referral_date'].dt.to_period('M')

data_2 = data[['colorectal_symptom_2_date_ref_date', 'colorectal_conversion_2']]
data_2 = data_2.rename(columns={"colorectal_symptom_2_date_ref_date":"referral_date", "colorectal_conversion_2":"conversion"})
data_2['referral_date'] = pd.to_datetime(data_2['referral_date'])
data_2['referral_date'] = data_2['referral_date'].dt.to_period('M')

data_3 = data[['colorectal_symptom_3_date_ref_date', 'colorectal_conversion_3']]
data_3 = data_3.rename(columns={"colorectal_symptom_3_date_ref_date":"referral_date", "colorectal_conversion_3":"conversion"})
data_3['referral_date'] = pd.to_datetime(data_3['referral_date'])
data_3['referral_date'] = data_3['referral_date'].dt.to_period('M')

data_4 = data[['colorectal_symptom_4_date_ref_date', 'colorectal_conversion_4']]
data_4 = data_4.rename(columns={"colorectal_symptom_4_date_ref_date":"referral_date", "colorectal_conversion_4":"conversion"})
data_4['referral_date'] = pd.to_datetime(data_4['referral_date'])
data_4['referral_date'] = data_4['referral_date'].dt.to_period('M')

data_5 = data[['colorectal_symptom_5_date_ref_date', 'colorectal_conversion_5']]
data_5 = data_5.rename(columns={"colorectal_symptom_5_date_ref_date":"referral_date", "colorectal_conversion_5":"conversion"})
data_5['referral_date'] = pd.to_datetime(data_5['referral_date'])
data_5['referral_date'] = data_5['referral_date'].dt.to_period('M')

data_6 = data[['colorectal_symptom_6_date_ref_date', 'colorectal_conversion_6']]
data_6 = data_6.rename(columns={"colorectal_symptom_6_date_ref_date":"referral_date", "colorectal_conversion_6":"conversion"})
data_6['referral_date'] = pd.to_datetime(data_6['referral_date'])
data_6['referral_date'] = data_6['referral_date'].dt.to_period('M')

data_referral_conversion = pd.concat([data_1, data_2, data_3, data_4, data_5, data_6])

unique_dates = data_referral_conversion['referral_date'].unique()

unique_dates = sorted(unique_dates)

dict = {}

for item in unique_dates:
    df = data_referral_conversion.loc[data_referral_conversion['referral_date'] == item]
    con = df['conversion'].mean()
    dict.update({item: con})

plt.bar(range(len(dict)), list(dict.values()), tick_label=list(dict.keys()))

plt.savefig('output/colorectal_cancer_9.jpg')