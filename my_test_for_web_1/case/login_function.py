
def login(driver,user='admin123',password='admin123'):
    driver.find_element_by_id('account').send_keys(user)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('submit').click()