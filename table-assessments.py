### COUNT RECORDS ####
def count_records(table,features):
    if table.empty==True:
        print "|---------------------------------------------|" 
        print "| NUMBER OF RECORDS: 0"
        print "|---------------------------------------------|"
    else:
        numberOfRecords = table.shape[0]
        print "|---------------------------------------------|" 
        print "| NUMBER OF RECORDS: "+str(numberOfRecords)
        print "|---------------------------------------------|"

    print "_______________________________________________\n"

def measure_status(table,features):
    measureStatusCounts = table['MeasureStatus'].value_counts()
    print "|---------------------------------------------|" 
    print "| MEASURE STATUS OF RECORDS "#+str(sum(measureStatusCounts))
    for measureStatusValue in measureStatusCounts.index.tolist():
        print "|---------------------------------------------|" 
        print "| > "+ measureStatusValue+": "+str(measureStatusCounts.values[measureStatusCounts.index.tolist().index(measureStatusValue)])
    measureStati = pd.DataFrame(pd.isnull(table['MeasureStatus']))
    missingMeasureStati = measureStati[measureStati['MeasureStatus']==True].index.tolist()
    if(len(missingMeasureStati)>0):
        print "|---------------------------------------------|" 
        print "| > Missing 'Measure Status': "+str(len(missingMeasureStati))
        print table[features].iloc[missingMeasureStati]
    print "|---------------------------------------------|"
    print "_______________________________________________\n"

def duplicate_participant_ids(table,features):
    participantTypeIDs = list(set(['YouthID','CaregiverID','VictimID','VictimID1']) & set(features))
    booleanDuplicatesRelations = pd.DataFrame(table[participantTypeIDs].duplicated(keep='first'))
    indicesOfDuplicateRelationsAmongParticipants = booleanDuplicatesRelations[booleanDuplicatesRelations[0]==True].index.tolist()
    if len(indicesOfDuplicateRelationsAmongParticipants)>0:
        duplicateRelationsAmongParticpants = table[features].iloc[indicesOfDuplicateRelationsAmongParticipants]
        print "|---------------------------------------------|" 
        print "| DUPLICATE RELATIONS AMONG PARTICIPANTS: "+str(duplicateRelationsAmongParticpants[participantTypeIDs].shape[0])
        print "|---------------------------------------------|" 
        print duplicateRelationsAmongParticpants[participantTypeIDs].reset_index(drop=True)
    else:
        print "|---------------------------------------------|" 
        print "| DUPLICATE RELATIONS AMONG PARTICIPANTS: "+str(len(indicesOfDuplicateRelationsAmongParticipants))
    print "|---------------------------------------------|" 
    print "_______________________________________________\n"  
    
def missing_participant_ids(table,features):
    participantTypeIDs = list(set(['YouthID','CaregiverID','VictimID','VictimID1']) & set(features))
    print "|---------------------------------------------|" 
    print "| MISSING PARTICIPANT IDS:                    |"
    for participantTypeID in participantTypeIDs:
        participantIDs = pd.DataFrame(pd.isnull(table[participantTypeID]))
        missingParticipantIDs = participantIDs[participantIDs[participantTypeID]==True].index.tolist()
        #print missingParticipantIDs
        if(len(missingParticipantIDs)>0):
            print "|---------------------------------------------|" 
            print "| > Missing "+participantTypeID+"s "+str(len(missingParticipantIDs))
            print table[features].iloc[missingParticipantIDs]
        else:
            print "|---------------------------------------------|" 
            print "| > Missing "+participantTypeID+"s: "+str(len(missingParticipantIDs))
        
    print "|---------------------------------------------|" 
    print "_______________________________________________\n"
