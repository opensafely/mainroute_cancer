from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
from codelists import *

start_date = "2018-04-30"
end_date = "2022-02-13"

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    population=patients.with_these_clinical_events(
        cancer_codes, 
        between=[start_date, end_date]
    ),

    cancer_date=patients.with_these_clinical_events(
        cancer_codes,
        between=[start_date, end_date],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"rate": "uniform", "incidence": 1.0, "date": {"earliest": start_date, "latest": end_date}},
    ),

    age=patients.age_as_of(
        "cancer_date", 
        return_expectations={"rate" : "universal", "int" : {"distribution" : "population_ages"}},
    ),
)