from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com')
# driver.find_element_by_xpath('//*[@class="s_ipt"]').send_keys('百度一下。你就知道')

# driver.find_element_by_id('su').click()
# mouse = driver.find_element_by_link_text('设置')
# print(mouse)
# ActionChains(driver).move_to_element(mouse).perform()
# sleep(2)
# driver.find_element_by_css_selector('.setpref')
# sleep(2)
# driver.find_element_by_css_selector('#kw').send_keys('我爱你M')
# sleep(2)
# driver.find_element_by_css_selector('#kw').send_keys(Keys.BACK_SPACE)
# sleep(2)
# driver.find_element_by_css_selector('#kw').send_keys('琉璃神社')
# sleep(2)
# driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL, 'a')
# driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL, 'c')
# sleep(2)
# driver.find_element_by_css_selector('#kw').clear()
# sleep(2)
# driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL, 'v')
# sleep(1)
# driver.find_element_by_css_selector('#kw').send_keys(Keys.ENTER)
# sleep(2)
# driver.quit()


# 乘法口诀
for i in range(1,10):
    for j in range(1,10):
        if j>i :
            pass
        else:
            print("%d*%d=%d" % (i,j,i*j), end='   ')
    print('')

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print(" ")

# 水仙数字
for i in range(100,1000):
    a = i//100
    b = i % 100//10
    c = i % 10
    if i == pow(a, 3)+pow(b, 3)+pow(c, 3):
        print(i)

