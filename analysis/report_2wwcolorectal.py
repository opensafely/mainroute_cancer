import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("output/input_2wwcolorectal.csv")

data_null = data.notnull()

def condition1(s):
    if s['colorectal_referral_date'] & s['colorectal_diagnosis_date']:
        return 1
    else:
        return 0

data['colorectal_conversion_1'] = data_null.apply(condition1, axis=1)

data_referral_conversion = data[['colorectal_referral_date', 'colorectal_conversion_1']]
data_referral_conversion = data_referral_conversion.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_conversion_1":"conversion"})
data_referral_conversion['referral_date'] = pd.to_datetime(data_referral_conversion['referral_date'])
data_referral_conversion['referral_date'] = data_referral_conversion['referral_date'].dt.to_period('M')

unique_dates = data_referral_conversion['referral_date'].unique()

unique_dates = sorted(unique_dates)

dict = {}

for item in unique_dates:
    df = data_referral_conversion.loc[data_referral_conversion['referral_date'] == item]
    con = df['conversion'].mean()
    dict.update({item: con})

plt.bar(range(len(dict)), list(dict.values()), tick_label=list(dict.keys()))

plt.savefig('output/colorectal_cancer_10.jpg')

plt.clf()

data_null = data.notnull()

def condition2(s):
    if s['colorectal_referral_date'] & s['fit_date']:
        return 1
    else:
        return 0

data['colorectal_fit_rate'] = data_null.apply(condition2, axis=1)

data_fit_rate = data[['colorectal_referral_date', 'colorectal_fit_rate']]
data_fit_rate = data_fit_rate.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_fit_rate":"fit_rate"})
data_fit_rate['referral_date'] = pd.to_datetime(data_fit_rate['referral_date'])
data_fit_rate['referral_date'] = data_fit_rate['referral_date'].dt.to_period('M')

unique_dates = data_fit_rate['referral_date'].unique()

unique_dates = sorted(unique_dates)

dict = {}

for item in unique_dates:
    df = data_fit_rate.loc[data_fit_rate['referral_date'] == item]
    con = df['fit_rate'].mean()
    dict.update({item: con})

plt.bar(range(len(dict)), list(dict.values()), tick_label=list(dict.keys()))

plt.savefig('output/colorectal_cancer_11.jpg')

plt.clf()

data_null = data.notnull()

def condition3(s):
    if s['colorectal_referral_date'] & s['anaemia_symptom_date']:
        return 1
    else:
        return 0

data['colorectal_anaemia_rate'] = data_null.apply(condition3, axis=1)

data_anaemia_rate = data[['colorectal_referral_date', 'colorectal_anaemia_rate']]
data_anaemia_rate = data_anaemia_rate.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_anaemia_rate":"anaemia_rate"})
data_anaemia_rate['referral_date'] = pd.to_datetime(data_anaemia_rate['referral_date'])
data_anaemia_rate['referral_date'] = data_anaemia_rate['referral_date'].dt.to_period('M')

unique_dates = data_anaemia_rate['referral_date'].unique()

unique_dates = sorted(unique_dates)

dict = {}

for item in unique_dates:
    df = data_anaemia_rate.loc[data_anaemia_rate['referral_date'] == item]
    con = df['anaemia_rate'].mean()
    dict.update({item: con})

plt.bar(range(len(dict)), list(dict.values()), tick_label=list(dict.keys()))

plt.savefig('output/colorectal_cancer_12.jpg')

plt.clf()

data_null = data.notnull()

def condition4(s):
    if s['colorectal_referral_date'] & s['cibh_symptom_date']:
        return 1
    else:
        return 0

data['colorectal_cibh_rate'] = data_null.apply(condition4, axis=1)

data_cibh_rate = data[['colorectal_referral_date', 'colorectal_cibh_rate']]
data_cibh_rate = data_cibh_rate.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_cibh_rate":"cibh_rate"})
data_cibh_rate['referral_date'] = pd.to_datetime(data_cibh_rate['referral_date'])
data_cibh_rate['referral_date'] = data_cibh_rate['referral_date'].dt.to_period('M')

unique_dates = data_cibh_rate['referral_date'].unique()

unique_dates = sorted(unique_dates)

dict = {}

for item in unique_dates:
    df = data_cibh_rate.loc[data_cibh_rate['referral_date'] == item]
    con = df['cibh_rate'].mean()
    dict.update({item: con})

plt.bar(range(len(dict)), list(dict.values()), tick_label=list(dict.keys()))

plt.savefig('output/colorectal_cancer_13.jpg')

plt.clf()

data_null = data.notnull()

def condition5(s):
    if s['colorectal_referral_date'] & s['prbleeding_symptom_date']:
        return 1
    else:
        return 0

data['colorectal_prbleeding_rate'] = data_null.apply(condition5, axis=1)

data_prbleeding_rate = data[['colorectal_referral_date', 'colorectal_prbleeding_rate']]
data_prbleeding_rate = data_prbleeding_rate.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_prbleeding_rate":"prbleeding_rate"})
data_prbleeding_rate['referral_date'] = pd.to_datetime(data_prbleeding_rate['referral_date'])
data_prbleeding_rate['referral_date'] = data_prbleeding_rate['referral_date'].dt.to_period('M')

unique_dates = data_prbleeding_rate['referral_date'].unique()

unique_dates = sorted(unique_dates)

dict = {}

for item in unique_dates:
    df = data_prbleeding_rate.loc[data_prbleeding_rate['referral_date'] == item]
    con = df['prbleeding_rate'].mean()
    dict.update({item: con})

plt.bar(range(len(dict)), list(dict.values()), tick_label=list(dict.keys()))

plt.savefig('output/colorectal_cancer_14.jpg')

plt.clf()

data_null = data.notnull()

def condition6(s):
    if s['colorectal_referral_date'] & s['wl_symptom_date']:
        return 1
    else:
        return 0

data['colorectal_wl_rate'] = data_null.apply(condition6, axis=1)

data_wl_rate = data[['colorectal_referral_date', 'colorectal_wl_rate']]
data_wl_rate = data_wl_rate.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_wl_rate":"wl_rate"})
data_wl_rate['referral_date'] = pd.to_datetime(data_wl_rate['referral_date'])
data_wl_rate['referral_date'] = data_wl_rate['referral_date'].dt.to_period('M')

unique_dates = data_wl_rate['referral_date'].unique()

unique_dates = sorted(unique_dates)

dict = {}

for item in unique_dates:
    df = data_wl_rate.loc[data_wl_rate['referral_date'] == item]
    con = df['wl_rate'].mean()
    dict.update({item: con})

plt.bar(range(len(dict)), list(dict.values()), tick_label=list(dict.keys()))

plt.savefig('output/colorectal_cancer_15.jpg')