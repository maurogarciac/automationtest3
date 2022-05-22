from appium import webdriver
from appium.webdriver import mobilecommand
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {}
desired_caps["app"] = "Excel"
driver = webdriver.Remote(
    'http://127.0.0.1:4723',
    desired_caps)

try:
    driver.find_element(MobileBy.NAME, "CalculatorResults")
    driver.keyevent()
    driver.find_element(MobileBy.IMAGE, "/eight.png")

finally:
    driver.quit()

#Cant make keyboard do things yet apparently new workbook - "Alt, F, N"
#screenshotBase64 = driver.get_screenshot_as_base64()
#screenshotBase64