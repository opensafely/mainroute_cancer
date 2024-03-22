import pandas as pd
import numpy as np

df = pd.read_csv("output/data/referral_test.csv")

num_patients = df.shape[0]

#num_colorectal_surg_21d = df["colorectal_surg_clinic_21d"].value_counts().to_frame()
#num_colorectal_surg_21d.columns = ["referral cohort"]

num_colorectal_surg_6w = df["colorectal_surg_clinic_6w"].value_counts().to_frame()
num_colorectal_surg_6w.columns = ["referral cohort"]

#num_gastro_clinic_21d = df["gastro_clinic_21d"].value_counts().to_frame()
#num_gastro_clinic_21d.columns = ["referral cohort"]

num_gastro_clinic_6w = df["gastro_clinic_6w"].value_counts().to_frame()
num_gastro_clinic_6w.columns = ["referral cohort"]

#num_colonoscopy_21d = df["colonoscopy_21d"].value_counts().to_frame()
#num_colonoscopy_21d.columns = ["referral cohort"]

#num_colonoscopy_6w = df["colonoscopy_6w"].value_counts().to_frame()
#num_colonoscopy_6w.columns = ["referral cohort"]

num_apcs_diagnostic_6w = df["apcs_diagnostic_6w"].value_counts().to_frame()
num_apcs_diagnostic_6w.columns = ["referral cohort"]

num_opa_diagnostic_6w = df["opa_diagnostic_6w"].value_counts().to_frame()
num_opa_diagnostic_6w.columns = ["referral cohort"]

num_lowergi_diagnostic_6w = df["lowergi_diagnostic_6w"].value_counts().to_frame()
num_lowergi_diagnostic_6w.columns = ["referral cohort"]

num_lowergi_referral_6w = df["lowergi_referral_6w"].value_counts().to_frame()
num_lowergi_referral_6w.columns = ["referral cohort"]

#num_opa_6w_tfc = df["opa_6w_tfc"].value_counts().to_frame()
#num_opa_6w_tfc.columns = ["referral cohort"]

#num_proc_6w_opcs = df["proc_6w_opcs"].value_counts().to_frame()
#num_proc_6w_opcs.columns = ["referral cohort"]

#num_apcs_6w_icd10 = df["apcs_6w_icd10"].value_counts().to_frame()
#num_apcs_6w_icd10.columns = ["referral cohort"]

#num_apcs_6w_hrg = df["apcs_6w_hrg"].value_counts().to_frame()
#num_apcs_6w_hrg.columns = ["referral cohort"]

num_gp_events_6w = df["gp_events_snomed"].value_counts().to_frame()
num_gp_events_6w.columns = ["referral cohort"]

agg_data_whole_cohort = pd.concat([num_colorectal_surg_6w, num_gastro_clinic_6w, num_apcs_diagnostic_6w, num_opa_diagnostic_6w, num_lowergi_diagnostic_6w, num_lowergi_referral_6w, num_gp_events_6w])

agg_data_whole_cohort.columns = agg_data_whole_cohort.columns.str.strip()

agg_data_whole_cohort.to_csv("output/data/summary_referral_test.csv")
