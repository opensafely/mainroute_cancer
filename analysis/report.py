import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("output/input_paired.csv")

data_symptom = data[["colorectal_symptom_1_date_symp_date", "colorectal_symptom_2_date_symp_date", "colorectal_symptom_3_date_symp_date", "colorectal_symptom_4_date_symp_date", "colorectal_symptom_5_date_symp_date", "colorectal_symptom_6_date_symp_date"]]
data_referral = data[["colorectal_symptom_1_date_ref_date", "colorectal_symptom_2_date_ref_date", "colorectal_symptom_3_date_ref_date", "colorectal_symptom_4_date_ref_date", "colorectal_symptom_5_date_ref_date", "colorectal_symptom_6_date_ref_date"]]
data_diagnosis = data[["colorectal_symptom_1_date_diag_date", "colorectal_symptom_2_date_diag_date", "colorectal_symptom_3_date_diag_date", "colorectal_symptom_4_date_diag_date", "colorectal_symptom_5_date_diag_date", "colorectal_symptom_6_date_diag_date"]]

num_symptoms = data_symptom.count(axis=1)

plt.hist(num_symptoms.values.tolist(), bins=6)

plt.savefig('output/colorectal_cancer.jpg')

plt.clf()

data_symptom['colorectal_symptom_1_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_1_date_symp_date'])
data_symptom['colorectal_symptom_2_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_2_date_symp_date'])
data_symptom['colorectal_symptom_3_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_3_date_symp_date'])
data_symptom['colorectal_symptom_4_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_4_date_symp_date'])
data_symptom['colorectal_symptom_5_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_5_date_symp_date'])
data_symptom['colorectal_symptom_6_date_symp_date'] = pd.to_datetime(data_symptom['colorectal_symptom_6_date_symp_date'])
data_month_year_1 = data_symptom['colorectal_symptom_1_date_symp_date'].dt.to_period('M')
data_month_year_2 = data_symptom['colorectal_symptom_2_date_symp_date'].dt.to_period('M')
data_month_year_3 = data_symptom['colorectal_symptom_3_date_symp_date'].dt.to_period('M')
data_month_year_4 = data_symptom['colorectal_symptom_4_date_symp_date'].dt.to_period('M')
data_month_year_5 = data_symptom['colorectal_symptom_5_date_symp_date'].dt.to_period('M')
data_month_year_6 = data_symptom['colorectal_symptom_6_date_symp_date'].dt.to_period('M')

data_month_year = pd.concat([data_month_year_1, data_month_year_2, data_month_year_3, data_month_year_4, data_month_year_5, data_month_year_6], axis=1)

counts = data_month_year.stack().value_counts()

counts = counts.sort_index()

ax = counts.plot.bar()

plt.savefig('output/colorectal_cancer_2.jpg')

plt.clf()

data_referral['colorectal_symptom_1_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_1_date_ref_date'])
data_referral['colorectal_symptom_2_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_2_date_ref_date'])
data_referral['colorectal_symptom_3_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_3_date_ref_date'])
data_referral['colorectal_symptom_4_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_4_date_ref_date'])
data_referral['colorectal_symptom_5_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_5_date_ref_date'])
data_referral['colorectal_symptom_6_date_ref_date'] = pd.to_datetime(data_referral['colorectal_symptom_6_date_ref_date'])
data_ref_month_year_1 = data_referral['colorectal_symptom_1_date_ref_date'].dt.to_period('M')
data_ref_month_year_2 = data_referral['colorectal_symptom_2_date_ref_date'].dt.to_period('M')
data_ref_month_year_3 = data_referral['colorectal_symptom_3_date_ref_date'].dt.to_period('M')
data_ref_month_year_4 = data_referral['colorectal_symptom_4_date_ref_date'].dt.to_period('M')
data_ref_month_year_5 = data_referral['colorectal_symptom_5_date_ref_date'].dt.to_period('M')
data_ref_month_year_6 = data_referral['colorectal_symptom_6_date_ref_date'].dt.to_period('M')

data_ref_month_year = pd.concat([data_ref_month_year_1, data_ref_month_year_2, data_ref_month_year_3, data_ref_month_year_4, data_ref_month_year_5, data_ref_month_year_6], axis=1)

counts_ref = data_ref_month_year.stack().value_counts()

counts_ref = counts_ref.sort_index()

ax = counts_ref.plot.bar()

plt.savefig('output/colorectal_cancer_3.jpg')

plt.clf()

data_diagnosis['colorectal_symptom_1_date_diag_date'] = pd.to_datetime(data_diagnosis['colorectal_symptom_1_date_diag_date'])
data_diagnosis['colorectal_symptom_2_date_diag_date'] = pd.to_datetime(data_diagnosis['colorectal_symptom_2_date_diag_date'])
data_diagnosis['colorectal_symptom_3_date_diag_date'] = pd.to_datetime(data_diagnosis['colorectal_symptom_3_date_diag_date'])
data_diagnosis['colorectal_symptom_4_date_diag_date'] = pd.to_datetime(data_diagnosis['colorectal_symptom_4_date_diag_date'])
data_diagnosis['colorectal_symptom_5_date_diag_date'] = pd.to_datetime(data_diagnosis['colorectal_symptom_5_date_diag_date'])
data_diagnosis['colorectal_symptom_6_date_diag_date'] = pd.to_datetime(data_diagnosis['colorectal_symptom_6_date_diag_date'])
data_diag_month_year_1 = data_diagnosis['colorectal_symptom_1_date_diag_date'].dt.to_period('M')
data_diag_month_year_2 = data_diagnosis['colorectal_symptom_2_date_diag_date'].dt.to_period('M')
data_diag_month_year_3 = data_diagnosis['colorectal_symptom_3_date_diag_date'].dt.to_period('M')
data_diag_month_year_4 = data_diagnosis['colorectal_symptom_4_date_diag_date'].dt.to_period('M')
data_diag_month_year_5 = data_diagnosis['colorectal_symptom_5_date_diag_date'].dt.to_period('M')
data_diag_month_year_6 = data_diagnosis['colorectal_symptom_6_date_diag_date'].dt.to_period('M')

data_diag_month_year = pd.concat([data_diag_month_year_1, data_diag_month_year_2, data_diag_month_year_3, data_diag_month_year_4, data_diag_month_year_5, data_diag_month_year_6], axis=1)

counts_diag = data_diag_month_year.stack().value_counts()

counts_diag = counts_diag.sort_index()

ax = counts_diag.plot.bar()

plt.savefig('output/colorectal_cancer_4.jpg')
