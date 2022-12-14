from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import time 
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\nishk\\Desktop\\chromedriver.exe')
driver.get("https://indiankanoon.org/search/?formInput=divorce+cases/")
for j in range(1,2):
    for i in range(10):

        time.sleep(7)
        driver.get("https://indiankanoon.org/search/?formInput=divorce%20cases/&pagenum="+str(j))
        getalllinks=driver.find_elements(By.CLASS_NAME,'result_title')      
        get=getalllinks[i].find_element(By.TAG_NAME,'a').click()
        viewdoc=driver.find_element(By.PARTIAL_LINK_TEXT,'Complete').click()
        download=driver.find_element(By.CLASS_NAME,'docoptions')
        downloaddoc=download.find_element(By.XPATH, "//form[input/@value='Get this document in PDF']").click()
  
