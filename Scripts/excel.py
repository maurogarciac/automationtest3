from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {}
desired_caps["app"] = "Excel"
driver = webdriver.Remote(
    'http://127.0.0.1:4723',
    desired_caps)

#screenshotBase64 = driver.get_screenshot_as_base64()
#screenshotBase64