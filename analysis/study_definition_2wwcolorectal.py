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
        
    colorectal_diagnosis_date=patients.with_these_clinical_events(
        colorectal_diagnosis_codes_snomed,
        between=["colorectal_referral_date", "colorectal_referral_date + 122 days"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
    ),

    colorectal_diagnosis_flag=patients.with_these_clinical_events(
        colorectal_diagnosis_codes_snomed,
        between=["colorectal_referral_date", "colorectal_referral_date + 122 days"],
        returning='binary_flag',
        return_binary_flag=None,
    ),

    anaemia_symptom_date=patients.with_these_clinical_events(
        anaemia_codes,
        between=["colorectal_referral_date - 30 days", "colorectal_referral_date"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
    ),

    anaemia_symptom_flag=patients.with_these_clinical_events(
        anaemia_codes,
        between=["colorectal_referral_date - 30 days", "colorectal_referral_date"],
        returning='binary_flag',
        return_binary_flag=None,
    ),

    cibh_symptom_date=patients.with_these_clinical_events(
        cibh_codes,
        between=["colorectal_referral_date - 30 days", "colorectal_referral_date"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
    ),

    cibh_symptom_flag=patients.with_these_clinical_events(
        cibh_codes,
        between=["colorectal_referral_date - 30 days", "colorectal_referral_date"],
        returning='binary_flag',
        return_binary_flag=None,
    ),

    prbleeding_symptom_date=patients.with_these_clinical_events(
        prbleeding_codes,
        between=["colorectal_referral_date - 30 days", "colorectal_referral_date"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
    ),

    prbleeding_symptom_flag=patients.with_these_clinical_events(
        prbleeding_codes,
        between=["colorectal_referral_date - 30 days", "colorectal_referral_date"],
        returning='binary_flag',
        return_binary_flag=None,
    ),

    wl_symptom_date=patients.with_these_clinical_events(
        wl_codes,
        between=["colorectal_referral_date - 30 days", "colorectal_referral_date"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
    ),

    wl_symptom_flag=patients.with_these_clinical_events(
        wl_codes,
        between=["colorectal_referral_date - 30 days", "colorectal_referral_date"],
        returning='binary_flag',
        return_binary_flag=None,
    ),

    fit_date=patients.with_these_clinical_events(
        fit_codes,
        between=["colorectal_referral_date - 60 days", "colorectal_referral_date"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_last_match_in_period=True,
    ),

    fit_flag=patients.with_these_clinical_events(
        fit_codes,
        between=["colorectal_referral_date - 60 days", "colorectal_referral_date"],
        returning='binary_flag',
        return_binary_flag=None,
    ),

    age=patients.age_as_of(
        "colorectal_referral_date", 
        return_expectations={"rate" : "universal", "int" : {"distribution" : "population_ages"}},
    ),

    sex=patients.sex(
        return_expectations={"rate": "universal", "category": {"ratios": {"M": 0.5, "F": 0.5}}},
    ),

)