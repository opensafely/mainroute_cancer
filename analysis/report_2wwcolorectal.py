import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("output/input_2wwcolorectal.csv")

def ageband(x):
    if (x < 40):
        return 1
    elif ((x >= 40) & (x < 60)):
        return 2
    elif ((x >= 60) & (x < 80)):
        return 3
    elif (x >= 80):
        return 4

data['ageband'] = data['age'].apply(ageband)

########## diagnosis conversion plot ##########
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

########## FIT test plot ##########
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

########## anaemia symptom plot ##########
data_null = data.notnull()

def condition3(s):
    if s['colorectal_referral_date'] & s['anaemia_symptom_date'] & s['age']>=60:
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

########## CIBH symptom plot ##########
data_null = data.notnull()

def condition4(s):
    if s['colorectal_referral_date'] & s['cibh_symptom_date'] & s['age']>=60:
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

########## PR bleeding symptom plot ##########
data_null = data.notnull()

def condition5(s):
    if s['colorectal_referral_date'] & s['prbleeding_symptom_date'] & s['age']>=50:
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

########## weight loss symptom plot ##########
data_null = data.notnull()

def condition6(s):
    if s['colorectal_referral_date'] & s['wl_symptom_date'] & s['age']>=40:
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

plt.clf()

########## time to diagnosis plot ##########
data_null = data.notnull()

data['colorectal_diagnosis_date'] = pd.to_datetime(data['colorectal_diagnosis_date'])
data['colorectal_referral_date'] = pd.to_datetime(data['colorectal_referral_date'])

data['timetodiag'] = data['colorectal_diagnosis_date'] - data['colorectal_referral_date']

data['timetodiag'] = data['timetodiag'].dt.days

def year(x):
    if (x >= pd.to_datetime('2019-03-23')) & (x < pd.to_datetime('2020-03-23')):
        return 1
    elif (x >= pd.to_datetime('2020-03-23')) & (x < pd.to_datetime('2021-03-23')):
        return 2
    elif (x >= pd.to_datetime('2021-03-23')) & (x < pd.to_datetime('2022-03-23')):
        return 3

data['timecovid'] = data['colorectal_referral_date'].apply(year)

data_precovid = data[data['timecovid'] == 1]
data_yr1covid = data[data['timecovid'] == 2]
data_yr2covid = data[data['timecovid'] == 3]

times_precovid = data_precovid['timetodiag'].to_numpy()
times_yr1covid = data_yr1covid['timetodiag'].to_numpy()
times_yr2covid = data_yr2covid['timetodiag'].to_numpy()

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.hist(times_precovid)
ax2.hist(times_yr1covid)
ax3.hist(times_yr2covid)

ax.set_xlabel('Days between Colorectal Referral and Diagnosis')
ax.set_ylabel('Frequency')

ax1.set_title('Pre COVID')
ax2.set_title('Year 1 COVID')
ax3.set_title('Year 2 COVID')

plt.savefig('output/colorectal_cancer_16.jpg')

plt.clf()

########## diagnosis conversion <40 plot ##########
data_null = data.notnull()

def condition7(s):
    if s['colorectal_referral_date'] & s['colorectal_diagnosis_date'] & s['ageband']==1:
        return 1
    else:
        return 0

data['colorectal_conversion_1'] = data_null.apply(condition7, axis=1)

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

plt.savefig('output/colorectal_cancer_17.jpg')

plt.clf()

########## diagnosis conversion 40-60 plot ##########
data_null = data.notnull()

def condition8(s):
    if s['colorectal_referral_date'] & s['colorectal_diagnosis_date'] & s['ageband']==2:
        return 1
    else:
        return 0

data['colorectal_conversion_1'] = data_null.apply(condition8, axis=1)

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

plt.savefig('output/colorectal_cancer_18.jpg')

plt.clf()

########## diagnosis conversion 60-80 plot ##########
data_null = data.notnull()

def condition9(s):
    if s['colorectal_referral_date'] & s['colorectal_diagnosis_date'] & s['ageband']==3:
        return 1
    else:
        return 0

data['colorectal_conversion_1'] = data_null.apply(condition9, axis=1)

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

plt.savefig('output/colorectal_cancer_19.jpg')

plt.clf()

########## diagnosis conversion 80+ plot ##########
data_null = data.notnull()

def condition10(s):
    if s['colorectal_referral_date'] & s['colorectal_diagnosis_date'] & s['ageband']==4:
        return 1
    else:
        return 0

data['colorectal_conversion_1'] = data_null.apply(condition10, axis=1)

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

plt.savefig('output/colorectal_cancer_20.jpg')

plt.clf()