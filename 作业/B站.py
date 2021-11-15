'''
b站登陆脚本，然后搜索一个视频，点击播放，点赞
'''

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Edge()
# driver.implicitly_wait(15)
# driver.get('https://www.bilibili.com/')
# driver.maximize_window()
#
# driver.find_element(By.XPATH,'//*[@id="nav_searchform"]/input').send_keys('jony j')
# driver.find_element(By.XPATH,'//*[@id="nav_searchform"]/div').click()
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.XPATH,'//*[@id="all-list"]/div[1]/div[2]/ul[2]/li[1]/a/div/div[3]').click()
# driver.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[1]').click()
import time

from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get('https://www.bilibili.com/')
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element(By.XPATH,"//input[@class='nav-search-input']").send_keys('jony j')
driver.find_element(By.XPATH,"//span[@class='nav-search-btn-text']").click()
time.sleep(1)


driver.switch_to.window(driver.window_handles[1])

# driver.find_element(By.XPATH,"//div[@class='van-framepreview']").click()
# driver.find_element(By.CSS_SELECTOR,"//*[@class='van-framepreview']").click()

driver.find_element(By.XPATH,"//a[@title='炸翻！豆芽Jony J《玩家》2017 OKAY南京演唱会现场（自制字幕）']").click()

time.sleep(3)
driver.quit()