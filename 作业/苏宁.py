'''
苏宁的搜索一个商品，然后点击添加购物车
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https://www.suning.com/')

driver.find_element('id','searchKeywords').send_keys('羊腰子')
driver.find_element('id','searchSubmit').click()
driver.find_element(By.XPATH,'//*[@id="ssdsn_search_pro_baoguang-1-0-1_1_02:0070214321_10574165200"]/img').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element('id','addCart').click()
time.sleep(5)
driver.quit()



