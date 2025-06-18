from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建Chrome浏览器驱动实例
driver = webdriver.Chrome()

# 访问校园网登录页面
driver.get('http://10.100.100.22')
driver.maximize_window()

# 设置显式等待，最长等待10秒
wait = WebDriverWait(driver, 10)

# 等待用户名输入框可交互，然后输入用户名
username_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='username']")))
username_input.send_keys('23040102041')
time.sleep(1)

# 直接定位密码输入框并等待其可交互，然后输入密码

move01 = driver.find_element(By.XPATH, '//*[@id="jizhummNo"]/div')
move = driver.find_element(By.XPATH, '//*[@id="pwd_tip"]')
ActionChains(driver).move_to_element(move01).click().perform()
ActionChains(driver).move_to_element(move).click().perform()


password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pwd']")))
password = "304829oL!"
for char in password:
    password_input.send_keys(char)
    time.sleep(0.1)

# 等待登录按钮可交互，然后点击登录按钮
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginLink_div"]')))
login_button.click()

# 尝试截取登录页面的屏幕截图保存到指定路径，这里假设路径是D盘根目录下的校园网登录.png
driver.get_screenshot_as_file("D://校园网登录.png")

print('连上了吗？？？')

# 关闭浏览器驱动
driver.close()