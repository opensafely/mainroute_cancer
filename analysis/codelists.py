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