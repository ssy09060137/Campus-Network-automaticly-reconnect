# Campus-Network-automaticly-reconnect
校园网自动重连（无法无感认证，MAC被注册）

没有自动化环境或pycharm等软件需要在CMD终端中输入：
 pip install selenium

在Windows任务计划程序中设置基础任务。


—————————————————————————————————————————————————————————————————————————————————————————————————

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建Chrome浏览器驱动实例
driver = webdriver.Chrome()

# 1.访问校园网登录页面
#下面👇↓这个http地址替换为校园网实际地址👇↓
driver.get('http://10.100.100.22')
driver.maximize_window()

# 设置显式等待，最长等待10秒
wait = WebDriverWait(driver, 10)

# 等待用户名输入框可交互，然后输入用户名
#下面第二行👇↓这个*23040102041*替换为自己的实际用户名账号👇↓
username_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='username']")))
username_input.send_keys('23040102041')
time.sleep(1)

# 直接定位密码输入框并等待其可交互，然后输入密码

move01 = driver.find_element(By.XPATH, '//*[@id="jizhummNo"]/div')
move = driver.find_element(By.XPATH, '//*[@id="pwd_tip"]')
ActionChains(driver).move_to_element(move01).click().perform()
ActionChains(driver).move_to_element(move).click().perform()

#下面第二行👇↓这个*12345678*替换为自己的实际密码👇↓
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pwd']")))
password = "12345678"
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
