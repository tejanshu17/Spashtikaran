import PyPDF2
fileToRead = open('Spashtikaran\Dataset\case  (24).PDF','rb')
fileReader = PyPDF2.PdfFileReader(fileToRead)
numberOfPages = fileReader.numPages
sectionarray = []
actArray=[]
countOfAct=0
actsToSearch = ['Indian Penal Code','IPC']
def runThroughAllPages(num):
    # looping through all pages 
    for i in range(0,num-1):
        currentPage = fileReader.pages[i]
        currentPageText = currentPage.extract_text()
        findActsFromCurrentPage(currentPageText,countOfAct)


def findActsFromCurrentPage(pageText,countOfAct):
    for phrase in actsToSearch:
        if phrase in pageText:
            for j in range(0,pageText.count(phrase)):
                findIndex = pageText.find(phrase)
                actArray.append(pageText[findIndex-16:findIndex+32])
                pageText.replace(phrase,'#',1)
    

def findSectionNumber(actArray):
    for sentence in actArray:
        for i in range(0,len(sentence),3):
            if sentence[i].isnumeric():
                sectionarray.append(sentence[i-2:i+3])
    outputOfSections(sectionarray)


def outputOfSections(sectionArray):
    finalSectionSet = set(sectionarray)
    print(finalSectionSet)
    file = open('Spashtikaran\pre-processed results\IPCoutput.txt','w')
    file.write(str(finalSectionSet))


runThroughAllPages(numberOfPages)
findSectionNumber(actArray)






        
    