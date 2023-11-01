from codelists import *
from cohortextractor import (
    StudyDefinition,
    Measure,
    codelist,
    codelist_from_csv,
    combine_codelists,
    filter_codes_by_category,
    patients,
)

all_lowerGI_symptom_codes = combine_codelists(
    cibh_codes,
    anaemia_codes,
    wl_codes,
    prbleeding_codes
)

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    index_date="2018-03-01",

    population=patients.satisfying(
        'registered AND (age >=18 AND age <= 110)',
        registered=patients.registered_as_of("index_date"),
    ),
    
    age=patients.age_as_of(
        "index_date",
        return_expectations={"rate" : "universal", "int" : {"distribution" : "population_ages"}},
    ),

    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),

    lowerGI_symptom_date=patients.with_these_clinical_events(
        all_lowerGI_symptom_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"date": {"earliest": "2018-03-01", "latest": "today"}},
    ),

    lowerGI_symptom=patients.satisfying(
        '(cibh OR (weight_loss AND age >= 40) OR (pr_bleed AND age < 50 AND weight_loss) OR (pr_bleed AND age >=50) OR (anaemia AND age >=60)) AND NOT prev_event',
        cibh=patients.with_these_clinical_events(
            cibh_codes, 
            between=["index_date", "last_day_of_month(index_date)"],
        ),
        anaemia=patients.with_these_clinical_events(
            anaemia_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
        weight_loss=patients.with_these_clinical_events(
            wl_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
        pr_bleed=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
        prev_event=patients.with_these_clinical_events(
            all_lowerGI_symptom_codes,
            between=["lowerGI_symptom_date - 30 days","lowerGI_symptom_date - 1 day"],
        ),
    ),

    colorectal_ca_diagnosis=patients.with_these_clinical_events(
        colorectal_diagnosis_codes_snomed,
        between=["lowerGI_symptom_date", "lowerGI_symptom_date + 183 days"],
        returning='binary_flag',
        return_binary_flag=None,
    ),

    fit_test=patients.with_these_clinical_events(
        fit_codes,
        between=["lowerGI_symptom_date", "lowerGI_symptom_date + 30 days"],
        returning='binary_flag',
        return_binary_flag=None,
    ),
)

measures = [
    Measure(
        id="lowerGI_symptom_rate",
        numerator="lowerGI_symptom",
        denominator="population",
        group_by="population",
    ),
    Measure(
        id="lowerGI_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="lowerGI_symptom",
        group_by="population",
    ),
    Measure(
        id="lowerGI_symptom_fit_conversion",
        numerator="fit_test",
        denominator="lowerGI_symptom",
        group_by="population",
    ),
]