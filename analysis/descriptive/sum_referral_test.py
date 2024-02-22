import pandas as pd
import numpy as np

df = pd.read_csv("output/data/referral_test.csv")

num_patients = df.shape[0]

num_colorectal_surg_21d = df["colorectal_surg_clinic_21d"].value_counts().to_frame()
num_colorectal_surg_21d.columns = ["referral cohort"]

num_colorectal_surg_1m = df["colorectal_surg_clinic_1m"].value_counts().to_frame()
num_colorectal_surg_1m.columns = ["referral cohort"]

num_gastro_clinic_21d = df["gastro_clinic_21d"].value_counts().to_frame()
num_gastro_clinic_21d.columns = ["referral cohort"]

num_gastro_clinic_1m = df["gastro_clinic_1m"].value_counts().to_frame()
num_gastro_clinic_1m.columns = ["referral cohort"]

num_colonoscopy_21d = df["colonoscopy_21d"].value_counts().to_frame()
num_colonoscopy_21d.columns = ["referral cohort"]

num_colonoscopy_1m = df["colonoscopy_1m"].value_counts().to_frame()
num_colonoscopy_1m.columns = ["referral cohort"]

num_opa_1m_tfc = df["opa_1m_tfc"].value_counts().to_frame()
num_opa_1m_tfc.columns = ["referral cohort"]

agg_data_whole_cohort = pd.concat([num_colorectal_surg_21d, num_colorectal_surg_1m, num_gastro_clinic_21d, num_gastro_clinic_1m, num_colonoscopy_21d, num_colonoscopy_1m, num_opa_1m_tfc])

agg_data_whole_cohort.columns = agg_data_whole_cohort.columns.str.strip()

agg_data_whole_cohort.to_csv("output/data/summary_referral_test.csv")
