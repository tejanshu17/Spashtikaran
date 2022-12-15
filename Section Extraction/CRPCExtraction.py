import PyPDF2
import os
for foldername,subfolders,files in os.walk(r"Dataset"):
    for file in files:
        # open the pdf file
        fileReader = PyPDF2.PdfFileReader(os.path.join(foldername,file))
        numberOfPages = fileReader.numPages
        sectionarray = []
        actArray=[]
        countOfAct=0
        actsToSearch = ['Code of Criminal Procedure','PC']
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
                        actArray.append(pageText[findIndex-18:findIndex+80])
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
            file = open('pre-processed results\CRPCoutput.txt','a',encoding="utf-8")
            if len(finalSectionSet)!=0:
                 file.write(str(finalSectionSet)+'\n')


        runThroughAllPages(numberOfPages)
        findSectionNumber(actArray)






        
    