import PyPDF2
import json
fileReader = PyPDF2.PdfFileReader('Corpus Building\CodeOfCivilProcedure.pdf')
sectionNumber=1
sectionInfo={}
dashes=['.—','. —']
dots=['. ',' .']
def collectAllSection(sectionNumber):
    for page in range(7,48):  #run from 7 to 147
        currentPage=fileReader.pages[page]
        currText=currentPage.extract_text()
        sectionNumber=findSections(currText,sectionNumber)

def findSections(text,sectionNumber):
    flag=1
    while flag!=0:

        if sectionNumber==80:
            print(sectionNumber)
        findSectionStartIndex=text.find(str(sectionNumber)+". ")
        minimum=10000
        for dash in dashes:
            findSectionTitleEnd=text.find(dash,findSectionStartIndex)
            if findSectionTitleEnd!=-1 and minimum>(findSectionTitleEnd-findSectionStartIndex):
                minimum=findSectionTitleEnd-findSectionStartIndex
        sectionNumber+=1
        findnextSectionStart=text.find(str(sectionNumber)+". ")
        minimum2=10000
        for dash in dashes:
            findDash=text.find(dash,findnextSectionStart)
            if findDash!=-1 and minimum2>(findDash-findnextSectionStart):
                minimum2=findDash-findnextSectionStart

        if findnextSectionStart!=-1 and minimum2!=10000:
            sectionInfo[str(sectionNumber-1)]=text[findSectionStartIndex+minimum+2:findnextSectionStart]
        else:
            findspace=text.find('\n          ',findSectionStartIndex+minimum+2)
            sectionInfo[str(sectionNumber-1)]=text[findSectionStartIndex+minimum+2:findspace]
            flag=0
    
    if sectionInfo[str(sectionNumber-1)]=="":
        sectionInfo[str(sectionNumber-2)]=sectionInfo[str(sectionNumber-2)]+text
        return sectionNumber-1
    else:
        return sectionNumber
    
collectAllSection(sectionNumber)
json_object = json.dumps(sectionInfo, indent=4)
with open("cpc.json", "w") as outfile:
    outfile.write(json_object)
