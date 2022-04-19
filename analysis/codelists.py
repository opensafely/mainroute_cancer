from cohortextractor import codelist, codelist_from_csv

colorectal_referral_codes = codelist_from_csv(
    "codelists/phc-2ww-referral-colorectal.csv", system="snomed", column="code"
)

colorectal_symptom_codes = codelist_from_csv(
    "codelists/phc-symptoms-colorectal-cancer.csv", system="snomed", column="code"
)