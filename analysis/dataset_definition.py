from ehrql import Dataset, years, days, months, minimum_of, maximum_of, case, when
from ehrql.tables.core import patients
from ehrql.tables.tpp import practice_registrations, ons_deaths, clinical_events, clinical_events_ranges, apcs

import codelists

def make_dataset_lowerGI(index_date, end_date):
    
    dataset = Dataset()

    reg_date = practice_registrations.where(practice_registrations.start_date.is_on_or_between(index_date, end_date)
                                                    ).sort_by(
                                                        practice_registrations.start_date
                                                    ).first_for_patient().start_date
    
    age_16_date = patients.date_of_birth + years(16)

    dataset.entry_date = maximum_of(reg_date, age_16_date, "2018-03-23")

    death_date = ons_deaths.date

    age_110_date = patients.date_of_birth + years(110)

    dereg_date = practice_registrations.sort_by(practice_registrations.end_date
                                              ).first_for_patient().end_date

    colorectal_ca_diag_date = clinical_events.where(clinical_events.snomedct_code.is_in(codelists.colorectal_diagnosis_codes_snomed)
                                                        ).sort_by(
                                                            clinical_events.date
                                                        ).first_for_patient().date
    
    dataset.exit_date = minimum_of(death_date, age_110_date, dereg_date, colorectal_ca_diag_date, "2023-10-22")

    dataset.death_date = death_date

    def first_event(codelist):
        return clinical_events.where(clinical_events.snomedct_code.is_in(codelist)
            ).where(
                clinical_events.date.is_on_or_between(index_date, end_date)
            ).where(
                clinical_events.date.is_on_or_between(dataset.entry_date, dataset.exit_date)
            ).sort_by(
                clinical_events.date
            ).first_for_patient()
    
    def prev_event(codelist, symp_date):
        return clinical_events.where(clinical_events.snomedct_code.is_in(codelist)
            ).where(
                clinical_events.date.is_on_or_between(symp_date - days (42), symp_date - days(1))
            ).exists_for_patient()

    ida_date = first_event(codelists.ida_codes).date
    cibh_date = first_event(codelists.cibh_codes).date
    prbleed_date = first_event(codelists.prbleeding_codes).date
    wl_date = first_event(codelists.wl_codes).date
    abdomass_date = first_event(codelists.abdomass_codes).date
    abdopain_date = first_event(codelists.abdopain_codes).date
    anaemia_date = first_event(codelists.anaemia_codes).date

    fit_test_any_date = first_event(codelists.fit_codes).date

    def has_event(codelist):
        return first_event(codelist).exists_for_patient()

    dataset.ida_symp = has_event(codelists.ida_codes) & ~prev_event(codelists.ida_codes, ida_date)
    dataset.cibh_symp = has_event(codelists.cibh_codes) & ~prev_event(codelists.cibh_codes, cibh_date)
    dataset.abdomass_symp = has_event(codelists.abdomass_codes) & ~prev_event(codelists.abdomass_codes, abdomass_date)
    dataset.prbleed_symp = has_event(codelists.prbleeding_codes) & ~prev_event(codelists.prbleeding_codes, prbleed_date)
    dataset.wl_symp = has_event(codelists.wl_codes) & ~prev_event(codelists.wl_codes, wl_date)
    dataset.abdopain_symp = has_event(codelists.abdopain_codes) & ~prev_event(codelists.abdopain_codes, abdopain_date)
    dataset.anaemia_symp = has_event(codelists.anaemia_codes) & ~prev_event(codelists.anaemia_codes, anaemia_date)

    dataset.prbleed_symp_50 = has_event(codelists.prbleeding_codes) & (patients.age_on(prbleed_date) >= 50) & ~prev_event(codelists.prbleeding_codes, prbleed_date)
    dataset.wl_symp_50 = has_event(codelists.wl_codes) & (patients.age_on(wl_date) >= 50) & ~prev_event(codelists.wl_codes, wl_date)
    dataset.abdopain_symp_50 = has_event(codelists.abdopain_codes) & (patients.age_on(abdopain_date) >= 50) & ~prev_event(codelists.abdopain_codes, abdopain_date)
    dataset.anaemia_symp_60 = has_event(codelists.anaemia_codes) & (patients.age_on(anaemia_date) >= 60) & ~prev_event(codelists.anaemia_codes, anaemia_date)
    dataset.wl_abdopain_symp_40 = has_event(codelists.wl_codes) & has_event(codelists.abdopain_codes) & ((patients.age_on(wl_date) >= 40) | (patients.age_on(abdopain_date) >= 40)) & ~prev_event(codelists.wl_codes, wl_date) & ~prev_event(codelists.abdopain_codes, abdopain_date)
    dataset.prbleed_abdopain_symp = has_event(codelists.prbleeding_codes) & has_event(codelists.abdopain_codes) & (patients.age_on(prbleed_date) < 50) & ~prev_event(codelists.prbleeding_codes, prbleed_date) & ~prev_event(codelists.abdopain_codes, abdopain_date)
    dataset.prbleed_wl_symp = has_event(codelists.prbleeding_codes) & has_event(codelists.wl_codes) & (patients.age_on(prbleed_date) < 50) & ~prev_event(codelists.prbleeding_codes, prbleed_date) & ~prev_event(codelists.wl_codes, wl_date)
    
    dataset.lowerGI_any_symp = (dataset.ida_symp | dataset.cibh_symp | dataset.abdomass_symp | dataset.prbleed_symp | dataset.wl_symp | dataset.abdopain_symp | dataset.anaemia_symp)
    dataset.lowerGI_2ww_symp = (dataset.ida_symp | dataset.cibh_symp | dataset.abdomass_symp | dataset.prbleed_symp_50 | dataset.wl_symp_50 | dataset.abdopain_symp_50 | dataset.anaemia_symp_60 | dataset.wl_abdopain_symp_40 | dataset.prbleed_abdopain_symp | dataset.prbleed_wl_symp)

    dataset.fit_test_any = has_event(codelists.fit_codes) & ~prev_event(codelists.fit_codes, fit_test_any_date)

    def symptom_date(symp_date, symp_event):
        return case(when(symp_event).then(symp_date))
    
    dataset.ida_date = symptom_date(ida_date, dataset.ida_symp)
    dataset.cibh_date = symptom_date(cibh_date, dataset.cibh_symp)
    dataset.prbleed_date = symptom_date(prbleed_date, dataset.prbleed_symp)
    dataset.wl_date = symptom_date(wl_date, dataset.wl_symp)
    dataset.abdomass_date = symptom_date(abdomass_date, dataset.abdomass_symp)
    dataset.abdopain_date = symptom_date(abdopain_date, dataset.abdopain_symp)
    dataset.anaemia_date = symptom_date(anaemia_date, dataset.anaemia_symp)
    dataset.fit_test_any_date = symptom_date(fit_test_any_date, dataset.fit_test_any)

    fit_test_any_value = clinical_events_ranges.where(clinical_events_ranges.snomedct_code.is_in(codelists.fit_codes)
        ).where(
            clinical_events_ranges.date.is_on_or_after(dataset.fit_test_any_date)
        ).sort_by(
            clinical_events_ranges.date
        ).first_for_patient().numeric_value
    
    fit_test_any_comparator = clinical_events_ranges.where(clinical_events_ranges.snomedct_code.is_in(codelists.fit_codes)
        ).where(
            clinical_events_ranges.date.is_on_or_after(dataset.fit_test_any_date)
        ).sort_by(
            clinical_events_ranges.date
        ).first_for_patient().comparator
    
    dataset.fit_test_any_positive = case(when((fit_test_any_value>=10) & (fit_test_any_comparator!="<")).then(True), otherwise=False)

    def fit_6_weeks(symp_date):
        return clinical_events.where(clinical_events.snomedct_code.is_in(codelists.fit_codes)
        ).where(
            clinical_events.date.is_on_or_between(symp_date, symp_date + days(42))
        ).sort_by(
            clinical_events.date
        ).first_for_patient()
        
    dataset.fit_6_ida = dataset.ida_symp & fit_6_weeks(ida_date).exists_for_patient()
    dataset.fit_6_cibh = dataset.cibh_symp & fit_6_weeks(cibh_date).exists_for_patient()
    dataset.fit_6_abdomass = dataset.abdomass_symp & fit_6_weeks(abdomass_date).exists_for_patient()
    dataset.fit_6_prbleed = dataset.prbleed_symp_50 & fit_6_weeks(prbleed_date).exists_for_patient()
    dataset.fit_6_wl = dataset.wl_symp_50 & fit_6_weeks(wl_date).exists_for_patient()
    dataset.fit_6_abdopain = dataset.abdopain_symp_50 & fit_6_weeks(abdopain_date).exists_for_patient()
    dataset.fit_6_anaemia = dataset.anaemia_symp_60 & fit_6_weeks(anaemia_date).exists_for_patient()
    dataset.fit_6_wl_abdopain = dataset.wl_abdopain_symp_40 & (fit_6_weeks(wl_date).exists_for_patient() | fit_6_weeks(abdopain_date).exists_for_patient())
    dataset.fit_6_prbleed_abdopain = dataset.prbleed_abdopain_symp & fit_6_weeks(prbleed_date).exists_for_patient()
    dataset.fit_6_prbleed_wl = dataset.prbleed_wl_symp & fit_6_weeks(prbleed_date).exists_for_patient()
    dataset.fit_6_all_lowerGI = (dataset.fit_6_ida | dataset.fit_6_cibh | dataset.fit_6_abdomass | dataset.fit_6_prbleed | dataset.fit_6_wl | dataset.fit_6_abdopain | dataset.fit_6_anaemia | dataset.fit_6_wl_abdopain | dataset.fit_6_prbleed_abdopain | dataset.fit_6_prbleed_wl)

    def colorectal_ca_symp_6_months(symp_date):
        return clinical_events.where(clinical_events.snomedct_code.is_in(codelists.colorectal_diagnosis_codes_snomed)
        ).where(
            clinical_events.date.is_on_or_between(symp_date, symp_date + months(6))
        ).sort_by(
            clinical_events.date
        ).first_for_patient()

    dataset.ca_6_ida = dataset.ida_symp & colorectal_ca_symp_6_months(ida_date).exists_for_patient()
    dataset.ca_6_cibh = dataset.cibh_symp & colorectal_ca_symp_6_months(cibh_date).exists_for_patient()
    dataset.ca_6_abdomass = dataset.abdomass_symp & colorectal_ca_symp_6_months(abdomass_date).exists_for_patient()
    dataset.ca_6_prbleed = dataset.prbleed_symp_50 & colorectal_ca_symp_6_months(prbleed_date).exists_for_patient()
    dataset.ca_6_wl = dataset.wl_symp_50 & colorectal_ca_symp_6_months(wl_date).exists_for_patient()
    dataset.ca_6_abdopain = dataset.abdopain_symp_50 & colorectal_ca_symp_6_months(abdopain_date).exists_for_patient()
    dataset.ca_6_anaemia = dataset.anaemia_symp_60 & colorectal_ca_symp_6_months(anaemia_date).exists_for_patient()
    dataset.ca_6_wl_abdopain = dataset.wl_abdopain_symp_40 & (colorectal_ca_symp_6_months(wl_date).exists_for_patient() | colorectal_ca_symp_6_months(abdopain_date).exists_for_patient())
    dataset.ca_6_prbleed_abdopain = dataset.prbleed_abdopain_symp & colorectal_ca_symp_6_months(prbleed_date).exists_for_patient()
    dataset.ca_6_prbleed_wl = dataset.prbleed_wl_symp & colorectal_ca_symp_6_months(prbleed_date).exists_for_patient()
    dataset.ca_6_all_lowerGI = (dataset.ca_6_ida | dataset.ca_6_cibh | dataset.ca_6_abdomass | dataset.ca_6_prbleed | dataset.ca_6_wl | dataset.ca_6_abdopain | dataset.ca_6_anaemia | dataset.ca_6_wl_abdopain | dataset.ca_6_prbleed_abdopain | dataset.ca_6_prbleed_wl)

    return dataset

