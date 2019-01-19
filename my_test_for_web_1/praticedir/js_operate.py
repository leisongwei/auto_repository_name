from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://kyfw.12306.cn/otn/index/init')
js = '''
    document.getElementById('train_date').value='2137-12';
    document.getElementById('fromStationText').value='01-17-12';
    document.getElementById('search_one').click()
    '''
driver.execute_script(js)