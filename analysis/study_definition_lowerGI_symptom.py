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
    ida_codes,
    anaemia_codes,
    wl_codes,
    prbleeding_codes,
    abdomass_codes,
    abdopain_codes
)

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    index_date="2018-03-01",

    population=patients.satisfying(
        'registered AND (age >=16 AND age <= 110) AND (NOT died) AND (NOT prev_colorectal_ca_diagnosis) AND (cibh_1 OR abdo_mass_1 OR ida_1 OR (weight_loss_1 AND abdo_pain_1 AND age >= 40) OR (pr_bleed_1 AND age < 50 AND (weight_loss_1 OR abdo_pain_1)) OR ((pr_bleed_1 OR abdo_pain_1 OR weight_loss_1) AND age >=50) OR (anaemia_1 AND age >=60))',
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
        cibh_1=patients.with_these_clinical_events(
            cibh_codes, 
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="binary_flag",
            find_first_match_in_period=True,
            return_expectations={"incidence": 0.001},
        ),
        anaemia_1=patients.with_these_clinical_events(
            anaemia_codes,
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="binary_flag",
            find_first_match_in_period=True,
            return_expectations={"incidence": 0.001},
        ),
        weight_loss_1=patients.with_these_clinical_events(
            wl_codes,
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="binary_flag",
            find_first_match_in_period=True,
            return_expectations={"incidence": 0.001},
        ),
        pr_bleed_1=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="binary_flag",
            find_first_match_in_period=True,
            return_expectations={"incidence": 0.001},
        ),
        abdo_mass_1=patients.with_these_clinical_events(
            abdomass_codes,
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="binary_flag",
            find_first_match_in_period=True,
            return_expectations={"incidence": 0.001},
        ),
        ida_1=patients.with_these_clinical_events(
            ida_codes,
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="binary_flag",
            find_first_match_in_period=True,
            return_expectations={"incidence": 0.001},
        ),
        abdo_pain_1=patients.with_these_clinical_events(
            abdopain_codes,
            between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
            returning="binary_flag",
            find_first_match_in_period=True,
            return_expectations={"incidence": 0.001},
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

    lowerGI_symptom_date=patients.with_these_clinical_events(
        all_lowerGI_symptom_codes,
        between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"date": {"earliest": "2018-03-23", "latest": "today"}},
    ),

    prev_event=patients.satisfying(
        'cibh_2 OR abdo_mass_2 OR ida_2 OR (weight_loss_2 AND abdo_pain_2 AND age >= 40) OR (pr_bleed_2 AND age < 50 AND (weight_loss_2 OR abdo_pain_2)) OR ((pr_bleed_2 OR abdo_pain_2 OR weight_loss_2) AND age >=50) OR (anaemia_2 AND age >=60)',
        cibh_2=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_symptom_date - 42 days", "lowerGI_symptom_date - 1 day"],
        ),
        anaemia_2=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_symptom_date - 42 days", "lowerGI_symptom_date - 1 day"],
        ),
        weight_loss_2=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_symptom_date - 42 days", "lowerGI_symptom_date - 1 day"],
        ),
        pr_bleed_2=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_symptom_date - 42 days", "lowerGI_symptom_date - 1 day"],
        ),
        abdo_mass_2=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_symptom_date - 42 days", "lowerGI_symptom_date - 1 day"],
        ),
        ida_2=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_symptom_date - 42 days", "lowerGI_symptom_date - 1 day"],
        ),
        abdo_pain_2=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_symptom_date - 42 days", "lowerGI_symptom_date - 1 day"],
        ),
    ),

    cibh_symptom=patients.with_these_clinical_events(
        cibh_codes,
        between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    cibh_symptom_date=patients.date_of("cibh_symptom", date_format="YYYY-MM-DD"),

    abdomass_symptom=patients.with_these_clinical_events(
        abdomass_codes,
        between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    abdomass_symptom_date=patients.date_of("abdomass_symptom", date_format="YYYY-MM-DD"),

    ida_symptom=patients.with_these_clinical_events(
        ida_codes,
        between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    ida_symptom_date=patients.date_of("ida_symptom", date_format="YYYY-MM-DD"),

    wl_symptom=patients.with_these_clinical_events(
        wl_codes,
        between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    wl_symptom_date=patients.date_of("wl_symptom", date_format="YYYY-MM-DD"),

    prbleed_symptom=patients.with_these_clinical_events(
        prbleeding_codes,
        between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    prbleed_symptom_date=patients.date_of("prbleed_symptom", date_format="YYYY-MM-DD"),

    abdopain_symptom=patients.with_these_clinical_events(
        abdopain_codes,
        between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    abdopain_symptom_date=patients.date_of("abdopain_symptom", date_format="YYYY-MM-DD"),

    anaemia_symptom=patients.with_these_clinical_events(
        anaemia_codes,
        between=["index_date + 22 days", "last_day_of_month(index_date) + 22 days"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    anaemia_symptom_date=patients.date_of("anaemia_symptom", date_format="YYYY-MM-DD"),

    colorectal_ca_diagnosis=patients.with_these_clinical_events(
        colorectal_diagnosis_codes_snomed,
        between=["lowerGI_symptom_date", "lowerGI_symptom_date + 183 days"],
        returning='binary_flag',
        return_binary_flag=None,
    ),
    colorectal_ca_date=patients.date_of("colorectal_ca_diagnosis", date_format="YYYY-MM-DD"),

    fit_test=patients.with_these_clinical_events(
        fit_codes,
        between=["lowerGI_symptom_date", "lowerGI_symptom_date + 30 days"],
        returning='binary_flag',
        return_binary_flag=None,
    ),

    lowerGI_2wwreferral=patients.with_these_clinical_events(
        colorectal_referral_codes,
        between=["lowerGI_symptom_date", "lowerGI_symptom_date + 42 days"],
        returning='binary_flag',
        return_binary_flag=None,
    ),
    lowerGI_2ww_date=patients.date_of("lowerGI_2wwreferral", date_format="YYYY-MM-DD"),
)

measures = [
    Measure(
        id="lowerGI_symptom",
        numerator="population",
        denominator="population",
        group_by="population",
    ),
    Measure(
        id="lowerGI_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="population",
        group_by="population",
    ),
    Measure(
        id="lowerGI_symptom_fit_conversion",
        numerator="fit_test",
        denominator="population",
        group_by="population",
    ),
    Measure(
        id="lowerGI_referral_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="lowerGI_2wwreferral",
        group_by="population",
    ),
    Measure(
        id="cibh_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="cibh_symptom",
        group_by="population",
    ),
    Measure(
        id="abdomass_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="abdomass_symptom",
        group_by="population",
    ),
    Measure(
        id="ida_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="ida_symptom",
        group_by="population",
    ),
    Measure(
        id="wl_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="wl_symptom",
        group_by="population",
    ),
    Measure(
        id="prbleed_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="prbleed_symptom",
        group_by="population",
    ),
    Measure(
        id="abdopain_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="abdopain_symptom",
        group_by="population",
    ),
    Measure(
        id="anaemia_symptom_cancer_conversion",
        numerator="colorectal_ca_diagnosis",
        denominator="anaemia_symptom",
        group_by="population",
    ),
    Measure(
        id="lowerGI_symptom_ethnicity",
        numerator="population",
        denominator="population",
        group_by="ethnicity",
    ),
    Measure(
        id="lowerGI_symptom_imd",
        numerator="population",
        denominator="population",
        group_by="imd",
    ),
    Measure(
        id="lowerGI_symptom_region",
        numerator="population",
        denominator="population",
        group_by="region",
    ),
]