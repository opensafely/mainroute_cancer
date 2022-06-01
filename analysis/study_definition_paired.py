from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
from codelists import *
from datetime import datetime, timedelta

start_date = "2018-03-23"
end_date = "2022-03-23"


def colorectal_symp_ref_date_X(name, symp_codelist, ref_codelist, diag_codelist, index_date, n, ref_window_weeks=6):
  def var_signature(
    name,
    symp_codelist,
    ref_codelist,
    diag_codelist,
    on_or_after,
  ):
    symp_date = f"{name}_symp_date"
    ref_date = f"{name}_ref_date"
    diag_date = f"{name}_diag_date"
    symp_on_or_after = on_or_after
    ref_on_or_before = (datetime.strptime("2020-01-01","%Y-%m-%d")+timedelta(weeks=ref_window_weeks)).strftime("%Y-%m-%d")
    return {
      symp_date: patients.with_these_clinical_events(
        symp_codelist,
        on_or_after=symp_on_or_after,
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD"
      ),
      ref_date: patients.with_these_clinical_events(
        ref_codelist,
        between=[symp_on_or_after,ref_on_or_before],
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD"
      ),
      diag_date: patients.admitted_to_hospital(
        with_these_diagnoses=diag_codelist,
        returning="date_admitted",
        on_or_after=symp_on_or_after,
        find_first_match_in_period=True,
        date_format="YYYY-MM-DD"
      )
    }
    
  variables = var_signature(f"{name}_1_date", symp_codelist, ref_codelist, diag_codelist, index_date)

  for i in range(2, n+1):
    variables.update(var_signature(
      name=f"{name}_{i}_date",
      symp_codelist=symp_codelist,
      ref_codelist=ref_codelist,
      diag_codelist=diag_codelist, 
      on_or_after=f"{name}_{i-1}_date_symp_date + 1 day",
    ))

  return variables

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    index_date = "2018-03-23",

    population=patients.satisfying(
        "registered",
        registered=patients.registered_as_of("index_date - 1 day",),
    ),
    
    **colorectal_symp_ref_date_X(
        name = "colorectal_symptom",
        symp_codelist = colorectal_symptom_codes,
        ref_codelist = colorectal_referral_codes,
        diag_codelist = colorectal_diagnosis_codes,
        index_date = "2018-02-23",
        n = 6,
        ref_window_weeks = 6,
    )
)