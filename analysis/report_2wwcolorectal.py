import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("output/input_2wwcolorectal.csv")

########## diagnosis conversion plot ##########
#data_null = data.notnull()

"""def condition1(s):
    if ~s['colorectal_referral_date'].isna() & ~s['colorectal_diagnosis_date'].isna():
        return 1
    else:
        return 0

data['colorectal_conversion_1'] = data.apply(condition1, axis=1)"""

data_referral_conversion = data[['colorectal_referral_date', 'colorectal_diagnosis_flag']]
data_referral_conversion = data_referral_conversion.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_diagnosis_flag":"conversion"})
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
#data_null = data.notnull()

"""def condition2(s):
    if ~s['colorectal_referral_date'].isna() & ~s['fit_date'].isna():
        return 1
    else:
        return 0

data['colorectal_fit_rate'] = data.apply(condition2, axis=1)"""

data_fit_rate = data[['colorectal_referral_date', 'fit_flag']]
data_fit_rate = data_fit_rate.rename(columns={"colorectal_referral_date":"referral_date", "fit_flag":"fit_rate"})
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
#data_null = data.notnull()

#data.loc[data["age"]<60, "anaemia_symptom_date"] = ""

def condition3(s):
    if (s['anaemia_symptom_flag']==1) & (s['age']>=60):
        return 1
    else:
        return 0

data['anaemia_symptom_flag2'] = data.apply(condition3, axis=1)

data_anaemia_rate = data[['colorectal_referral_date', 'anaemia_symptom_flag2']]
data_anaemia_rate = data_anaemia_rate.rename(columns={"colorectal_referral_date":"referral_date", "anaemia_symptom_flag2":"anaemia_rate"})
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
#data_null = data.notnull()

#data.loc[data["age"]<60, "cibh_symptom_date"] = ""

def condition4(s):
    if (s['cibh_symptom_flag']==1) & (s['age']>=60):
        return 1
    else:
        return 0

data['cibh_symptom_flag2'] = data.apply(condition4, axis=1)

data_cibh_rate = data[['colorectal_referral_date', 'cibh_symptom_flag2']]
data_cibh_rate = data_cibh_rate.rename(columns={"colorectal_referral_date":"referral_date", "cibh_symptom_flag2":"cibh_rate"})
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
#data_null = data.notnull()

#data.loc[data["age"]<50, "prbleeding_symptom_date"] = ""

def condition5(s):
    if (s['prbleeding_symptom_flag']==1) & (s['age']>=50):
        return 1
    else:
        return 0

data['prbleeding_symptom_flag2'] = data.apply(condition5, axis=1)

data_prbleeding_rate = data[['colorectal_referral_date', 'prbleeding_symptom_flag2']]
data_prbleeding_rate = data_prbleeding_rate.rename(columns={"colorectal_referral_date":"referral_date", "prbleeding_symptom_flag2":"prbleeding_rate"})
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
#data_null = data.notnull()

#data.loc[data["age"]<40, "wl_symptom_date"] = ""

def condition6(s):
    if (s['wl_symptom_flag']==1) & (s['age']>=40):
        return 1
    else:
        return 0

data['wl_symptom_flag2'] = data.apply(condition6, axis=1)

data_wl_rate = data[['colorectal_referral_date', 'wl_symptom_flag2']]
data_wl_rate = data_wl_rate.rename(columns={"colorectal_referral_date":"referral_date", "wl_symptom_flag2":"wl_rate"})
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
#data_null = data.notnull()

data_time_to_diagnosis = data[data['colorectal_diagnosis_flag']==1]

data_time_to_diagnosis['colorectal_diagnosis_date'] = pd.to_datetime(data_time_to_diagnosis['colorectal_diagnosis_date'])
data_time_to_diagnosis['colorectal_referral_date'] = pd.to_datetime(data_time_to_diagnosis['colorectal_referral_date'])

data_time_to_diagnosis['timetodiag'] = data_time_to_diagnosis['colorectal_diagnosis_date'] - data_time_to_diagnosis['colorectal_referral_date']

data_time_to_diagnosis['timetodiag'] = data_time_to_diagnosis['timetodiag'].dt.days

def year(x):
    if (x >= pd.to_datetime('2019-03-23')) & (x < pd.to_datetime('2020-03-23')):
        return 1
    elif (x >= pd.to_datetime('2020-03-23')) & (x < pd.to_datetime('2021-03-23')):
        return 2
    elif (x >= pd.to_datetime('2021-03-23')) & (x < pd.to_datetime('2022-03-23')):
        return 3

data_time_to_diagnosis['timecovid'] = data_time_to_diagnosis['colorectal_referral_date'].apply(year)

data_precovid = data_time_to_diagnosis[data_time_to_diagnosis['timecovid'] == 1]
data_yr1covid = data_time_to_diagnosis[data_time_to_diagnosis['timecovid'] == 2]
data_yr2covid = data_time_to_diagnosis[data_time_to_diagnosis['timecovid'] == 3]

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
#data_null = data.notnull()

data_40 = data[data['age']<40]

#data_40['colorectal_conversion_2'] = data_40.apply(condition1, axis=1)

data_referral_conversion = data_40[['colorectal_referral_date', 'colorectal_diagnosis_flag']]
data_referral_conversion = data_referral_conversion.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_diagnosis_flag":"conversion"})
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
#data_null = data.notnull()

data_60 = data[(data['age']>=40) & (data['age']<60)]

#data_60['colorectal_conversion_3'] = data_60.apply(condition1, axis=1)

data_referral_conversion = data_60[['colorectal_referral_date', 'colorectal_diagnosis_flag']]
data_referral_conversion = data_referral_conversion.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_diagnosis_flag":"conversion"})
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
#data_null = data.notnull()

data_80 = data[(data['age']>=60) & (data['age']<80)]

#data_80['colorectal_conversion_4'] = data_80.apply(condition1, axis=1)

data_referral_conversion = data_80[['colorectal_referral_date', 'colorectal_diagnosis_flag']]
data_referral_conversion = data_referral_conversion.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_diagnosis_flag":"conversion"})
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
#data_null = data.notnull()

data_80plus = data[data['age']>=80]

#data_80plus['colorectal_conversion_5'] = data_80plus.apply(condition1, axis=1)

data_referral_conversion = data_80plus[['colorectal_referral_date', 'colorectal_diagnosis_flag']]
data_referral_conversion = data_referral_conversion.rename(columns={"colorectal_referral_date":"referral_date", "colorectal_diagnosis_flag":"conversion"})
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