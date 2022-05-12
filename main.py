from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:/Users/JC/Desktop/chromedriver.exe")

driver.get("https://www.fiercepharma.com/")
elements = driver.find_elements(By.XPATH,'//a[contains(text(),"COVID")]')

for element in elements:
    print(element.text+'\n')
driver.close()
