from time import sleep


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

mouse = driver.find_element_by_css_selector("#u1 [name = 'tj_settingicon']")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_css_selector('.setpref').click()
sleep(1)
driver.find_element_by_css_selector('#nr').find_element_by_css_selector("option[value='50']").click()
driver.find_element_by_id('nr').click()
sleep(2)
driver.find_element_by_css_selector('#nr').find_element_by_css_selector("option[value='20']").click()
driver.find_element_by_id('nr').click()
sleep(2)
driver.find_element_by_css_selector('.prefpanelgo').click()
a = driver.switch_to.alert
a.accept()
sleep(3)
driver.quit()

