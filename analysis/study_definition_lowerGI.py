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
        "incidence": 0.2,
    },

    index_date="2018-03-01",

    population=patients.satisfying(
        'registered AND (age >=18 AND age <= 110) AND (NOT died) AND (NOT prev_colorectal_ca_diagnosis)',
        registered=patients.registered_as_of("index_date + 15 days"),
        died=patients.died_from_any_cause(
            on_or_before="index_date",
            returning="binary_flag",
            return_expectations={"incidence": 0.01},
        ),
        prev_colorectal_ca_diagnosis=patients.with_these_clinical_events(
            colorectal_diagnosis_codes_snomed,
            on_or_before="index_date",
            returning="binary_flag",
        ),
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

    ethnicity=patients.categorised_as(
        {
            "Missing": "DEFAULT",
            "White": """ ethnicity_code=1 """,
            "Mixed": """ ethnicity_code=2 """,
            "South Asian": """ ethnicity_code=3 """,
            "Black": """ ethnicity_code=4 """,
            "Other": """ ethnicity_code=5 """,
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "Missing": 0.4,
                    "White": 0.2,
                    "Mixed": 0.1,
                    "South Asian": 0.1,
                    "Black": 0.1,
                    "Other": 0.1,
                }
            },
        },
        ethnicity_code=patients.with_these_clinical_events(
            ethnicity_codes,
            returning="category",
            find_last_match_in_period=True,
            on_or_before="index_date",
            return_expectations={
            "category": {"ratios": {"1": 0.4, "2": 0.4, "3": 0.2, "4":0.2,"5": 0.2}},
            "incidence": 0.75,
            },
        ),
    ),

    exit_date=patients.minimum_of(
        death_date=patients.died_from_any_cause(
            between=["index_date", "last_day_of_month(index_date)"],
            returning="date_of_death",
            date_format="YYYY-MM-DD",
        ),
        dereg_date=patients.date_deregistered_from_all_supported_practices(
            between=["index_date", "last_day_of_month(index_date)"],
            date_format="YYYY-MM-DD",
        ),
        colorectal_ca_diagnosis_any_date=patients.with_these_clinical_events(
            colorectal_diagnosis_codes_snomed,
            between=["index_date", "last_day_of_month(index_date)"],
            returning="date",
            date_format="YYYY-MM-DD",
            find_first_match_in_period=True,
            return_expectations={"date": {"earliest": "2018-03-01", "latest": "today"}},
        ),
    ),

    lowerGI_condition_1=patients.with_these_clinical_events(
        abdomass_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    lowerGI_condition_1_date=patients.date_of("lowerGI_condition_1", date_format="YYYY-MM-DD"),

    prev_event_condition_1=patients.satisfying(
        'cibh_1 OR abdo_mass_1 OR ida_1 OR (weight_loss_1 AND abdo_pain_1 AND age >= 40) OR (pr_bleed_1 AND age < 50 AND (weight_loss_1 OR abdo_pain_1)) OR ((pr_bleed_1 OR abdo_pain_1 OR weight_loss_1) AND age >=50) OR (anaemia_1 AND age >=60)',
        cibh_1=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_1_date - 42 days", "lowerGI_condition_1_date - 1 day"],
        ),
        anaemia_1=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_1_date - 42 days", "lowerGI_condition_1_date - 1 day"],
        ),
        weight_loss_1=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_1_date - 42 days", "lowerGI_condition_1_date - 1 day"],
        ),
        pr_bleed_1=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_1_date - 42 days", "lowerGI_condition_1_date - 1 day"],
        ),
        abdo_mass_1=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_1_date - 42 days", "lowerGI_condition_1_date - 1 day"],
        ),
        ida_1=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_1_date - 42 days", "lowerGI_condition_1_date - 1 day"],
        ),
        abdo_pain_1=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_1_date - 42 days", "lowerGI_condition_1_date - 1 day"],
        ),
    ),

    lowerGI_condition_2=patients.with_these_clinical_events(
        cibh_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    lowerGI_condition_2_date=patients.date_of("lowerGI_condition_2", date_format="YYYY-MM-DD"),

    prev_event_condition_2=patients.satisfying(
        'cibh_2 OR abdo_mass_2 OR ida_2 OR (weight_loss_2 AND abdo_pain_2 AND age >= 40) OR (pr_bleed_2 AND age < 50 AND (weight_loss_2 OR abdo_pain_2)) OR ((pr_bleed_2 OR abdo_pain_2 OR weight_loss_2) AND age >=50) OR (anaemia_2 AND age >=60)',
        cibh_2=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_2_date - 42 days", "lowerGI_condition_2_date - 1 day"],
        ),
        anaemia_2=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_2_date - 42 days", "lowerGI_condition_2_date - 1 day"],
        ),
        weight_loss_2=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_2_date - 42 days", "lowerGI_condition_2_date - 1 day"],
        ),
        pr_bleed_2=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_2_date - 42 days", "lowerGI_condition_2_date - 1 day"],
        ),
        abdo_mass_2=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_2_date - 42 days", "lowerGI_condition_2_date - 1 day"],
        ),
        ida_2=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_2_date - 42 days", "lowerGI_condition_2_date - 1 day"],
        ),
        abdo_pain_2=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_2_date - 42 days", "lowerGI_condition_2_date - 1 day"],
        ),
    ),

    lowerGI_condition_3=patients.with_these_clinical_events(
        ida_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        find_first_match_in_period=True,
        return_binary_flag=None,
        return_expectations={"incidence": 0.001},
    ),
    lowerGI_condition_3_date=patients.date_of("lowerGI_condition_3", date_format="YYYY-MM-DD"),

    prev_event_condition_3=patients.satisfying(
        'cibh_3 OR abdo_mass_3 OR ida_3 OR (weight_loss_3 AND abdo_pain_3 AND age >= 40) OR (pr_bleed_3 AND age < 50 AND (weight_loss_3 OR abdo_pain_3)) OR ((pr_bleed_3 OR abdo_pain_3 OR weight_loss_3) AND age >=50) OR (anaemia_3 AND age >=60)',
        cibh_3=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_3_date - 42 days", "lowerGI_condition_3_date - 1 day"],
        ),
        anaemia_3=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_3_date - 42 days", "lowerGI_condition_3_date - 1 day"],
        ),
        weight_loss_3=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_3_date - 42 days", "lowerGI_condition_3_date - 1 day"],
        ),
        pr_bleed_3=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_3_date - 42 days", "lowerGI_condition_3_date - 1 day"],
        ),
        abdo_mass_3=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_3_date - 42 days", "lowerGI_condition_3_date - 1 day"],
        ),
        ida_3=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_3_date - 42 days", "lowerGI_condition_3_date - 1 day"],
        ),
        abdo_pain_3=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_3_date - 42 days", "lowerGI_condition_3_date - 1 day"],
        ),
    ),

    lowerGI_condition_4=patients.satisfying(
        'weight_loss AND abdo_pain AND age >= 40',
        weight_loss=patients.with_these_clinical_events(
            wl_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
        abdo_pain=patients.with_these_clinical_events(
            abdopain_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
    ),
    lowerGI_condition_4_date=patients.minimum_of(
        weight_loss_date_4=patients.with_these_clinical_events(
            wl_codes,
            between=["index_date", "last_day_of_month(index_date)"],
            returning="date",
            date_format="YYYY-MM-DD",
            find_first_match_in_period=True,
        ),
        abdo_pain_date_4=patients.with_these_clinical_events(
            abdopain_codes,
            between=["index_date", "last_day_of_month(index_date)"],
            returning="date",
            date_format="YYYY-MM-DD",
            find_first_match_in_period=True,
        ),
    ),
    
    prev_event_condition_4=patients.satisfying(
        'cibh_4 OR abdo_mass_4 OR ida_4 OR (weight_loss_4 AND abdo_pain_4 AND age >= 40) OR (pr_bleed_4 AND age < 50 AND (weight_loss_4 OR abdo_pain_4)) OR ((pr_bleed_4 OR abdo_pain_4 OR weight_loss_4) AND age >=50) OR (anaemia_4 AND age >=60)',
        cibh_4=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_4_date - 42 days", "lowerGI_condition_4_date - 1 day"],
        ),
        anaemia_4=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_4_date - 42 days", "lowerGI_condition_4_date - 1 day"],
        ),
        weight_loss_4=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_4_date - 42 days", "lowerGI_condition_4_date - 1 day"],
        ),
        pr_bleed_4=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_4_date - 42 days", "lowerGI_condition_4_date - 1 day"],
        ),
        abdo_mass_4=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_4_date - 42 days", "lowerGI_condition_4_date - 1 day"],
        ),
        ida_4=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_4_date - 42 days", "lowerGI_condition_4_date - 1 day"],
        ),
        abdo_pain_4=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_4_date - 42 days", "lowerGI_condition_4_date - 1 day"],
        ),
    ),

    lowerGI_condition_5=patients.satisfying(
        'pr_bleed AND age < 50 AND abdo_pain',
        pr_bleed=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
    ),
    lowerGI_condition_5_date=patients.minimum_of(
        abdo_pain_date_5=patients.with_these_clinical_events(
            abdopain_codes,
            between=["index_date", "last_day_of_month(index_date)"],
            returning="date",
            date_format="YYYY-MM-DD",
            find_first_match_in_period=True,
        ),
        pr_bleed_date_5=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["index_date", "last_day_of_month(index_date)"],
            returning="date",
            date_format="YYYY-MM-DD",
            find_first_match_in_period=True,
        ),
    ),

    prev_event_condition_5=patients.satisfying(
        'cibh_5 OR abdo_mass_5 OR ida_5 OR (weight_loss_5 AND abdo_pain_5 AND age >= 40) OR (pr_bleed_5 AND age < 50 AND (weight_loss_5 OR abdo_pain_5)) OR ((pr_bleed_5 OR abdo_pain_5 OR weight_loss_5) AND age >=50) OR (anaemia_5 AND age >=60)',
        cibh_5=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_5_date - 42 days", "lowerGI_condition_5_date - 1 day"],
        ),
        anaemia_5=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_5_date - 42 days", "lowerGI_condition_5_date - 1 day"],
        ),
        weight_loss_5=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_5_date - 42 days", "lowerGI_condition_5_date - 1 day"],
        ),
        pr_bleed_5=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_5_date - 42 days", "lowerGI_condition_5_date - 1 day"],
        ),
        abdo_mass_5=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_5_date - 42 days", "lowerGI_condition_5_date - 1 day"],
        ),
        ida_5=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_5_date - 42 days", "lowerGI_condition_5_date - 1 day"],
        ),
        abdo_pain_5=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_5_date - 42 days", "lowerGI_condition_5_date - 1 day"],
        ),
    ),

    lowerGI_condition_6=patients.satisfying('pr_bleed AND age < 50 AND weight_loss'),
    lowerGI_condition_6_date=patients.minimum_of(
        weight_loss_date_6=patients.with_these_clinical_events(
            wl_codes,
            between=["index_date", "last_day_of_month(index_date)"],
            returning="date",
            date_format="YYYY-MM-DD",
            find_first_match_in_period=True,
        ), 
        pr_bleed_date_6=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["index_date", "last_day_of_month(index_date)"],
            returning="date",
            date_format="YYYY-MM-DD",
            find_first_match_in_period=True,
        ),
    ),

    prev_event_condition_6=patients.satisfying(
        'cibh_6 OR abdo_mass_6 OR ida_6 OR (weight_loss_6 AND abdo_pain_6 AND age >= 40) OR (pr_bleed_6 AND age < 50 AND (weight_loss_6 OR abdo_pain_6)) OR ((pr_bleed_6 OR abdo_pain_6 OR weight_loss_6) AND age >=50) OR (anaemia_6 AND age >=60)',
        cibh_6=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_6_date - 42 days", "lowerGI_condition_6_date - 1 day"],
        ),
        anaemia_6=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_6_date - 42 days", "lowerGI_condition_6_date - 1 day"],
        ),
        weight_loss_6=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_6_date - 42 days", "lowerGI_condition_6_date - 1 day"],
        ),
        pr_bleed_6=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_6_date - 42 days", "lowerGI_condition_6_date - 1 day"],
        ),
        abdo_mass_6=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_6_date - 42 days", "lowerGI_condition_6_date - 1 day"],
        ),
        ida_6=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_6_date - 42 days", "lowerGI_condition_6_date - 1 day"],
        ),
        abdo_pain_6=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_6_date - 42 days", "lowerGI_condition_6_date - 1 day"],
        ),
    ),

    lowerGI_condition_7=patients.satisfying('age >=50 AND pr_bleed'),
    lowerGI_condition_7_date=patients.with_these_clinical_events(
        prbleeding_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
    ),

    prev_event_condition_7=patients.satisfying(
        'cibh_7 OR abdo_mass_7 OR ida_7 OR (weight_loss_7 AND abdo_pain_7 AND age >= 40) OR (pr_bleed_7 AND age < 50 AND (weight_loss_7 OR abdo_pain_7)) OR ((pr_bleed_7 OR abdo_pain_7 OR weight_loss_7) AND age >=50) OR (anaemia_7 AND age >=60)',
        cibh_7=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_7_date - 42 days", "lowerGI_condition_7_date - 1 day"],
        ),
        anaemia_7=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_7_date - 42 days", "lowerGI_condition_7_date - 1 day"],
        ),
        weight_loss_7=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_7_date - 42 days", "lowerGI_condition_7_date - 1 day"],
        ),
        pr_bleed_7=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_7_date - 42 days", "lowerGI_condition_7_date - 1 day"],
        ),
        abdo_mass_7=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_7_date - 42 days", "lowerGI_condition_7_date - 1 day"],
        ),
        ida_7=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_7_date - 42 days", "lowerGI_condition_7_date - 1 day"],
        ),
        abdo_pain_7=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_7_date - 42 days", "lowerGI_condition_7_date - 1 day"],
        ),
    ),

    lowerGI_condition_8=patients.satisfying('age >=50 AND abdo_pain'),
    lowerGI_condition_8_date=patients.with_these_clinical_events(
        abdopain_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
    ),

    prev_event_condition_8=patients.satisfying(
        'cibh_8 OR abdo_mass_8 OR ida_8 OR (weight_loss_8 AND abdo_pain_8 AND age >= 40) OR (pr_bleed_8 AND age < 50 AND (weight_loss_8 OR abdo_pain_8)) OR ((pr_bleed_8 OR abdo_pain_8 OR weight_loss_8) AND age >=50) OR (anaemia_8 AND age >=60)',
        cibh_8=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_8_date - 42 days", "lowerGI_condition_8_date - 1 day"],
        ),
        anaemia_8=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_8_date - 42 days", "lowerGI_condition_8_date - 1 day"],
        ),
        weight_loss_8=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_8_date - 42 days", "lowerGI_condition_8_date - 1 day"],
        ),
        pr_bleed_8=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_8_date - 42 days", "lowerGI_condition_8_date - 1 day"],
        ),
        abdo_mass_8=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_8_date - 42 days", "lowerGI_condition_8_date - 1 day"],
        ),
        ida_8=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_8_date - 42 days", "lowerGI_condition_8_date - 1 day"],
        ),
        abdo_pain_8=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_8_date - 42 days", "lowerGI_condition_8_date - 1 day"],
        ),
    ),

    lowerGI_condition_9=patients.satisfying('age >=50 AND weight_loss'),
    lowerGI_condition_9_date=patients.with_these_clinical_events(
        wl_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
    ),

    prev_event_condition_9=patients.satisfying(
        'cibh_9 OR abdo_mass_9 OR ida_9 OR (weight_loss_9 AND abdo_pain_9 AND age >= 40) OR (pr_bleed_9 AND age < 50 AND (weight_loss_9 OR abdo_pain_9)) OR ((pr_bleed_9 OR abdo_pain_9 OR weight_loss_9) AND age >=50) OR (anaemia_9 AND age >=60)',
        cibh_9=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_9_date - 42 days", "lowerGI_condition_9_date - 1 day"],
        ),
        anaemia_9=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_9_date - 42 days", "lowerGI_condition_9_date - 1 day"],
        ),
        weight_loss_9=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_9_date - 42 days", "lowerGI_condition_9_date - 1 day"],
        ),
        pr_bleed_9=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_9_date - 42 days", "lowerGI_condition_9_date - 1 day"],
        ),
        abdo_mass_9=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_9_date - 42 days", "lowerGI_condition_9_date - 1 day"],
        ),
        ida_9=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_9_date - 42 days", "lowerGI_condition_9_date - 1 day"],
        ),
        abdo_pain_9=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_9_date - 42 days", "lowerGI_condition_9_date - 1 day"],
        ),
    ),

    lowerGI_condition_10=patients.satisfying(
        'age >=60 AND anaemia',
        anaemia=patients.with_these_clinical_events(
            anaemia_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
    ),
    lowerGI_condition_10_date=patients.with_these_clinical_events(
        anaemia_codes,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
    ),

    prev_event_condition_10=patients.satisfying(
        'cibh_10 OR abdo_mass_10 OR ida_10 OR (weight_loss_10 AND abdo_pain_10 AND age >= 40) OR (pr_bleed_10 AND age < 50 AND (weight_loss_10 OR abdo_pain_10)) OR ((pr_bleed_10 OR abdo_pain_10 OR weight_loss_10) AND age >=50) OR (anaemia_10 AND age >=60)',
        cibh_10=patients.with_these_clinical_events(
            cibh_codes, 
            between=["lowerGI_condition_10_date - 42 days", "lowerGI_condition_10_date - 1 day"],
        ),
        anaemia_10=patients.with_these_clinical_events(
            anaemia_codes,
            between=["lowerGI_condition_10_date - 42 days", "lowerGI_condition_10_date - 1 day"],
        ),
        weight_loss_10=patients.with_these_clinical_events(
            wl_codes,
            between=["lowerGI_condition_10_date - 42 days", "lowerGI_condition_10_date - 1 day"],
        ),
        pr_bleed_10=patients.with_these_clinical_events(
            prbleeding_codes,
            between=["lowerGI_condition_10_date - 42 days", "lowerGI_condition_10_date - 1 day"],
        ),
        abdo_mass_10=patients.with_these_clinical_events(
            abdomass_codes,
            between=["lowerGI_condition_10_date - 42 days", "lowerGI_condition_10_date - 1 day"],
        ),
        ida_10=patients.with_these_clinical_events(
            ida_codes,
            between=["lowerGI_condition_10_date - 42 days", "lowerGI_condition_10_date - 1 day"],
        ),
        abdo_pain_10=patients.with_these_clinical_events(
            abdopain_codes,
            between=["lowerGI_condition_10_date - 42 days", "lowerGI_condition_10_date - 1 day"],
        ),
    ),

    lowerGI_symptom=patients.satisfying(
        'lowerGI_condition_1 OR lowerGI_condition_2 OR lowerGI_condition_3 OR lowerGI_condition_4 OR lowerGI_condition_5 OR lowerGI_condition_6 OR lowerGI_condition_7 OR lowerGI_condition_8 OR lowerGI_condition_9 OR lowerGI_condition_10'
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
        id="lowerGI_condition_1_rate",
        numerator="lowerGI_condition_1",
        denominator="population",
        group_by="prev_event_condition_1",
    ),
    Measure(
        id="lowerGI_condition_2_rate",
        numerator="lowerGI_condition_2",
        denominator="population",
        group_by="prev_event_condition_2",
    ),
    Measure(
        id="lowerGI_condition_3_rate",
        numerator="lowerGI_condition_3",
        denominator="population",
        group_by="prev_event_condition_3",
    ),
    Measure(
        id="lowerGI_condition_4_rate",
        numerator="lowerGI_condition_4",
        denominator="population",
        group_by="prev_event_condition_4",
    ),
    Measure(
        id="lowerGI_condition_5_rate",
        numerator="lowerGI_condition_5",
        denominator="population",
        group_by="prev_event_condition_5",
    ),
    Measure(
        id="lowerGI_condition_6_rate",
        numerator="lowerGI_condition_6",
        denominator="population",
        group_by="prev_event_condition_6",
    ),
    Measure(
        id="lowerGI_condition_7_rate",
        numerator="lowerGI_condition_7",
        denominator="population",
        group_by="prev_event_condition_7",
    ),
    Measure(
        id="lowerGI_condition_8_rate",
        numerator="lowerGI_condition_8",
        denominator="population",
        group_by="prev_event_condition_8",
    ),
    Measure(
        id="lowerGI_condition_9_rate",
        numerator="lowerGI_condition_9",
        denominator="population",
        group_by="prev_event_condition_9",
    ),
    Measure(
        id="lowerGI_condition_10_rate",
        numerator="lowerGI_condition_10",
        denominator="population",
        group_by="prev_event_condition_10",
    ),
]