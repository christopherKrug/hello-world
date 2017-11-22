def youth_referral(table,tableAssessments,assessments):
    
    print "*************** REFERRAL ***************"
    features = ['ID','Date of entry','YouthID','CaregiverID','MeasureStatus']
    
    tableVariables = {
'ID':'referral_id',
'SITE ID':'site_id',
'Date of entry':'data_of_entry',
'YouthID':'youth_id',
'CaregiverID':'caregiver_id',
'FR_date':'referral_date',
'FR01':'referral_source',
'FR01Secondary':'secondary_referral_source',
'FR01_other':'referral_source_other_specified',
'FRY01':'gender',
'FRY02':'date_of_birth',
'FRY03a_White':'white',
'FRY03b_Black':'black',
'FRY03c_Asian':'asian',
'FRY03d_Indian':'native_american',
'FRY03e_Hispanic':'hispanic',
'FRY03f_Other':'other',
'FRY03f_Otherspecify':'other_specified',
'FRY04':'primary_language_at_home',
'FRY04Other':'primary_language_at_home_other_specified',
'YSI01':'age_at_incident_problematic_sexual_behavior',
'YSI02year':'year_of_incident_problematic_sexual_behavior',
'YSI02month':'month_of_incident_problematic_sexual_behavior',
'YSI02day':'day_of_incident_problematic_sexual_behavior',
'YSI03':'was_youth_charged',
'YSI04':'was_youth_adjudicated',
'YSI05':'', ##################
'YSI06a_com_service':'',##################
'YSI06b_court_cost':'',##################
'YSI06c_curfew':'',##################
'YSI06d_charges':'',##################
'YSI06e_probation':'',##################
'YSI06f_tracking':'',##################
'YSI06g_sbp':'',##################
'YSI06h_parent_tx':'',##################
'YSI06i_sch':'',##################
'YSI06j_drug_test':'',##################
'YSI06j_Sabuse_tx':'',##################
'YSI06k_minor':'',##################
'YSI06l_sexreg':'',##################
'YSI06m_pnotify':'',##################
'YSI06m_snotify':'',##################
'YSI07':'number_previous_non_sexual_offenses',
'YSI08':'number_previous_sexual_offenses',
'YSI09':'was_criminal_court_involved',
'YSI09describe':'description_criminal_court_involvement',
'YSI10':'is_youth_involved_in_child_welfare',
'YSI10abusetypes':'abuse_neglect_types',
'YSI10openDHS':'is_child_welfare_case_open',
'MeasureStatus':'measures_status',
'extradetails1':'extra_details_1',
'extradetails2':'extra_details_2',
'extradetails3':'extra_details_3',
'SUBSITEID':'sub_site_id',
'NumVictims':'number_of_victims',
'NoVicReason':'description_reason_no_victim',
'extraVictimdetails':'extra_victim_details',
'NumCaregivers':'number_of_caregivers',
'extraCaregiverdetails':'extra_caregiver_details',
'FRC01':'',##################
'FRC02':'was_youth_moved_to_another_placement',
'county':'county',
'StateCustody':'youth_in_state_custody',
'secondlang':'secondary_language_at_home',
'municipality':'municipality',
'EHNo':'electronic_health_record_number'   
}
    
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def caregiver_referral(table,tableAssessments,assessments):
    
    print "*************** REFERRAL ***************"
    features = ['ID','Date of entry','YouthID','CaregiverID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
        
def victim_referral(table,tableAssessments,assessments):
    
    print "*************** REFERRAL ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','VictimID1','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def youth_intake(table,tableAssessments,assessments):
    
    print "*************** INTAKE ***************"
    features =  ['ID','Dateofentry','YouthID','CaregiverID','VictimID1','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
        
def caregiver_intake(table,tableAssessments,assessments):
    
    print "*************** INTAKE ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','VictimID1','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
        
def victim_intake(table,tableAssessments,assessments):
    
    print "*************** INTAKE ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','VictimID1','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)    
        
def youth_exit(table,tableAssessments,assessments):
    
    print "*************** EXIT ***************"
    features = ['ID','Date of entry','YouthID','CaregiverID','VictimID1','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def caregiver_exit(table,tableAssessments,assessments):
    
    print "*************** EXIT ***************"
    features = ['ID','Date of entry','YouthID','CaregiverID','VictimID1','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def victim_exit(table,tableAssessments,assessments):
    
    print "*************** EXIT ***************" 
    features = ['ID','Date of entry','YouthID','CaregiverID','VictimID1','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def jsoap_intake(table,tableAssessments,assessments):
    
    print "*************** J-SOAP INTAKE ***************"
    features = ['ID','Date of entry','YouthID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

    
def jsoap_exit(table,tableAssessments,assessments):
    
    print "*************** J-SOAP EXIT ***************"
    features = ['id','Date of entry','YouthID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

    
def fsss_intake(table,tableAssessments,assessments):
    
    print "*************** FSSS INTAKE ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def fsss_exit(table,tableAssessments,assessments):
    
    print "*************** FSSS EXIT ***************"
    features = ['ID','eDateofentry','YouthID','CaregiverID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def psb_intake(table,tableAssessments,assessments):
    
    print "*************** PSB INTAKE ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def psb_inservice(table,tableAssessments,assessments):
    
    print "*************** PSB IN-SERVICE ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def psb_exit(table,tableAssessments,assessments):
    
    print "*************** PSB EXIT ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def cbc_youth_intake(table,tableAssessments,assessments):
    
    print "*************** CBCL YOUTH INTAKE ***************"
    features = ['ID','Dateofentry','YouthID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def cbc_youth_exit(table,tableAssessments,assessments):
    
    print "*************** CBCL YOUTH EXIT ***************"
    features = ['ID','Dateofentry','YouthID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def cbc_caregiver_youth_intake(table,tableAssessments,
                    assessments):
    print "*************** CBCL CAREGIVER ON YOUTH INTAKE ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def cbc_caregiver_youth_exit(table,tableAssessments,assessments):
    
    print "*************** CBCL CAREGIVER ON YOUTH EXIT ***************"
    features = ['ID','Dateofentry','YouthID','CaregiverID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def cbc_victim_intake(table,tableAssessments,assessments):
    
    print "*************** CBCL VICTIM INTAKE ***************"
    features = ['ID','Dateofentry','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def cbc_victim_exit(table,tableAssessments,assessments):
    
    print "*************** CBCL VICTIM EXIT ***************"
    features = ['ID','Dateofentry','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def ucla_ptsd_caregiver_youth_intake(table,tableAssessments,
                    assessments):
    print "*************** UCLA PTSD CAREGIVER ON YOUTH INTAKE ***************"
    features = ['ID','Dateofentry','CaregiverID','YouthID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def ucla_ptsd_caregiver_youth_exit(table,tableAssessments,assessments):
    
    print "*************** UCLA PTSD CAREGIVER ON YOUTH EXIT ***************"
    features = ['ID','Dateofentry','CaregiverID','YouthID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def ucla_ptsd_caregiver_victim_intake(table,tableAssessments,assessments):
    
    print "*************** UCLA PTSD CAREGIVER ON VICTIM INTAKE ***************"
    features = ['ID','Dateofentry','CaregiverID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def ucla_ptsd_caregiver_victim_exit(table,tableAssessments,assessments):
    
    print "*************** UCLA PTSD CAREGIVER ON VICTIM EXIT ***************"
    features = ['ID','Dateofentry','CaregiverID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def ucla_ptsd_clinician_youth_intake(table,tableAssessments,assessments):
    
    print "*************** UCLA PTSD CLINICIAN ADMINISTERED ON YOUTH INTAKE ***************"
    features = ['ID','Dateofentry','CaregiverID','YouthID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def ucla_ptsd_clinician_youth_exit(table,tableAssessments,assessments):
    
    print "*************** UCLA PTSD CLINICIAN ADMINISTERED ON YOUTH EXIT ***************"
    features = ['ID','Dateofentry','CaregiverID','YouthID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def ucla_ptsd_clinician_victim_intake(table,tableAssessments,assessments):
    
    print "*************** UCLA PTSD CLINICIAN ADMINISTERED ON VICTIM INTAKE ***************"
    features = ['ID','Dateofentry','CaregiverID','YouthID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def ucla_ptsd_clinician_victim_exit(table,tableAssessments,assessments):
    
    print "*************** UCLA PTSD CLINICIAN ADMINISTERED ON VICTIM EXIT ***************"
    features = ['ID','Dateofentry','CaregiverID','YouthID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def psb_satisfaction_youth(table,tableAssessments,assessments):

    print "*************** PSB YOUTH SATISFACTION ***************"
    features = ['ID','Dateofentry','YouthID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
    
def psb_satisfaction_caregiver(table,tableAssessments,assessments):
    
    print "*************** PSB CAREGIVER SATISFACTION ***************"
    features = ['ID','Dateofentry','CaregiverID','VictimID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)

def psb_questionnaire(table,tableAssessments,assessments):
    
    print "*************** PSB TREATMENT QUESTIONNAIRE ***************"
    features = ['ID','Dateofentry','CaregiverID','YouthID','MeasureStatus']
    for assessment in assessments:
        tableAssessments[assessment](table,features)
