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
import urllib.request
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class webscraper():
    def __init__(self):
        '''
        This class is used to scrape a website and extract links and images.
        The website chosen for the task is Google, therefore it will scrap Radhakrishna details.
        '''
        self.date = str(date.today())
        self.hour = datetime.now()
        self.current_time = str(self.hour.strftime("%H:%M"))
        self.image_number = 0
        self.all_links = []
        self.page = 0
        chromeOptions = Options()
        chromeOptions.add_argument('--headless')
        #self.driver = webdriver.Chrome(options=chromeOptions)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def search(self, query): 
        self.driver.get(f"https://www.google.com/search?q={query}&tbm=isch")
      
    def accept_form(self):
        '''A Method that accepts the cookies.'''
        try:
         accept_button = self.driver.find_element(By.XPATH, value=
              '//button[@aria-label="Accept all"]')
         accept_button.click()
         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
         #time.sleep(2)
        except:
            pass

  
        #print(accept_button)

    def scroll_to_bottom(self):
     
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
                except:
                    break
            last_height = new_height
            
               
    def get_all_links(self, query):
        '''A method that creates a list of links to the images to scrape'''
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
                #print(link)
                all_links.append({"ID": self.image_id,"link": link,"Date scraped": self.date,"Time scraped": self.current_time})
                #print(all_links)
            except:
                pass
        
        path1 = os.path.join('/Users/vikasiniperemakumar/Desktop/AiCore/Data_Collection_Pipeline/raw_data')
        os.mkdir(path1)
        with open(f'/Users/vikasiniperemakumar/Desktop/AiCore/Data_Collection_Pipeline/raw_data/data.json','w') as fp:
            json.dump(all_links, fp)      
       
    def get_all_images(self, query):
        '''A method that gets all images and stores it in a folder.'''
        self.search(query)
        self.accept_form()
        self.scroll_to_bottom()
        #self.get_all_links(query)

        imgResults = self.driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")

        src = []
        for img in imgResults:
            src.append(img.get_attribute('src'))

        for i in range(len(src)):
            try:
             urllib.request.urlretrieve(str(src[i]),"sample_images/radhakrishna{}.jpg".format(i))
            except:
                pass
    
    def run_scraper(self, query):
        self.search(query) 
        self.accept_form()
        self.scroll_to_bottom()
        self.get_all_links(query)
        self.get_all_images(query)    
    
scraper = webscraper()
query = "radhakrishna"
scraper.run_scraper(query)




 
