'''
京东，搜索一个商品，然后点击添加购物车
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#创建空的浏览器
driver = webdriver.Edge()

#隐式等待
driver.implicitly_wait(5)

#访问ip地址
driver.get("https://www.jd.com/")
#最大化
driver.maximize_window()
#输入框
driver.find_element('id','key').send_keys("智能马桶")
#搜索键
driver.find_element(By.XPATH,'//*[@id="search"]/div/div[2]/button').click()
#选择商品
driver.find_element(By.XPATH,'//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
#选择界面
driver.switch_to.window(driver.window_handles[1])
#加入购物车
driver.find_element(By.XPATH,'//*[@id="btn-reservation"]').click()

time.sleep(5)
driver.quit()



