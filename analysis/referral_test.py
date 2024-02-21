from ehrql import Dataset, years, days, months, minimum_of, maximum_of, case, when
from ehrql.tables.core import patients, clinical_events
from ehrql.tables.tpp import practice_registrations, ons_deaths, opa, opa_proc

import codelists

index_date = "2018-03-23"
end_date = "2023-10-22"

dataset = Dataset()

lowerGI_2ww_ref = clinical_events.where(clinical_events.snomedct_code.is_in(codelists.colorectal_referral_codes)
            ).where(
                clinical_events.date.is_on_or_between(index_date, end_date)
            ).sort_by(
                clinical_events.date
            ).first_for_patient()

has_lowerGI_2ww = lowerGI_2ww_ref.exists_for_patient()

dataset.define_population(
    has_lowerGI_2ww
)

dataset.lowerGI_2ww_date = lowerGI_2ww_ref.date

colorectal_surg_clinic_code = ["104"]
gastro_clinic_code = ["301"]

colorectal_surg_clinic_2ww = (
    opa.where(opa.treatment_function_code.is_in(colorectal_surg_clinic_code)
        ).where(
            opa.appointment_date.is_on_or_between(dataset.lowerGI_2ww_date, dataset.lowerGI_2ww_date + days(21))          
        ).sort_by(
            opa.appointment_date
        ).first_for_patient()
)

dataset.colorectal_surg_clinic_3weeks = colorectal_surg_clinic_2ww.exists_for_patient()

gastro_clinic_2ww = (
    opa.where(opa.treatment_function_code.is_in(gastro_clinic_code)
        ).where(
            opa.appointment_date.is_on_or_between(dataset.lowerGI_2ww_date, dataset.lowerGI_2ww_date + days(21))          
        ).sort_by(
            opa.appointment_date
        ).first_for_patient()
)

dataset.gastro_clinic_3weeks = gastro_clinic_2ww.exists_for_patient()
