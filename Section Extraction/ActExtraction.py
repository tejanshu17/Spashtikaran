import os
import PyPDF2
for foldername,subfolders,files in os.walk(r"Dataset"):
    for file in files:
            fileReader = PyPDF2.PdfFileReader(os.path.join(foldername,file))
            numberOfPages = fileReader.numPages
            sectionarray = []
            actArray=[]
            countOfAct=0
            actsToSearch = ['Act']

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
                            actArray.append(pageText[findIndex-40:findIndex+40])
                            pageText.replace(phrase,'#',1)
                        

            def findSectionNumber(actArray):
                
                for sentence in actArray:
                    index=sentence.find('Act')
                    if sentence[index-4:index]!='the ':
                        sectionarray.append(sentence[index-20:index+20])
                
                outputOfSections(sectionarray)


            def outputOfSections(sectionArray):
                finalSectionSet = set(sectionArray)
                print(finalSectionSet)
                file = open('pre-processed results\Actouput.txt','a',encoding='UTF-8')
                if len(finalSectionSet)!=0:
                    file.write(str(finalSectionSet)+'\n')


            runThroughAllPages(numberOfPages)
            findSectionNumber(actArray)






        
    