from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# import subprocess as sp
# programName = "notepad.exe"
# fileName = "aaa.txt"
# sp.Popen([programName, fileName])


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver=webdriver.Chrome()

start_url = "https://translate.google.com/#view=home&op=translate&sl=en&tl=tr"
driver.get(start_url)
senedler=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[1]/nav/div[2]/button/span')
senedler.click()
kns=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[2]/c-wiz/div/form/div[1]/div[3]/label')
kns.click()
time.sleep(2)
send_keys(Keys.CONTROL, 'v') #paste

print('success!')
