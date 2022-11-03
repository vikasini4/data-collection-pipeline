from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import date, datetime
import json
import os
from base64 import b64decode
from pathlib import Path
import requests

class webscraper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.date = str(date.today())
        self.hour = datetime.now()
        self.current_time = str(self.hour.strftime("%H:%M"))
        self.image_number = 0
    
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
        
        all_links = []

        for element in container:  
            try:
                self.image_number += 1
                self.image_id = 'image_' + str(self.image_number)
                a_tag = element.find_element(By.XPATH,'./a[1]')
                a_tag.send_keys(Keys.ENTER)
           #time.sleep(3)
                link = a_tag.get_attribute('href')
                print(link)
                all_links.append({"ID": self.image_id,"link": link,"Date scraped": self.date,"Time scraped": self.current_time})
                print(all_links)
            except:
                pass
        
        path1 = os.path.join('/Users/vikasiniperemakumar/Desktop/AiCore/Data_Collection_Pipeline/raw_data')
        os.mkdir(path1)
        with open(f'/Users/vikasiniperemakumar/Desktop/AiCore/Data_Collection_Pipeline/raw_data/data.json','w') as fp:
            json.dump(all_links, fp)

    def get_all_images(self, query):
        self.search(query)
        self.accept_form()
        self.scroll_to_bottom()
       
        containers = self.driver.find_element(By.ID, "islrg")
        image_containers = containers.find_elements(By.XPATH, "div/div")
    
        "/a/div/img"
        for img_container in image_containers:
            title = img_container.find_element(
                By.TAG_NAME,"h3").text.lower().replace(' ','-')
            print(title)
            img = img_container.find_element(By.XPATH, "a/div/img")
            img_src = img.get_attribute('src')
            query_dir = f"images/{query}"
            Path(query_dir).mkdir(parents=True, exist_ok=True)
            fp = f"{query_dir}/{title}.jpeg"
            if "data:image/jpeg;base64," in img_src:
                img_data = self.get_img_bytes_from_b64(img_src)
            else:
                img_data = self.get_img_bytes_from_url(img_src)
            with open(fp, 'wb') as handler:
                handler.write(img_data)

    def get_img_bytes_from_url(self, img_url):
        return requests.get(img_url).content
       
    
    def get_img_bytes_from_b64(self, b64_string):
        b64_string = b64_string.replace('data:image/jpeg;base64,', '')
        b64_bytes = b64decode(b64_string)
        print(b64_bytes)
        return b64_bytes

scraper = webscraper()
query = "radhakrishna"
scraper.get_all_links(query)
scraper.get_all_images(query)
scraper.get_img_bytes_from_url()
scraper.get_img_bytes_from_b64()







 