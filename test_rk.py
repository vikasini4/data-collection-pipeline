from radhakrishna import webscraper
import unittest


class TestwebscraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = webscraper()
        self.query = "radhakrishna"
        
    def test__init__(self):
       pass

    def test_get_all_images(self, query):
        self.search(query)
        self.accept_form()
        self.scroll_to_bottom()
        self.get_all_links(query)
    
    def tearDown(self):
        self.scraper.driver.quit()
        del self.scraper
