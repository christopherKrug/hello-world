def assess_access_data(data,
                       participants=["youth","caregiver","victim"],
                       stages=['referral','intake','inservice','exit','post'],
                       assessments=['count_records','measure_status','missing_participant_ids',
                                    'duplicate_participant_ids']):
    
    accessFiles = data.keys()
    participantStageTables = {'youth':{'referral':['OJJDP Referral'],
                                       'intake':['Intake','CBC Youth','Data Table'],
                                       'inservice':[],
                                       'exit':['Program Exit','CBC Youth End','Data Table End','YSBP Satisfaction Youth'],
                                       'post':[]},
                              'caregiver':{'referral':['OJJDP Referral Caregiver'],
                                           'intake':['Intake - Caregivers','PSSS','Youth SBP Intake',
                                                     'CBC Caregiver on Youth Intake'],
                                           'inservice':['Youth SBP InServices'],
                                           'exit':['Program Exit caregivers','PSSS Exit',
                                                   'Youth SBP EndService','CBC Caregiver on Youth End','YSBP Satisfaction Caregiver'],
                                           'post':['POST YSBP Tx Questionnaire']},
                              'victim':{'referral':['Victims'],
                                        'intake':['Intake - Victims','CBC Child Intake'],
                                        'inservice':[],
                                        'exit':['Program Exit - Victims','CBC Child End'],
                                        'post':[]}}
    tableFunctions = {
        'OJJDP Referral':youth_referral,'OJJDP Referral Caregiver':caregiver_referral,'Victims':victim_referral,
        'Intake':youth_intake,'Intake - Caregivers':caregiver_intake,'Intake - Victims':victim_intake,
        'CBC Youth':cbc_youth_intake,'CBC Youth End':cbc_youth_exit,
        'CBC Caregiver on Youth Intake':cbc_caregiver_youth_intake,'CBC Caregiver on Youth End':cbc_caregiver_youth_exit,
        'CBC Child Intake':cbc_victim_intake,'CBC Child End':cbc_victim_exit,
        'Data Table':jsoap_intake,'Data Table End':jsoap_exit,
        'PSSS':fsss_intake,'PSSS Exit':fsss_exit,
        'YSBP Satisfaction Youth': psb_satisfaction_youth,'YSBP Satisfaction Caregiver':psb_satisfaction_caregiver,
        'Youth SBP Intake':psb_intake,'Youth SBP InServices':psb_inservice,'Youth SBP EndService':psb_exit,'POST YSBP Tx Questionnaire':psb_questionnaire,
        'Program Exit':youth_exit,'Program Exit caregivers':caregiver_exit,'Program Exit - Victims':victim_exit
        }
    
    tableAssessments = {'count_records':count_records,'measure_status':measure_status,
                        'missing_participant_ids':missing_participant_ids,
                        'duplicate_participant_ids':duplicate_participant_ids}
    
    for accessFile in accessFiles:
        print "***********************************************"
        print "*                                             *"
        print "* "+accessFile
        print "*                                             *"
        print "***********************************************"
        
        for participant in participants:
            print participant.upper()
            for stage in stages:
                print "> "+stage
                stageTables = participantStageTables[participant][stage]
                if len(stageTables)>0:
                    for stageTable in stageTables:
                        tableFunctions[stageTable](data[accessFile][stageTable],tableAssessments,assessments)
