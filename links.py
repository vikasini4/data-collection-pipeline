from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class webscraper():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def search(self, query): 
        self.driver.get(f"https://www.google.com/search?q={query}&tbm=isch")
      
    def accept_form(self):
        accept_button = self.driver.find_element(
            By.XPATH, "//button[@aria-label='Accept all']")

        accept_button.click()   
        #print(accept_button)

    def scroll_to_bottom(self):
         #print('\nScrolling to the bottom of the page right now, then clicking on \'next page\'.')
         #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
         #time.sleep(3)
         #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
         #time.sleep(3)
         # Get scroll height after first time page load
        # Get scroll height after first time page load
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page / use a better technique like `waitforpageload` etc., if possible
            time.sleep(2)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Show more results']"))).click()
                except TimeoutException:
                    break
            last_height = new_height
            
               
    def get_all_links(self, query):
        self.search(query)
        self.accept_form()
        self.scroll_to_bottom()
        container = self.driver.find_elements(By.XPATH, '//*[@id="islrg"]/div[1]/div') 
        
       
        for element in container:
            
            try:
                a_tag = element.find_element(By.XPATH,'./a[1]')
                a_tag.send_keys(Keys.ENTER)
           #time.sleep(3)
                link = a_tag.get_attribute('href')
                print(link)
            except:
                pass
    
scraper = webscraper()
query = "radhakrishna"
scraper.get_all_links(query)



 
