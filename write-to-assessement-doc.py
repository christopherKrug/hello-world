def write_to_assessment_doc():
    fileName = site+"_"+assessment+"_"+timestamp+'.docx'
    if os.path.isfile(fileName):
        assessmentDoc = docx.Document(fileName)
        assessmentDoc.add_heading(assessment, level=1) # (()
        assessmentDoc.add_paragraph("to fill")
        assessmentDoc.save(fileName)
    else:
        assessmentDoc = docx.Document()
        assessmentDoc.add_heading(site+" "+timestamp,0)
        assessmentDoc.save(fileName)      
