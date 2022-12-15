import pdfplumber
import json
finaldict = {}
with pdfplumber.open("Spashtikaran\Corpus Building\IndianPenalCode.pdf") as pdf:
    for page in range(14,len(pdf.pages)):
        currentPage = pdf.pages[page]
        sectionNumberAndName = currentPage.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
        delimiter = ".—"
        keypos = []
        trial = sectionNumberAndName.extract_text()
        fullPageContent = currentPage.extract_text()
        sectionnumberarray=[]
        value = ""

        for i in range(0,len(trial)-1,2):
            if trial[i].isnumeric():
                key = trial[i]+trial[i+1]
                keypos.append(fullPageContent.find(key))
        
        for j in range(0,len(keypos)-1):
            findStart = fullPageContent.find(delimiter,keypos[j])
            findStop = fullPageContent.find(delimiter,keypos[j+1])
            key = fullPageContent[keypos[j]]+fullPageContent[keypos[j]+1]
            value = fullPageContent[findStart+2:findStop]
            finaldict[key] = value

json_object = json.dumps(finaldict, indent=4)
with open("IPCcorpus.json","w") as outfile:
    outfile.write(json_object)


            
                
                    

            
            
    


            



            

