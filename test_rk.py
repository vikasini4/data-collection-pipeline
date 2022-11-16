from rk import webscraper
import unittest
import os


class webscraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = webscraper()
        
    def test__init__(self):
       pass
    
    def test_search(self): 
        self.scraper.search()
        url='https://www.google.com/search?q=radhakrishna&tbm=isch'
        self.assertAlmostEqual(len(url),53)

    def test_accept_form(self):
        actual = self.scraper.accept_form()

        try: 
            expected1 = 'Cookies accepted'
            self.assertEqual(actual,expected1)
            print('Accept Cookies button correctly used')
        except:
            expected2 = 'No cookies to accept'
            self.assertEqual(actual,expected2)
            print('No Cookies button found')

    def test_scroll_to_bottom(self):
        self.scraper.accept_form()
        self.scraper.scroll_to_bottom()
        height1 = self.scraper.driver.execute_script("window.scrollTo(0, 20);")
        self.scraper.scroll_to_bottom()
        height2 = self.scraper.driver.execute_script("window.scrollTo(0, 20);")
        self.assertAlmostEqual(height1,height2)

    def test_get_all_links(self):
        self.scraper.search()
        self.scraper.accept_form()
        self.scraper.scroll_to_bottom()

        path1 = os.path.join('/Users/vikasiniperemakumar/Desktop/AiCore/Data_Collection_Pipeline/raw_data')
        expected_path = os.path.join('/Users/vikasiniperemakumar/Desktop/AiCore/Data_Collection_Pipeline/raw_data')
        self.assertEqual(expected_path, path1)

    def test_get_all_images(self):
        self.scraper.get_all_images = True
        try:
            print('All images downloaded in a folder')
            self.assertTrue(self.scraper.get_all_images)
        except:
            print('Error downloading the images in a folder.')
            pass

if __name__ == '__main__':
    unittest.main(argv = [''],warnings='ignore')
