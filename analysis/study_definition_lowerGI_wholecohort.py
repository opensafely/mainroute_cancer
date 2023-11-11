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

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.9,
    },

    index_date="2018-03-01",

    population=patients.satisfying(
        'registered AND (age >=16 AND age <= 110) AND (NOT died) AND (NOT prev_colorectal_ca_diagnosis)',
        registered=patients.registered_as_of("last_day_of_month(index_date) + 7 days"),
        died=patients.died_from_any_cause(
            on_or_before="index_date + 22 days",
            returning="binary_flag",
            return_expectations={"incidence": 0.01},
        ),
        prev_colorectal_ca_diagnosis=patients.with_these_clinical_events(
            colorectal_diagnosis_codes_snomed,
            on_or_before="index_date + 22 days",
            returning="binary_flag",
        ),
    ),
    
    age=patients.age_as_of(
        "index_date + 22 days",
        return_expectations={"rate" : "universal", "int" : {"distribution" : "population_ages"}},
    ),

    exit_date=patients.minimum_of(
        death_date=patients.died_from_any_cause(
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="date_of_death",
            date_format="YYYY-MM-DD",
        ),
        dereg_date=patients.date_deregistered_from_all_supported_practices(
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            date_format="YYYY-MM-DD",
        ),
        colorectal_ca_diagnosis_any_date=patients.with_these_clinical_events(
            colorectal_diagnosis_codes_snomed,
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="date",
            date_format="YYYY-MM-DD",
            find_first_match_in_period=True,
            return_expectations={"date": {"earliest": "2018-03-23", "latest": "today"}},
        ),
    ),
)

measures = [
    Measure(
        id="whole_cohort",
        numerator="population",
        denominator="population",
        group_by="population",
    ),
    Measure(
        id="whole_cohort_ethnicity",
        numerator="population",
        denominator="population",
        group_by="ethnicity",
    ),
    Measure(
        id="whole_cohort_imd",
        numerator="population",
        denominator="population",
        group_by="imd",
    ),
    Measure(
        id="whole_cohort_region",
        numerator="population",
        denominator="population",
        group_by="region",
    ),
]