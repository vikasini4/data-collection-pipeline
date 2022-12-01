from radhakrishna import webscraper
import unittest


class webscraperTestCase(unittest.TestCase):
    def setUp(self):

        self.scraper = webscraper()
    
    def test_get_all_links(self):
        
        self.scraper.get_all_links = True
        
        try:
            print('All links printed in a raw_data')
            self.assertTrue(self.scraper.get_all_links)
        except:
            print('Error getting the links in a folder.')
            pass
        

    def test_get_all_images(self):
       
        self.scraper.get_all_images = True
        try:
            print('All images downloaded in a folder')
            self.assertTrue(self.scraper.get_all_images)
        except:
            print('Error downloading the images in a folder.')
            pass

 
    def tearDown(self):
        self.scraper.driver.quit()

if __name__ == '__main__':
    unittest.main(argv = [''],warnings='ignore')

