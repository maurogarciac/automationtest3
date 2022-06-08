from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


desired_caps = {
    "automationName" : "UiAutomator2",
    "platformName" : "Android",
    "platformVersion" : "11.0",
    "deviceName" : "pixel_2",
    "app" : "F:\COSAS IMPORTANTES\SCRIPSTSTSTSTS\Calculator_v8.1 (403424005)_apkpure.com.apk"
}
driver = webdriver.Remote(
    'http://127.0.0.1:4723/wd/hub',
    desired_caps)


try:
    ...
    seven_button = driver.find_element(MobileBy.ID, "digit_7")
    nine_button = driver.find_element(MobileBy.ID, "digit_9")
    add_button = driver.find_element(MobileBy.ID, "op_add")
    equals_button = driver.find_element(MobileBy.ID, "eq")

    
    seven_button.click()
    add_button.click()
    nine_button.click()
    equals_button.click()
    

    driver.get_screenshot_as_png()
 
finally:
    ...
    driver.quit()
