
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
    seven_button = driver.find_element(MobileBy.ID, "digit_7")
    nine_button = driver.find_element(MobileBy.ID, "digit_9")
    add_button = driver.find_element(MobileBy.ID, "op_add")
    equals_button = driver.find_element(MobileBy.ID, "eq")
    display = driver.find_element(MobileBy.ID, "formula")
    pre_display = driver.find_element(MobileBy.ID, "result_preview")
    minus_android = driver.find_element(MobileBy.IMAGE, "minus_android.png")


    seven_button.click()
    add_button.click()
    nine_button.click()
    minus_android.click()
    
    print(pre_display.text)
    equals_button.click()
    #print(display.text)

    driver.save_screenshot("screenshot.png")


 
finally:
    driver.quit()
