import pandas as pd
import numpy as np

df = pd.read_csv("output/data/referral_test.csv")

num_patients = df.shape[0]

num_colorectal_surg_3weeks = df["colorectal_surg_clinic_3weeks"].value_counts().to_frame()
num_colorectal_surg_3weeks.columns = ["referral cohort"]

num_gastro_clinic_3weeks = df["gastro_clinic_3weeks"].value_counts().to_frame()
num_gastro_clinic_3weeks.columns = ["referral cohort"]

agg_data_whole_cohort = pd.concat([num_colorectal_surg_3weeks, num_gastro_clinic_3weeks])

agg_data_whole_cohort.columns = agg_data_whole_cohort.columns.str.strip()

agg_data_whole_cohort.to_csv("output/data/summary_referral_test.csv")
