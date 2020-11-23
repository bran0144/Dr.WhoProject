from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:5000')
assert browser.title == 'Doctor Who What Where'

season = browser.find_element_by_id('season')
season.send_keys('2')
episode = browser.find_element_by_id('episode')
episode.send_keys('3')

btn = browser.find_element_by_id('season-submit')
btn.click()

result = browser.find_element_by_id()
