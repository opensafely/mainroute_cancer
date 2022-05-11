from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
from codelists import *

start_date = "2018-03-23"
end_date = "2022-03-23"

def colorectalsymp_date_X(name, codelist, index_date, n):
  def var_signature(
    name,
    codelist,
    on_or_after,
  ):
    return {
      name: patients.with_these_clinical_events(
        codelist,
        on_or_after=on_or_after,
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD"
      ),
    }
    
  variables = var_signature(f"{name}_1_date", codelist, index_date)
  for i in range(2, n+1):
    variables.update(var_signature(
      f"{name}_{i}_date",
      codelist, 
      f"{name}_{i-1}_date + 1 day",
    ))
  return variables

def colorectalref_date_X(name, codelist, index_date, n):
  def var_signature(
    name,
    codelist,
    on_or_after,
  ):
    return {
      name: patients.with_these_clinical_events(
        codelist,
        on_or_after=on_or_after,
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD"
      ),
    }
    
  variables = var_signature(f"{name}_1_date", codelist, index_date)
  for i in range(2, n+1):
    variables.update(var_signature(
      f"{name}_{i}_date",
      codelist, 
      f"{name}_{i-1}_date + 1 day",
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
    
    **colorectalsymp_date_X(
        name = "colorectal_symptom",
        codelist = colorectal_symptom_codes,
        index_date = "2018-03-23", 
        n = 10,
    ),

    **colorectalref_date_X(
        name = "colorectal_referral",
        codelist = colorectal_referral_codes,
        index_date = "2018-02-23",
        n = 5,
    ),
)