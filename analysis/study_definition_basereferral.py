from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv, combine_codelists  # NOQA
from codelists import *
from datetime import datetime, timedelta

start_date = "2018-03-23"
end_date = "2022-03-23"

'''colorectal_diagnosis_codes_gp = combine_codelists(
    colorectal_diagnosis_codes_snomed,
    colorectal_diagnosis_codes_read
)'''

def colorectal_ref_diag_date_X(name, ref_codelist, diag_codelist, index_date, n, diag_window_weeks):
  def var_signature(
    name,
    ref_codelist,
    diag_codelist,
    on_or_after,
  ):
    ref_date = f"{name}_ref_date"
    diag_date = f"{name}_diag_date"
    ref_on_or_after = on_or_after
    diag_on_or_before = (datetime.strptime("2022-03-23","%Y-%m-%d")+timedelta(weeks=diag_window_weeks)).strftime("%Y-%m-%d")
    return {
      ref_date: patients.with_these_clinical_events(
        ref_codelist,
        on_or_after=ref_on_or_after,
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD"
      ),
      diag_date: patients.with_these_clinical_events(
        diag_codelist,
        between=[ref_on_or_after,diag_on_or_before],
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD"
      )
    }
    
  variables = var_signature(f"{name}_1_date", ref_codelist, diag_codelist, index_date)

  for i in range(2, n+1):
    variables.update(var_signature(
      name=f"{name}_{i}_date",
      ref_codelist=ref_codelist,
      diag_codelist=diag_codelist, 
      on_or_after=f"{name}_{i-1}_date_ref_date + 1 day",
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
    
    **colorectal_ref_diag_date_X(
        name = "colorectal_symptom",
        ref_codelist = colorectal_referral_codes,
        diag_codelist = colorectal_diagnosis_codes_snomed,
        index_date = "2018-02-23",
        n = 6,
        diag_window_weeks = 18,
    )
)