from cohortextractor import codelist, codelist_from_csv, combine_codelists

cancer_codes = codelist_from_csv(
    "codelists/opensafely-cancer-excluding-lung-and-haematological.csv", system="ctv3", column="CTV3ID"
)

#snomed_cancer_codes = codelist_from_csv(
    #"codelists/opensafely-cancer-excluding-lung-and-haematological-snomed.csv", system="snomed", column="id"
#)