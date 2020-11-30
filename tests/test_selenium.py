from selenium import webdriver
import unittest

class TestDoctorWho(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:5000')
        self.assertEqual(self.browser.title, 'Doctor Who What Where')

    def test_season_episode(self):
        self.browser.get('http://localhost:5000')
        season = self.browser.find_element_by_id('season')
        season.send_keys('2')
        episode = self.browser.find_element_by_id('episode')
        episode.send_keys('3')
        btn = self.browser.find_element_by_id('season-submit')
        btn.click()
        result = self.browser.find_element_by_id('searched_map')
        self.assertEqual(result.text, 'School Reunion')

    def test_title_search(self):
        self.browser.get('http://localhost:5000')
        title = self.browser.find_element_by_id('episode-title')
        title.send_keys('Rose')
        btn = self.browser.find_element_by_id('title-submit')
        btn.click()
        result = self.browser.find_element_by_id('searched_map')
        self.assertEqual(result.text, '1_1')

    def test_doctor(self):
        self.browser.get('http://localhost:5000')
        doctor = self.browser.find_element_by_id('doctor')
        doctor.send_keys('Smith')
        btn = self.browser.find_element_by_id('doctor-submit')
        btn.click()
        result = self.browser.find_element_by_id('searched_map')
        self.assertEqual(result.text, 'Amy Pond')

    def test_companion(self):
        self.browser.get('http://localhost:5000')
        companion = self.browser.find_element_by_id('companion')
        companion.send_keys('Martha Jones')
        btn = self.browser.find_element_by_id('companion-submit')
        btn.click()
        result = self.browser.find_element_by_id('searched_map')
        self.assertEqual(result.text, 'Tennant')

    def test_guest_star(self):   
        self.browser.get('http://localhost:5000')
        guest_star = self.browser.find_element_by_id('guest_star')
        guest_star.send_keys('River Song')
        btn = self.browser.find_element_by_id('guest-star-submit')
        btn.click()
        result = self.browser.find_element_by_id('searched_map')
        self.assertEqual(result.text, 'Smith')