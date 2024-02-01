from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class webpage:
    def __init__(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_url(self):
        #get url
        self.driver.get("https://www.imdb.com/search/name/")
        #maximize window
        self.driver.maximize_window()

    def fill_form_search(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            #first show all hidden items. So click expand all button
            expand_all = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@data-testid="adv-search-expand-all"]')))
            #but some error, this expand all, it's not a clickable button (::before or ::after used)
            #So I use script code
            self.driver.execute_script("arguments[0].click();", expand_all)
            #next fill name
            name = wait.until(EC.presence_of_element_located((By.ID,'text-input__3')))
            name.send_keys("Shivaji Ganesan")
            #fill from birth and to birth
            from_birth = wait.until(EC.presence_of_element_located((By.ID,'text-input__8')))
            from_birth.send_keys("01-10-1928 ")
            to_birth = wait.until(EC.presence_of_element_located((By.ID,'text-input__9')))
            to_birth.send_keys("21-07-2001")
            #fill birthday
            birthday = wait.until(EC.presence_of_element_located((By.ID,'text-input__4')))
            birthday.send_keys("10-1928")
            #then click page of topic
            page_of_topic = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="accordion-item-pageTopicsAccordion"]/div/div/section/button[2]/span')))
            #but the page of topic its not clickable button, so i use script 
            self.driver.execute_script("arguments[0].click();",page_of_topic)
            #select gender
            gender = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="accordion-item-genderIdentityAccordion"]/div/section/button[1]/span')))
            #gender also not a clickable button so i use script
            self.driver.execute_script("arguments[0].click();",gender)
            #finally fill some important items and last click see result button, and get output in the webpage window
            see_result = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button[2]/span')))
            self.driver.execute_script("arguments[0].click();",see_result)
        
        except NoSuchElementException as selenium_error:
            print("form fill search errors :\n",selenium_error)

        finally:
            print("code run successfully completed")
web = webpage()
web.get_url()
web.fill_form_search()
