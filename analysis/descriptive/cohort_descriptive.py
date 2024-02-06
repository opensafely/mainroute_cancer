import pandas as pd
import numpy as np

df = pd.read_csv("output/data/dataset_static.csv.gz")

num_patients = df.shape[0]
#num_patients.to_frame.to_csv("output/num_patients.csv")
num_age_group = df["age_group"].value_counts().to_frame()
num_age_group.columns = ["whole cohort"]
num_sex = df["sex"].value_counts().to_frame()
num_sex.columns = ["whole cohort"]
num_imd5 = df["imd5"].value_counts().to_frame()
num_imd5.columns = ["whole cohort"]
num_ethnicity6 = df["ethnicity6"].value_counts().to_frame()
num_ethnicity6.columns = ["whole cohort"]
num_region = df["region"].value_counts().to_frame()
num_region.columns = ["whole cohort"]
num_colorectalca = df["colorectal_ca_diag"].value_counts().to_frame()
num_colorectalca.columns = ["whole cohort"]

#a = df.loc[df['lowerGI_any_symp'] == True]
#num_age_group_lowerGI = a["age_group"].value_counts().to_frame()
#num_age_group_lowerGI.columns = ["lowerGI symptom"]
#num_sex_lowerGI = a["sex"].value_counts().to_frame()
#num_sex_lowerGI.columns = ["lowerGI symptom"]
#num_imd5_lowerGI = a["imd5"].value_counts().to_frame()
#num_imd5_lowerGI.columns = ["lowerGI symptom"]
#num_ethnicity6_lowerGI = a["ethnicity6"].value_counts().to_frame()
#num_ethnicity6_lowerGI.columns = ["lowerGI symptom"]

agg_data_whole_cohort = pd.concat([num_age_group, num_sex, num_imd5, num_ethnicity6, num_region, num_colorectalca])
#agg_data_lowerGI = pd.concat([num_age_group_lowerGI, num_sex_lowerGI, num_imd5_lowerGI, num_ethnicity6_lowerGI])
#agg_data = pd.concat([agg_data_whole_cohort, agg_data_lowerGI], axis=1)

agg_data_whole_cohort.columns = agg_data_whole_cohort.columns.str.strip()

s = (agg_data_whole_cohort['whole cohort'] % 5)
agg_data_whole_cohort['whole cohort_round'] = agg_data_whole_cohort['whole cohort']  + np.where(s>=3,5-s,-s)

agg_data_whole_cohort.to_csv("output/data/demographic_data.csv")