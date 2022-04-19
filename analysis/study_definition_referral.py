from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
from codelists import *

start_date = "2018-03-23"
end_date = "2022-03-23"

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    population=patients.with_these_clinical_events(
        colorectal_referral_codes, 
        between=[start_date, end_date],
    ),

    colorectal_referral_date=patients.with_these_clinical_events(
        colorectal_referral_codes,
        between=[start_date, end_date],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"rate": "uniform", "incidence": 1.0, "date": {"earliest": start_date, "latest": end_date}},
    ),
)