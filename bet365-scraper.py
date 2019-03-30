
from selenium import webdriver
mobile_emulation = {
    "deviceName": "Nexus 5"
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(
    executable_path='C:/chromedriver_win32/chromedriver.exe',
    chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.get('http://mobile.bet365.com/#/IP/')
