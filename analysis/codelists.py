from cohortextractor import codelist, codelist_from_csv

colorectal_referral_codes = codelist_from_csv(
    "codelists/phc-2ww-referral-colorectal.csv", system="snomed", column="code"
)

colorectal_symptom_codes = codelist_from_csv(
    "codelists/phc-symptoms-colorectal-cancer.csv", system="snomed", column="code"
)

colorectal_diagnosis_codes = codelist_from_csv(
    "codelists/phc-colorectal-cancer-icd10.csv", system="icd10", column="code"
)

colorectal_diagnosis_codes_snomed = codelist_from_csv(
    "codelists/phc-phc-colorectal-cancer-snomed.csv", system="snomed", column="code"
)

colorectal_diagnosis_codes_read = codelist_from_csv(
    "codelists/phc-phc-colorectal-cancer-ctv3.csv", system="ctv3", column="code"
)

anaemia_codes = codelist_from_csv(
    "codelists/phc-symptom-colorectal-anaemia.csv", system="snomed", column="code"
)

cibh_codes = codelist_from_csv(
    "codelists/phc-symptom-colorectal-cibh.csv", system="snomed", column="code"
)

prbleeding_codes = codelist_from_csv(
    "codelists/phc-symptom-colorectal-pr-bleeding.csv", system="snomed", column="code"
)

wl_codes = codelist_from_csv(
    "codelists/phc-symptom-colorectal-wl.csv", system="snomed", column="code"
)

fit_codes = codelist_from_csv(
    "codelists/phc-fit-test.csv", system="snomed", column="code"
)